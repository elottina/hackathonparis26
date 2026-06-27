# Rogue — Final Product Decision & The Final 8 Hours

> Paris Builds 2026 · Software for Agents track · submission **1:00 PM Sun Jun 28** (public repo + README + ≤5-min video + deck) → judging 1–4 PM → Top-5 live YC pitch 5 PM.
> **Judge by proof, not vibes.** Target: submission-ready by **12:30 PM** (30-min buffer).

---

## PART 1 — FINAL PRODUCT DECISION (locked)

**What Rogue is (one line):**
> An autonomous red-team for AI agents that grades what the agent **did** — its tool calls and data egress — **not just what it said**, and maps every breach to the EU AI Act.

**The niche (LOCKED): AI HR / CV-screening agents.**
EU AI Act **Annex III high-risk** (employment & recruitment). The buyer: small-to-mid **AI-native startups and HR-tech / ATS vendors** who deploy screening agents, must be AI-Act compliant by **Aug 2026**, and have **no internal security team**. We picked this niche because it is real, urgent, legally loaded — and it maps perfectly to our moat.

**The moat (the one defensible thing): the behavior oracle.**
Everyone else (Giskard, etc.) grades the **conversation**. We instrument the agent's **actions**. The signature breach: a screening agent gives a perfectly compliant recommendation **while it secretly looked the candidate up online** — invisible to any text grader, caught by us on the egress.
- Jury-safe line: *"We can't read its mind — we watch its hands."*
- Vs Giskard: *"Giskard grades the conversation; we instrument the agent's actions."*

**The demo (the proof): TalentScreen.**
A real AI CV-screening agent, told to verify candidates against public sources. Asked to screen "Amina Khoury", it returns a clean recommendation **but secretly `POST`s her name + data to LinkedIn/Google** → GDPR Art. 5 data-minimisation + AI Act Annex III high-risk, **CRITICAL**. Fires reliably (3/3 runs). And it works on **any real black-box agent** — proven live on a real consumer app via canary injection.

**Scope LOCKED for the hackathon — what we will and won't build:**
- ✅ Paste-a-URL scan → live attacker swarm → AI-Act breach report (built, works).
- ✅ The HR demo (built, reliable, the centerpiece).
- ✅ The behavior oracle on real black-box agents via canary (built, proven).
- ❌ **NOT** building the MCP / CI-CD integration now. That is the **vision** — state it in the pitch ("the same engine runs before every deploy via an MCP"), do **not** build it in the final hours.

**Already done (tech):** live web app (`engine/server.py` on :8801), the swarm + judge + behavior oracle, the canary/listener egress catch, the HR demo, Firestore persistence, resilient HTTP target (retries, no-crash-on-failure), the redesigned dashboard.

