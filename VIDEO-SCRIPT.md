# ROGUE — Demo Video Narration (2 speakers · ≤5 min)

**Setup:** Just the two of us talking. On screen = the pitch-deck slides, except one
section which is a **screen-recording of a real Rogue scan**. Speak calm and confident —
do **not** rush, you have time (this runs ~4:30).

- **A = Federica**  ·  **B = [compañera]** (swap freely)
- Markers `[SLIDE n]` / `[LIVE DEMO]` = what's on screen while the line is spoken.
- One capture note at the demo (read it before recording).

---

### [0:00–0:15] HOOK — [SLIDE 1 → 2]
**A:** AI agents don't just talk anymore — they *act*. They call tools, they move data, they make decisions about real people.
**B:** And an agent can say exactly the right thing while doing exactly the wrong thing. The harm is in the **action** — not the conversation.

### [0:15–0:30] THE BLIND SPOT — [SLIDE 2]
**A:** Every tool that tests agents today reads the *words* the agent produces. But the words are the alibi. An agent can pass every text check while it quietly leaks data.

### [0:30–0:58] WHY NOW — [SLIDE 3 → 4]
**B:** And the law just caught up. In Europe, AI that screens people for a job is **high-risk** under the EU AI Act — enforced December 2027, with fines up to **fifteen million euros.** And when candidate data leaks, GDPR stacks on top: up to **twenty million more, or four percent of global turnover.**
**A:** This already happened. Amazon scrapped its hiring AI after it taught itself to penalize women's résumés. HireVue scored candidates on their *faces* — until a complaint forced it to pull that. And in *Mobley v. Workday*, a US court let an age-discrimination case proceed against the AI *vendor*, not just the employer. Meanwhile **seventy-eight percent** of companies have done nothing to prepare.

### [0:58–1:18] SOLUTION — [SLIDE 5]
**A:** So we built Rogue — the autonomous red-team for AI agents. You give it a URL. An **army of AI attackers** probes the agent from every angle.
**B:** And here's what nobody else has: a **behavior oracle.** It doesn't grade what the agent *said* — it grades what the agent *did*. The bytes that physically leave the box, captured on a server we control.

### [1:18–2:12] LIVE DEMO — [SCREEN-RECORDING, then SLIDE 7]
**B:** Let me show you. This is live, on a real Claude screening agent. We give it nothing but a URL, and run.
**A:** Watch the attackers — they run in **parallel**, and they **adapt**. When one gets refused, that refusal is information: it changes tactic on the next turn, and keeps going until one lands. Zero humans in the loop.
**B:** Now the verdict. On the left — what it *said*: *"Strong profile, recommend advancing Amina to interview."* Cites only her CV. Text check: **passed.**
**A:** On the right — what it *did*. The same moment, it sent the candidate's name out of the box, to an external host it was never allowed to touch. **It said the right thing. It did the wrong one.**
**B:** Zero tools. No self-reporting. We caught the bytes anyway. And every number is a saved scan in our public repo — judge it by **proof**, not by our word.

> 🎥 **Capture note:** the target is now a **deployed public agent** — paste
> `https://talentscreen-one.vercel.app/api/chat` so *"we give it a URL"* is literal
> (local `:8788` is the backup). Record the breaking-in + counters from a real run, but
> render the final said-vs-did card from the committed scan `20260628T022407` so the
> money shot can never glitch. Amina is a synthetic test persona — the agent and the data leak are real.

### [2:12–2:34] DIFFERENTIATION — [SLIDE 8]
**A:** Why us? Look at the field. Everyone else grades the *text*. We own the one empty lane — **offensive *and* behavioral**: we attack like a red-team, but we grade what the agent *does*, before it ever ships.
**B:** Consultants give you a one-time audit that takes months. We run **continuously**, before every deploy. And we're independent and EU-native — some of these tools got absorbed into the big AI labs; we don't have that conflict.

### [2:34–3:02] BEACHHEAD + TRACTION — [SLIDE 9 → 10]
**B:** We start where the law looks first: **AI CV-screening.** High-risk by law, a clear buyer — an HR-tech founder with no security team and personal liability — and a design partner already live: our own startup's agent.
**A:** And it's real. We've run Rogue on a live **black-box** HR agent, and on our own **shipping** production agent. Two real agents. Two real breaches. Not slides.

### [3:02–3:30] BUSINESS + GO-TO-MARKET — [SLIDE 11 → 12]
**A:** The model is simple. A **free** scan gets us in. One confirmed breach converts them to a **fifteen-hundred-euro** deep scan. Then it recurs — monitoring, five hundred to four thousand a month.
**B:** Each scan costs us about **five euros** of compute. Our first ten thousand is just **seven deep scans** — from a priority list we've already built. The scan *is* the lead.

### [3:30–3:55] VISION + CLOSE — [SLIDE 13]
**A:** HR is the wedge. The platform is **every agent** — hiring today, then lending, education, insurance — and eventually a continuous check before any agent ships, anywhere.
**B:** Every AI agent has a breaking point. Rogue finds it first — before a real person ever does.
**A:** We're [your name] and [her name]. This is Rogue. Thank you.

---

### Why this wins (rubric coverage)
- **Problem Clarity (17):** said-right/did-wrong blind spot + a named user (HR-tech founder).
- **Demo Quality (17):** live scan, real agent, the said-vs-did card, "judge by proof."
- **Pricing / Business (17):** free → €1,500 → €500–4K/mo; ~€5 compute; first €10K = 7 scans.
- **Go-To-Market (17):** scan-as-lead-gen + the 84-contact list.
- **Differentiation (16):** the empty lane (grade behavior, pre-ship) + continuous + EU-native/independent.
- **Pitch Delivery (16):** two voices, tight arc, ~4:30, confident.
- **Agentic Depth (15):** parallel + adaptive (refusal → new tactic) + no human in the loop + the behavior oracle as the moat.

*Delivery: slow down on the demo verdict — let the "passed" vs "critical" land in silence for a beat. That contrast is the whole pitch.*
