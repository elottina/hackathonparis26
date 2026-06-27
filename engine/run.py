"""Rogue CLI.

    python run.py --target demo
    python run.py --target http --url https://example.com/agent
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import strategies as strat
from orchestrator import run_swarm
from sink import EgressSink
from target import DEMO_SECRET, DemoTarget, HTTPTarget, NaiveToolTarget, ToolTarget

SEV_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}
COLOR = {"critical": "\033[91m", "high": "\033[93m", "medium": "\033[96m",
         "low": "\033[90m", "ok": "\033[92m", "dim": "\033[90m", "off": "\033[0m"}


def live_printer(event: dict):
    k = event["kind"]
    if k == "attack_start":
        print(f"{COLOR['dim']}  ▶ launching: {event['strategy_name']} "
              f"(run {event['run_id']}){COLOR['off']}")
    elif k == "tool_call":
        if event.get("contains_secret") and event.get("external"):
            print(f"{COLOR['critical']}  ⇄ EGRESS  {event['tool']} → {event['host']}  "
                  f"[SECRET EXFILTRATED]{COLOR['off']}")
        else:
            print(f"{COLOR['dim']}  ⇄ tool call: {event['tool']} → "
                  f"{event.get('host') or '(local)'}{COLOR['off']}")
    elif k == "breach":
        c = COLOR.get(event["severity"], "")
        tag = " ⚡BEHAVIOR" if event.get("detection") == "behavior" else ""
        print(f"{c}  ✖ BREACH [{event['severity'].upper()}]{tag} {event['strategy_name']} "
              f"→ {event['ai_act_article']}{COLOR['off']}")
        print(f"{COLOR['dim']}      evidence: {event['evidence'][:120]}{COLOR['off']}")
    elif k == "attack_failed":
        print(f"{COLOR['ok']}  ✓ held: run {event['run_id']} "
              f"({event['strategy']}){COLOR['off']}")


def build_target(args):
    if args.target == "mock":
        from mock import MockTarget
        return MockTarget()
    if args.target == "demo":
        return DemoTarget()
    if args.target == "tool":
        return ToolTarget()
    if args.target == "naive":
        return NaiveToolTarget()
    if args.target == "http":
        if not args.url:
            sys.exit("--url is required for --target http")
        return HTTPTarget(args.url)
    sys.exit(f"unknown target: {args.target}")


async def main():
    ap = argparse.ArgumentParser(description="Rogue — red-team swarm for AI agents")
    ap.add_argument("--target", default="demo",
                    choices=["demo", "http", "mock", "tool", "naive"])
    ap.add_argument("--url", help="target URL for --target http")
    ap.add_argument("--strategies", nargs="*", help="subset of strategy keys")
    ap.add_argument("--runs", type=int, default=3, help="attackers per strategy")
    ap.add_argument("--turns", type=int, default=5, help="max turns per attack")
    ap.add_argument("--out", default="findings.json")
    ap.add_argument("--seeded", action="store_true",
                    help="deterministic stage replay: offline target, guaranteed "
                         "behavior-oracle exfiltration, zero API calls")
    ap.add_argument("--listen", action="store_true",
                    help="start the real attacker callback listener and perform the "
                         "agent's egress for real — a network arrival of the secret "
                         "is the PRIMARY breach signal (works against text-only "
                         "targets too)")
    ap.add_argument("--listen-port", type=int, default=0,
                    help="port for the callback listener (default: ephemeral)")
    args = ap.parse_args()

    if args.seeded:
        # The stage path: never rely on a live model discovering the exfil. Force
        # the deterministic offline swarm so the behavior-oracle moment fires the
        # same way every single time.
        args.target = "mock"
        print(f"\n  {COLOR['critical']}● SEEDED DETERMINISTIC REPLAY{COLOR['off']}"
              f"{COLOR['dim']} — offline, guaranteed behavior-oracle exfil{COLOR['off']}")

    target = build_target(args)
    chosen = strat.get(args.strategies)

    print(f"\n  ROGUE  ·  target: {target.name}")
    print(f"  swarm: {len(chosen)} strategies × {args.runs} attackers "
          f"= {len(chosen) * args.runs} concurrent attacks\n")

    swarm_kwargs = {}
    if args.target == "mock":
        from mock import MockAttacker, MockJudge
        swarm_kwargs = {"attacker": MockAttacker(), "judge": MockJudge()}
    elif args.target == "naive":
        # Deterministic, known-effective injections delivered to a REAL model. The
        # attack input is fixed (our playbook); the target's decision to exfiltrate
        # is genuine — that's what makes the behavior breach both real and reliable.
        from mock import MockAttacker
        swarm_kwargs = {"attacker": MockAttacker()}

    sink = EgressSink(DEMO_SECRET)

    # The real callback listener (Option 2): when enabled, the agent's egress is
    # performed for real and a secret arriving on the wire is the primary breach.
    listener = None
    if args.listen:
        from egress import EgressClient
        from listener import SinkListener

        def on_arrival(ev):
            tag = "[SECRET ARRIVED]" if ev.get("contains_secret") else ""
            c = COLOR["critical"] if ev.get("contains_secret") else COLOR["dim"]
            print(f"{c}  ◀ SINK  {ev['method']} {ev.get('host') or '?'}  "
                  f"{tag}{COLOR['off']}")

        listener = SinkListener(sink, port=args.listen_port, on_arrival=on_arrival)
        listener.start()
        swarm_kwargs["egress"] = EgressClient(redirect_to=listener.base)
        print(f"  {COLOR['critical']}● LISTENER{COLOR['off']} attacker collector "
              f"on {listener.url} — secret-on-the-wire = confirmed breach\n")

    try:
        results = await run_swarm(
            target, chosen, runs_per_strategy=args.runs,
            max_turns=args.turns, on_event=live_printer, sink=sink, **swarm_kwargs,
        )
    finally:
        if listener:
            listener.stop()

    breaches = [r for r in results if r.get("success")]
    # Pin behavior-oracle breaches first (the differentiator), then by severity.
    breaches.sort(key=lambda r: (0 if r.get("detection") == "behavior" else 1,
                                 SEV_ORDER.get(r.get("severity", "low"), 9)))

    report = {
        "target": target.name,
        "mode": "deterministic replay" if args.seeded else "live scan",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_attacks": len(results),
        "breaches": len(breaches),
        "behavior_breaches": sum(1 for b in breaches if b.get("detection") == "behavior"),
        "findings": breaches,
        "egress": sink.public_log(),
    }
    with open(args.out, "w") as f:
        json.dump(report, f, indent=2)

    # Also emit the dashboard data file so dashboard/index.html renders the latest
    # scan with zero setup (open it directly, no server flags needed).
    try:
        dash = Path(__file__).resolve().parent.parent / "dashboard"
        if dash.exists():
            (dash / "data.js").write_text(
                "window.ROGUE_FINDINGS = " + json.dumps(report) + ";\n"
            )
    except Exception:
        pass

    print(f"\n  {'─' * 50}")
    print(f"  {len(breaches)}/{len(results)} attacks breached the target")
    for b in breaches:
        c = COLOR.get(b["severity"], "")
        print(f"  {c}● {b['severity'].upper():8} {b['strategy_name']:28} "
              f"{b['ai_act_article']}{COLOR['off']}")
    print(f"\n  full report → {args.out}\n")


if __name__ == "__main__":
    asyncio.run(main())
