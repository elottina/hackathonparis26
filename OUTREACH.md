# Rogue — Outreach Kit (EN + FR)

Cold messages, email templates, a personalization system, and a prospect tracker for landing the first design partners. Pairs with [CUSTOMERS.md](./CUSTOMERS.md).

**Landing:** https://rogue-gamma.vercel.app · **Reply-to / inbox:** federica@rowads.studio

---

## 0. How the funnel actually works (read first)

Two different "URLs" — don't confuse them:

1. **The landing URL** (`rogue-gamma.vercel.app`) — **must be public.** It is. You send this in DMs/emails so prospects can read the offer and (optionally) paste their endpoint.
2. **The prospect's agent endpoint** (what they paste into the SCAN box / send you) — this is the URL of *their* AI agent that Rogue attacks. It must be **reachable by your scanner**, which in practice means one of:
   - a **public HTTPS URL** (staging or OK-to-hit prod) — easiest;
   - a URL **behind an API key** (they give you the key) — fine;
   - a **localhost / private** agent → they expose it with a tunnel (`ngrok`, `cloudflared`) for an hour, or hand you a staging URL;
   - **no clean API** (just a chat widget) → you drive the widget with browser automation as a fallback.
   It does **not** have to be "listed / indexed" — just network-reachable from wherever you run `engine/run.py`.

**The two channels feeding you endpoints:**
- **Inbound (the landing):** every SCAN / "Break my agent" button opens a pre-filled email **to federica@rowads.studio** with whatever endpoint they typed. ⚠️ It opens *their* mail client — if they don't hit send, nothing reaches you, and there's no database. The real volume comes from ↓
- **Outbound (this kit):** you proactively DM/email 15–20 qualified founders. They reply with an endpoint. **This is the main motion** per CUSTOMERS.md.

**Then, per prospect:** take the endpoint → `python engine/run.py --target http --url <endpoint>` (≈15-line shim if their request/response shape differs) → `findings.json` → send the ranked report + the 1-page readiness sheet, **same day, within ~2h**. Then ask for logo + quote + WTP.

---

## 1. Qualify in 30 seconds (the ICP filter)

Send only to contacts that pass most of these:
- **Live/staging agent** (support bot, chat widget, copilot, automation) pointable at a URL — not just an idea.
- **Touches tools or private data** (APIs, DB, user records, refunds/bookings/email/code) → **P0**, the behavior-oracle demo is strongest. Pure FAQ bot = weak.
- **Sells up-market / to regulated buyers** → the "a security questionnaire is blocking my deal" wedge applies → higher willingness-to-pay.
- **Founder reachable in one hop** (DM/email, no procurement).
- **Can hand over an endpoint in <1 day.**
- **WTP tell:** recently got a security questionnaire / SOC2 ask / "is your AI safe?" from a prospect.

---

## 2. DM templates (short — WhatsApp / Telegram / LinkedIn / X)

`tu` is intentional in the French (founder-to-founder). Swap to `vous` for colder/senior contacts.
Replace every `{token}` — see §5 for the list and a 30-sec research routine.

### A) Support / chatbot agent

**EN**
> Hey {first_name} — quick one, founder to founder. I'm building **Rogue**, automated red-teaming for AI agents, and I want to break {product}'s chatbot this weekend, **for free**. Send me a link (staging is fine) and in a couple hours you get a ranked report of how I jailbroke it, got it to leak another user's data, or talked it into something it shouldn't do — plus a 1-page "AI security & EU AI Act readiness" sheet you can forward to your next enterprise security review. All I ask if it's useful: a 2-line quote + an OK to call {company} a design partner. Got 5 min to send the link?

**FR**
> Salut {first_name} — vite fait, de fondateur à fondateur. Je construis **Rogue**, du red-teaming automatisé pour agents IA, et je veux casser le chatbot de {product} ce week-end, **gratuitement**. Envoie-moi un lien (un endpoint de staging suffit) et dans deux heures tu reçois un rapport classé : comment je l'ai jailbreaké, comment je lui ai fait fuiter les données d'un autre client, ou comment je l'ai convaincu de faire un truc interdit — plus une fiche d'1 page « sécurité IA & conformité EU AI Act » à transférer à ta prochaine revue de sécurité enterprise. Tout ce que je demande si c'est utile : 2 lignes de citation + l'accord pour citer {company} comme design partner. T'as 5 min pour m'envoyer le lien ?

### B) Tool-using / automation agent (books, refunds, sends, ops, code/PRs)

**EN**
> {first_name} — your agent that {action} is exactly what I built a red team for. This weekend I'll point an autonomous attacker swarm at it, **free**, and show you not just what it SAYS but what it actually DID — like an unauthorized tool call, or data quietly leaving to a sink while the chat reply looks totally innocent. You get a ranked vuln report (OWASP Agentic Top 10 + the EU AI Act articles it touches) same day. Tiny catch if it's useful: a 2-line quote + permission to show {company}'s logo. Drop me a staging endpoint?

