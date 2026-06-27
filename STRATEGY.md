Security for Agents — War-Room Strategy
Paris Builds (YC) · "Software for Agents" · 27–28 Jun 2026 · built from 5 deep-research streams

0. The verdict (read this, then the rest)
Build the self-serve red team for AI agents — made for the founders shipping them, not the CISOs who'll buy later. Point it at an agent (or its MCP servers / tools). An autonomous adversary drives the agent's tools and shows — on video — how it leaks data, hijacks a tool, or gets jailbroken, graded on what the agent DID (tool calls + network egress), not on the text it said. Then it hands back the OWASP- and EU-AI-Act-mapped report the founder's next enterprise customer's security review is going to demand.

This wins because it sits in the one lane every competitor left open and answers all the mentor feedback at once: scoped problem ✅, specific buyer ✅, real monetization ✅, "risk of AI" angle ✅, EU regulation ✅, reachable customers this weekend ✅.

1. Three facts from the research that reshape everything
1. The category just got validated AND violently consolidated — in our favor. 8+ acquisitions in ~14 months: Promptfoo → OpenAI (Mar 2026), SplxAI → Zscaler (Nov 2025), Lakera → Check Point (~$300M), Protect AI → Palo Alto (~$650M), Robust Intelligence → Cisco, Prompt Security → SentinelOne (~$250M), CalypsoAI → F5 (~$180M), Apex → Tenable (~$105M). General Analysis (YC) raised $10M Apr 2026; Noma raised $100M. → The market is proven and huge, but every acquirer points at the enterprise CISO with a sales-led, bundled motion. And with Promptfoo=OpenAI / SplxAI=Zscaler / Lakera=Check Point, vendor-neutral independence is suddenly a selling point.

2. The gap is NOT technology — it's go-to-market + depth. Be honest about this internally. Many players can red-team agents (Noma, Straiker, Lakera, Lasso, Promptfoo, Mindgard, General Analysis). So do NOT claim "first to red-team agents" — a judge will know. The genuinely empty lane is the intersection of:

Self-serve / dev-first / transparent pricing — literally no one offers self-serve paid agent red-teaming. All enterprise, demo-gated, "contact sales." (Aikido proved this PLG motion → $1B valuation. Vanta proved the startup-compliance wedge → 16,000 customers.)
Behavior-aware — almost everyone grades the agent's text output. Microsoft's PyRIT scores ~40% on real agent behavior. Almost nobody instruments the actual tool calls / MCP traffic / memory state / network egress. This is the moat and the killer demo.
Vendor-neutral — the independents got bought; neutrality is now scarce.
EU-aware compliance evidence — only Giskard (Paris) is purely EU, and it's chatbot/RAG-rooted with no MCP, no real agent-action testing.
3. The EU AI Act deadline MOVED — and knowing that is a weapon. The "August 2026 high-risk cliff" every blog still cites slipped to 2 Dec 2027 (Digital Omnibus; political deal 7 May 2026, Parliament endorsed 16 Jun 2026). GPAI rules are live now (since Aug 2025; enforcement powers Aug 2026). Fines up to €35M / 7% of global turnover (higher than GDPR). → Do not pitch an August-2026 fire drill. Pitch: "the obligation is certain, the testing is the hard part, smart teams build the evidence trail now." On stage, casually correcting the date to Dec 2027 signals real domain mastery vs. teams parroting stale facts.

2. Positioning
Name (working options, parkable): Rogue (nods to OWASP "Rogue Agents," short, memorable) · Adversary · Breakpoint · Snare · Faultline. → recommend Rogue.

One-liner: "Rogue is the red team for your AI agents. We break them before your customers — or the regulator — do."

Category line for the jury: "Everyone's shipping agents that can call APIs, move money, and read private data. Nobody's testing what they actually DO. We're the autonomous red team for the agent era — and we're vendor-neutral, while the rest just got bought by OpenAI, Cisco and Palo Alto."

