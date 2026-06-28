# Rogue — Deployment Runbook (localhost → live & public)

## TL;DR — what "fully live" means
Rogue is a dashboard SPA (`dashboard/index.html`) + a Python backend (`engine/server.py`).
**`server.py` serves BOTH the dashboard at `/` AND the `/api/*` endpoints** (static `do_GET`,
`POST /api/scan`, `GET /api/stream/<id>` SSE, `GET /api/history`, `GET /api/scan/<id>`).
So **ONE always-on host running `server.py` = the entire live tool** — same-origin, no CORS,
no second deploy.

The backend **cannot run on Vercel**: it's a persistent process with background threads,
asyncio, multi-minute scans, and a long-lived `while True` SSE stream. Vercel serverless is
stateless + short-timeout → incompatible. It needs an **always-on host** (Render / Railway /
Fly.io). This runbook uses **Render** — a Blueprint (`render.yaml`) already exists at repo root.

> The dashboard routes all 4 backend calls through `const API = window.ROGUE_API || ''`
> (default = same-origin). When the Render service serves the dashboard itself, everything
> works with **zero config / no CORS**. You only set `window.ROGUE_API` if the dashboard lives
> on a **different origin** than the backend (e.g. dashboard on Vercel + backend on Render);
> the server already sends CORS headers (`do_OPTIONS` + `Access-Control-Allow-Origin: *`).

---

## Step 1 — Deploy the backend+tool to Render (Blueprint)
`render.yaml` (repo root) defines the service: `rootDir: engine`, build
`pip install -r requirements.txt`, start `python server.py`, `healthCheckPath: /`,
`PYTHON_VERSION 3.12.4`. `server.py` binds `0.0.0.0:$PORT` (Render injects `$PORT`; falls back
to `ROGUE_PORT`, then `8799` locally) — so no port config needed.

1. **[USER-ONLY]** Create a Render account and connect GitHub.
   *(An AI assistant is prohibited from creating accounts.)*
2. Render → **New → Blueprint** → select this repo. Render reads `render.yaml` automatically.
3. Set the env vars (both are `sync: false`, i.e. entered in the dashboard, never committed):
   - `ANTHROPIC_API_KEY` — **[USER-ONLY]** paste the secret in the Render dashboard.
     *(An AI assistant is prohibited from entering secrets.)*
   - `TALENTSCREEN_URL` = `https://talentscreen-one.vercel.app/api/chat`
     (defaults to `http://localhost:8788/chat`, which a remote host can't reach — set this so
     the `hr` preset works from the cloud).
   - `PYTHON_VERSION` = `3.12.4` (already pinned in the Blueprint).
4. Deploy. When the health check on `/` passes, open the service URL — the dashboard loads and
   `/api/*` is live on the same origin.

---

## Step 2 — Finish TalentScreen so the `hr` preset works from the cloud
The target agent **TalentScreen is already deployed** to Vercel:
- App: `https://talentscreen-one.vercel.app`
- Endpoint: `https://talentscreen-one.vercel.app/api/chat`

It still needs its own key. Without it, `/api/chat` returns
`{"error":"ANTHROPIC_API_KEY is not set"}`.

1. **[USER-ONLY]** Vercel → talentscreen project → **Settings → Environment Variables →
   Production** → add `ANTHROPIC_API_KEY`. *(Assistant cannot enter secrets.)*
2. **Redeploy** so the key takes effect — either:
   ```bash
   cd targets/talentscreen && vercel --prod --yes
   ```
   *(the assistant CAN run this deploy command)*, or use the Vercel dashboard **"Redeploy"**.
3. Verify it's keyed:
   ```bash
   curl -s https://talentscreen-one.vercel.app/api/chat \
     -H 'Content-Type: application/json' -d '{"message":"hi"}'
   ```
   Should NOT return the `ANTHROPIC_API_KEY is not set` error.

---

## Step 3 — (optional) Deploy Cowork and wire its URL
**Cowork** (the Rowads agent) is the user's **own separate product/repo** (not in this repo).
Until it's public, the `cowork` preset only works against a **locally-running** Cowork on
`:8790`.

1. **[USER-ONLY]** The user deploys Cowork from its own repo → gets a public URL.
2. Point the `cowork` preset / paste-a-URL flow at that public URL (or run Cowork locally on
   `:8790` for the demo). No Render redeploy needed if you paste the URL in the dashboard.

---

## Verify — open the Render URL and check the presets
| Preset | Needs | Behaves on the hosted backend |
|---|---|---|
| `demo` | nothing (offline, no key, no target) | **Works anywhere — bulletproof.** |
| `hr` | TalentScreen public + `TALENTSCREEN_URL` set | Scans the live TalentScreen agent. |
| paste-any-URL | any **public** agent URL | Works for any reachable public agent. |
| `cowork` | Cowork reachable (local `:8790` or public URL) | Works once Cowork is up. |

Open the Render service URL → dashboard loads → run `demo` first (always green) → then `hr`.

---

## Risks & key rotation
- **Cold start.** Render free tier sleeps after ~15 min idle and cold-starts in ~50s. For a
  **live on-stage demo**, 50s = dead air → **warm the URL right before** you present, or
  upgrade to **Render Starter ($7/mo)** to stay always-warm.
- **No auth + open CORS.** The hosted backend sends `Access-Control-Allow-Origin: *` and has
  **no auth** → anyone with the URL can run scans and spend your Anthropic credits. Keep it up
  **only during the judging window**, watch usage, and rotate the key afterward.
- **Rotate the key.** The `ANTHROPIC_API_KEY` was pasted into a chat earlier — **it must be
  rotated after the hackathon regardless** (Anthropic Console → API Keys → revoke + regenerate).
- **For the screen-recorded video, use localhost.** Zero cold-start, zero latency, fully
  reliable. Deploying is for a public "try-it" link for judges — not for the recording.
