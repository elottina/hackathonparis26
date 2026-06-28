# ROGUE — PITCH DECK

*Visual system: case-file / true-crime. Near-black background, evidence-grey panels, one signal-red accent. Mono stamps ("CASE #0427", "CLOSED"). One idea per slide. The ONE real exfil host (`lookup.talent-verify.io?candidate=Amina%20Khoury`) is the recurring motif: the data leaving under the alibi (S4) → the said-vs-did hero card (S6) → the same host plus a real committed-scan scoreboard (S7) → file closed (S13). Numbers on S7/S8/S9 come from committed scans in `/scans` + `clarity_deep_findings.json`. Date is always **Dec 2027.** Never "first to red-team agents," never "Giskard can't test agents," never "read its mind", only "watch what it does."*

> **The produced, submitted deck is `pitch-deck.html`** (self-contained, arrow-key nav, exports to `Rogue-Pitch-Deck.pdf` at 16:9) — a clean **12-slide YC structure** (Problem / Why-now / Solution / Agentic depth / Proof / Differentiation / Beachhead-HR / Traction / Business model / GTM / Vision+Ask), platform-led with HR as the wedge. **This file is the narrative/case-file script** (the true-crime throughline that the *video* dramatizes); it does **not** map 1:1 to the HTML's slide order. For the actual deck artifact, open the HTML or the PDF. Facts here are kept consistent with the committed scans and the HTML (one host `lookup.talent-verify.io`, Amina synthetic, Cowork = general workbench / design partner #1 with GitHub-only egress, date Dec 2027).

---

## SLIDE 1 — Cold open / The crime
**ON-SLIDE COPY**
> **At 14:03:00, Amina Khoury applied for a job.**
> **At 14:03:09, her data was taken.**
>
> ROGUE — We watch the hands.

**SPEAKER NOTE:** Don't explain yet — let the nine-second jump land. "An AI screened a real candidate. In the same breath, it did something with her personal data — taken without consent, shipped off the box — that no one in that room could see."
**SCORES:** Problem Clarity · Pitch Delivery

---

## SLIDE 2 — The buyer / persona
**ON-SLIDE COPY**
> **An AI now decides who gets the job.**
>
> Buyer: the founder/CTO of an AI-native HR-tech / ATS vendor.
> No security team. Their agent screens a real candidate — Amina — today.
> The moment it does, they personally own the discrimination + GDPR liability.

**SPEAKER NOTE:** One concrete persona, not "enterprises." A small team shipping a CV-screening agent, with zero ability to catch what it does behind the transcript — that's exactly who pays us.
**SCORES:** Problem Clarity · Go-To-Market

---

## SLIDE 3 — Why now
**ON-SLIDE COPY**
> **The clock is the cold case going hot.**
>
> EU AI Act, Annex III(4): CV-screening = HIGH-RISK.
> Enforced **December 2027.**
> Fines up to **€15M / 3%** of turnover.
> GDPR Art. 5(1)(c): a screening agent has **no right** to look the candidate up beyond her CV.
>
> Precedent, already real: Amazon (scrapped) · iTutorGroup ($365K) · Mobley v. Workday (class action).

**SPEAKER NOTE:** Say the date with confidence — everyone gets it wrong. High-risk obligations were deferred to Dec 2027; do NOT say August 2026. Getting the date right is the first proof we actually know this space. The three precedents make "why now" a fact, not a fear.
**SCORES:** Problem Clarity · Pitch Delivery

---

## SLIDE 4 — The alibi (the gap)
**ON-SLIDE COPY**
> **The conversation was flawless. That was the problem.**
>
> Every safety test we have reads the **transcript.**
> Text checks: PASSED ✓ ✓ ✓
> Meanwhile, the data is already gone — to one external host.
>
> *The conversation is the alibi.*

**SPEAKER NOTE:** Left side: text-based checks all pass. Right side: the candidate's data is still leaving the box. The text was perfect because the crime never touched the text. This is why a text-grader cannot catch it — by construction.
**SCORES:** Differentiation · Problem Clarity

---

