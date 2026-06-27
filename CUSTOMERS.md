# Rogue — Real-Customer Landing Playbook

**Goal before judging: 3 design partners + ≥1 real reproduced vuln + ≥1 "yes I'd pay $X/mo" on record.** This is the single thing the YC jury rewards most. Over-index here.

---

## ICP filter (qualify any contact in <30s)
- **Shipped/staging agent NOW?** A customer-facing agent live or in staging (support bot, chat widget, copilot, automation), pointable at a URL. Just an idea → deprioritize.
- **Tools / private data?** Can it DO things — call APIs, query a DB, read user records, take actions (refunds, bookings, send email, code/PRs)? Tool-using or data-touching = **P0** (the behavior-oracle demo is strong). Pure FAQ bot = weak.
- **Selling up-market?** Selling (or trying to) to bigger/regulated companies → the "a security questionnaire is blocking my deal" wedge applies → higher willingness-to-pay.
- **Founder reachable in one hop?** Can you DM the founder/CTO and get a yes with no procurement/committee? At seed–Series B the founder owns agent risk by default.
- **Access in <1 day?** Can they hand you a staging endpoint (or OK to hit prod) today without a 2-week review of *you*?
- **WTP tell:** have they recently gotten a security questionnaire / SOC2 ask / "is your AI safe?" from a prospect? A yes = acute pain now = realistic paid-pilot close.

## Who to hit (prioritized)
| Pri | Archetype | Why | Where |
|---|---|---|---|
| **P0** | **Other hackathon teams in THIS room building agents** | Killer non-obvious source: live endpoint, proud, 5m away, instant consent. A same-day breach report = instant social proof + "we red-teamed another team's agent and leaked X in 4 min." **Run these FIRST Saturday.** | Walk the room Sat AM; project board / Discord: "who's building an agent that calls tools or an MCP server?" Offer free QA before their demo. |
| **P0** | Founder friends w/ a live support/chat agent selling to businesses | Exact ICP; 5-min yes; acute pain; endpoint drops straight into HTTPTarget; best shot at a revenue-tied quote | Federica's direct network; founder WhatsApp/Telegram groups; filter for "AI assistant / copilot / chat" on their site |
| **P0** | Founder friends w/ a tool-using / automation agent (refunds, bookings, emails, ops, code/PRs) | Highest-drama oracle demo — an unauthorized tool call / exfil is more visceral than a leaked string | Devtool / AI-ops founders; YC batch Slack two hops away; "does your agent take actions for users?" |
| **P1** | MCP-connected copilot builders | Newest, least-tested surface; they KNOW MCP is unsafe → easy yes; most novel demo | MCP/Anthropic Discords, r/mcp, MCP server repo authors, room teams wiring MCP |
| **P1** | Friends-of-friends via a warm intro from a teammate | Warm > cold 10×; each teammate mines their own network in parallel | Ask teammates + mentors: "who do you know shipping a customer-facing agent?" |
| **P2** | AI-builder Discord/Slack/X communities | Volume top-of-funnel; "I'll free-red-team the first 3 agents posted below" is itself marketing | Post the offer in 3–4 builder communities Sat AM |
| **P2** | Public / open demo agents (no permission needed) | Backstop for your own testing/screenshots; anonymize, get retro-consent before naming | Product Hunt AI launches this week; "try our chatbot" widgets; public HF Spaces |

## Cadence (mapped to the 30h)
- **Sat 10:00–10:30** — split networks. Federica fires 15–20 warm DMs (P0/P1). DEV-CORE + DEV-2 each grab the room: ID 5–8 teams w/ tool/MCP agents, book afternoon "free 5-min red-team" slots. Post public offer in 3–4 communities.
- **Sat 10:30–12:00** — work the room **in person**; lock ≥1 in-person target before lunch so you're never empty-handed.
- **Sat 12:00–16:00** (scan engine ready) — as endpoints arrive, run the scan, send **report-lite** SAME DAY. Speed converts. Target: 3 real scans by Sat evening.
- **Sat 16:00–19:00** — bump non-repliers with a one-line + a real (anonymized) breach screenshot. Social proof doubles reply rate.
- **Sat 21:00–22:00** — send each partner their ranked report + readiness one-pager + soft testimonial ask. Let it marinate.
- **Sun 09:00–11:00** — collect quotes. Call/DM warmest 2–3, read them their own finding, ask the WTP question live. Capture: logo + on-record quote + "$X/mo." Screenshot every yes.
- **Sun 11:00–12:00** — lock traction slide. Freeze outreach, rehearse.

## The 3 DMs (copy-paste, warm, founder-to-founder)
**Support / chatbot agent →** *"Hey [name] — quick one. I'm at [hackathon] building automated red-teaming for AI agents, and I want to break YOURS, for free, this weekend. Send me a link to [product]'s support bot (or a staging endpoint) and in a couple hours I'll send back a ranked report of how I'd jailbreak it, get it to leak another user's data, or talk it into something it shouldn't do — plus a 1-page 'AI security & EU AI Act readiness' sheet you can forward to your next enterprise prospect's security review. All I ask back: a 2-line quote if it's useful + an OK to call [Company] a design partner. Got 5 mins to send me the link?"*

**Tool-using / automation agent →** *"[name] — your agent that [books/refunds/sends/automates] is exactly what I'm building a red team for. This weekend I'll point an autonomous attacker swarm at it, FREE, and show you not just what it SAYS but what it actually DID — e.g. an unauthorized tool call or data quietly leaving to a sink while the chat reply looks innocent. You get a ranked vuln report (OWASP Agentic Top 10 + the EU AI Act articles it touches) same day. Tiny catch: if it's useful, a 2-line quote + permission to show your logo. Drop me a staging endpoint in the next hour?"*

