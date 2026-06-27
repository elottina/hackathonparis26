"""Backfill: push every archived scan in scans/ to the cloud (Firestore).

Run this once after Firestore is enabled to upload all historical scans:

    python engine/sync_all.py

It reads scans/index.json, loads each scan file, and calls store.push_scan on it.
Safe to re-run: documents are keyed by scan id, so re-syncing overwrites in place
instead of creating duplicates. No-op (prints a hint) if the cloud isn't configured.
"""
from __future__ import annotations

import json
from pathlib import Path

import store

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    idx_path = ROOT / "scans" / "index.json"
    if not idx_path.exists():
        print("no scans/index.json — run a scan first")
        return
    index = json.loads(idx_path.read_text())
    print(f"syncing {len(index)} scan(s) to the cloud…")
    ok = 0
    for entry in index:
        f = ROOT / entry["file"]
        if not f.exists():
            print(f"  ! missing {entry['file']}")
            continue
        report = json.loads(f.read_text())
        sid = store.push_scan(report)
        if sid:
            ok += 1
            print(f"  ✓ {entry['target'][:40]:40}  → {sid}")
        else:
            print(f"  · {entry['target'][:40]:40}  (not synced)")
    print(f"\ndone: {ok}/{len(index)} synced")


if __name__ == "__main__":
    main()
