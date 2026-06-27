"""Hydra CLI.

    python run.py --target demo
    python run.py --target http --url https://example.com/agent
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from datetime import datetime, timezone

import strategies as strat
from orchestrator import run_swarm
from target import DemoTarget, HTTPTarget

SEV_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}
COLOR = {"critical": "\033[91m", "high": "\033[93m", "medium": "\033[96m",
         "low": "\033[90m", "ok": "\033[92m", "dim": "\033[90m", "off": "\033[0m"}


def live_printer(event: dict):
    k = event["kind"]
    if k == "attack_start":
        print(f"{COLOR['dim']}  ▶ launching: {event['strategy_name']} "
              f"(run {event['run_id']}){COLOR['off']}")
    elif k == "breach":
        c = COLOR.get(event["severity"], "")
        print(f"{c}  ✖ BREACH [{event['severity'].upper()}] {event['strategy_name']} "
              f"→ {event['ai_act_article']}{COLOR['off']}")
        print(f"{COLOR['dim']}      evidence: {event['evidence'][:120]}{COLOR['off']}")
    elif k == "attack_failed":
        print(f"{COLOR['ok']}  ✓ held: run {event['run_id']} "
              f"({event['strategy']}){COLOR['off']}")


def build_target(args):
    if args.target == "demo":
        return DemoTarget()
    if args.target == "http":
        if not args.url:
            sys.exit("--url is required for --target http")
        return HTTPTarget(args.url)
    sys.exit(f"unknown target: {args.target}")


async def main():
    ap = argparse.ArgumentParser(description="Hydra — red-team swarm for AI agents")
    ap.add_argument("--target", default="demo", choices=["demo", "http"])
    ap.add_argument("--url", help="target URL for --target http")
    ap.add_argument("--strategies", nargs="*", help="subset of strategy keys")
    ap.add_argument("--runs", type=int, default=3, help="attackers per strategy")
    ap.add_argument("--turns", type=int, default=5, help="max turns per attack")
    ap.add_argument("--out", default="findings.json")
    args = ap.parse_args()

    target = build_target(args)
    chosen = strat.get(args.strategies)

    print(f"\n  HYDRA  ·  target: {target.name}")
    print(f"  swarm: {len(chosen)} strategies × {args.runs} attackers "
          f"= {len(chosen) * args.runs} concurrent attacks\n")

    results = await run_swarm(
        target, chosen, runs_per_strategy=args.runs,
        max_turns=args.turns, on_event=live_printer,
    )

    breaches = [r for r in results if r.get("success")]
    breaches.sort(key=lambda r: SEV_ORDER.get(r.get("severity", "low"), 9))

    report = {
        "target": target.name,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_attacks": len(results),
        "breaches": len(breaches),
        "findings": breaches,
    }
    with open(args.out, "w") as f:
        json.dump(report, f, indent=2)

    print(f"\n  {'─' * 50}")
    print(f"  {len(breaches)}/{len(results)} attacks breached the target")
    for b in breaches:
        c = COLOR.get(b["severity"], "")
        print(f"  {c}● {b['severity'].upper():8} {b['strategy_name']:28} "
              f"{b['ai_act_article']}{COLOR['off']}")
    print(f"\n  full report → {args.out}\n")


if __name__ == "__main__":
    asyncio.run(main())
