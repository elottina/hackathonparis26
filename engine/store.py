"""Optional cloud persistence: sync each scan to a Supabase Postgres table.

Why: files in scans/ are the local source of truth, but for the DEPLOYED dashboard
to show every scan (and so nothing is ever lost across machines), each scan also
gets pushed to a `scans` table in Supabase.

Activation is zero-config: if SUPABASE_URL + SUPABASE_KEY are set (e.g. in
engine/.env), run.py syncs automatically; if not, it's a silent no-op. Table schema
lives in db/schema.sql.

    SUPABASE_URL=https://<project>.supabase.co
    SUPABASE_KEY=<service_role key>   # server-side only; never ship to the frontend
"""
from __future__ import annotations

import os


def push_scan(report: dict) -> str | None:
    """Insert one scan report into Supabase. Returns the row id, or None if not
    configured / on any error (never raises — persistence to files already happened)."""
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if not (url and key):
        return None

    row = {
        "target": report.get("target"),
        "mode": report.get("mode"),
        "generated_at": report.get("generated_at"),
        "total_attacks": report.get("total_attacks"),
        "breaches": report.get("breaches"),
        "behavior_breaches": report.get("behavior_breaches", 0),
        "report": report,          # full report in a jsonb column
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