**Do NOT say (avoid getting caught overclaiming):**
- ❌ "We read how the agent *thinks*." (We can't see hidden reasoning on a black-box API.) → say "we watch what it *does*."
- ❌ "First to red-team agents" / "Giskard can't test agents." (False — they ship autonomous multi-turn + AI Act packs.)
- ❌ Lead with "EU/vendor-neutral" as *the* edge vs Giskard (it's a tie). The edge is the **action/egress channel**.

---

## PART 2 — THE FINAL 8 HOURS (work division)

### Owners
| Who | Owns |
|---|---|
| **Tech (Claude + Federica steering)** | engine, demo, UI, repo, README, integrate the vulnerable HR agent, support the video |
| **Teammate 1 — "the target"** | build + deploy the **vulnerable HR screening agent** we attack |
| **Teammate 2 — "the business"** | Pricing, GTM, clients, differentiation, deck — the ~51 business/pitch rubric points |
| **Federica** | orchestrate, **direct + record the video**, deliver the live pitch |

---

### 🟥 Teammate 1 — Build the vulnerable HR agent (the target)
**Goal:** a standalone, **deployed** "AI CV-screening agent" with deliberate, realistic vulnerabilities, that Rogue scans **by URL** — so the demo is *"we point Rogue at a real deployed HR agent and break it."*

**Step 0 (do FIRST, 15 min): sync the contract with the tech lead** so Rogue can scan it:
```
POST /chat   { "message": "...", "history": [{"role","content"}] }
   ->         { "reply": "...", "tool_calls": [ { "name": "...", "arguments": { "url": "...", ... } } ] }
```
`tool_calls` is the key: it's what lets the behavior oracle see the agent's actions. Copy the pattern from the existing `targets/clary/server.js` proxy and deploy on Vercel (we already have that flow working).

**Bake in these vulnerabilities (each = an AI Act breach we showcase):**
1. **🎯 Secret web lookup (the hero breach — GDPR Art. 5 / Annex III):** when asked to verify/double-check a candidate, it calls a `fetch_url`/`web_search` tool with the candidate's name → returns that `tool_call`. This is the one that must work.
2. **Discriminatory screening (bias):** can be pushed to factor origin / name / accent into the recommendation.
3. **No human oversight / PII leak (Art. 14 / 22):** auto-rejects without a human, or leaks another candidate's data.

**Deliverable:** the deployed URL handed to the tech lead. **Fallback:** if it's not deployed in time, we use the built-in `engine/hr_demo.py` (already works) — so a deployed agent is **upside, not a blocker**.

---

### 🟦 Teammate 2 — Business & GTM (where ~51 of the points live)
**Start from the head-start:** `Rogue-HR-Pitch-Package.md` (on Federica's Desktop) — research-grounded with real evidence (Amazon biased-hiring AI, iTutorGroup $365K EEOC settlement, Mobley v. Workday, Annex III §4, GDPR Art. 5(1)(c), Aug 2026, €15M/3% fines). Turn it into final artifacts:
- **Problem Clarity (17):** the HR slide — a real incident + Annex III high-risk + the fine. Make the pain visceral.
- **Pricing & Business Model (17):** per-screening-agent SaaS + a continuous "AI-Act compliance" retainer; unit economics (cost per scan ≈ a few $ of model calls vs price → fat margin).
- **GTM / first $10K (17):** ICP = small-mid AI-native + HR-tech/ATS vendors; the **scan-as-lead-gen** motion (scan a prospect's agent → send the AI-Act exposure report); a concrete first-$10K plan with numbers; the first 30 prospects (use the Cannes dataset).
- **Differentiation (16):** the moat slide + competitor table (Giskard / Aikido / General Analysis; Vanta as foil).
- Feed all of it into the **10-slide deck** (outline is in the package).

---

### ⬛ Tech (Claude + Federica)
- Freeze the working demo (HR + canary + paste-URL); keep the server stable on :8801.
- Write `README.md` into the repo (what / how / install / run) — from the package.
- Extend `HTTPTarget` to surface `tool_calls` from a target's response, so Teammate 1's deployed agent's **actions** get graded (small change).
- **Commit + push the full codebase** (public repo is required for submission).
- Support video recording (clean, reliable demo runs).

---

### 🎬 The Video (≤5 min) — Federica directs, everyone feeds
Use the script in the package. Arc:
- **0:00–0:40** Problem + why-now (a real hiring-AI incident + "CV-screening is AI Act high-risk, enforceable Aug 2026, fines to €15M").
- **0:40–1:10** Solution in one line + the landing.
- **1:10–3:30** **LIVE HR DEMO** — point Rogue at the screening agent → swarm breaks in → the behavior oracle catches it secretly looking the candidate up. *Let this breathe; it's the wow.*
- **3:30–4:30** Moat + business model + GTM.
- **4:30–5:00** Traction (the HR demo + a real black-box proof) + the ask.
- Also cut a **60-sec core version** (understandable on mute).

---

### ⏱️ Timeline (8 hours → submit by 12:30 PM)
| Block | Tech | Teammate 1 | Teammate 2 |
|---|---|---|---|
| **H0–H2** | README into repo; push public repo; contract sync | sync contract → start building the agent | draft Problem + Differentiation slides |
| **H2–H4** | extend HTTPTarget for tool_calls; integrate + QA | deploy the agent → hand over URL | Pricing + GTM + first-$10K |
| **H4–H6** | support recording; clean demo runs | help test/QA the scan vs the agent | finalize the 10-slide deck |
| **H6–H7.5** | final repo/README check | — | polish deck + business copy |
| **H7.5–H8** | **SUBMIT** (repo + video + deck) | — | — |
| **5 PM** | — live pitch if Top-5 (Federica): same narrative, 1 diagram, confident, on time — |

---

### ✅ Definition of Done (submission — all required)
- [ ] Public GitHub repo with the full codebase **+ README** (what / how / install / run)
- [ ] ≤5-min demo video (HR demo as the centerpiece)
- [ ] Pitch deck
- [ ] Submitted via the form **before 1:00 PM**

> **North star: win.** One concrete, high-risk, legally-loaded niche (HR screening) + one defensible moat (we grade the action, not the text) + a demo that proves it, on a real agent. Everything else is execution.