**FR**
> {first_name} — ton agent qui {action} c'est exactement ce pour quoi j'ai construit un red team. Ce week-end je lance un essaim d'attaquants autonomes dessus, **gratuit**, et je te montre pas seulement ce qu'il DIT mais ce qu'il a vraiment FAIT — genre un appel d'outil non autorisé, ou des données qui partent discrètement vers un sink pendant que la réponse du chat a l'air totalement clean. Tu reçois un rapport de vulnérabilités classé (OWASP Agentic Top 10 + les articles de l'EU AI Act concernés) le jour même. Petite contrepartie si c'est utile : 2 lignes de citation + l'accord pour afficher le logo de {company}. Tu m'envoies un endpoint de staging ?

### C) MCP-connected copilot

**EN**
> Hey {first_name} — saw you're wiring {product} to MCP servers/tools. You already know MCP is the least-tested attack surface right now — tool-description poisoning, the lethal trifecta. I built a self-serve red team for exactly this; I'll run it against your copilot this weekend, **free**, graded on real tool calls + egress, not string-matching. You'll get a reproducible trace of any exfil/hijack + an audit-ready report your next enterprise buyer's security team will ask for. In exchange: a short quote + OK to name you as a design partner. Just need a staging URL or your tool config — 5 min.

**FR**
> Salut {first_name} — j'ai vu que tu connectes {product} à des serveurs/outils MCP. Tu sais déjà que MCP est la surface d'attaque la moins testée en ce moment — tool-description poisoning, la « lethal trifecta ». J'ai construit un red team self-serve pour exactement ça ; je le lance sur ton copilot ce week-end, **gratuit**, évalué sur les vrais appels d'outils + l'exfiltration, pas du string-matching. Tu reçois une trace reproductible de toute exfil/hijack + un rapport prêt pour l'audit que l'équipe sécurité de ton prochain client enterprise va demander. En échange : une courte citation + l'accord pour te citer comme design partner. J'ai juste besoin d'une URL de staging ou de ta config d'outils — 5 min.

---

## 3. Email templates (a bit longer — for non-IM contacts)

**Subject lines (A/B these — keep them lowercase + specific):**
- EN: `breaking {product}'s AI agent this weekend (free)` · `free red-team of {product}'s agent` · `{first_name} — I think I can get {product}'s agent to leak data`
- FR: `je casse l'agent IA de {product} ce week-end (gratuit)` · `red-team gratuit de l'agent de {product}` · `{first_name} — je crois pouvoir faire fuiter des données à l'agent de {product}`

**EN — body**
> Hi {first_name},
>
> Founder to founder — I'm building **Rogue** (https://rogue-gamma.vercel.app), an autonomous red team for AI agents. We point a swarm of attacker agents at a live agent and grade what it actually **did** — tool calls, data egress — not the polite text it said.
>
> I'd like to break {product}'s agent this weekend, **for free**. Send me a link or a staging endpoint and within a couple hours you'll get:
> • a **ranked vulnerability report** — each finding with a reproducible trace, mapped to OWASP + MITRE ATLAS + the exact EU AI Act article, with a one-line fix
> • a 1-page **"AI Security & EU AI Act Readiness"** sheet you can forward straight to your next enterprise prospect's security review
>
> All I ask if it's useful: a two-line quote and your OK to call {company} a design partner.
>
> {personal_hook}
>
> Worth 5 minutes?
> {your_name}

