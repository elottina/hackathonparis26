# Rogue — Outreach Kit

Cold/warm messages for landing HR-screening design partners.

**Landing:** https://rogue-gamma.vercel.app  
**Reply-to:** federica@rowads.studio

---

## 1. Funnel

Two URLs matter:

1. **Rogue landing URL** — what we send prospects.
2. **Prospect agent endpoint** — the staging/demo URL Rogue scans.

Best-case scan input:

```text
POST /chat { "message": "...", "history": [...] }
→ { "reply": "...", "tool_calls": [...] }
```

If their shape differs, we write a small shim. If they only have a widget, we can still test text-level
behavior. For behavior-oracle proof, ask for one planted canary, tool trace, callback sink, or returned
`tool_calls`.

---

## 2. Qualify Before Sending

Send only if the person/company likely has:

- HR-tech, ATS, recruiting automation, candidate ranking, or CV-screening AI.
- Candidate PII or candidate decisioning.
- European, enterprise, or regulated customers.
- A founder/CTO/product lead reachable directly.
- A staging/demo surface we can test quickly.

Use generic AI-agent prospects only as backup proof, not as the main wedge.

---

## 3. Short DM

> Hey {first_name} — quick founder-to-founder note. I’m building **Rogue**, an autonomous red-team
> for AI HR / CV-screening agents.  
>  
> I’d like to run a free exposure scan on {product}: candidate PII leaks, hidden web lookup, proxy
> bias, missing human oversight, and prompt injection. The output is a blurred GDPR / EU AI Act
> exposure report you can keep.  
>  
> If it’s useful, I’ll ask for a short quote or a paid deep scan. Can you send a staging endpoint or
> demo login?

---

## 4. Email

**Subject options**

- `free exposure scan for {product}'s screening agent`
- `{first_name} — can Rogue catch candidate-data leakage in {product}?`
- `red-team of {product}'s CV-screening agent`

**Body**

> Hi {first_name},  
>  
> I’m building **Rogue**, an autonomous red-team for AI agents, focused on HR / CV-screening systems.  
>  
> We test what the agent **did**, not only what it said: prompt injection, candidate PII leakage,
> hidden external lookup, proxy discrimination, missing human oversight, and unsafe tool calls. Each
> finding is mapped to GDPR / EU AI Act risk.  
>  
> I’d like to run a free exposure scan on {product}. You get a blurred report with finding count,
> severity, and mapped obligations. If it is useful, we can do a paid deep scan with full trace and
> remediation.  
>  
> {personal_hook}  
>  
> Worth sending a staging endpoint or demo login?  
> {your_name}

---

## 5. Follow-Up

> {first_name} — quick proof bump. Rogue catches the case text-only tests miss: a screening agent
> gives a clean candidate recommendation while candidate data leaves via a tool call / external
> lookup.  
>  
> Happy to run the free exposure scan on {product}; you keep the report either way.

---

## 6. Personalisation Tokens

| Token | Meaning | Example |
|---|---|---|
| `{first_name}` | First name | Maya |
| `{company}` | Company | MeetPia |
| `{product}` | Product / agent name | MeetPia screening agent |
| `{personal_hook}` | One true detail | "Saw you process thousands of CVs/day." |
| `{your_name}` | Sender | Federica |

Research routine:

1. Does the product screen/rank/recommend candidates?
2. Does it mention Europe, enterprise, compliance, GDPR, or AI Act?
3. Is there a demo, widget, API, or public workflow?
4. Who is the founder/CTO/product owner?

---

## 7. Tracker Fields

| Name | Company | Product | HR use case | Endpoint? | Canary? | Status | WTP |
|---|---|---|---|---|---|---|---|
| | | | CV screen / ATS / recruiter copilot | y/n | y/n | new → sent → endpoint → scanned → quote | € |

Status flow:

`new → sent → replied → endpoint → scanned → report sent → readout → quote → WTP → paid scan`
