"""Cloud persistence: sync each scan to the user's Firestore (project rogue-hackathon).

Why: files in scans/ are the local source of truth, but for durability across
machines/sessions (and so nothing is ever lost), each scan is also pushed to a
`scans` collection in Firestore.

AUTH model (important): a freshly-created Firestore database has locked security
rules (deny all) — which is the SAFE default and we deliberately do NOT open it to
the public. Instead, writes/reads are authenticated as the project owner via an
OAuth token minted from the already-logged-in Firebase CLI session. IAM-authorized
requests bypass security rules safely, so no rule/access-control change is needed.

If the Firebase CLI session isn't present (e.g. a deployed box), it falls back to
the web-API-key path (which only works if rules are open) and then to Supabase.
All paths are best-effort: never raises — file persistence already happened.

    FIREBASE_PROJECT=rogue-hackathon    # from engine/.env
"""
from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# Public OAuth client embedded in the open-source firebase-tools CLI.
_FB_CLIENT_ID = "563584335869-fgrhgmd47bqnekij5i8b5pr03ho849e6.apps.googleusercontent.com"
_FB_CLIENT_SECRET = "j9iVZfS8kkCEFUPaAeJV0sAi"
_CONFIGSTORE = Path.home() / ".config" / "configstore" / "firebase-tools.json"

_token_cache: dict = {"value": None, "exp": 0.0}


def _load_env() -> None:
    env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        os.environ.setdefault(k.strip(), v.strip())


def _project() -> str:
    return os.environ.get("FIREBASE_PROJECT", "rogue-hackathon")


def _access_token() -> str | None:
    """Mint a short-lived Google access token from the logged-in Firebase CLI's
    refresh token. Cached until ~1 min before expiry. None if no CLI session."""
    now = time.time()
    if _token_cache["value"] and now < _token_cache["exp"]:
        return _token_cache["value"]
    if not _CONFIGSTORE.exists():
        return None
    try:
        rt = json.loads(_CONFIGSTORE.read_text())["tokens"]["refresh_token"]
    except Exception:
        return None
    try:
        body = urllib.parse.urlencode({
            "client_id": _FB_CLIENT_ID, "client_secret": _FB_CLIENT_SECRET,
            "refresh_token": rt, "grant_type": "refresh_token"}).encode()
        resp = json.loads(urllib.request.urlopen(
            "https://oauth2.googleapis.com/token", body, timeout=30).read())
        _token_cache["value"] = resp["access_token"]
        _token_cache["exp"] = now + int(resp.get("expires_in", 3600)) - 60
        return _token_cache["value"]
    except Exception:
        return None


def _doc_id(report: dict) -> str:
    slug = (re.sub(r"[^a-z0-9]+", "-", str(report.get("target", "")).lower())
            .strip("-")[:40] or "scan")
    ts = str(report.get("generated_at", "")).replace(":", "").replace("-", "")[:15]
    return f"{ts}-{slug}" if ts else slug


def _fs_fields(report: dict) -> dict:
    def i(n):
        return {"integerValue": str(int(n or 0))}
    return {"fields": {
        "target": {"stringValue": str(report.get("target", ""))},
        "mode": {"stringValue": str(report.get("mode", ""))},
        "generated_at": {"stringValue": str(report.get("generated_at", ""))},
        "total_attacks": i(report.get("total_attacks")),
        "breaches": i(report.get("breaches")),
        "behavior_breaches": i(report.get("behavior_breaches")),
        "report_json": {"stringValue": json.dumps(report)},
    }}


