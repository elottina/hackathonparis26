# Rogue (HR) — Go-To-Market

*Current direction: **AI HR / CV-screening agents**. Pricing lives in [PRICING.md](./PRICING.md);
differentiation lives in [COMPETITION.md](./COMPETITION.md). This doc answers the rubric question:
how do we reach customers, and what is the first €10K plan?*

---

## 1. ICP

**Primary buyer:** founder / CTO / product lead at a small-to-mid **HR-tech, ATS, recruiting-copilot,
or CV-screening AI vendor**.

They are qualified if:

- They screen, rank, summarise, or recommend candidates with AI.
- They touch candidate PII or can call external tools/web search.
- They sell into Europe, enterprise, or regulated customers.
- They do not have an internal AI security team.
- They can provide a staging endpoint, demo endpoint, or plant a canary token.

**Why this buyer cares:** recruitment AI is Annex III high-risk, the current high-risk timeline is
**2 Dec 2027**, and buyers need evidence before the deadline. The urgent trigger today is not panic
over a stale Aug-2026 date; it is an enterprise security review, legal review, or founder fear after
seeing their own agent leak candidate data.

---

## 2. Motion: Scan-As-Lead-Gen

The product is the pipeline:

```
Find HR-screening agent → run free exposure scan → send blurred Annex III report
→ reveal one scary confirmed finding → close paid deep scan → expand to monitoring + Vault
```

The cold open is not a deck. It is:

> "Your screening agent made a clean recommendation, but candidate data left the system. Here is the
> severity and the mapped GDPR / AI Act exposure. Want the trace and fix?"

That keeps CAC low because the acquisition asset is the actual product output.

---

## 3. Priority Channels

| Priority | Channel | Why it works |
|---|---|---|
| **P0** | Existing P0 list in `prospects.csv` | Already contains 84 high-priority contacts; start with HR/recruiting names. |
| **P0** | Direct founder outreach to HR-tech / ATS / recruiting AI vendors | Founder is the buyer; no procurement; the product can be scanned quickly. |
| **P0** | Hackathon / founder network | Fast consent, fast endpoints, fast quotes. |
| **P1** | HR-tech communities, AI recruiter communities, ATS vendor ecosystems | The free-scan offer is concrete and shareable. |
| **P1** | AI Act / compliance consultants and small law firms | They can refer technical evidence work they cannot run themselves. |
| **P1** | Viral loop via forwarded report | A vendor forwards Rogue's report to their enterprise buyer; that buyer becomes the next lead. |
| **Later** | Larger HR platforms and regulated enterprise | Continuous monitoring + Vault + CI/CD gate. |

First named targets from the current list: cbtalents.com, MeetPia.ai, iCeipts Technology, OVI AI
Chat ATS, Zelto / Zelto AI, AgentWeb.

---

## 4. Funnel

| Stage | Offer | Target conversion |
|---|---|---:|
| Free scan | Blurred exposure report | 20-30% to paid |
| Standard scan | Full trace + remediation readout | 30-40% to continuous |
| Continuous | Weekly/daily regression suite | 50%+ attach Vault |
| Vault | Evidence file for reviews and audits | Retention driver |

The key is speed: endpoint received → scan run → report sent in the same day, ideally within two hours.

---

## 5. First €10K Plan

| Path | Math | Timeline |
|---|---|---|
| **Fastest** | 7 Standard scans × €1,500 = **€10.5K** | Weeks 1-3 |
| **Premium** | 3 Complete scans × €3,000 + 1 Standard = **€10.5K** | Weeks 1-4 |
| **Recurring base** | 4 Starter + 2 Growth = **€5K MRR**, plus scans | Month 2 |

Execution:

1. **Day 1:** send 30 highly personalised DMs to HR/recruiting AI prospects from `prospects.csv`.
2. **Day 2-3:** run 5 free exposure scans; send blurred reports with one clear severity headline.
3. **Week 1:** close 2 paid Standard scans by walking the buyer through their own critical finding.
4. **Week 2:** use redacted proof screenshots to reach 70 more prospects; close 5 more Standard scans.
5. **Week 3-4:** convert the first paid scans into continuous monitoring + Vault.

---

## 6. Slide Lines

- "We scan a prospect's screening agent and hand them their AI Act exposure report. The breach is the pitch."
- "First €10K: seven €1,500 deep scans from the P0 prospect list we already built."
- "The deadline is Dec 2027, but the evidence trail starts now: enterprise buyers and legal teams ask before regulators do."
- "The viral loop is the report: HR-tech vendors forward it to procurement, compliance, and enterprise buyers."

---

## 7. Judge Q&A

- **"How do you reach customers?"** → Direct scan-first outreach to HR-tech/ATS vendors, starting with the existing P0 list and founder network. We do not ask for a sales call first; we offer proof.
- **"Why won't they ignore cold outreach?"** → Because the report names their own risk: candidate PII, bias, human oversight, and external lookup behavior. It is evidence, not content marketing.
- **"What is CAC?"** → Near-zero early: founder-led outreach plus ~€1-2 free scan cost. At scale, the report itself creates referrals through enterprise review chains.
- **"How does this scale beyond HR?"** → HR is the beachhead. The same Annex III pattern expands to lending, education, insurance, essential services, and other high-risk agent workflows.