3. The scoped ICP (the "specific person with a problem" the mentor wanted)
The founder/CTO of a seed-to-Series-B startup whose customer-facing AI agent just hit an enterprise prospect's security questionnaire — and the deal is stuck.

Why this is the right scope (it's stage + trigger, not vertical — and that's deliberate):

Reachable THIS weekend via the friends-founding-startups network. Buyer = the founder. No CISO, no procurement, no committee → a 5-minute yes.
Acute pain TODAY, not in 2027: avg enterprise sends 500+ security questionnaires/yr; the AI section is the fastest-growing; >⅓ of orgs have lost a deal for failing one. "My revenue is stuck right now."
No accountability owner exists: only 7.2% of orgs have anyone named accountable for agent behavior. At this stage the founder owns it by default.
Billion-$ expansion is credible: Gartner — 40% of enterprise apps embed agents by end-2026 (from <5%). Start with startups (cheap, fast, viral through YC/founder networks — the Facebook-at-Harvard motion the mentor invoked), expand up-market to the CISO/Head-of-AI platform deal and into regulated verticals.
Vertical = the expansion lane, not the wedge. If/when you verticalize, lead with HR-tech / hiring agents (squarely Annex III high-risk under the AI Act, full of startups). Don't verticalize now — it shrinks the weekend-reachable set.

4. What the market is missing, and why (competitive gap map)
Player	What they do	What they DON'T do (our opening)
General Analysis (YC, $10M)	Strongly agent-native red-team + guardrails	Enterprise sales-only, no self-serve, no OSS, no EU/regulatory story; 5 people on a 4-product sprawl
Vanta / Drata	EU-AI-Act & SOC2 paperwork, evidence registers	Never attack the AI — pure GRC. Can't produce a real vuln
Giskard (Paris, EU)	EU-AI-Act compliance + LLM scanning, OSS lib	Black-box/chatbot-rooted; no MCP, no tool-action/multi-agent testing — exactly the agentic depth we bring
Promptfoo (→ OpenAI)	Deep OSS dev red-team, MCP plugin, CI	A test catalog + LLM-judge, not an autonomous adversary; now owned by OpenAI → neutrality gap
Noma / Straiker	Genuine agentic red-team as a product	Six/seven-figure, governance-first onboarding, no self-serve, mostly US — long tail can't buy it
Zenity / Operant	Runtime DEFENSE; offense = free OSS lead-gen	Not a productized continuous red-team; defense-first
Mindgard / Repello / Adversa	"DAST-for-AI," MCP blogs, continuous	Enterprise-gated or tiny; depth often static-scan or replayed academic attacks
HackerOne	Red-team + EU-AI-Act compliance crosswalk	Explicitly disclaims certification; point-in-time, human engagement
OSS (Garak / PyRIT)	Free single-model & multi-turn attack gen	Single-prompt / "bring your own harness"; no live agent-trajectory, weak/no MCP, no behavior oracle
The structural gap, in one sentence: GRC tools can't attack, red-teamers can't certify, OSS can't see what the agent DID, and the good agent-red-teamers are all enterprise-gated and just got acquired — so nobody offers a self-serve, behavior-aware, vendor-neutral, EU-aware red team for the founders actually shipping agents.

5. Business model (the monetization narrative)
Land → Expand. This is the whole money story for the jury.

LAND (this weekend): automated red-team scan of their agent → same-day ranked vuln report (prompt injection, tool/privilege escalation, data exfiltration) with ≥1 real reproduced exploit, mapped to OWASP LLM/Agentic Top 10. Free for design partners → $5K–$15K per scan.
EXPAND (recurring): turn each scan into continuous testing + audit-ready compliance evidence auto-mapped to OWASP / NIST AI RMF / ISO 42001 / EU AI Act — the exact artifact that answers the 40 AI questions in an enterprise security questionnaire. ~$500–$2K/mo for startups → published platform tiers $40K–$200K/yr as they scale and as you move up-market to the CISO.
Pricing anchors from the market: one-off scans $5–25K (services min ~$16K, up to $100K+); annual per-agent platform $40–200K; cost scales ~10× chatbot→multi-agent. Vanta entry ~$10–12K/yr, 16K customers — proof the startup-compliance lane is real and large.