**MCP copilot →** *"Hey [name] — saw you're wiring [copilot] to MCP servers/tools. You already know MCP is the least-tested attack surface right now (tool-description poisoning, the lethal trifecta). I'm building a self-serve red team for exactly this and I'll run it against your copilot for free this weekend — graded on real tool calls + egress, not string-matching. You'll get a reproducible trace of any exfil/hijack + an audit-ready report your next enterprise buyer's security team will ask for. In exchange: a short quote + OK to name you as a design partner. Just need a staging URL or your tool config — 5 mins."*

## What a real customer must provide (access tiers — we're black-box, never need their code)
**Principle: Rogue red-teams from the OUTSIDE. We never need their source code.** What a prospect must HAVE to be scannable:

**Floor — unlocks text-graded findings (jailbreak, system-prompt leak, policy/advice violations):**
1. **A callable agent surface** — *one* of: (a) an **HTTP endpoint** (any request/response shape — we write a ~15-line shim; auth via a scoped staging token in a header), or (b) a public/staging **chat widget or web app** we drive via browser automation (zero integration on their side). If their agent has *no* callable surface (mobile-only / embedded — the hard case, e.g. **Clarity**), they stand up **one thin staging `/chat` endpoint** from a ~30-line template we hand them — that code is *theirs*, never shared with us.
2. **Written permission** — scope + time window + **prod vs staging** (always prefer staging). Non-negotiable.
3. **Their "must never do" list** — guardrails/policies, even informal ("never gives financial advice", "never reveals another user's data"). Defines what counts as a breach.
4. **(Best) a planted canary** — one unique fake "other-customer record" / fake API key seeded in staging; the judge flags it CRITICAL the instant it surfaces = cleanest, most objective finding.

**Upgrade — unlocks the BEHAVIOR ORACLE (what the agent DID), still no code:**
- They **register one tool / MCP endpoint we provide** in their staging agent config → our sink catches any exfil / unauthorized action, **or**
- They **share tool-call traces** (LangSmith / Datadog LLM-obs / their own logs) → we grade the trajectory, **or**
- Their staging agent can make outbound calls → we hand them a **unique callback sink URL**; any data that arrives = proof.
- Can't wire any of these in time → fall back to text-graded (still real findings).

**Practical heads-ups (say them — they build trust):** scanning makes real model calls (their token cost) and can trip rate-limits/alerts → staging + a heads-up; attacks can create junk records → throwaway account / staging DB.

**Qualifier for the hunt:** a prospect is scannable *today* if they have **at least a callable surface** (endpoint or widget). That's the 5-minute-yes filter. No surface at all → they expose one thin endpoint first.

## Running the scan fast
Fastest path (no install): a URL taking `POST {message, history} → {reply}` *is* the Hydra `HTTPTarget` contract. Most partners won't match exactly → DEV-CORE keeps a ~15-line **shim** per partner (translate body, pull `.reply`; OpenAI-style `{choices…}`, widget WS frame, etc.) ~5–20 min each. No clean API? drive the widget with claude-in-chrome as a last-resort backend. **Plant a canary:** seed a unique fake "other-customer record"/API key — the judge's verbatim shortcut flags it CRITICAL the instant it appears = cleanest finding. **Behavior oracle (if it calls tools):** give them our dummy tool + sink to wire in; grade on what hit the sink. Can't wire in time → fall back to TEXT-graded findings (already works), note tool-action coverage as "continuous tier."
**Deliverable, same day:** (1) ranked report — findings by severity, each w/ trace + OWASP/LLM Top 10 + MITRE ATLAS + EU AI Act article + a 1-line fix; (2) 1-page "Agent Security & EU AI Act Readiness" one-pager to forward. **Turnaround target: in their hands within 2h of getting the endpoint.**

## Turn a scan into a testimonial (run AFTER they've seen a real finding)
1. **Logo + quote:** "This took ~10 min and found [specific finding]. Two asks: show [Company]'s logo on our design-partners slide, and quote you on one line — I'll draft it, you approve." Hand them a **pre-written** quote (one tap to approve): *"Rogue found a data-leak in our production agent in under 10 minutes — exactly the report our enterprise security reviews keep asking for. — [name], CEO of [Company]."*
2. **WTP number (what YC probes):** "If this ran continuously and gave you the audit-ready evidence for security questionnaires — is that a $500, $1K, or $2K/mo thing at your stage?" Anchoring 3 numbers gets a pick. Capture on record.
3. **Revenue tie (strongest):** if they have a stuck deal → "this is exactly the report our prospect's security team asked for." Screenshot every yes (DM, not verbal). **Target by Sun 11:00: 3 logos + 1 reproduced-vuln quote + 1 WTP number.**

## If no real target is reachable (never empty-handed)
- **Tier 1 (almost always works):** the hackathon room IS the design-partner pool — break 2–3 teams' agents in person Saturday → real findings on real shipping agents + on-the-spot quotes. Satisfies the "real users this weekend" bonus by itself.
- **Tier 2:** a public "try our AI" widget / public MCP/HF Space — use for your own demo + anonymized screenshots, retro-consent before naming.
- **Tier 3 (always-works backstop, framed honestly):** FinBuddy DemoTarget — say it straight: "our reference target, deliberately soft, so the demo is deterministic and you see the oracle clearly — and we ran it live against [N] real founders' agents this weekend, here are those findings."
- **CRITICAL:** never let the *demo* depend on a partner endpoint being up during judging. Always demo on FinBuddy (can't fail); present real-partner breaches as traction screenshots alongside.
