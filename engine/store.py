"""Cloud persistence: sync each scan to the user's Firestore (project rogue-hackathon).

Why: files in scans/ are the local source of truth, but for the DEPLOYED dashboard
to show every scan from anywhere (and so nothing is ever lost across machines), each
scan is also pushed to a `scans` collection in Firestore.

Zero-config activation: if FIREBASE_PROJECT + FIREBASE_API_KEY are set (engine/.env,
which is gitignored), run.py syncs automatically; otherwise it's a silent no-op.
Supabase remains supported as a fallback if SUPABASE_URL/KEY are set instead.

The whole report is stored as one JSON string field (`report_json`) plus a few
flat summary fields, so the document shape is trivial and the dashboard just
JSON.parses report_json. No firebase-admin / service account needed for writes
when Firestore is in test mode; the web API key authorizes the REST call.

    FIREBASE_PROJECT=rogue-hackathon
    FIREBASE_API_KEY=<web api key>     # not secret; identifies the project
"""
from __future__ import annotations

import json
import os
from pathlib import Path


def _load_env() -> None:
    """Tiny no-dependency .env loader so FIREBASE_*/SUPABASE_* are available even
    when the process wasn't started with them exported."""
    env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        os.environ.setdefault(k.strip(), v.strip())


def push_scan(report: dict) -> str | None:
    """Persist one scan report to the cloud. Returns a document/row id, or None if
    not configured / on any error (never raises — file persistence already happened)."""
    _load_env()
    project = os.environ.get("FIREBASE_PROJECT")
    api_key = os.environ.get("FIREBASE_API_KEY")
    if project and api_key:
        return _push_firestore(report, project, api_key)

    # Fallback: Supabase, if that's what's configured instead.
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if url and key:
        return _push_supabase(report, url, key)
    return None


def _fs_fields(report: dict) -> dict:
    """Map a report to Firestore's typed-value JSON. We keep flat summary fields
    queryable and stash the full report as a single JSON string."""
    def i(n):  # Firestore integerValue must be a string
        return {"integerValue": str(int(n or 0))}
    return {
        "fields": {
            "target": {"stringValue": str(report.get("target", ""))},
            "mode": {"stringValue": str(report.get("mode", ""))},
            "generated_at": {"stringValue": str(report.get("generated_at", ""))},
            "total_attacks": i(report.get("total_attacks")),
            "breaches": i(report.get("breaches")),
            "behavior_breaches": i(report.get("behavior_breaches")),
            "report_json": {"stringValue": json.dumps(report)},
        }
    }


def _push_firestore(report: dict, project: str, api_key: str) -> str | None:
    """Create one document in the `scans` collection via the Firestore REST API.
    Idempotent-ish: we name the doc after the scan's id (target+timestamp) when we
    can, so re-syncing the same scan overwrites rather than duplicates."""
    base = (f"https://firestore.googleapis.com/v1/projects/{project}"
            f"/databases/(default)/documents/scans")
    # Stable doc id from target + timestamp (mirrors the local scans/ filename).
    import re
    slug = (re.sub(r"[^a-z0-9]+", "-", str(report.get("target", "")).lower())
            .strip("-")[:40] or "scan")
    ts = str(report.get("generated_at", "")).replace(":", "").replace("-", "")[:15]
    doc_id = f"{ts}-{slug}" if ts else None

    try:
        import httpx
        if doc_id:
            # PATCH to a specific id = create-or-replace (no duplicate on re-sync).
            url = f"{base}/{doc_id}?key={api_key}"
            r = httpx.patch(url, json=_fs_fields(report), timeout=20)
        else:
            url = f"{base}?key={api_key}"
            r = httpx.post(url, json=_fs_fields(report), timeout=20)
        if r.status_code >= 400:
            body = r.text  # the real reason lives in the body, not the status line
            if "has not been used" in body or "it is disabled" in body or "SERVICE_DISABLED" in body:
                print("  [store] Firestore not enabled yet — turn it on in the "
                      "console (Build → Firestore Database → Create database), "
                      "then run:  python engine/sync_all.py")
            elif "PERMISSION_DENIED" in body or "Missing or insufficient" in body:
                print("  [store] Firestore reachable but rules deny writes — set "
                      "test-mode rules (or a service account), then re-run sync.")
            else:
                print(f"  [store] Firestore sync skipped (HTTP {r.status_code}).")
            return None
        name = r.json().get("name", "")
        return name.split("/")[-1] or doc_id
    except Exception as e:
        print(f"  [store] Firestore sync skipped: {e}")
        return None


def _push_supabase(report: dict, url: str, key: str) -> str | None:
    row = {
        "target": report.get("target"),
        "mode": report.get("mode"),
        "generated_at": report.get("generated_at"),
        "total_attacks": report.get("total_attacks"),
        "breaches": report.get("breaches"),
        "behavior_breaches": report.get("behavior_breaches", 0),
        "report": report,
    }
    try:
        import httpx
        r = httpx.post(
            f"{url.rstrip('/')}/rest/v1/scans",
            headers={
                "apikey": key,
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
                "Prefer": "return=representation",
            },
            json=row,
            timeout=20,
        )
        r.raise_for_status()
        data = r.json()
        return (data[0] if isinstance(data, list) and data else {}).get("id")
    except Exception as e:
        print(f"  [store] Supabase sync skipped: {e}")
        return None
