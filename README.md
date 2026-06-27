# Rogue

**Penetration testing for AI agents, run by an AI agent.**

Rogue is an autonomous red-team swarm. You point it at any deployed AI agent (a
URL, an API endpoint, a chat widget) and it spawns attacker agents that adapt in
real time to break the target: extract its system prompt, jailbreak its policy,
leak data, trigger unauthorized actions. Agent-on-agent, no human in the core
loop.

Every confirmed vulnerability is mapped to the specific **EU AI Act** obligation
it violates, producing the conformity evidence the buyer is legally required to
hold.

Built for Paris Builds 2026 — track: *Software for Agents*.

## How it works

```
        target agent (URL / API)
                  ^
                  |  adversarial conversations
                  |
   ┌──────────────┴───────────────┐
   │        Orchestrator          │   runs N attackers in parallel (asyncio)
   └──────────────┬───────────────┘
                  |
   ┌──────────────┴───────────────┐
   │   Attacker agents (swarm)    │   each runs one strategy, adapts per turn
   └──────────────┬───────────────┘
                  |
   ┌──────────────┴───────────────┐
   │           Judge              │   did the attack succeed? severity? AI Act article?
   └──────────────┬───────────────┘
                  |
              findings.json  ->  dashboard
```

- **`engine/target.py`** — adapter to talk to the agent under test. Ships with a
  deliberately vulnerable `DemoTarget` so the whole pipeline runs end to end with
  zero external setup, plus an `HTTPTarget` for real endpoints.
- **`engine/strategies.py`** — the attack playbook (prompt extraction, jailbreak,
  data leak, unauthorized action).
- **`engine/attacker.py`** — an attacker agent that, given a strategy and the
  conversation so far, writes the next adversarial message.
- **`engine/judge.py`** — scores whether the attack landed, its severity, and the
  EU AI Act article it breaks.
- **`engine/orchestrator.py`** — fans out the swarm and aggregates findings.
- **`engine/run.py`** — CLI entry point.

## Quickstart

```bash
cd engine
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...

# Attack the built-in vulnerable demo target:
python run.py --target demo

# Attack a real HTTP agent (expects {"reply": "..."} for a POST {"message": "..."}):
python run.py --target http --url https://example.com/agent
```

Findings are written to `engine/findings.json`.

## Stack

- Python + asyncio for the swarm (cheap parallelism, the unfair advantage).
- Anthropic Claude as the attacker / judge brain (`claude-haiku-4-5` for the
  swarm, `claude-sonnet-4-6` for the judge).
- Dashboard: TBD (Next.js) — reads `findings.json` and shows attacks live.

## Scope (36h)

Build the engine + the live dashboard. No auth, no billing, no multi-tenant.
Pre-test live targets for the demo, map findings to the AI Act, nail the pitch.
