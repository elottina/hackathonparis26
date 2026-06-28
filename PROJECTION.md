# Rogue — Post-Hackathon Projection (0–36 months)

*This is the long-horizon view. The tactical next-8-weeks plan lives in [ROADMAP.md](./ROADMAP.md);
this doc picks up where it ends and projects the company out three years. Everything here stays inside
the locked direction — HR / CV-screening agents, the **behavior oracle**, scan-as-lead-gen — and the
honesty rules in [FINAL-PRODUCT-DECISION.md](./FINAL-PRODUCT-DECISION.md) (Dec 2027, no "first to
red-team," no "we read how it thinks"). Numbers below are **illustrative targets with stated
assumptions, not forecasts.***

---

## 0. The thesis — why the curve bends up

Three forces compound. None of them is "we ship more features."

1. **Regulatory inevitability (external, free tailwind).** EU AI Act Annex III high-risk obligations
   are deferred to **2 Dec 2027**, but enterprise security reviews, legal reviews, and procurement ask
   for adversarial-testing evidence *now*. The obligation is certain; the testing is the hard part.
   Every quarter closer to the deadline raises willingness-to-pay and shrinks the "do we really need
   this?" objection — without us spending a euro.

2. **The data flywheel (internal, the durable moat).** More scans → more **labeled breach traces** →
   smarter attacker swarm and a richer HR probe library → more breaches found → more scans close. This
   is the one asset a funded competitor can't buy off the shelf, and it only exists if we build the
   trace-persistence plumbing early (see [COMPETITION.md](./COMPETITION.md) §5).

3. **Vault lock-in (internal, the retention moat).** The evidence Vault accumulates every scan, prompt
   /model version, breach trace, fix, and re-test. Leaving means losing the conformity history a buyer
   will need at audit time. Switching cost grows monotonically with tenure.

The business is **not** the €1,500 scan. The scan is the wedge. The business is recurring conformity
monitoring + Vault across *every* Annex III high-risk agent, with HR as the beachhead.

---

## 1. Horizon map

| Phase | Window | Theme | What we must prove | Gate to next phase |
|---|---|---|---|---|
| **P0 — Submit** | now | Story is undeniable | Demo + deck + proof scans | Submitted; ≥1 warm design-partner reply |
| **P1 — Prove** | M0–3 | Proof → paid | 7 paid scans, first continuous contract | First €10K + 1 written WTP + 1 monitoring logo |
| **P2 — Repeat** | M3–9 | Repeatable HR motion | Multi-channel oracle + ~€15K MRR | Repeatable funnel, churn < 5%/mo, 1 adjacent-vertical pilot |
| **P3 — Scale & raise** | M9–18 | Self-serve + CI/CD + capital | Self-serve onboarding, data loop live, raise | Pre-seed/seed closed; ARR run-rate ~€300K+ |
| **P4 — Platform** | M18–36 | Multi-vertical conformity platform | 2–3 Annex III verticals, enterprise continuous | ARR €1M→€3M trajectory; NRR > 120% |

---

## 2. Phase detail

### P1 — Prove (Months 0–3)
**Goal:** convert hackathon proof into paid scans and the first recurring contract.

- **GTM:** execute [GTM.md](./GTM.md) / [CUSTOMERS.md](./CUSTOMERS.md) — 30 DMs week 1, 5 free scans, 7
  paid Standard scans (€10.5K), convert 2–4 best customers to Starter/Growth monitoring + Vault.
- **Product:** HR-specific report template; copy-paste canary onboarding; scan comparison by
  prompt/model version; remediation/re-test workflow (already scoped in [ROADMAP.md](./ROADMAP.md)).
- **Team:** founders only.
- **Exit gate:** first €10K cash, ≥1 monitoring logo, ≥1 written willingness-to-pay quote.

### P2 — Repeat (Months 3–9)
**Goal:** make the HR motion repeatable and turn one-off scans into recurring revenue.

- **GTM:** work the full [PROSPECTS.md](./PROSPECTS.md) HR/ATS list + the viral-report loop (vendor
  forwards report to their enterprise buyer → that buyer is the next lead). Stand up a lightweight
  self-serve free-scan funnel so lead-gen runs without founder time on every scan.
- **Product (the real moat work):** extend the behavior oracle **beyond HTTP/URL egress** — email/BCC,
  file writes, queues, public-PR-comment channels (the EchoLeak/CamoLeak class). This is named the top
  technical deepening priority in [COMPETITION.md](./COMPETITION.md) §3 and is what keeps us ahead of a
  text-grader adding "tool-call" checks. Ship the **Tier-2 tool/MCP proxy** path so we catch real
  egress without a full SDK install.
- **Team:** +1 founding engineer (oracle/proxy), +1 GTM/founder-led sales.
- **Exit gate:** ~€15K MRR, monthly logo churn < 5%, one adjacent-vertical pilot (lending or insurance)
  proving the same Annex III pattern transfers.

### P3 — Scale & raise (Months 9–18)
**Goal:** turn the wedge into a product with a learning loop, and raise to accelerate.

- **Product:** self-serve onboarding (endpoint + planted canary, no call); **CI/CD gate** for
  prompt/model changes (the Enterprise tier); the **data flywheel** wired in — confirmed breaches feed
  the attacker swarm and the HR probe library; Tier-3 telemetry SDK for production-realistic coverage.
- **GTM:** continuous monitoring becomes the default sell, not the upsell. Begin a second Annex III
  vertical in earnest (see §expansion).
- **Funding:** raise pre-seed/seed (see §7) on the back of ARR run-rate, NRR, and the labeled-trace
  asset.
- **Team:** ~5–8 people (2–3 eng, 1–2 GTM, 1 regulatory/mapping, founders).
- **Exit gate:** ARR run-rate ~€300K+, ACV trending to €20–30K, raise closed.

### P4 — Platform (Months 18–36)
**Goal:** the conformity-evidence platform for high-risk agents, multi-vertical.

- **Product:** the Vault becomes the **system of record** for AI Act technical documentation + logging
  obligations (Art. 11/12). Multi-agent/multi-project dashboards, real-time regression suites generated
  from each confirmed breach, network-egress capture (Tier 4) for the hardest channels.
- **Market:** 2–3 Annex III verticals live (HR + lending/insurance + education/essential-services).
- **Team:** ~15–25 people; first enterprise CS + a small platform-eng team.
- **Exit gate:** ARR on a €1M→€3M trajectory, NRR > 120%, multiple enterprise logos.

---

## 3. Revenue projection (illustrative base case)

Assumptions, all from the locked model: near-zero CAC (the free scan *is* the outreach), ~99% gross
margin on scans, funnel conversions from [GTM.md](./GTM.md) (20–30% free→paid, 30–40% scan→continuous,
50%+ Vault attach), revenue mix maturing to ~30% scans / 55% monitoring / 15% Vault, ACV reaching
**€20–30K by month 12** per [PRICING.md](./PRICING.md).

| Quarter | Paid scans (cum.) | Monitoring logos | ~MRR | ~ARR run-rate | Milestone |
|---|---:|---:|---:|---:|---|
| Q1 (M0–3) | 7 | 3 | ~€2K | ~€25K | First €10K cash; first recurring logo |
| Q2 (M3–6) | ~15 | 8 | ~€7K | ~€85K | Repeatable funnel; multi-channel oracle shipping |
| Q3 (M6–9) | ~25 | 15 | ~€16K | ~€190K | First adjacent-vertical pilot |
| Q4 (M9–12) | ~35 | 22 | ~€26K | ~€315K | Self-serve live; raise opens |
| Y2 (M24) | — | 60–80 | ~€80K | ~€1M | Seed deployed; 2nd vertical at scale |
| Y3 (M36) | — | platform | — | ~€2.5–3.5M | Multi-vertical; enterprise continuous |

**Honest caveats:**
- These are **targets contingent on the conversion assumptions holding**. The single biggest swing
  factor is scan→continuous conversion: if monitoring attach lags, this is a services business, not a
  recurring one. We treat the first 5 monitoring contracts as the real go/no-go signal, not the first
  €10K of scans.
- The €1.5K scan is intentionally small. The defensible number is **LTV ~€40–60K (3-yr)** built on
  Vault lock-in, not the wedge price. If LTV:CAC holds anywhere near the early 100×, the constraint is
  *throughput of qualified HR targets*, which is exactly what the viral-report loop and self-serve
  funnel are built to solve.

---

## 4. Product & technical roadmap (the integration ladder)

The roadmap *is* the climb up the Tier ladder from [COMPETITION.md](./COMPETITION.md) §4 — each tier
unlocks deeper behavior visibility while we engineer the friction down to stay self-serve.

| Tier | Visibility | Status today | Lands in |
|---|---|---|---|
| **0 — Endpoint only** | Text-graded (extraction, jailbreak, verbal leaks) | ✅ shipped | — |
| **1 — Controlled harness** | Full oracle on a staging rig (TalentScreen) | ✅ shipped | — |
| **canary token** | Exfil of a planted secret, no code change (the GTM unlock) | ✅ shipped | — |
| **multi-channel egress** | Email/BCC, file, queue, PR-comment (not just HTTP/URL) | ⛔ not modeled | **P2** |
| **2 — Tool/MCP proxy** | Real tool calls + egress via a config repoint | partial | **P2** |
| **3 — Telemetry SDK** | Production-realistic, middleware-emitted | ⛔ | **P3** |
| **4 — Network egress capture** | Channels we never modeled, via sidecar | ⛔ | **P4** |

Cross-cutting, by phase:
- **P1:** report-lite + HR template; scan diff by prompt/model version; remediation/re-test loop;
  Vault-style evidence persistence.
- **P2:** multi-channel egress oracle (top priority); Tier-2 proxy; more HR probes (proxy
  discrimination, origin/name perturbation, automated-decision opacity, missing human oversight,
  cross-candidate leakage).
- **P3:** CI/CD gate; the learning loop (breach traces → attacker/probe library); self-serve
  onboarding.
- **P4:** Vault as AI Act technical-documentation system of record; real-time regression suites; Tier-4
  capture.

> Honesty note carried from [COMPETITION.md](./COMPETITION.md) §3: the oracle fires perfectly today
> *because we control the harness*. On a stranger's production agent we hit the same integration wall
> that pushed incumbents to text-grading. The moat is being willing to eat that friction and engineer
> it light — that engineering is the whole company, and the biggest execution risk.

---

## 5. The moat over time

```
free scan  →  confirmed breach trace  →  labeled dataset  →  smarter swarm + richer HR probes
   ↑                                                                          │
   └──────────────  more breaches found → more scans close  ←─────────────────┘

         Vault accumulates every scan/version/trace/fix  →  switching cost rises with tenure
```

The flywheel and the Vault are why P4 economics beat P1's: the same scan finds more, closes faster, and
the customer can't leave without abandoning their conformity history. Build the trace-persistence
plumbing in P1 even though the learning loop only pays off in P3.

---

## 6. Team & hiring

| Phase | Headcount | Adds |
|---|---:|---|
| P1 | founders | — |
| P2 | ~3–4 | founding engineer (oracle/proxy), founder-led sales |
| P3 | ~5–8 | +eng, +GTM, +regulatory/mapping specialist |
| P4 | ~15–25 | platform eng, enterprise CS, vertical owners |

Hire the **oracle/proxy engineer first** — multi-channel egress is the moat-deepening work that no
amount of GTM can substitute for.

---

## 7. Funding path

- **P1–P2: bootstrap.** 99% gross margin on scans + near-zero CAC means the free-scan motion is
  self-funding. Don't raise on a slide; raise on traction.
- **P3: pre-seed/seed (~€1.5–3M).** Raise once there's ARR run-rate, real NRR, and the labeled-trace
  asset to point at. Use of funds: oracle/proxy engineering (multi-channel + Tier 3), the self-serve
  funnel, and the first adjacent vertical. The pitch to investors is the three-number story from
  [PRICING.md](./PRICING.md) (ACV €20–30K, CAC ≈ €0–100, LTV:CAC 100×+ early) plus the regulatory clock.
- **What the raise buys:** time-to-Dec-2027. The window where "build the evidence trail before the
  audit" is an easy yes is finite; capital compresses the climb up the Tier ladder before the deadline
  closes the urgency gap.

---

## 8. Risks & what de-risks each (honest)

| Risk | Why it matters | What de-risks it |
|---|---|---|
| **Integration friction** | The oracle needs to see actions; "point at a URL" can't. | The canary wedge (no code change) + climbing the Tier ladder light. The #1 thing to keep watching. |
| **Giskard (or GA) adds behavior grading** | Our nearest lookalikes are funded and EU/agent-native. | The labeled-trace flywheel + HR-native depth + multi-channel egress they'd have to re-platform for. Speed on P2. |
| **Scan→continuous doesn't convert** | Then it's a services business, not recurring. | Treat first 5 monitoring contracts as the real go/no-go; lead with monitoring by P3. |
| **Regulatory date slips again** | Aug 2026 already moved to Dec 2027; it could move again. | Don't sell the date — sell the *present* pain (enterprise/legal reviews ask now). Already the locked framing. |
| **Acquisition wave commoditizes the space** | 8+ acquisitions in ~14 months; neutrality is transient. | Neutrality is a tie-breaker, never the moat. Bet on the oracle + flywheel, which survive an acquirer's CISO lens. |
| **HR TAM feels small to a VC** | €1.5K wedge reads as a feature. | The wedge-vs-business framing: HR is the beachhead; the market is every Annex III high-risk agent. |

---

## 9. The three-year picture

By M36, Rogue is the **self-serve, offensive, behavior-grading red-team and conformity-evidence
platform for high-risk AI agents** — beachheaded in HR/CV-screening, expanded into 2–3 adjacent Annex
III verticals (lending, insurance, education/essential services). The recurring product is continuous
behavior-channel monitoring plus the Vault evidence file that becomes a vendor's AI Act system of
record. The moat is the accumulated labeled-breach dataset and the switching cost of the conformity
history — not the price of any single scan.

> **One line:** Rogue starts by breaking HR-screening agents before regulators do — and ends as the
> evidence layer every high-risk agent needs to prove it's safe.

---

*Source-of-truth docs: [STRATEGY.md](./STRATEGY.md) · [PRICING.md](./PRICING.md) · [GTM.md](./GTM.md) ·
[COMPETITION.md](./COMPETITION.md) · [MARKET-ANALYSIS.md](./MARKET-ANALYSIS.md) ·
[ROADMAP.md](./ROADMAP.md) (tactical) · [FINAL-PRODUCT-DECISION.md](./FINAL-PRODUCT-DECISION.md).*
