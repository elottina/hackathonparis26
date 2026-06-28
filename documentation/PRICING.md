# Rogue (HR) — Pricing & Business Model

*Current direction: **AI HR / CV-screening agents**. Acquisition lives in [GTM.md](./GTM.md);
the moat lives in [COMPETITION.md](./COMPETITION.md). The one sentence to keep straight:
we grade what the agent **did**, not how it "thinks".*

---

## 1. Who Pays, And Why

**Buyer:** founders / CTOs / product leads at small-to-mid **AI-native HR-tech, ATS, and
CV-screening vendors**.

**Why now:** CV-screening and candidate-ranking AI is an **EU AI Act Annex III high-risk**
use case. The high-risk obligations were **originally due Aug 2026, then deferred to 2 Dec 2027**
(the Digital Omnibus) — most teams still parrot the stale "Aug 2026 cliff," so knowing the date
moved is itself a credibility signal. The urgency today is still real: enterprise buyers, legal teams,
and future auditors need evidence before the deadline, and the vendor owns discrimination + GDPR
liability as soon as the agent screens real candidates.

**Pricing anchor:** not "their budget," but the downside:
Amazon scrapped a biased hiring AI; iTutorGroup paid a **$365K** EEOC settlement; *Mobley v.
Workday* keeps AI-screening discrimination in the courts; GDPR Art. 5(1)(c) requires data
minimisation; high-risk AI Act breaches can carry fines up to **€15M / 3% of turnover**.
Against that, a **€1.5K** scan is an easy yes.

---

## 2. Pricing Tiers

### FREE — Exposure Scan

- ~20 probes: prompt injection, system-prompt extraction, HR-bias smoke test, obvious PII leaks
- Text-graded only unless they plant a canary token
- Output: **blurred Annex III exposure report** with finding count, severity, and mapped obligations
- Cost to us: **~€1-2 / scan**
- Purpose: lead generation; the finding is the pitch

### PRO — Deep Scan

| Tier | Coverage | Behavior oracle | Report | Price |
|---|---|---:|---|---:|
| **Essentials** | 50 probes, 2 breach classes | No | Basic exposure report | **€500** |
| **Standard** | 100 probes, 4 breach classes | Yes | Full Annex III + GDPR mapping | **€1,500** |
| **Complete** | 200+ probes, all breach classes | Yes + remediation | Full report + re-test plan | **€3,000** |

**HR breach classes:** candidate PII exfiltration / secret web lookup, proxy discrimination
by name/origin/gender/age, missing human oversight, cross-candidate data leak, automated-decision
opacity. The hero breach is behavioral: the agent gives a clean recommendation while secretly
looking the candidate up online.

### CONTINUOUS — Conformity Monitoring

| Plan | Agents | Frequency | Price |
|---|---:|---|---:|
| **Starter** | 1 screening agent | Weekly | **€500/mo** |
| **Growth** | Up to 5 agents | Daily | **€1,500/mo** |
| **Enterprise** | Unlimited | CI/CD gate + real-time regression suite | **€2,000-4,000/mo** |

Continuous beats a one-time audit because HR teams reprompt, retrain, and swap models. AI Act
conformity is a lifecycle obligation; a consulting audit is a snapshot, Rogue is the regression
alarm.

### VAULT — Evidence File Add-On

- **€100/mo** on top of any paid plan
- Stores every scan, prompt/model version, trace, fix, and re-test result
- Packages the evidence trail needed for technical documentation and logging obligations
- Lock-in: leaving means losing the accumulated conformity history

---

## 3. Unit Economics

**One line:** a human AI-hiring audit can cost **€15-90K** and take weeks; our scan costs a few
euros of model calls and runs in minutes.

| Tier | Price | Cost / scan | Gross margin |
|---|---:|---:|---:|
| Free | €0 | ~€1-2 | Marketing spend |
| Essentials | €500 | ~€3 | ~99% |
| Standard | €1,500 | ~€5 | ~99% |
| Complete | €3,000 | ~€8 | ~99% |
| Starter / mo | €500 | ~€10/mo | ~98% |
| Growth / mo | €1,500 | ~€30/mo | ~98% |

**Cost breakdown:** ~400 model calls per full scan. Attacker swarm uses the cheaper model tier;
the judge uses the stronger model. Sink/listener infrastructure is negligible. The target agent's
own tokens are on the client's bill.

### The three numbers a VC scores on

| Metric | Value | Why |
|---|---|---|
| **ACV** (annual contract value) | **€20–30K** by month 12 | €1.5K wedge scan → continuous monitoring + Vault; mix ~30% scans / 55% monitoring / 15% Vault |
| **CAC** | **≈ €0–100** | The free scan (~€1–2 of compute) *is* the outreach — founder-led, no paid acquisition; the report is the pitch |
| **LTV** | **~€40–60K** (3-yr) | AI Act conformity is a lifecycle obligation; the Vault creates switching cost (leaving loses the accumulated conformity history) |
| **LTV : CAC** | **100×+ early** | 99% gross margin on a self-funding, report-driven sales motion |

**Wedge-vs-business (preempt "is €1.5K too small to be venture-scale?"):** €1.5K is the *wedge*, not
the business. The business is recurring conformity monitoring + the evidence Vault (lock-in), and the
market is *every* EU AI Act Annex III high-risk agent — HR is just the beachhead.

---

## 4. Expansion Path

```
M1   Free exposure scan                                €0
M1   Standard deep scan                                €1,500 one-off
M2   Starter continuous                                €500/mo
M4   Growth continuous + Vault                         €1,600/mo
M8   Enterprise CI/CD gate + Vault                     €2,100-4,100/mo
M12  Annual customer value                             ~€20K-30K
```

Target revenue mix at month 12: 30% one-off scans, 55% continuous monitoring, 15% Vault.
One-off scans create cash and proof; continuous + Vault create retention.

---

## 5. Slide Lines

- "Free exposure scan → €500-3K deep scan → €500-4K/mo continuous monitoring + evidence vault."
- "A human AI-hiring audit costs €15-90K and takes weeks. Rogue costs a few euros to run and produces evidence in minutes."
- "The deadline is Dec 2027, but enterprise buyers ask for evidence now. Rogue builds that evidence trail before the audit."
- "Vault is the accumulating conformity file: every scan, prompt change, breach trace, fix, and re-test."

---

## 6. Judge Q&A

- **"Is the AI Act deadline really Aug 2026?"** → It *was* — then it moved. Annex III high-risk obligations were **deferred from Aug 2026 to 2 Dec 2027** (the Digital Omnibus). Knowing the real date is the credibility; the current pain is what sells: enterprise reviews and evidence-building start now.
- **"Why would a startup pay €1.5K?"** → Because the alternative is a weeks-long audit, legal exposure, and a blocked enterprise buyer. A scan that finds and documents the issue is cheap.
- **"Why not a one-time consultant?"** → Agents change every time the team reprompts, changes tools, or swaps models. The recurring product is regression monitoring plus the evidence trail.
- **"Do the economics work?"** → Yes. A Standard scan is ~€5 of model calls sold for €1,500. The margin funds R&D and founder-led sales.
