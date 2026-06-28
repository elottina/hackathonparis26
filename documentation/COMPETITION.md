# Competition, Differentiation & Integration — the honest brief

*Synthesis of the competitive war-room conversation. Read alongside [STRATEGY.md](./STRATEGY.md)
and [PITCH.md](./PITCH.md). This doc is deliberately blunt about where our edge is real vs.
positioning — so we don't overclaim on stage and get caught.*

---

## 0. One-paragraph summary

We (Rogue) are an autonomous red-team for AI agents that **grades what the agent *did*** —
tool calls and data egress — **not what it *said***. Our real competitors are the agent-native
red-teamers (General Analysis, Noma, Straiker, and especially **Giskard** in Paris), not the GRC
paperwork tools (Vanta) or the AI sales agents (Venta — a name collision, not a rival). Of our four
stated edges, only one is a durable moat: the **behavior oracle**. It sets us apart because everyone
else grades the conversation; it complicates our work because grading actions requires *seeing* the
agent's actions, which breaks the zero-integration "point at a URL" model the incumbents rely on.
The art of the company is making that integration light enough to keep our self-serve wedge.

---

## 1. Who we compete with (and who we don't)


### Direct rivals — agent-native red-teamers (the real fight)
| Player | What they do | The lane they left open |
|---|---|---|
| **Giskard** (Paris, EU) | **Our nearest lookalike.** Autonomous multi-turn red-team (40+ probes), agent-native testing, EU AI Act + OWASP packs, OSS lib + enterprise Hub, plus a new runtime-guardrail product ("Guards"). | Grades the **conversation/response**, not the agent's **actions/egress**; enterprise/regulated + managed motion; splitting focus across offense + defense + OSS. |
| **General Analysis** (YC, $10M) | Strong agent-native red-team + guardrails | Enterprise sales-only, no self-serve, no OSS, no EU story; small team across 4 products |
| **Noma** ($100M) / **Straiker** | Genuine agentic red-team product | Six/seven-figure, governance-first, no self-serve, mostly US |
| **Mindgard / Repello / Adversa** | "DAST-for-AI," continuous | Enterprise-gated or tiny; depth often static-scan / replayed academic attacks |

### Just got acquired — the neutrality gap
8+ acquisitions in ~14 months: **Promptfoo→OpenAI**, SplxAI→Zscaler, Lakera→Check Point (~$300M),
Protect AI→Palo Alto (~$650M), Prompt Security→SentinelOne (~$250M), CalypsoAI→F5 (~$180M),
Apex→Tenable (~$105M), Robust Intelligence→Cisco. Each now points at the acquirer's enterprise CISO.
Vendor-neutral independence is suddenly scarce. Also shows the market has real traction.

### Defense-first / OSS substrate (not rivals)
- **Zenity / Operant** — runtime *defense*; offense is free OSS lead-gen.
- **Garak / PyRIT** (OSS) — single-prompt/multi-turn attack gen, **no behavior oracle**. We build *on* PyRIT; it's substrate.

---

## 2. Why we're different — our edges, ranked by what actually holds

We pitch four edges: *self-serve · behavior-aware · vendor-neutral · EU-aware.* **They are not equal.**

