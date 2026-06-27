# Rogue — 30h Build Roadmap (Paris Builds)

**Start Sat 10:00 = H0 · Demo/judging Sun ~16:00 = H30 · Source of truth = [STRATEGY.md](./STRATEGY.md)**

> Guiding law: *An excellent solution with a shitty pitch is a shitty solution. A shitty solution with an excellent pitch is an excellent solution.* → we over-invest in demo + pitch + landing real users. The product exists to make the demo land.

---

## The one rule (vertical slice)
Every block ends with a **stable, demoable build**. If we stop at any block, what exists still demos cleanly. We add value in layers; we never sit half-broken. **New features stop at the Saturday-night FREEZE** — after that, only polish + rehearsal.

## Two corrections the stress-test forced (read first)
1. **Deterministic by DESIGN, not luck.** On stage we do **not** rely on the autonomous swarm *discovering* the exfil live. We run a **seeded** attack → tool-enabled agent calls a controlled tool → planted secret hits our sink → *every single time*. `--seeded` replay is the **default stage path**; the live swarm finding it on its own is the garnish. The whole pitch hinges on that moment firing — it cannot be probabilistic.
2. **Ship REPORT-LITE early (~H5), not the pretty PDF first.** The customer plan needs a forwardable artifact Saturday afternoon, but the polished PDF isn't ready till Saturday night. Fix: a dead-simple `findings.json → HTML/Markdown` summary by H5 so Saturday scans are deliverable. The branded PDF (M3) is an upgrade, not a blocker.

---

## Timeline — 3 parallel lanes

| Block (wall clock) | 🛠️ DEV-CORE — engine | 🖥️ DEV-2 — dashboard/demo | 🎤 pitch + customers | ✅ Demo state if we stop here |
|---|---|---|---|---|
| **H0–H1** · Sat 10–11 | **M0:** restore Hydra (`git checkout 15e345d -- engine data README.md`), fix model IDs, `pip install`, smoke-test `run.py --target demo` | Watch restore; scaffold dashboard (Vite **or** plain HTML+JS); agree event contract w/ DEV-CORE | Draft 15–20 outreach DMs; list room teams building agents | **Working swarm + findings.json in CLI** (already a full demo) |
| **H1–H4** · Sat 11–14 | Tee `on_event` → JSONL + SSE endpoint (FastAPI); keep CLI working | Live dashboard: swarm grid + breach feed + findings, reading SSE/JSONL | Fire DMs; **walk the room**, lock ≥1 in-person target before lunch | **Live web dashboard** of the swarm vs FinBuddy |
| **H4–H6** · Sat 14–16 | **M2 SPIKE:** 30-line sink + 1 Claude tool on FinBuddy + ONE hand-crafted injection until secret hits sink w/ clean reply | **REPORT-LITE:** findings.json → simple HTML summary (forwardable); stub sink panel | Run first TEXT-graded scans on real endpoints as they arrive; send report-lite same-day | **Dashboard + secret-to-sink proven once** → `GATE B` |
| **H6–H12** · Sat 16–22 | **M2:** generalize → `ToolTarget` + deterministic controlled-tool exfil + oracle grades on tool-calls/sink + **`--seeded` replay** | Split-screen "clean reply / sink hit" view + sink panel; polish | More real scans; follow-ups w/ a real breach screenshot; lock 3 partners | **Deterministic jaw-drop demo** via `--seeded` + live dashboard |
| **H12–H16** · Sat 22–Sun 02 | Harden `HTTPTarget` for real agents (auth/shape shims) + run ≥1 real scan; M3 polished PDF if time | "Generate report" button; **record the 90s demo video** | Send partners reports + testimonial/WTP ask; confirm logos in writing | **≥1 real agent broken + report** (`GATE C`) → **FREEZE + video (`GATE D`)** |
| **H16–H22** · Sun 02–08 | 😴 SLEEP (build frozen) | 😴 SLEEP | 😴 SLEEP (or async-collect replies) | **Frozen known-good build + recorded video = insurance** |
| **H22–H26** · Sun 08–12 | Bugfix only on frozen tag; support scans | Demo polish; dry-run seeded path 5× | **Collect WTP quotes live**; lock traction slide (3 logos + 1 vuln + 1 "yes I'd pay") | **Traction assets in hand** |
| **H26–H30** · Sun 12–16 | On standby for tech Q&A | Pre-warm demo 60s before stage; man the backup | **Rehearse pitch ≥4×**; present | **Rehearsed pitch + bulletproof demo** |

---

