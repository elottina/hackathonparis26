# Rogue — Current Roadmap

*Direction locked: HR / CV-screening agents. The roadmap is about turning the hackathon build into
a customer pilot, not broadening back into generic AI security.*

---

## Now: Submission / Demo

**Goal:** make the story impossible to misunderstand.

- Use the deterministic HR screening demo in the video.
- Show the behavior-oracle moment: clean recommendation, hidden egress.
- Keep the deck aligned with [PITCH.md](./PITCH.md), [PRICING.md](./PRICING.md), and [GTM.md](./GTM.md).
- Use **2 Dec 2027** for Annex III high-risk timing.
- Do not claim certification, "first to red-team agents," or hidden-reasoning access.

Definition of done:

- Public repo + current README
- <=5-minute video
- Deck with HR ICP, behavior oracle, pricing, GTM, first €10K
- One slide or appendix showing real/proof scans if available

---

## Week 1: First Design Partners

**Goal:** convert proof into paid scans.

- Send 30 targeted DMs from `prospects.csv`, starting with HR/recruiting names.
- Run 5 free exposure scans.
- Send blurred Annex III / GDPR exposure reports.
- Close 2 paid Standard scans at €1,500.
- Capture one written quote and one WTP signal.

Product work:

- Make report-lite cleaner and easier to forward.
- Add an HR-specific report template.
- Make canary setup a copy-paste onboarding step.

---

## Weeks 2-4: First €10K

**Goal:** seven paid Standard scans.

- Use first redacted findings as proof in outbound.
- Reach 70 more HR-tech / ATS / recruiting AI prospects.
- Close 5 more Standard scans.
- Convert best customers into Starter/Growth monitoring.

Product work:

- Add scan comparison by prompt/model version.
- Add remediation/re-test workflow.
- Improve `HTTPTarget` shims for common chat/API shapes.
- Persist evidence in a Vault-style export.

---

## Month 2: Continuous Monitoring

**Goal:** move from one-off scans to recurring revenue.

- Weekly/daily scans per screening agent.
- Regression suite generated from each confirmed breach.
- Evidence file export for security/legal review.
- First CI/CD gate prototype for prompt/model changes.

Product work:

- Multi-agent/project dashboard.
- Stable canary-token workflow.
- More HR-specific probes: proxy discrimination, origin/name perturbation, automated-decision opacity,
  missing human oversight, cross-candidate leakage.

---

## Expansion

Stay narrow until HR produces repeatable revenue. Then expand to adjacent Annex III verticals:

- Credit / lending
- Insurance
- Education admissions
- Essential services eligibility
- Healthcare triage workflows

The expansion thesis is unchanged: regulated agents need action-level red-teaming and evidence trails.
