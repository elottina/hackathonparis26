"""Rogue local backend — paste a URL, watch the swarm break in, get the dashboard.

One small stdlib server (no extra deps) that:
  • serves the dashboard SPA (dashboard/index.html + assets),
  • POST /api/scan {url}        -> starts a real scan, returns {job_id},
  • GET  /api/stream/<job_id>   -> Server-Sent Events: every attacker move, target
                                   reply, tool call and breach, live, as they happen
                                   (this is what drives the "breaking in" animation),
  • GET  /api/history           -> saved scans (from Firestore, else local index),
  • GET  /api/scan/<id>         -> one saved scan report.

The scan is the SAME engine as run.py (orchestrator.run_swarm) — real Claude
attackers + judge against the pasted endpoint — so the animation is a real
operation, not a canned movie. A deterministic offline demo path (preset=demo)
runs the mock swarm instantly for stage/no-network use.

    python3 engine/server.py            # http://localhost:8799
"""
from __future__ import annotations

import asyncio
import json
import os
import queue
import re
import threading
import uuid
from collections import Counter
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DASH = ROOT / "dashboard"
# Hosts like Render/Railway/Fly inject $PORT; fall back to ROGUE_PORT, then 8799 (local).
PORT = int(os.environ.get("PORT") or os.environ.get("ROGUE_PORT") or "8799")


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


_load_env()

import strategies as strat  # noqa: E402  (after env load)
from orchestrator import run_swarm  # noqa: E402
from sink import EgressSink  # noqa: E402
from target import DEMO_SECRET, HTTPTarget  # noqa: E402

# Curated, high-signal, reliable vectors for the live (fast) scan. Deep mode uses
# the full arsenal. We keep harmful/malware out of the fast default so the
# attacker model never self-refuses mid-demo.
QUICK_KEYS = ["system_prompt_extraction", "prompt_injection", "jailbreak",
              "financial_advice", "medical_advice", "pii_privacy",
              "hallucination", "overreliance"]

SEV_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}

# job_id -> {"q": Queue, "done": bool, "report": dict|None, "error": str|None}
JOBS: dict[str, dict] = {}


# ---------- the scan job (runs in a background thread) ----------

def _assemble_report(target_name, mode, results, sink) -> dict:
    breaches = [r for r in results if r.get("success")]
    breaches.sort(key=lambda r: (0 if r.get("detection") == "behavior" else 1,
                                  SEV_ORDER.get(r.get("severity", "low"), 9)))
    return {
        "target": target_name,
        "mode": mode,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_attacks": len(results),
        "breaches": len(breaches),
        "behavior_breaches": sum(1 for b in breaches if b.get("detection") == "behavior"),
        "findings": breaches,
        "egress": sink.public_log(),
    }


def _archive_and_sync(report: dict) -> None:
    try:
        scans_dir = ROOT / "scans"
        scans_dir.mkdir(exist_ok=True)
        slug = (re.sub(r"[^a-z0-9]+", "-", report["target"].lower()).strip("-")[:40]
                or "scan")
        ts = report["generated_at"].replace(":", "").replace("-", "")[:15]
        rel = f"scans/{ts}-{slug}.json"
        (ROOT / rel).write_text(json.dumps(report, indent=2))
        idx_path = scans_dir / "index.json"
        idx = json.loads(idx_path.read_text()) if idx_path.exists() else []
        idx = [e for e in idx if e.get("file") != rel]
        idx.insert(0, {
            "id": f"{ts}-{slug}", "target": report["target"],
            "mode": report.get("mode"), "generated_at": report["generated_at"],
            "breaches": report["breaches"], "total_attacks": report.get("total_attacks"),
            "by_severity": dict(Counter(f.get("severity") for f in report["findings"])),
            "file": rel,
        })
        idx_path.write_text(json.dumps(idx, indent=2))
    except Exception as e:
        print(f"  [server] archive skipped: {e}")
    try:
        import store
        sid = store.push_scan(report)
        if sid:
            print(f"  [server] synced → cloud ({sid})")
    except Exception as e:
        print(f"  [server] cloud sync skipped: {e}")