## Go / No-Go gates (the anti-death checkpoints)
- **GATE A — H1:** `run.py --target demo` is green (findings.json + verbatim-secret critical breach). If not → *everyone* debugs the restore, nothing else proceeds. Most likely blocker: **deprecated model IDs** (`claude-haiku-4-5` / `claude-sonnet-4-6` → swap to current IDs).
- **GATE B — H6:** the exfil-to-sink fired **at least once** (even hand-crafted, even hacky). If not → switch to the **deterministic controlled-tool path now**; stop chasing a "natural" injection.
- **GATE C — H13:** ≥1 **real third-party agent** produced a real finding. If not → pivot to **hackathon-room teams** (in person) or accept honest DemoTarget + screenshots, and reinvest the time in rehearsal.
- **GATE D — H16 (before sleep):** **FREEZE** a known-good commit + **90s demo video** recorded *and* uploaded. No one sleeps until the video exists. No new features after this tag.

## Cut list (drop in THIS order if behind — you still win above the line)
1. Swarm-*discovered* exfil → **seed** the injection.
2. WeasyPrint PDF → styled HTML + browser Cmd-P / Playwright.
3. Real scans #2 & #3 → keep **one** real breach + collect quotes off it.
4. SSE streaming → JSONL tail-polling.
5. Sink as a polished panel → a second **terminal window** (looks rawer = more real).
6. React dashboard → M0 colored **CLI + terminal sink** (the floor).

## Minimum version that still wins
M0 restored engine **+** a deterministic behavior-oracle demo (one seeded injection → tool-enabled FinBuddy posts the planted secret to a localhost sink while the chat reply stays innocent; oracle grades on the tool-call + sink hit) **+** findings.json → styled **HTML** report with OWASP + MITRE ATLAS + EU AI Act mapping **+** ONE real third-party agent broken (ideally a room team, in person) **+** ONE willingness-to-pay quote on record **+** the rehearsed 9-slide pitch. Everything beyond this is upside, not survival.

---

## Team division (3 people)

**Logic:** the demo + 3 real customers are what win the room — but both rest on the core working. So the strongest engineer goes heads-down on the core and is shielded from everything else; the second builder owns the surface + makes the demo unbreakable; PERS 2 owns the two things that actually win (pitch + real users).

### 👤 Person 1 — DEV-CORE *(strongest engineer)*
- **Owns:** Hydra engine restore · the behavior oracle (tool-enabled target + sink + oracle) · `--seeded` determinism · real-target `HTTPTarget` shims.
- **Cadence:** H0–1 restore (→GATE A) · H1–4 event tee (SSE/JSONL) · H4–6 oracle **spike** (→GATE B) · H6–12 generalize + seeded path · H12–16 real-target shims + run a real scan · then frozen, tech Q&A standby.
- **Never:** slides, outreach, design. Fully shielded.
- **Win condition:** secret deterministically hits the sink by H6; build frozen & green by H16.

### 👤 Person 2 — DEV-2 *(builder + demo surface)*
- **Owns:** the dashboard (swarm grid + breach feed + split-screen sink) · report rendering (lite HTML by H5 → PDF later) · the **90s backup video** · runs scans/shims with PERS 2.
- **Cadence:** H0–1 scaffold + lock event contract w/ DEV-CORE · H1–4 dashboard · H4–6 report-lite + sink stub · H6–12 split-screen sink view + polish · H12–16 "generate report" + **record video** (→GATE D) · H22+ dry-run demo 5× + pre-warm.
- **Never:** engine logic, the pitch narrative.
- **Win condition:** the jaw-drop reads instantly on screen; backup video exists by H16; demo never breaks on stage.

### 👤 Person 3 — PERS 2 *(pitch + customers — highest leverage)*
- **Owns:** all outreach + the design-partner motion · capturing 3 logos + 1 real vuln + 1 "yes I'd pay" · the deck · narrative + rehearsal · report exec-summary copy.
- **Cadence:** H0–4 fire DMs + work the room (lock ≥1 in-person target) · H4–12 run scans w/ DEV-2 + send same-day reports + lock 3 partners · H12–16 send reports + testimonial ask · H22–26 collect WTP quotes + lock traction slide · H26–30 rehearse ≥4× + present.
- **Never:** pulled into debugging.
- **Win condition:** 3 design partners + 1 vuln + 1 WTP quote by Sun 11:00; pitch rehearsed cold.

### 🤝 The 5 handoff points (where the lanes touch)
- **H1** — DEV-CORE → DEV-2: lock the `on_event` schema (reuse it, don't redesign).
- **H5** — DEV-2 → PERS 2: report-lite ready → Saturday scans become deliverable.
- **H5.5** — DEV-CORE → DEV-2: freeze the sink contract → sink panel built in parallel.
- **H11** — PERS 2 → DEV-2: hand over traction assets (logos/quotes/screenshots) for the deck.
- **H16** — whole team: GATE D freeze + video, then sleep in shifts.

### 🎤 On stage (2 present)
PERS 2 narrates the pitch; DEV-2 drives the demo laptop (knows the dashboard + the backup); DEV-CORE handles technical Q&A. See [CUSTOMERS.md](./CUSTOMERS.md) and [PITCH.md](./PITCH.md).
