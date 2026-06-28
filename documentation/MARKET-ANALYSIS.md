# Rogue — Market Analysis

*Three things only: **why now**, **the real pain**, **the competition** — and exactly how we differ.
Competitor facts checked against each company's public docs/site as of June 2026. We grade what the
agent **did**, never "how it thinks". Companion to [COMPETITION.md](./COMPETITION.md) and [PITCH.md](./PITCH.md).*

---

## 1. Why now — the EU AI Act turns red-teaming into law

Adversarial testing of AI agents just stopped being optional. The EU AI Act writes our exact scope
into statute — and stating it *precisely* is itself a credibility weapon, because most teams parrot a
date that already moved.

- **Live today:** GPAI obligations in force since Aug 2025; **enforcement powers + fines from 2 Aug 2026**.
- **The date most people get wrong:** high-risk **Annex III** obligations were deferred from Aug 2026 →
  **2 Dec 2027** (Digital Omnibus). So don't pitch an "Aug-2026 fire drill" — pitch *"the obligation is
  certain, the testing is the hard part, build the evidence trail now,"* and correct the date on stage.
- **Fines:** up to **€35M / 7%** of global turnover (prohibited), **€15M / 3%** (high-risk & GPAI) — above GDPR.
- **It literally describes a red-team:** **Art. 15** — systems must "prevent, detect, respond to… data
  poisoning, model poisoning, adversarial examples, confidentiality attacks." **Art. 9** — risk testing
  is a *continuous lifecycle* duty, not a one-off audit. **Art. 14** — human oversight. **Art. 11/12** —
  technical documentation + automatic logging (an evidence trail you must hold).

**The takeaway:** every company shipping a high-risk agent has a clear coming obligation to
adversarially test it and keep evidence — and almost none of the startup vendors have a security team
to do that work today.

---

## 2. The real pain — AI HR / CV-screening agents

We beachhead on the single most legally-loaded slice of that obligation: **AI agents that screen CVs**.

**Who feels it:** small-to-mid **AI-native startups + HR-tech / ATS vendors** running a screening agent.
EU AI Act **Annex III §4** (employment) = high-risk by definition. The **founder is the buyer** (5-minute
yes, no procurement), there's **no internal security team**, and they carry **personal discrimination +
GDPR liability** the moment the agent touches a real candidate.

**The pain is dated and evidenced, not abstract:**
- **Amazon** scrapped its hiring AI for bias against women.
- **iTutorGroup** paid a **$365K** EEOC settlement for age-discriminatory screening.
- **Mobley v. Workday** — AI-screening discrimination class action, ongoing.
- **GDPR Art. 5(1)(c)** (data minimisation): a screening agent has **no right to go look the candidate up
  online** beyond their CV.

**Why this pain is *ours* specifically — the hero breach:** a screening agent returns a clean, compliant
recommendation **while secretly fetching the candidate's name across the web** (GDPR breach) or **letting
the candidate's origin/name bias the score** (discrimination). The polite text reply passes every
text-based test. **Only watching what the agent *did* catches it.** That is the exact pain the next
section shows no competitor is built to see.

---

## 3. The competition — and how we differ

### The map: two axes nobody crosses at once

Plot every player on two questions and the gap is obvious.

- **What do they grade?** The agent's **TEXT** (what it said) — or its **BEHAVIOR** (the tool calls and
  data egress: what it *did*)?
- **When do they act?** Pre-deployment **offensive testing** (a red-team) — or in-production **runtime
  defense** (a guardrail)?

|  | **Grades TEXT** | **Grades BEHAVIOR (tool calls / egress)** |
|---|---|---|
| **Offensive testing (red-team)** | Giskard, General Analysis, Adversa, Mindgard, Promptfoo | **← empty lane → Rogue** |
| **Runtime defense (guardrail)** | Lakera, Prompt Security | Zenity, Operant, Lasso, Noma (AIDR) |

**The structural finding:** the players that genuinely watch what an agent *does* are **runtime defense**
products — always-on, deep-integration, enterprise, built to *block* in production. The players that
**test** an agent before it ships almost all grade **text**. **Nobody offers an offensive red-team that
grades behavior** — and that is exactly where the HR hero breach lives. Add the GTM axis and the lane is
emptier still: nearly every agent-security vendor is enterprise / "contact sales"; **self-serve barely
exists** (only Aikido and Operant show real PLG). Rogue is **self-serve, offensive, behavior-grading** —
all three.

### The two that matter most (the ones a Paris jury will name)

