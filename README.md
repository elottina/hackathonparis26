# Rogue

**Autonomous red-teaming for AI agents, focused on HR / CV-screening agents.**

Rogue points an attacker swarm at an AI agent and reports how it can be broken:
prompt extraction, jailbreaks, candidate PII leaks, biased screening behavior, missing human
oversight, and unauthorized tool use. Its core difference is the **behavior oracle**:
Rogue grades what the agent **did** — tool calls and data egress — not only what it said in the
chat response.

The attackers run **in parallel and adapt** — when a probe is refused, that refusal becomes
information and the next turn changes tactic, with **zero humans in the loop**.

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
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-... # Windows: set ANTHROPIC_API_KEY=...
```

Run the local dashboard:

```bash
python server.py                    # http://localhost:8799  (override with ROGUE_PORT)
```

Then open **http://localhost:8799** and pick one of the three one-click demo presets:

| Preset | Target | What it proves |
| --- | --- | --- |
| **Scan a live HR agent** (`hr`) | **TalentScreen** — a real Claude-powered, *black-box* CV-screening agent (exposes zero tools) | The behavior oracle works with **no tool visibility**: the candidate's name physically arrives on the wire while the written recommendation reads clean. The hero demo. |
| **Red-team a real production agent** (`cowork`) | **Cowork** — a real, shipping AI agent used for CV screening | Rogue scans a genuine production agent live (design partner #1). |
| **Watch the 20-second demo** (`demo`) | FinBuddy (offline mock) | Deterministic, zero-API-call backup so the on-stage moment can never fail. |

Run the deterministic demo from the CLI (no API key needed):

```bash
python run.py --seeded
```

To scan your own agent, paste its URL into the dashboard, or point Rogue at any endpoint that accepts:

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

## Pitch deck, video & proof

- **[pitch-deck.html](./pitch-deck.html)** — the submission deck (13 slides, self-contained, arrow-key nav). Open in any browser; print to PDF for 16:9.
- **[Rogue-Pitch-Deck.pdf](./Rogue-Pitch-Deck.pdf)** — the exported deck PDF.
- [DECK.md](./DECK.md) — slide-by-slide copy + rubric mapping.
- [VIDEO-SCRIPT.md](./VIDEO-SCRIPT.md) — the final ≤5-min two-speaker narration (timecoded, slide-synced).
- [VIDEO-DIRECTION.md](./VIDEO-DIRECTION.md) — video direction notes: 60s cut and capture list.

**Proof, not vibes:** every number on the deck comes from a committed scan you can open:

- [`/scans`](./scans) — real saved scans. The HR black-box breach (TalentScreen, the candidate's name arriving at `lookup.talent-verify.io`) and the live Cowork scan are here.
- [`clarity_deep_findings.json`](./clarity_deep_findings.json) — the deep adaptive run on the third-party Clary agent (60 attacks → 29 graded breaches).
- The **offline deterministic mock** (FinBuddy) — the zero-API demo backup — is saved under [`/scans`](./scans) as the `*-finbuddy-offline-mock-target.json` runs; `python run.py --seeded` regenerates it to `findings.json`.

## Business Direction

Current documents:

- [FINAL-PRODUCT-DECISION.md](./FINAL-PRODUCT-DECISION.md) — locked direction and demo arc
- [PITCH.md](./PITCH.md) — deck and video script
- [PRICING.md](./PRICING.md) — pricing, unit economics, Q&A
- [GTM.md](./GTM.md) — scan-as-lead-gen and first €10K plan
- [COMPETITION.md](./COMPETITION.md) — differentiation and moat
- [MARKET-ANALYSIS.md](./MARKET-ANALYSIS.md) — full market/rubric synthesis
- [ROADMAP.md](./ROADMAP.md) — tactical next-8-weeks plan
- [PROJECTION.md](./PROJECTION.md) — long-horizon 0–36-month projection (revenue, moat, funding, risks)

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
