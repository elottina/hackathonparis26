# Rogue

**Autonomous red-teaming for AI agents, focused on HR / CV-screening agents.**

Rogue points an attacker swarm at an AI agent and reports how it can be broken:
prompt extraction, jailbreaks, candidate PII leaks, biased screening behavior, missing human
oversight, and unauthorized tool use. Its core difference is the **behavior oracle**:
Rogue grades what the agent **did** — tool calls and data egress — not only what it said in the
chat response.

The beachhead is **AI HR / CV-screening agents**, an EU AI Act Annex III high-risk workflow.
Rogue turns each confirmed finding into an evidence-backed report mapped to GDPR / AI Act risk.

Built for Paris Builds 2026 — track: *Software for Agents*.

## Why Rogue Exists

A screening agent can look safe in chat while doing something unsafe behind the scenes:

> "I recommend this candidate based only on the CV."  
> Meanwhile: a tool call sends the candidate's name and data to an external lookup endpoint.

Text-only red-team tools miss that. Rogue watches the action channel.

Pitch line:

> **We grade what the agent did, not what it said.**

## How It Works

```
target agent (URL / API / staging endpoint)
        |
        v
autonomous attacker swarm
        |
        v
target replies + tool calls + egress events
        |
        v
judge + behavior oracle
        |
        v
AI Act / GDPR mapped report
```

Key modules:

- `engine/strategies.py` — attack playbook, including HR/privacy/bias/tool-exfiltration probes
- `engine/attacker.py` — attacker agent that adapts turn by turn
- `engine/orchestrator.py` — runs the swarm concurrently
- `engine/target.py` — demo, tool-enabled, and HTTP target adapters
- `engine/sink.py` — deterministic egress sink for the behavior oracle
- `engine/oracle.py` — converts confirmed egress into critical behavior findings
- `engine/server.py` — local dashboard + scan API
- `dashboard/` — browser UI for live scans and archived reports

## Quickstart

```bash
cd engine
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
set ANTHROPIC_API_KEY=sk-ant-...
```

Run the local dashboard:

```bash
python server.py
```

Open:

```text
http://localhost:8799
```

Run the deterministic demo from CLI:

```bash
python run.py --seeded
```

Run the HR demo from the dashboard by choosing the HR preset, or scan a real endpoint that accepts:

```json
POST /chat
{
  "message": "...",
  "history": [{"role": "user", "content": "..."}]
}
```

Expected response:

```json
{
  "reply": "...",
  "tool_calls": [
    {"name": "web_search", "arguments": {"url": "https://example.com", "body": "..."}}
  ]
}
```

For basic text-graded scans, `reply` is enough. For behavior-oracle findings, Rogue needs a canary,
tool-call trace, callback sink hit, or staging tool integration.

## Business Direction

Current documents:

- [FINAL-PRODUCT-DECISION.md](./FINAL-PRODUCT-DECISION.md) — locked direction and demo arc
- [PITCH.md](./PITCH.md) — deck and video script
- [PRICING.md](./PRICING.md) — pricing, unit economics, Q&A
- [GTM.md](./GTM.md) — scan-as-lead-gen and first €10K plan
- [COMPETITION.md](./COMPETITION.md) — differentiation and moat
- [MARKET-ANALYSIS.md](./MARKET-ANALYSIS.md) — full market/rubric synthesis

Important positioning:

- HR/CV-screening AI is Annex III high-risk.
- Use **2 Dec 2027** as the pitch-safe high-risk timeline, not the stale Aug-2026 line.
- Urgency today comes from enterprise review, legal review, and evidence-building.
- Do not claim "first to red-team agents"; claim the action/egress channel.

## Scope

Hackathon scope:

- Paste-a-URL scan
- Autonomous attacker swarm
- HR screening demo
- Behavior oracle via sink/listener/canary
- AI Act / GDPR mapped report
- Local dashboard and scan archive

Not in this build:

- Full certification product
- Full MCP proxy / CI/CD integration
- Billing, auth, or multi-tenant SaaS