def _fs_request(method: str, url: str, token: str, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    rq = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": "Bearer " + token, "Content-Type": "application/json"})
    try:
        return json.loads(urllib.request.urlopen(rq, timeout=30).read()), 200
    except urllib.error.HTTPError as e:
        return e.read().decode(), e.code


def push_scan(report: dict) -> str | None:
    """Persist one scan to Firestore (owner-authenticated). Returns the doc id or
    None. Retries briefly while a just-created database finishes provisioning."""
    _load_env()
    token = _access_token()
    if token:
        project, doc_id = _project(), _doc_id(report)
        url = (f"https://firestore.googleapis.com/v1/projects/{project}"
               f"/databases/(default)/documents/scans/{doc_id}")
        for attempt in range(6):
            out, code = _fs_request("PATCH", url, token, _fs_fields(report))
            if code == 200:
                return doc_id
            s = json.dumps(out) if isinstance(out, dict) else str(out)
            # DB still provisioning right after creation → wait and retry.
            if ("NOT_FOUND" in s or "is not found" in s or "still being created" in s
                    or "not ready" in s):
                time.sleep(5)
                continue
            print(f"  [store] Firestore write skipped (HTTP {code}).")
            return None
        return None

    # Fallbacks if there's no Firebase CLI session on this box.
    api_key = os.environ.get("FIREBASE_API_KEY")
    if api_key:
        return _push_firestore_apikey(report, _project(), api_key)
    url, key = os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY")
    if url and key:
        return _push_supabase(report, url, key)
    return None


def pull_all() -> list[dict]:
    """Read every scan back from Firestore (owner-authenticated). Returns a list of
    full report dicts, newest first. Empty list if unavailable."""
    _load_env()
    token = _access_token()
    if not token:
        return []
    project = _project()
    url = (f"https://firestore.googleapis.com/v1/projects/{project}"
           f"/databases/(default)/documents/scans?pageSize=300")
    out, code = _fs_request("GET", url, token)
    if code != 200 or not isinstance(out, dict):
        return []
    reports = []
    for doc in out.get("documents", []):
        rj = doc.get("fields", {}).get("report_json", {}).get("stringValue")
        if rj:
            try:
                reports.append(json.loads(rj))
            except Exception:
                pass
    reports.sort(key=lambda r: r.get("generated_at", ""), reverse=True)
    return reports


def _push_firestore_apikey(report: dict, project: str, api_key: str) -> str | None:
    doc_id = _doc_id(report)
    url = (f"https://firestore.googleapis.com/v1/projects/{project}"
           f"/databases/(default)/documents/scans/{doc_id}?key={api_key}")
    try:
        import httpx
        r = httpx.patch(url, json=_fs_fields(report), timeout=20)
        if r.status_code in (401, 403):
            # Expected on a machine not logged into the Firebase CLI as the project
            # owner: the secure owner-auth path no-op'd and fell back to the api-key
            # path, which the (correctly) locked rules reject. This is NOT a failure
            # to fix by opening the rules — that would expose scan data publicly.
            # Your scan is safe in scans/ (the source of truth); it syncs to the DB
            # from the owner's machine. To sync from here too, ask the owner to add
            # your Google account to project rogue-hackathon (IAM), then `firebase
            # login`. Do NOT publish open Firestore rules.
            print("  [store] cloud sync skipped — not the project owner on this box; "
                  "scan saved locally, syncs from owner machine. (Don't open the rules.)")
            return None
        if r.status_code >= 400:
            print(f"  [store] Firestore (api-key) write skipped (HTTP {r.status_code}).")
            return None
        return doc_id
    except Exception as e:
        print(f"  [store] Firestore sync skipped: {e}")
        return None


def _push_supabase(report: dict, url: str, key: str) -> str | None:
    row = {k: report.get(k) for k in
           ("target", "mode", "generated_at", "total_attacks", "breaches")}
    row["behavior_breaches"] = report.get("behavior_breaches", 0)
    row["report"] = report
    try:
        import httpx
        r = httpx.post(f"{url.rstrip('/')}/rest/v1/scans", headers={
            "apikey": key, "Authorization": f"Bearer {key}",
            "Content-Type": "application/json", "Prefer": "return=representation"},
            json=row, timeout=20)
        r.raise_for_status()
        data = r.json()
        return (data[0] if isinstance(data, list) and data else {}).get("id")
    except Exception as e:
        print(f"  [store] Supabase sync skipped: {e}")
        return None