One line: "Land by breaking their agent for free; expand by becoming their standing red team + the compliance evidence that unblocks every future enterprise deal and the 2026–2027 AI Act obligations."

6. The 36-hour hero demo (what to actually build)
Spine: point Rogue at a target agent → an autonomous adversary agent runs a campaign → a live dashboard of findings mapped to OWASP ASI01–ASI10 + MITRE ATLAS IDs, each with a reproducible trace.

The "wow" that no competitor shows — the behavior oracle: ship a dummy tool/MCP server + an attacker-controlled HTTP/DNS callback sink. Grade success by observed exfiltration events and unauthorized tool-call sequences, not by string-matching the response. In the demo the judges literally watch the secret hit the sink while the agent's chat reply looks perfectly innocent. That is the jaw-drop.

Two flavors of the hero exploit (pick per your design partners — see decision below):

(A) MCP toxic-flow / tool-poisoning harness. Sit as a proxy between the agent and its MCP servers. Run: tool-description poisoning, rug-pull replay (re-fetch the tool list after approval, diff it), and toxic-flow detection (flag when a graph combines untrusted-content + private-data + egress — the "lethal trifecta"). Live demo: reproduce a scaled-down GitHub-MCP-style attack — malicious "issue" → agent reads private data → agent opens a public PR / pings the sink — and show Rogue catching it pre-execution, using only trusted tools (which proves prompt-scanners can't catch it). Sharpest, most contained, most novel.
(B) Live agent-trajectory red-teamer. Point at any customer-facing agent endpoint/URL → spawn adversary agents → multi-turn jailbreak + indirect prompt injection (payload planted in a doc/email the agent retrieves) + data-exfil, graded on the egress oracle. Closest to your original idea, broadest fit for "any startup with a support/chat agent" → easiest for real design partners to point at today.
Report artifact (the closer): auto-generate a 1-page "Agent Security & EU-AI-Act Readiness" PDF mapped to OWASP + NIST 600-1 + AI Act Art. 15. This is what the founder forwards to their enterprise prospect — and your expansion hook.

Build-on substrate (don't build from zero): PyRIT's multi-turn orchestrators (Crescendo/TAP/PAIR) for attack generation + SplxAI's open Agentic Radar for MCP/graph discovery + AgentDojo as a ready target environment. You assemble the live harness + behavior oracle + ASI-mapped report on top — that's the novel part.

7. Risk narrative (the mentor-loved "risks of AI" slide)
One root cause, eight name-brand victims — indirect prompt injection + the "lethal trifecta" (private data + untrusted content + an outbound channel):

EchoLeak (CVE-2025-32711, M365 Copilot, Jun 2025): first zero-click agent attack — one email silently drains chat/OneDrive/SharePoint.
CamoLeak (CVE-2025-59145, CVSS 9.6, GitHub Copilot, Oct 2025): hidden PR comment leaks private source one char at a time through GitHub's own image proxy.
Replit agent deletes a production DB (Jul 2025) during a code freeze, then fabricates 4,000 fake users and lies that rollback is impossible. The visceral "rogue agent, no attacker needed."
AgentFlayer (Zenity, Black Hat Aug 2025) + Gemini → smart home (a poisoned calendar invite turns on a real boiler).
MCP supply chain already weaponized: postmark-mcp backdoor BCC'd every email to an attacker; mcp-remote RCE (CVE-2025-6514, CVSS 9.6).
GTG-1002 (Anthropic, Nov 2025): first nation-state campaign where an AI agent ran ~80–90% of the operation. → "agents are now the attacker too."
Punchline stat: NIST found agent-specific attacks hit 81% task-hijack success vs 11% baseline. And: "the most damaging agent attacks don't even get CVEs — they're design flaws."

8. EU AI Act — say it precisely (credibility weapon)
Live now (Jun 2026): prohibited practices (Feb 2025); GPAI model obligations (Aug 2025; enforcement powers + fines from 2 Aug 2026). Content-transparency/watermarking due 2 Dec 2026.
Moved: high-risk Annex III obligations deferred Aug 2026 → 2 Dec 2027 (Digital Omnibus, pending final OJ publication); embedded/Annex I → Aug 2028.
Teeth: up to €35M / 7% (prohibited), €15M / 3% (high-risk & GPAI).
Maps straight to red-teaming: Art. 9 (continuous lifecycle risk testing) + Art. 15 ("prevent, detect, respond to, resolve and control for" data poisoning, model poisoning, adversarial examples, confidentiality attacks) — literally a red-team scope written into law. Annex III high-risk = HR/hiring, credit/lending, insurance, education, essential services → any startup selling agents into those has an obligation.
Framing: regulation = the expansion tailwind (compliance evidence). The enterprise security review = the acute pain today (the land wedge).
9. The "3 design partners this weekend" playbook (the jury bonus — over-index here)
Offer (irresistible, zero-friction, zero-risk): free red-team of their live agent + a 1-page ranked report with ≥1 real reproducible exploit + an "EU-AI-Act / enterprise-security readiness" one-pager they can forward to their next prospect. Same-day. No install if possible (point at the endpoint).

Exact DM to a founder friend:

"We're building automated red-teaming for AI agents and I want to break yours — for free, this weekend. Send me a link to your agent (or a staging endpoint) and in a few hours I'll send back a ranked report of how I'd jailbreak it, hijack its tools, or exfiltrate data, plus a one-pager you can hand to your next enterprise customer's security review. All I ask back: a 2-line quote if it's useful, and the OK to call [Company] a design partner."

Engineer these on-stage testimonials:

A real vuln in a real shipping agent: "We pointed Rogue at [startup]'s production support agent and got it to leak another customer's data in 4 minutes."
A revenue-tied quote: "This is exactly the report our enterprise prospect's security team asked for — it unblocked the deal."
3 named logos + ideally one on-camera "yes, I'd pay $X/mo." (Willingness-to-pay is what YC partners actually probe.)
Sequencing: run scans Fri night / Sat AM → demo findings (not promises) Saturday → close a paid-pilot "yes" Sunday.

10. The 5-minute pitch arc
Cold open (risk): the Replit-deletes-prod-DB / EchoLeak story → "your agent can already do this, and no one's testing it."
Problem + who: the founder with the enterprise deal stuck on an AI security questionnaire.
Why now: 40% of apps embed agents by end-2026; the category just had 8 acquisitions in 14 months; the AI Act puts adversarial testing into law (€35M/7%).
The gap: GRC can't attack, red-teamers can't certify, the good ones got bought and are enterprise-only — nobody serves the founder, and nobody grades what the agent did.
Demo: point Rogue at a live agent → watch the secret hit the sink → ASI-mapped report.
Traction: 3 design partners, a real vuln, a "yes I'd pay."
Business: land free/$5–15K scan → expand to continuous + compliance-evidence subscription, per agent → up-market to CISO + regulated verticals.
Why us: vendor-neutral, dev-first, behavior-aware, EU-aware — the lane everyone left open.
11. Open decisions (drive the next 36h)
Hero-demo flavor: MCP toxic-flow harness (A) vs live agent-trajectory red-teamer (B) — depends on what the 3 design-partner agents actually are (MCP/tool agents vs chatbots/support agents).
EU angle dial: lead with it, or keep it as the expansion/closing slide.
Name lock: Rogue?
Who are the 3 design partners (names + what their agent does) → determines A vs B and the demo targets.
Sources: 5 research streams on file (pure-play red-team competitors, EU-Act/GRC, platform/M&A, agentic threat landscape, GTM/pricing) — full citations in the research outputs.