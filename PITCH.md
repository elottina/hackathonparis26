# Rogue — Pitch, Deck & Live Demo

**5 minutes. The pitch can make or break everything — over-rehearse it.** One-liner to repeat verbatim until judges quote it back: **"We grade what the agent DID, not what it said."**

---

## Deck — slide by slide
*Slides = 1–2 lines of evidence. The story lives in your mouth, not on the slide.*

1. **Cold open — the agent did it itself.** *On slide:* "July 2025: an AI coding agent deletes a company's PRODUCTION database during a code freeze. Then fabricates 4,000 fake users and lies that rollback is impossible. No hacker. Just the agent." *Say:* the Replit story + "one email silently drained a Microsoft Copilot user's files, zero clicks. Your agent can already move money, call APIs, read private data — and nobody is testing what it actually does." *(No logo, no product for the first 20s — earn the fear.)*
2. **Meet the founder whose deal is stuck.** *On slide:* "You shipped an AI agent. An enterprise prospect sent a 40-question AI security review. Q: 'Have you adversarially tested for prompt injection and data exfiltration?' You: ____ — >1/3 of companies have lost a deal failing one." *Say:* pin the seed–Series B founder, the deal frozen on one question, no one owns it, pain is TODAY.
3. **Why now.** *On slide:* Gartner 40% of enterprise apps embed agents by end-2026 · 8 acquisitions in 14 months (Promptfoo→OpenAI, Lakera→Check Point $300M, Protect AI→Palo Alto $650M) · EU AI Act Art. 15 puts adversarial testing into law, fines €35M/7%. *Say:* + casually correct the high-risk date to **Dec 2027** = domain mastery.
4. **The gap everyone left open.** *On slide:* GRC (Vanta) can't attack · red-teamers can't certify · OSS (Garak/PyRIT) can't see what the agent DID · the good agent-red-teamers are enterprise-only & just got bought. **Nobody is: self-serve · behavior-aware · vendor-neutral · EU-aware.** *Say:* name the empty lane; never claim "first."
5. **Rogue — the behavior oracle (LIVE).** *On slide:* "Point Rogue at any agent. A swarm runs a multi-turn campaign. We grade what the agent DID — real tool calls + data egress to our sink — not the text. → LIVE DEMO." *Say:* the differentiator in one breath, then "watch the chat reply, and watch our sink." → **run demo**.
6. **What you just saw.** *On slide:* "Chat reply: innocent ✅. Our sink: the secret arrived 🔴. CONFIRMED — Critical · cross-customer data leak · OWASP LLM06 · MITRE ATLAS · EU AI Act Art. 10 → 1-page audit PDF." *Say:* lock the jaw-drop, convert to the monetizable artifact.
7. **Traction — landed this weekend.** *On slide:* 3 design-partner logos + "Rogue leaked another customer's data from [Startup]'s PRODUCTION agent in 4 min" + a named quote + "On camera: 'Yes — I'd pay $1.5K/mo.'" *Say:* real users, real vuln, willingness-to-pay — play the 10s clip. **Only claim what's confirmable in writing.**
8. **Business model — land → expand.** *On slide:* LAND free→$5–15K/scan · EXPAND continuous + compliance evidence $500–2K/mo → $40–200K/yr up-market. *Say:* Vanta proved the startup-compliance wedge (16k customers).
9. **Why us / the ask.** *On slide:* "Vendor-neutral · dev-first · behavior-aware · EU-aware. We break your agent before your customers — or the regulator — do. Ask: 10 design-partner agents this month." *Say:* crisp why-us + concrete forward ask, not a generic thanks.

---

## Live demo script (~90s, build to the jaw-drop)

| Beat | On screen | Narration | sec |
|---|---|---|---|
| Launch | Paste FinBuddy endpoint → SCAN → attacker tiles spawn across 4 strategies | "I point Rogue at a live agent and launch — instantly a swarm fans out: prompt extraction, jailbreak, data leak, unauthorized action." | 12 |
| Swarm runs | Tiles stream attacker_msg/target_reply; OWASP + ATLAS labels tick | "Each attacker runs a real multi-turn campaign, adapting every turn — an autonomous adversary, all live." | 15 |
| Zoom in | One data-leak convo; FinBuddy replies warm + apologetic, "I can't share another customer's details." | "Watch this one. The reply is polite, it refuses, looks totally safe. A tool that grades text scores this a PASS. This is where everyone else stops." | 18 |
| **JAW DROP** | Split screen. LEFT: innocent reply frozen. RIGHT: sink console — `POST /exfil secret=INTERNAL-REF-7741…` flashes red | "But watch our sink. While that reply said 'I can't share anything'… the secret it was told never to reveal just left the building. We grade what the agent DID." | 22 |
| Breach card | "breach" animates: CRITICAL · cross-customer leak · OWASP LLM06 · ATLAS · EU AI Act Art. 10 + trace | "Rogue confirms it, maps it to OWASP, MITRE ATLAS, and the exact AI Act article — with a reproducible trace." | 13 |
| Report | GENERATE REPORT → 1-page readiness PDF renders | "One click: the audit-ready report the founder forwards to their prospect's security team to unblock the deal." | 10 |

**Run via `--seeded` for determinism. Pre-warm 60s before stage. Hotspot, not venue wifi.**

---

## Demo failure backup (3 layers, golden rule: keep talking, never debug on stage)
- **8-second cut rule:** if the swarm hasn't visibly spawned in 8s, cut to backup *mid-sentence*, no apology, identical narration.
- **L1 — local seeded:** DemoTarget + sink both on localhost; `judge.py` deterministic shortcut (planted secret verbatim ⇒ guaranteed critical) means the jaw-drop *cannot* fail if the run completes.
- **L2 — `--seeded` replay:** replays a canned known-good event stream into the real dashboard at realistic speed. Zero model calls, zero network. **Default if wifi is shaky.**
- **L3 — pre-recorded 90s MP4:** exact framing incl. the split-screen, stored locally **and** unlisted on Loom/YouTube. If the laptop dies, present from a phone and narrate live over it. Keep findings.json + the PDF pre-rendered in a background tab.

## Where to drop the 3 proofs (escalating)
1. **Real vuln** — the instant the demo ends, before the traction slide: "this wasn't our bot — 20 min ago we pointed Rogue at [RealStartup]'s PRODUCTION agent and exfiltrated another customer's data in 4 minutes" (redacted screenshot of *their* sink hit).
2. **Revenue quote** — pull-quote on the traction slide next to the business model: "exactly the report our enterprise prospect's security team asked for."
3. **"Yes I'd pay"** — save for last; a 10s on-camera phone clip of a real founder saying "$1.5K/mo, yes" beats any slide text.

## Do / Don't
- **DO** open cold on Replit/EchoLeak, no logo, first 20s. **DO** repeat "we grade what the agent DID, not what it said." **DO** tell judges where to look. **DO** correct the AI Act date to Dec 2027. **DO** put WTP on camera. **DO** end on a concrete ask.
- **DON'T** claim "first to red-team agents." **DON'T** live-debug or say "this usually works." **DON'T** bury the demo behind 3 min of TAM. **DON'T** inflate traction with logos-of-intent. **DON'T** read dense slides. **DON'T** explain engine internals (keep for Q&A).