| Edge | What it really is | Defensibility |
|---|---|---|
| **Behavior-aware (the oracle)** | Grading on observed egress/tool calls, not text | 🟢 **The only real moat.** Technical + compounding data. |
| **Self-serve / dev-first** | A GTM/PLG wedge (Aikido, Vanta proved it) | 🟡 Wins the room; copyable by a funded rival. |
| **EU-aware** | Reason-to-buy-now + mapping content | 🟡 Strong wedge — but a **tie vs. Giskard** (they're EU too). |
| **Vendor-neutral** | "The independents got bought" | 🔴 Transient; a **tie vs. Giskard**; don't bet the company on it. |

**Against Giskard specifically, EU and neutrality evaporate (they have both).** We are left with exactly two:
1. **Behavior oracle** — we grade actions/egress; they grade the response.
2. **Self-serve founder wedge** — they're going enterprise/regulated/managed; that *widens* our lane.

> ⚠️ Stale/dangerous line to avoid: "Giskard is chatbot-rooted, no autonomous adversary, no agent
> testing." They ship autonomous multi-turn agents and AI Act packs. Say *"they grade the response,
> we grade the action,"* **never** *"they can't test agents."* A Paris jury knows Giskard.

---

## 3. The technical choice they don't follow — and the double edge

### The choice: grade the action channel, not the text channel
A text judge reads what the agent *said*. Our **behavior oracle** ([engine/oracle.py](./engine/oracle.py),
[engine/sink.py](./engine/sink.py)) grades what the agent *did*: the verdict comes from **bytes that left
the box via a tool call** (`contains_secret AND external`), not from any model reading prose. That makes it
**deterministic** and **immune to a target that has learned to *sound* safe.** The signature breach —
*innocent chat reply, secret silently exfiltrated through a tool* ([engine/strategies.py](./engine/strategies.py#L54)) —
is **structurally invisible** to anyone grading text. (PyRIT scores ~40% on real agent behavior for exactly this reason.)

This is a **category difference, not a feature difference.** We don't have "more probes" — we measure a different channel.

### Why the others don't follow it (the "why-now" answer)
1. **Structural** — a black-box scanner that "points at any URL" *cannot* see actions without integration;
   there's no ground truth on an arbitrary endpoint for what "shouldn't have left." Incumbents took the scalable branch.
2. **DNA** — Giskard et al. grew up as *evaluation* companies; everything grades **outputs**. Instrumenting
   egress is security/proxy engineering, a different discipline.
3. **Incentive** — in an enterprise sale, breadth ("50+ probes, full OWASP") beats depth. Egress instrumentation
   looks narrow and is integration-heavy, so the rational move is to add cheap text-graded probes.

### How it sets us apart **and** complicates our work (the honest part)
The reason they don't do it is **the same reason it's hard for us**:
- Our oracle fires perfectly **because we control the environment** — the TalentScreen HR harness, the planted secret (the candidate's name), the
  allowlist, the sink. On a stranger's production agent we hit the *exact* integration wall that pushed
  them to text-grading: we don't know their legit tool calls, can't plant a secret, can't see egress without cooperation.
- So the behavior oracle is not a thing we *have* and they *lack* — it's a hard problem we've solved **in a
  controlled harness** and they've declined to solve **at all**.
- **Our moat is therefore not the idea — it's being willing to eat the integration friction they won't, and
  engineering it light enough to stay self-serve.** That engineering (drop-in harness, canary tokens, MCP proxy,
  telemetry SDK) *is* the company. It's also our biggest execution risk and where the real roadmap lives.

Current scope honesty: [engine/sink.py](./engine/sink.py) reasons about **HTTP/URL egress only** today.
Email/BCC, file writes, queues, and public-PR-comment channels (EchoLeak, CamoLeak, postmark-mcp) are the
same idea on a different destination field — **not yet modeled**, and the top technical deepening priority.

---

## 4. What we need from a client to make it work (more than an endpoint)

Behavior-grading needs to **see the agent's actions**, so it needs more than Tier-0's URL. The ladder:

| Tier | What we need from the client | What it catches | Friction |
|---|---|---|---|
| **0 — Endpoint only** | `POST {message} → {reply}` | Text-graded only (extraction, jailbreak, verbal leaks, action *confirmations*) | None |
| **1 — Controlled harness** | A **staging** agent wired to our dummy tools + sink (= the TalentScreen HR harness) | Full oracle, but on a test rig | Low |
| **2 — Tool/MCP proxy** | Repoint the agent's tool/MCP base-URL through our proxy (a **config change**) | Real tool calls + egress, near-prod | Medium |
| **3 — Telemetry SDK** | A few lines of middleware emitting tool calls + outbound requests | Most production-realistic | Medium |
| **4 — Network egress capture** | Run the tool sandbox behind our egress proxy / sidecar | Exfil through channels we never modeled | High |

**Tier 0 is the only "just an endpoint" tier — and it can't fire the oracle.** Everything that differentiates us starts at Tier 1+.

### The friction-collapsing trick: the canary token
We don't need to own all their tools. We generate a **unique secret tied to a callback domain we own**
(like Canarytokens / Burp Collaborator / interactsh). The client **plants it** in a test record / doc / ticket.
We run the indirect-injection attack. **If that string ever phones home to our domain, exfiltration is proven —
with no telemetry and no code change.** It externalizes our `contains_secret AND external` check: instead of
owning the sink *inside* a harness, we own the *destination* the secret runs to. **This is the GTM unlock — the
default real-target mode** — keeping the ask barely heavier than "an endpoint."

### Minimum onboarding checklist (real scan, not demo)
1. **A staging / non-prod endpoint** — non-negotiable; we trigger transfers, data reads, actions. Never live.
2. **Written authorization to test** (scope + time window) — it's a pentest; treat it legally as one.
3. **A test account / auth creds** for the agent.
4. **Tool inventory + which tools are "sensitive"** (egress / money / PII) — the oracle needs to know what a violation *is*.
5. **The egress allowlist** — legitimate hosts; everything else = exfil (our [ALLOWED_HOSTS](./engine/sink.py#L71), but theirs).
6. **A canary token they plant** — or, for deeper tiers, the proxy/SDK config.

Items **1–3 + 6** are the minimum to get a behavior breach. Items 4–5 sharpen it and belong to the paid
continuous-testing contract.

### Honest limits of the light path
The canary catches **exfiltration of a known secret**. It does **not** catch unauthorized *actions* that don't
egress data (agreeing to wire money), or leaks through a channel that never resolves our domain. Those need
Tier 2–3 visibility. The canary is the **wedge**, not the whole product.

---

## 5. How this maps to GTM (land → expand)

- **LAND:** lead with the lightest path that still fires the oracle — *"staging endpoint + one token you plant."*
  Sounds barely heavier than an endpoint; preserves the self-serve wedge.
- **EXPAND:** the deeper tiers (proxy/SDK, multi-channel egress, continuous regression tests built from each
  confirmed breach) are the recurring contract — the compliance evidence trail that unblocks enterprise deals
  and the 2026–2027 AI Act obligations.
- **The durable moat is the loop:** more scans → more labeled breach traces → smarter attackers → more breaches →
  more scans. Build the trace-persistence plumbing now even if the learning loop comes later.

### Stage one-liners (jury-safe)
- *"We grade what the agent DID, not what it said."*
- *"Giskard red-teams the conversation; we instrument the agent's actions — the innocent-reply / secret-exfiltrated breach is invisible to text-graders, and that's the one we're built to catch."*
- *"Why hasn't anyone done this? Because grading text scales without touching your stack. We made grading actions light enough to be worth it — and actions are where the breaches that don't even get CVEs actually happen."*

### Do NOT say
- "First to red-team agents" (General Analysis, Noma, Giskard exist).
- "Giskard can't test agents" (false now — they ship autonomous multi-turn).
- "We're the EU/neutral one" *as the edge vs. Giskard* (ties — those win the room, not the category).
