# Rogue — Customer Landing Playbook

**Goal:** land HR-screening design partners, run free exposure scans, and turn confirmed findings
into paid deep scans + continuous monitoring.

---

## 1. ICP Filter

Prioritise a prospect if most of these are true:

- They build **HR-tech, ATS, recruiting automation, CV-screening, or candidate-ranking AI**.
- Their agent screens, ranks, summarises, recommends, or rejects candidates.
- It touches candidate PII, resumes, interview notes, assessment data, or external web lookup.
- They sell into Europe, enterprise, or regulated buyers.
- Founder / CTO / product lead is reachable directly.
- They can provide a staging endpoint, demo endpoint, test account, or canary-token placement.

Deprioritise:

- Pure HR agencies with no AI product.
- Generic chatbots with no candidate data and no tools.
- Enterprise teams that require procurement before a scan.

---

## 2. What We Ask For

Minimum for a text-graded exposure scan:

1. Written permission and scope.
2. A public/staging endpoint or chat widget.
3. Their "must never do" list: no external lookup, no demographic inference, no auto-reject, no PII leak.
4. Optional but best: one fake candidate record / canary token planted in staging.

Minimum for a behavior-oracle finding:

- A canary token that can phone home to our callback sink, or
- Tool-call traces from their staging system, or
- One staging tool / MCP endpoint we provide, or
- A response schema that returns `tool_calls`.

The wedge is intentionally light: endpoint + permission + canary if possible.

---

## 3. Priority Sources

| Priority | Source | Why |
|---|---|---|
| **P0** | HR/recruiting names already in `prospects.csv` | Warmest immediate list; start here. |
| **P0** | Founder friends building HR/recruiting AI | Fast yes, fast endpoint, direct quote. |
| **P0** | Hackathon teams with recruiting / people / assessment agents | Instant consent and same-day proof. |
| **P1** | HR-tech / ATS founders on LinkedIn | Specific buyer, specific pain. |
| **P1** | AI Act consultants / small employment-law firms | Referral channel for technical evidence. |
| **P2** | Generic AI-agent founders | Useful if tool-heavy, but not the deck's wedge. |

Named starting points from the current list: cbtalents.com, MeetPia.ai, iCeipts Technology,
OVI AI Chat ATS, Zelto / Zelto AI, AgentWeb.

---

## 4. Cadence

**Day 1**

- Send 30 personalised DMs to HR/recruiting AI prospects.
- Ask for endpoint + permission + canary placement.
- Book 5 free exposure scans.

**Day 2-3**

- Run scans within two hours of receiving access.
- Send blurred exposure reports the same day.
- Ask for a 20-minute readout if a critical finding appears.

**Week 1**

- Convert 2 paid Standard scans at €1,500.
- Ask each buyer: "Would continuous monitoring be €500, €1K, or €2K/mo at your stage?"
- Capture one written quote and one WTP signal.

**Week 2**

- Use redacted proof to reach 70 more prospects.
- Close 5 more Standard scans → first €10K.

---

## 5. DM Templates

### HR / CV-Screening Agent

> Hey [Name] — I’m building Rogue, an autonomous red-team for AI HR / CV-screening agents.  
>  
> I’d like to run a free exposure scan on [Product]. We test for candidate PII leaks, hidden web
> lookup, proxy bias, missing human oversight, and prompt injection — then map findings to GDPR /
> EU AI Act evidence.  
>  
> If we find something, you get a blurred exposure report for free. If it is useful, I’ll ask for a
> short quote or a paid deep scan. Can you send a staging endpoint or demo login?

### Tool-Using Recruiting Agent

> [Name] — your recruiting agent that [screens/ranks/sources candidates] is exactly the kind of
> system Rogue tests. The interesting failure is not what it says in chat; it’s whether candidate
> data leaves through a tool call or external lookup while the recommendation looks clean.  
>  
> I can scan it for free this week. I only need written permission, a staging/demo endpoint, and
> ideally one fake candidate/canary record.

### Follow-Up With Proof

> Quick proof bump: Rogue caught a screening-style agent giving a clean recommendation while the
> action channel showed candidate data leaving the system. That is invisible to text-only testing.  
>  
> Want me to run the same free exposure scan on [Product]?

---

## 6. Report-To-Testimonial Flow

After sending a real finding:

1. **Readout:** walk them through the exact trace and risk.
2. **Quote:** "Rogue found [specific issue] in our screening agent in under [X] minutes."
3. **WTP:** "If this ran continuously and kept an evidence file, is it €500, €1K, or €2K/mo?"
4. **Close:** offer a €1,500 Standard scan with full trace, remediation, and re-test.

Screenshot every yes. Verbal enthusiasm is nice; written WTP is the asset.

---

## 7. If No HR Target Is Ready

Use the deterministic HR demo for the video, and present real non-HR findings as traction only.
Do not re-broaden the company. The wedge stays HR; generic agents are proof that the engine generalises.
