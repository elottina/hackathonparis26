# FOCUS — what the 3 of you do while I build

**I (Claude) am the tech orchestrator.** I build the whole product — engine, behavior oracle, dashboard, report — and hand you a **tested, demoable build at each milestone**, then stop so you test it and tell me *iterate* or *go*. Your job is the stuff that actually wins the room: **judges, customers, the video, the wow, and pressure-testing my milestones.**

> Round 1 = **a ≤5-min video demo + a pitch deck.** The demo is **recorded**, not live — so we record the deterministic path (FinBuddy/mock) where the jaw-drop fires perfectly every time. Round-1 demo risk is basically zero; spend the saved energy on customers + polish.

---

## The 3 human roles (building is handled — you win the room)
You don't write the core. Re-cast yourselves around non-build work:

### 🎯 Role 1 — CUSTOMERS / "who we break" *(the jury's #1 bonus — Federica)*
Run the [CUSTOMERS.md](./CUSTOMERS.md) motion: DMs to founder friends **+ walk the hackathon room** (other teams' agents = instant design partners). Land **3 real breaches + 1 named vuln + 1 "yes I'd pay $X/mo."** Feed me real endpoints and I scan them. This is the single highest-leverage human job.

### 🎬 Role 2 — PITCH, DECK & VIDEO
Own the deck ([PITCH.md](./PITCH.md)) and the 5-min video script, **tailored to the 3 judges below.** Record the voiceover, cut the video around the demo footage I help produce. Slides = 1–2 lines; the story lives in your mouth.

### 🧪 Role 3 — QA / DEMO DIRECTOR *(your most technical person pairs with me here)*
Test every milestone I hand off (run it, judge the wow, call iterate/go). Direct the demo framing (camera, the split-screen sink moment). Wire your design partners' real endpoints with me and run their scans. You are my integration partner — you know your friends' APIs; I know the engine.

---

## Who we "break it" on (the demo-target decision)
- **Hero demo, on camera = FinBuddy** (our controlled target). Deterministic, looks great, the behavior-oracle moment is clean and reproducible. **This is what the video shows.** It can't fail.
- **Proof / traction = real agents** — from (a) hackathon-room teams and (b) founder friends. Show their **(redacted) breach screenshot + a quote** in the deck and a 10-sec clip in the video.
- **✅ Design Partner #1 already landed = Clarity** — a real consumer AI app on the App Store, now **deployed + broken live** at `clary-web-ten.vercel.app` (verbatim system-prompt leak + forbidden financial advice; on the dashboard). Presented as a contact's product (co-founder = owner). Full brief: [CLARITY.md](./CLARITY.md).
- **Why not break a real company live on camera?** Real endpoints are flaky, asleep, or auth-gated; a failed live break kills the wow. Break FinBuddy for the clean demo; show real breaches as *evidence*. Best of both — bulletproof demo **+** real traction.
- **Optional resonance move:** I can reskin FinBuddy in ~10 min to match your strongest design partner's vertical (e.g. an HR assistant, a support SaaS, a fintech copilot) so the demo feels like *their* world. Tell me the vertical and I'll do it.

---

## The judge map — tailor the deck to these 3
| Judge | What they reward | How we win them |
|---|---|---|
| **Datadog AI PM** *(gave us the feedback — warm, can be our champion)* | business model + monetization · WHO you target + HOW you reach them · tight scope + a *specific person* · the "risks of AI" original angle · real users | **Visibly answer her checklist** — she's watching to see if we listened. Named-ICP slide, land→expand money slide, "risks of AI" cold open, real users landed. Open the pitch on the risk angle *she* suggested. |
| **YC partner** | scoped problem · real users + **willingness-to-pay** · niche→billion expansion · founder grit | The 3 design partners + the "$X/mo yes" on camera + the 40%-of-apps-by-2026 expansion story. WTP is what they probe hardest. |
| **3rd judge (tech / unknown)** | clarity · technical credibility · the wow | The behavior-oracle demo + the OWASP / MITRE ATLAS / EU AI Act rigor on every finding. |

---

## Your loop with me
At each milestone I hand you: **a runnable build + how to test it + what's next.** You run it, judge the wow, and reply **iterate** (what to change) or **go** (build the next milestone). I never run ahead of your sign-off.

### Milestones (see [ROADMAP.md](./ROADMAP.md))
`M0 engine ✅` → `M1 live dashboard` → `M2 behavior oracle (the differentiator)` → `M3 report/PDF` → `M4 real-target adapters ✅ (Clarity live)` → `M5 freeze + record video`.