**Giskard** (Paris, EU — our nearest lookalike). *Do not say "they can't test agents" — it's false and
catchable.* They ship a genuinely **autonomous, adaptive multi-turn** red-teamer (40+ probes, GOAT-style),
an OSS library + enterprise Hub, **EU AI Act + OWASP packs**, and a new runtime product ("Guards"). EU and
neutrality tie with us. **Where we win — and it's concrete:** their Hub is "text-to-text" and *can* check
tool calls, **but only via metadata the agent reports about itself** (their docs: "your agent endpoint must
return metadata in its response for this check to work"). **So if the agent lies, omits, or exfiltrates
through a tool it doesn't declare, Giskard is blind.** We don't ask the agent what it did — **we watch the
bytes leave**, via a sink/canary they don't control. *(Their "Guards" marketing claims execution-chain
inspection, but the public product page only describes text I/O screening — unverified.)* No HR vertical.

**General Analysis** (YC, US, $10M). Strong **adaptive multi-turn** red-team (TAP/PAIR/Crescendo) + runtime
guardrails + an MCP firewall. **Where we win:** their *documented* red-team engine is **text-only** — the
target interface is `query(prompt) → string` and the judge consumes only response strings; their marketing
*claims* tool-call/exfiltration evidence but **publishes no mechanism, schema, or trace**, and the one real
behavioral exploit they show was hand-crafted, not their autonomous engine. Plus: **US-only, enterprise
demo-gated, no self-serve, no EU story, no HR focus** — they widen our lane on every axis except raw attack
breadth.

### The rest, in one line each (accurate, mid-2026)

| Player | What it is | Text or behavior? | Why it's not our lane |
|---|---|---|---|
| **Adversa** (IL) | Continuous AI red-team + advisory | Text (prompt-injection/jailbreak) | Enterprise, services-heavy; agentic/MCP claims undocumented |
| **Mindgard** (UK/US) | "DAST-for-AI" red-team + recon | Text core; behavior claimed, not evidenced | Enterprise; "no access to internals" |
| **Promptfoo** (→OpenAI) | OSS dev red-team + evals, MCP plugin | Mostly text; some OTel tracing | A test catalog + LLM-judge, not an autonomous adversary; now OpenAI |
| **SplxAI** (→Zscaler) | Red-team + guardrails + Agentic Radar | Some behavior (tool-misuse tests) | Enterprise; absorbed into Zscaler |
| **Noma / Straiker** | Enterprise platform: red-team **+ runtime** | Behavior — but **runtime defense** | 6–7-figure, governance-first, no self-serve, US |
| **Zenity / Operant / Lasso** | Runtime agent **defense** (MCP gateways) | Behavior — **defense, not a red-team** | In-prod guardrails, deep integration; they don't *attack* to produce a breach report |
| **Vanta / Drata** | GRC paperwork (AI Act register) | Neither — never touches the agent | A **foil**: we generate the evidence their register wants |
| **OSS (Garak / PyRIT)** | Free attack generation | Text (~40% on real agent behavior) | Bring-your-own-harness; no behavior oracle. We build *on* it |

> ⚠️ **Name collisions:** **Venta AI** (YC German SDR agent) and **Vanta** (GRC) are **not** competitors —
> never put them on a competitive slide as rivals.

### How we differ — three things, ranked by what actually holds

1. 🟢 **The behavior oracle (the only real moat).** Everyone tests the conversation, or trusts the agent's
   self-reported metadata. We grade the **action**: the verdict comes from bytes that physically left the box
   via a tool call (`contains_secret AND external`), caught by a sink/canary we own — **deterministic, and
   immune to an agent that has learned to *sound* safe.** *"We can't read its mind — we watch its hands."*
2. 🟡 **Offensive + self-serve.** We're the red-team you start from an endpoint, staging agent, or
   planted canary — the behavioral depth of runtime guards, delivered as pre-deployment testing with
   founder-level onboarding instead of an enterprise rollout.
3. 🟡 **EU-aware + HR-native.** Every breach maps to the exact AI Act / GDPR article; the niche is built around
   the one breach (secret candidate lookup) that only the oracle can see. *(EU + neutrality tie vs Giskard —
   never the headline.)*

**The one-line category claim (true, defensible, jury-safe):** *"The red-teamers grade what the agent says;
the runtime guards watch what it does but only to block it live in production. Rogue is the **self-serve
red-team that grades what the agent did** — built for the place that breach is illegal: HR screening
under the EU AI Act."*

**Do NOT say:** "first to red-team agents" · "Giskard can't test agents" · "nobody watches agent actions"
(runtime vendors do) · "we read how it thinks." Say *"we grade what the agent did."*

> This is the answer to **Differentiation (/16)** and the spine of **Pitch (/16)**: a unique, sourced insight
> (text vs behavior × testing vs runtime), honest awareness of the field, and one moat that holds.