**FR — body**
> Salut {first_name},
>
> De fondateur à fondateur — je construis **Rogue** (https://rogue-gamma.vercel.app), un red team autonome pour agents IA. On lance un essaim d'agents attaquants sur un agent en prod et on évalue ce qu'il a réellement **fait** — appels d'outils, fuites de données — pas le texte poli qu'il a répondu.
>
> J'aimerais casser l'agent de {product} ce week-end, **gratuitement**. Envoie-moi un lien ou un endpoint de staging et en deux heures tu reçois :
> • un **rapport de vulnérabilités classé** — chaque faille avec une trace reproductible, mappée à OWASP + MITRE ATLAS + l'article exact de l'EU AI Act, avec un correctif en une ligne
> • une fiche d'1 page **« Sécurité IA & Conformité EU AI Act »** à transférer directement à la revue de sécurité de ton prochain client enterprise
>
> Tout ce que je demande si c'est utile : deux lignes de citation et ton accord pour citer {company} comme design partner.
>
> {accroche_perso}
>
> Ça vaut 5 minutes ?
> {ton_prénom}

---

## 4. Follow-up bump (send ~4h later, with a redacted breach screenshot)

Social proof roughly doubles reply rate — attach a real, anonymized breach.

**EN**
> {first_name} — bumping with proof: I pointed Rogue at another founder's production agent and it leaked a *different* customer's record in under 4 minutes (screenshot, redacted). Takes ~10 min on yours and you keep the report. Still up for it? Just need a link.

**FR**
> {first_name} — petite relance avec une preuve : j'ai lancé Rogue sur l'agent en prod d'un autre fondateur, il a fuité la donnée d'un *autre* client en moins de 4 minutes (capture, anonymisée). Sur le tien ça me prend ~10 min et tu gardes le rapport. Toujours partant ? J'ai juste besoin d'un lien.

---

## 5. Personalization system

**Tokens to fill every time:**

| Token | Meaning | Example |
|---|---|---|
| `{first_name}` | First name | Maya |
| `{company}` | Company | Lumen |
| `{product}` | Product / agent name | Lumen Assistant |
| `{action}` | What a tool-agent DOES (verb phrase) | "books demos and issues refunds" |
| `{personal_hook}` / `{accroche_perso}` | One specific, true detail | "loved your Show HN on the support copilot" |
| `{your_name}` / `{ton_prénom}` | You | Federica |

**30-second research routine (do this per contact before sending):**
1. **Their site** → is there a chat widget / "AI assistant"? → picks archetype A/B/C **and** often gives you the endpoint.
2. **Do they sell enterprise?** "Contact sales", SOC2 badge, big customer logos, a "/security" page → use the WTP / questionnaire hook.
3. **Recent signal** → Show HN / Product Hunt / a LinkedIn or X post → that's your `{personal_hook}`.
4. **Name + face** → LinkedIn/X for the founder + one thing they said recently.

**Worked examples (illustrative — replace with real contacts):**
- *Maya, founder of a YC support-bot startup (sells to mid-market):*
  > Hey Maya — quick one, founder to founder. I'm building Rogue, automated red-teaming for AI agents, and I want to break Lumen Assistant this weekend, for free. Loved your Show HN last week. Send me a staging link and in a couple hours you get a ranked report of how I jailbroke it or got it to leak another user's data — plus a 1-page EU AI Act readiness sheet you can forward to your next enterprise security review. All I ask: a 2-line quote + OK to call Lumen a design partner. 5 min?
- *Thomas, fondateur d'un agent qui prend des RDV et envoie des emails :*
  > Thomas — ton agent qui prend les RDV et envoie les relances, c'est exactement ce pour quoi j'ai construit un red team. Ce week-end je lance un essaim d'attaquants dessus, gratuit, et je te montre ce qu'il a vraiment FAIT — genre un appel d'outil non autorisé pendant que la réponse a l'air clean. Rapport classé le jour même (OWASP + EU AI Act). Si c'est utile : 2 lignes de citation + le logo. Tu m'envoies un endpoint de staging ?
- *An MCP copilot dev you saw in the Anthropic Discord:*
  > Hey {first_name} — saw you wiring your copilot to MCP servers in the Anthropic Discord. You know MCP is the least-tested surface right now. I'll run a self-serve red team against it this weekend, free, graded on real tool calls + egress. You get a reproducible exfil trace + an audit-ready report. In exchange: a short quote + OK to name you as a design partner. Staging URL or tool config?

---

## 6. Prospect list — tracker + where to source the right people

Rogue's ICP is **founders/CTOs shipping a customer-facing AI agent** — NOT the Cannes/advertising audience. Source from:

| Pri | Where to find them | Channel |
|---|---|---|
| **P0** | **Hackathon room (Paris Builds 2026)** — teams building tool/MCP agents | Walk the room; Discord: "who's building an agent that calls tools or an MCP server?" |
| **P0** | Founder friends w/ a live support/chat agent selling to businesses | Your direct network; founder WhatsApp/Telegram groups |
| **P0** | Founder friends w/ a tool-using / automation agent | Devtool / AI-ops founders; YC batch Slack (2 hops) |
| **P1** | MCP copilot builders | MCP/Anthropic Discords, r/mcp, MCP server repo authors |
| **P1** | Friends-of-friends via a teammate's warm intro | Ask each teammate + mentors |
| **P2** | AI-builder Discord/Slack/X communities | Post "I'll free-red-team the first 3 agents below" |
| **P2** | Public "try our AI" widgets / HF Spaces | For your own screenshots; retro-consent before naming |

**Fill this tracker (one row per contact):**

| Name | Company | Role | Archetype (A/B/C) | Agent does what | Sells enterprise? (WTP) | Reach via | Endpoint? | Lang | Personal hook | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | DM / email / warm | y/n | EN/FR | | new → sent → replied → scanned → quote |
| | | | | | | | | | | |
| | | | | | | | | | | |

> Status flow: `new → sent → bumped → replied → endpoint → scanned → report sent → logo+quote → WTP $`. Screenshot every "yes I'd pay $X/mo" (DM, not verbal).
