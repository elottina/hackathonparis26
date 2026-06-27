"""The orchestrator: fan out the attacker swarm in parallel and aggregate.

Each "attacker" runs a multi-turn conversation against the target for one
strategy, with the judge scoring every turn. We launch many of these at once
(asyncio) so hundreds of attacks run concurrently. That parallelism is the
unfair advantage made visible in the demo.
"""
from __future__ import annotations

import asyncio
from typing import Callable

from attacker import Attacker
from judge import Judge
from strategies import Strategy
from target import Target


async def run_attack(
    target: Target,
    strategy: Strategy,
    attacker: Attacker,
    judge: Judge,
    run_id: int,
    max_turns: int = 5,
    on_event: Callable[[dict], None] | None = None,
) -> dict:
    """One attacker vs the target for one strategy, up to max_turns."""
    transcript: list[dict] = []   # from the target's perspective
    history: list[dict] = []      # what we feed the target

    def emit(kind: str, **kw):
        if on_event:
            on_event({"kind": kind, "run_id": run_id,
                      "strategy": strategy.key, **kw})

    emit("attack_start", strategy_name=strategy.name)

    for turn in range(1, max_turns + 1):
        msg = await attacker.next_message(strategy, transcript, turn)
        emit("attacker_msg", turn=turn, text=msg)

        reply = await target.send(msg, history)
        emit("target_reply", turn=turn, text=reply)

        history.append({"role": "user", "content": msg})
        history.append({"role": "assistant", "content": reply})
        transcript.append({"role": "user", "content": msg})
        transcript.append({"role": "assistant", "content": reply})

        finding = await judge.evaluate(strategy, msg, reply)
        if finding["success"]:
            finding.update(run_id=run_id, turns=turn,
                           attacker_msg=msg, target_reply=reply)
            emit("breach", **finding)
            return finding

    emit("attack_failed", turns=max_turns)
    return {"strategy": strategy.key, "strategy_name": strategy.name,
            "success": False, "run_id": run_id, "turns": max_turns}


async def run_swarm(
    target: Target,
    strategies: list[Strategy],
    runs_per_strategy: int = 3,
    max_turns: int = 5,
    concurrency: int = 12,
    on_event: Callable[[dict], None] | None = None,
) -> list[dict]:
    """Launch runs_per_strategy attackers per strategy, capped at `concurrency`."""
    attacker = Attacker()
    judge = Judge()
    sem = asyncio.Semaphore(concurrency)

    async def guarded(strategy: Strategy, run_id: int):
        async with sem:
            return await run_attack(target, strategy, attacker, judge,
                                    run_id, max_turns, on_event)

    tasks = []
    rid = 0
    for s in strategies:
        for _ in range(runs_per_strategy):
            rid += 1
            tasks.append(guarded(s, rid))

    return await asyncio.gather(*tasks)