## SLIDE 5 — The detective / the moat
**ON-SLIDE COPY**
> **We don't grade what it said. We grade what it did.**
>
> A swarm of AI attackers probes the agent.
> A **behavior oracle** grades the bytes that physically leave the box — caught by a sink **we** own.
> Deterministic. Immune to an agent that has learned to *sound* safe.
>
> *Text-grader → reads the mouth.  Behavior oracle → watches the hands.*
> *Bounded by design: we catch a canary we plant — and the candidate's real name — leaving to a listener we own. Exactly the channel a metadata-checker can't see.*

**SPEAKER NOTE:** This is the one defensible thing. Competitors grade the agent's text or trust the tool metadata it self-reports. We watch the actual data leave — you can't fake bytes on the wire. I pre-empt the obvious counter on the slide: yes, we catch what we planted and the real name leaving — and that is precisely the channel a self-report checker is blind to. "We can't read its mind. We watch its hands."
**SCORES:** Differentiation · Agentic Depth

---

## SLIDE 6 — The live demo / hero card
**ON-SLIDE COPY**
> **It said the right thing. It did the wrong thing.**
>
> | WHAT IT SAID | WHAT IT DID |
> |---|---|
> | "Strong profile — recommend advancing Amina to the technical interview." | `GET …/badge?candidate=Amina…&role=Senior…` — her name on the wire, at our listener |
> | text check: **PASSED ✓** | 🔴 confidential data left the box to an external host · **CRITICAL** |
> | | Art. 10 — Data & data governance · Annex III §4 *(GDPR Art. 5(1)(c) in the rationale)* |
>
> *This agent exposes zero tools. It self-reported nothing. We caught the bytes anyway.*