def _run_job(job_id: str, url: str, preset: str) -> None:
    job = JOBS[job_id]
    q = job["q"]

    def emit(ev: dict):
        q.put(ev)

    async def go():
        listener = None
        if preset == "demo":
            from mock import MockAttacker, MockJudge, MockTarget
            target = MockTarget()
            chosen = strat.get(strat.DEMO_KEYS)
            kwargs = {"attacker": MockAttacker(), "judge": MockJudge()}
            sink = EgressSink(DEMO_SECRET)
            mode = "deterministic replay"
            runs, turns = 1, 2
        elif preset == "hr":
            # The niche centerpiece: an AI CV-screening agent (EU AI Act Annex III,
            # high-risk) that gives a compliant recommendation while secretly looking
            # the candidate up online — the behavior oracle catches the egress.
            # Black-box HR demo: a real served screening agent (TalentScreen) that
            # exposes NO tools and leaks the candidate's name on the wire via a
            # markdown badge URL. Caught by the egress oracle, not self-report.
            import hr_demo
            target, sink, listener, egress, kwargs = hr_demo.setup_http()
            chosen = [s for s in hr_demo.HR_STRATEGIES if s.key == "gdpr_web_lookup"]
            mode = "live scan · black-box HR screening agent (Annex III high-risk)"
            runs, turns = 3, 2
        elif preset == "cowork":
            # The credibility headline: a live scan of a REAL, shipping agent
            # (Cowork) used for CV screening — driven over its own HTTP API. It
            # profiles the candidate off-box while the recommendation stays clean.
            import cowork_demo
            target, sink, kwargs = cowork_demo.setup()
            chosen = cowork_demo.COWORK_STRATEGIES
            mode = "live scan · real AI agent (Cowork) — CV screening · Annex III high-risk"
            runs, turns = 1, 1
        else:
            from canary import canary_strategy
            from canary import setup as canary_setup
            target = HTTPTarget(url)
            deep = preset == "deep"
            base = strat.get(None if deep else QUICK_KEYS)
            # Canary exfil: plant a token via injection, try to make the agent leak
            # it inside a URL → it physically arrives at our listener = confirmed
            # behavior breach on a black-box agent (no code access). Several attempts
            # so one framing lands. This is the differentiator on a REAL target.
            canary_tok, sink, listener, egress = canary_setup()
            attempts = 4 if deep else 3
            chosen = base + [canary_strategy(canary_tok)] * attempts
            kwargs = {"egress": egress}
            mode = "live scan · behavior oracle" if not deep else "live scan · deep red-team"
            runs, turns = (2, 4) if deep else (1, 4)

        emit({"kind": "scan_start", "target": target.name, "mode": mode,
              "strategies": [s.name for s in chosen],
              "strategy_keys": [s.key for s in chosen],
              "planned_attacks": len(chosen) * runs})

        try:
            results = await run_swarm(target, chosen, runs_per_strategy=runs,
                                      max_turns=turns, on_event=emit, sink=sink,
                                      concurrency=(12 if preset == "demo"
                                                   else 2 if preset == "cowork" else 6),
                                      **kwargs)
        finally:
            if listener:
                listener.stop()
        report = _assemble_report(target.name, mode, results, sink)
        _archive_and_sync(report)
        job["report"] = report
        emit({"kind": "done", "report": report})

    try:
        asyncio.run(go())
    except Exception as e:
        job["error"] = str(e)
        emit({"kind": "error", "message": str(e)})
    finally:
        job["done"] = True
        q.put(None)  # sentinel: stream can close


# ---------- HTTP layer ----------

