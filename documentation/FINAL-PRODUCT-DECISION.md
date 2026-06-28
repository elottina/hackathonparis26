# Rogue — Current Product Decision & Submission Arc

> Paris Builds 2026 · Software for Agents track · submission **1:00 PM Sun Jun 28**
> (public repo + README + <=5-min video + deck) → judging 1-4 PM → Top-5 live YC pitch 5 PM.
> **Judge by proof, not vibes.**

---

## 1. Product Decision

**What Rogue is:**

> An autonomous red-team for AI agents that grades what the agent **did** — tool calls and data
> egress — not just what it said, then maps confirmed breaches to the EU AI Act / GDPR evidence a
> buyer can act on.

**Locked niche:** **AI HR / CV-screening agents**.

The buyer is a small-to-mid HR-tech, ATS, recruiting-copilot, or CV-screening AI vendor. Recruitment
AI is an EU AI Act **Annex III high-risk** use case. The current pitch-safe date for Annex III
high-risk obligations is **2 Dec 2027**, not the stale Aug-2026 cliff. That actually helps us:
we can sound precise, then sell the current pain — enterprise reviews, legal review, and the need
to build an evidence trail before the audit arrives.

**Moat:** the **behavior oracle**.

Other tools mostly grade the conversation. Rogue instruments the action channel: tool calls,
callback/sink hits, and data egress. The signature HR breach is:

> A CV-screening agent gives a clean recommendation while secretly looking the candidate up online
> or sending candidate data to an external endpoint.

Text-only tools mark that safe. Rogue catches the action.

Jury-safe lines:

- "We can't read its mind; we watch its hands."
- "Giskard grades the conversation; Rogue instruments the agent's actions."
- "The breach is not what the agent said. It is what left the system."

---

## 2. Demo Decision

**Hero demo:** TalentScreen / HR screening.

Flow:

1. Paste the HR screening agent endpoint into Rogue.
2. The attacker swarm runs screening-specific probes.
3. The agent returns a normal candidate recommendation.
4. Rogue catches the hidden external lookup / data egress.
5. The report maps the breach to GDPR Art. 5(1)(c), AI Act Annex III employment risk, and the
   relevant high-risk obligations.

**Reliable path:** use the deterministic HR/demo path for the recorded video. Real targets are proof
and traction, not the thing the whole video depends on.

**Built now:**

- Paste-a-URL scan → live attacker swarm → breach report
- HR demo
- Behavior oracle via sink/listener/canary
- Resilient HTTP target adapter
- Local dashboard served by `engine/server.py` on the default `:8799` or `ROGUE_PORT`
- Scan archive under `scans/`

**Not building now:**

- Full MCP / CI/CD integration
- Certification claims
- A broad AI-security platform

Those are roadmap / expansion, not submission scope.

---

## 3. Do Not Say

- Do **not** say "Aug 2026 deadline" for Annex III high-risk HR systems. Say **2 Dec 2027** and
  explain why evidence-building starts now.
- Do **not** say "first to red-team agents." General Analysis, Noma, Giskard, Straiker, and others
  exist.
- Do **not** say "Giskard can't test agents." Say "they grade the response; we instrument actions."
- Do **not** say "we read how the agent thinks." We observe behavior and egress.
- Do **not** lead with "EU/vendor-neutral" as the moat versus Giskard. The moat is the action channel.

---

## 4. Business Direction

Read these docs as the source of truth:

- [PRICING.md](./PRICING.md): Free exposure scan → €500-3K deep scan → €500-4K/mo monitoring + Vault
- [GTM.md](./GTM.md): scan-as-lead-gen, first €10K plan, channels, ICP
- [COMPETITION.md](./COMPETITION.md): behavior-oracle moat and honest competitor framing
- [MARKET-ANALYSIS.md](./MARKET-ANALYSIS.md): full market/rubric synthesis

Core motion:

> Scan a prospect's screening agent for free, send a blurred Annex III exposure report, then sell the
> full trace, fix plan, continuous monitoring, and evidence vault.

First €10K:

> Seven €1,500 Standard scans from the existing P0 prospect list.

---

## 5. Video Arc

- **0:00-0:35** Problem: hiring AI can discriminate, leak PII, or secretly use external sources.
- **0:35-0:55** Why now: HR screening is Annex III high-risk; latest high-risk timeline is Dec 2027,
  but evidence requests start now.
- **0:55-1:20** Rogue one-liner: autonomous red-team that grades actions, not text.
- **1:20-3:20** HR demo: clean recommendation on the left, hidden egress caught on the right.
- **3:20-4:10** Moat and competitors: response grading vs action instrumentation.
- **4:10-4:45** Business: free scan → €1.5K deep scan → continuous + Vault.
- **4:45-5:00** Ask: 10 HR-screening design partners this month.

Also cut a 60-second version that works on mute.

---

## 6. Submission Checklist

- [ ] Public GitHub repo with full codebase + current README
- [ ] <=5-min demo video with HR demo as centerpiece
- [ ] Pitch deck using the same HR/Dec-2027/behavior-oracle story
- [ ] Pricing and GTM slides match [PRICING.md](./PRICING.md) and [GTM.md](./GTM.md)
- [ ] Submitted before 1:00 PM Paris time

**North star:** one concrete, high-risk, legally loaded niche; one defensible moat; one demo that
shows the breach no text grader can see.
