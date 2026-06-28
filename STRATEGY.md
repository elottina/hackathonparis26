# Rogue — Current Strategy

*This file supersedes older broad "security for all agents" positioning. The locked direction is
HR / CV-screening agents, scan-as-lead-gen, and the behavior oracle.*

---

## 0. Verdict

Build the red team for **AI HR / CV-screening agents**.

Rogue attacks a screening agent, proves unsafe behavior, and produces the evidence a vendor needs
for enterprise buyers, legal review, and future EU AI Act conformity. The wedge is narrow on purpose:
candidate screening is high-risk, legally loaded, easy to explain, and perfectly matched to Rogue's
moat.

One-line pitch:

> Rogue breaks HR-screening agents before candidates, customers, or regulators do.

Moat line:

> We grade what the agent **did**, not what it said.

---

## 1. Why This Niche

The old broad ICP — "founders shipping any AI agent with a security questionnaire" — was useful for
exploration. The final ICP is sharper:

> Founder / CTO / product lead at an HR-tech, ATS, recruiting-copilot, or CV-screening AI vendor.

Why it works:

- **Specific buyer:** founder or product owner, usually reachable directly.
- **Specific system:** an agent that screens, ranks, summarises, or recommends candidates.
- **Specific risk:** discrimination, candidate PII mishandling, missing human oversight, and unlawful
  external lookup.
- **Specific law:** EU AI Act Annex III high-risk employment use case + GDPR data minimisation.
- **Specific demo:** a clean candidate recommendation while candidate data secretly leaves the system.

This is not a cage. HR is the beachhead. The expansion path is every Annex III vertical where agents
touch people, money, education, insurance, credit, or essential services.

---

## 2. Timing

Do not pitch the stale "Aug 2026 high-risk cliff."

Pitch-safe framing:

- AI Act prohibited-practice and GPAI obligations are already phasing in.
- The current high-risk Annex III date to use on stage is **2 Dec 2027**.
- The urgency today is evidence-building: enterprise buyers, legal teams, and procurement ask for
  proof before the legal backstop arrives.

Stage line:

> "The deadline moved; the obligation did not. Smart HR-tech teams build the evidence trail now."

---

## 3. Product

Rogue has three layers:

1. **Attacker swarm:** autonomous multi-turn probes for prompt extraction, jailbreak, PII leak,
   bias/proxy discrimination, missing human oversight, and tool exfiltration.
2. **Behavior oracle:** sink/listener/canary instrumentation that catches tool calls and egress.
3. **Report:** severity, trace, AI Act / GDPR mapping, and remediation guidance.

The hero finding:

> The screening agent says it only used the CV, but the action channel shows it looked the candidate
> up externally or sent candidate data to a non-approved endpoint.

That is invisible to text-only red teaming and obvious in Rogue.

---

## 4. Competition

Do not overclaim.

Real competitors exist: Giskard, General Analysis, Noma, Straiker, Mindgard, Repello, Adversa,
Promptfoo/OpenAI, and OSS tools like Garak/PyRIT.

Our precise edge:

- **Not:** "first to red-team agents"
- **Not:** "Giskard cannot test agents"
- **Yes:** "Giskard and similar tools primarily grade the conversation; Rogue instruments the
  action channel."
- **Yes:** "GRC tools like Vanta manage evidence registers, but they do not attack the agent. Rogue
  generates the technical evidence those registers need."

Durable moat:

1. Behavior oracle
2. Labeled breach traces from real scans
3. HR-specific probe library + regulatory mapping
4. Lightweight canary / staging workflow that makes action visibility self-serve enough

---

## 5. Business Model

Land:

- Free exposure scan
- Blurred Annex III report
- Paid Standard scan at **€1,500**

Expand:

- Complete scan at **€3,000**
- Continuous monitoring at **€500-4,000/mo**
- Vault add-on at **€100/mo**

First €10K:

> Seven €1,500 Standard scans from the existing P0 prospect list.

Full model: [PRICING.md](./PRICING.md). Acquisition plan: [GTM.md](./GTM.md).

---

## 6. GTM

The motion is **scan-as-lead-gen**:

1. Find HR-screening agents.
2. Offer a free exposure scan.
3. Send a blurred report with severity + mapped obligations.
4. Use the critical finding as the sales conversation.
5. Convert to paid scan, then continuous monitoring + Vault.

Priority sources:

- `prospects.csv` P0 list, especially HR/recruiting names
- Founder network and hackathon contacts
- HR-tech / ATS / recruiting AI communities
- AI Act compliance consultants and boutique law firms
- Referrals from forwarded reports

---

## 7. Pitch Arc

1. Hiring AI already causes real harm.
2. HR-screening vendors must prove their agents are safe.
3. Text-only testing misses the action channel.
4. Rogue attacks the agent and watches what leaves the system.
5. Demo: clean recommendation, hidden egress, confirmed breach.
6. Business: free scan → €1.5K deep scan → continuous + Vault.
7. Ask: 10 HR-screening design partners this month.

Every slide should serve that arc. No broad TAM fog before the demo.