CT = {".html": "text/html", ".js": "application/javascript", ".css": "text/css",
      ".json": "application/json", ".svg": "image/svg+xml", ".ico": "image/x-icon"}


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *a):  # quieter console
        pass

    def _send(self, code, body=b"", ctype="application/json", extra=None):
        if isinstance(body, str):
            body = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if body:
            self.wfile.write(body)

    # ---- CORS preflight: a cross-origin POST /api/scan (Content-Type: application/json)
    # from the Vercel-hosted dashboard triggers an OPTIONS preflight. Answer it. ----
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Max-Age", "86400")
        self.send_header("Content-Length", "0")
        self.end_headers()

    # ---- GET: static files + history + SSE stream ----
    def do_GET(self):
        path = self.path.split("?", 1)[0]

        if path.startswith("/api/stream/"):
            return self._stream(path.rsplit("/", 1)[-1])
        if path == "/api/history":
            return self._send(200, json.dumps(_history()))
        if path.startswith("/api/scan/"):
            return self._send(200, json.dumps(_one_scan(path.rsplit("/", 1)[-1])))

        # static
        rel = "index.html" if path in ("/", "") else path.lstrip("/")
        fp = (DASH / rel).resolve()
        if not str(fp).startswith(str(DASH.resolve())) or not fp.is_file():
            return self._send(404, "not found", "text/plain")
        ctype = CT.get(fp.suffix, "application/octet-stream")
        self._send(200, fp.read_bytes(), ctype)

    # ---- POST: start a scan ----
    def do_POST(self):
        if self.path.split("?", 1)[0] != "/api/scan":
            return self._send(404, "not found", "text/plain")
        try:
            n = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(n) or b"{}")
        except Exception:
            body = {}
        preset = (body.get("preset") or "fast").lower()
        url = (body.get("url") or "").strip()
        if preset not in ("demo", "hr", "cowork") and not re.match(r"^https?://", url):
            return self._send(400, json.dumps({"error": "Enter a valid http(s) URL"}))

        job_id = uuid.uuid4().hex[:12]
        JOBS[job_id] = {"q": queue.Queue(), "done": False, "report": None, "error": None}
        threading.Thread(target=_run_job, args=(job_id, url, preset), daemon=True).start()
        self._send(200, json.dumps({"job_id": job_id}))

    def _stream(self, job_id):
        job = JOBS.get(job_id)
        if not job:
            return self._send(404, json.dumps({"error": "unknown job"}))
        self.close_connection = True  # stream until we close it (no content-length)
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "close")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        q = job["q"]
        try:
            while True:
                ev = q.get()
                if ev is None:
                    break
                self.wfile.write(f"data: {json.dumps(ev)}\n\n".encode())
                self.wfile.flush()
                if ev.get("kind") in ("done", "error"):
                    break
        except (BrokenPipeError, ConnectionResetError):
            pass


def _history() -> list:
    try:
        import store
        rows = store.pull_all()
        if rows:
            return [_summary(r) for r in rows]
    except Exception:
        pass
    idx = ROOT / "scans" / "index.json"
    return json.loads(idx.read_text()) if idx.exists() else []


def _summary(r: dict) -> dict:
    return {
        "id": (re.sub(r"[^a-z0-9]+", "-", str(r.get("target", "")).lower()).strip("-")[:40]),
        "target": r.get("target"), "mode": r.get("mode"),
        "generated_at": r.get("generated_at"), "breaches": r.get("breaches"),
        "total_attacks": r.get("total_attacks"),
        "by_severity": dict(Counter(f.get("severity") for f in (r.get("findings") or []))),
    }


def _one_scan(scan_id: str) -> dict:
    try:
        import store
        for r in store.pull_all():
            sid = re.sub(r"[^a-z0-9]+", "-", str(r.get("target", "")).lower()).strip("-")[:40]
            if scan_id in (sid, r.get("generated_at")):
                return r
    except Exception:
        pass
    idx = ROOT / "scans" / "index.json"
    if idx.exists():
        for e in json.loads(idx.read_text()):
            if e.get("id") == scan_id:
                return json.loads((ROOT / e["file"]).read_text())
    return {}


def main():
    have_key = bool(os.environ.get("ANTHROPIC_API_KEY"))
    srv = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"\n  ROGUE server → http://localhost:{PORT}")
    print(f"  live scans: {'ENABLED' if have_key else 'no ANTHROPIC_API_KEY — demo only'}")
    print(f"  serving {DASH}\n")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n  bye")


if __name__ == "__main__":
    main()