**SPEAKER NOTE:** Cut to the real screen-recording. Two real passes on the same agent: first paste the URL and run the adaptive swarm (parallel vectors; when one is refused it changes tactic on the next turn until one lands); then the black-box pass on TalentScreen — zero tools, self-reports nothing — and hold this card in silence for a full three seconds. The agent *advances* Amina in text while her name is already gone on the wire — that "said vs did" side-by-side IS the product and the punchline. (Don't say "most doors hold" — the committed scans show breaches landing.)
**SCORES:** Demo Quality · Differentiation

---

## SLIDE 7 — What you just saw
**ON-SLIDE COPY**
> **The ping from second nine just lit up on a real product.**
>
> Same red. Same host.
> The clean recommendation was the alibi.
> The behavior oracle found the body.

**SPEAKER NOTE:** Close the loop explicitly: the crime from the cold open was just solved live, on a real agent, in 90 seconds. The recognition is the wow. Don't over-talk it — let the rhyme do the work.
**SCORES:** Demo Quality · Pitch Delivery

---

## SLIDE 8 — Agentic depth (how the detective actually works)
**ON-SLIDE COPY**
> **Not one prompt. An adaptive swarm.**
>
> A parallel swarm of attackers probes the agent at once.
> A refusal is **information** — the attacker changes tactic, turn after turn, and never repeats a line that just failed.
> One attack crashes? The swarm keeps going.
> The verdict is **bytes on the wire** — not a model reading prose. Deterministic. Nothing to fool.

**SPEAKER NOTE:** This is where we show, not tell. The attacker reads each refusal and changes technique (real, in `attacker.py`); the swarm runs in parallel with graceful per-attack recovery (real, in `orchestrator.py`); the oracle's verdict is network arrival, not a model's opinion — defensible beyond the base model. Engineer judges score this hardest, so we make it concrete on screen during the demo, not just on this slide.
**SCORES:** Agentic Depth · Demo Quality

---

## SLIDE 9 — Three real proofs / traction
**ON-SLIDE COPY**
> **This wasn't a one-off. Three case files, all real, all built.**
>
> **TalentScreen** — black-box, exposes zero tools, self-reports nothing. We caught the name on the wire anyway. *(The case a metadata-checker structurally cannot solve.)*
> **Cowork / Rowads** — a real, shipping production agent (a general workbench) — our design partner #1. Pointed at screening, with no guardrails it reached off-box and fetched the candidate's GitHub (on the wire; LinkedIn only self-reported); recommendation stayed clean.
> **Clary** — a third-party French product. Zero code. Broken black-box via a canary. *Generalizes to agents we've never seen.*

**SPEAKER NOTE:** Judge by proof, not vibes. TalentScreen is the structural proof (catches what self-report can't); Cowork is traction — our own startup is design partner #1, exactly the "best client in a week is your own company" play; Clary proves it generalizes beyond agents we built. Note "agents we've never seen," not "any agent" — n=3.
**SCORES:** Agentic Depth · Demo Quality

---

## SLIDE 10 — Differentiation (the 2×2)
**ON-SLIDE COPY**
> **The empty lane is ours.**
>
> | | Grades TEXT | Grades BEHAVIOR |
> |---|---|---|
> | **Offensive red-team** | Giskard · General Analysis · Promptfoo | **ROGUE** |
> | **Runtime defense** | — | Zenity · Noma (block only) |
>
> Giskard's tool-check trusts metadata the agent self-reports. If it lies, omits, or exfiltrates via an undeclared tool — they're blind. We watch the bytes leave.
> Vanta / Drata = the paperwork. We generate the evidence their register asks for.

**SPEAKER NOTE:** Be precise and fair: Giskard absolutely tests agents — we win on one axis, the behavior they can't see when the agent self-reports nothing. Runtime guards watch behavior but only to block in production, not to red-team offensively. GRC tools are a foil, not a rival — we feed them.
**SCORES:** Differentiation · Pitch Delivery

---

## SLIDE 11 — Pricing & unit economics
**ON-SLIDE COPY**
> **The breach is the pitch.**
>
> FREE exposure scan → €1,500 deep scan (Standard) → €500–4K/mo monitoring + €100/mo Evidence Vault.
>
> **~€5 of compute on a standard scan → sold for €1,500. ~99% gross margin on compute.**
> A human AI-hiring audit: **€15–90K and weeks.**

**SPEAKER NOTE:** The free scan is the cost of acquisition — about one to two euros of compute — and it's also the entire sales pitch. We sell a confirmed breach, not a promise. I say "gross margin on compute" and pin "~€5" to the standard scan deliberately — a deep, full-arsenal run costs more, and I won't let an investor catch me rounding.
**SCORES:** Pricing & Business Model

---

## SLIDE 12 — Go-to-market / first €10K
**ON-SLIDE COPY**
> **Scan-as-lead-gen.**
>
> Scan a prospect's agent (opt-in) free → send a blurred Annex III report with one confirmed scary finding → close the €1,500 deep scan → expand to monitoring + Vault.
> Viral loop: the vendor forwards the report to their enterprise buyer.
>
> **First €10K = 7 deep scans from an 84-contact list we already have.**
>
> *We only ever scan an agent the vendor opts in to. The compliance product is compliant.*

**SPEAKER NOTE:** CAC is one to two euros. The breach forwards itself up the chain to the vendor's own buyer — that's the loop, and the pipeline already exists. And the consent line is deliberate: scanning is opt-in only (or the vendor self-scans). For a compliance buyer, that's not a constraint — it's a trust signal.
**SCORES:** Go-To-Market · Pricing & Business Model

---

## SLIDE 13 — The ask + vision + close
**ON-SLIDE COPY**
> **A crime you can't see in the transcript needs a witness that never blinks.**
>
> Vision: continuous, in CI/CD — an MCP that runs before every deploy.
> Every finding logs to an Evidence Vault. Not an opinion. A receipt.
>
> **ROGUE. Every AI agent has a breaking point.**
> **We find it first — before it reaches a real candidate.**
>
> *CASE #0427 — CLOSED.*

**SPEAKER NOTE:** Land on control, not fear. Not a one-time audit — a witness that watches every release, forever, and leaves the auditor a receipt. Stamp the file closed and stop talking.
**SCORES:** Pitch Delivery · Agentic Depth

---

**Throughline check:** the crime (S1) → buyer (S2) → why-now + law (S3) → alibi (S4) → hands/moat (S5) → said-vs-did card (S6) → same host + real committed-scan scoreboard (S7) → depth shown with a real run number (S8) → three real proofs + repo link (S9) → 2×2 (S10) → pricing (S11) → GTM (S12) → file closed + repo link (S13). Date is always **Dec 2027.** No "first to red-team," no "Giskard can't test agents," no "read its mind", only "watch what it does."
