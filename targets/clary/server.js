// Clary proxy — exposes the REAL Clarity assistant ("Clary") behind the HTTP
// contract Rogue's HTTPTarget speaks:  POST {message, history} -> {reply}.
// It uses Clary's actual system prompt + response schema + production model
// (gpt-4.1-mini), so a scan against this endpoint is a scan against the real
// shipped assistant. Zero deps (Node 18+ global fetch). Key is read from the
// Clarity app's .env and never logged.
const http = require('http');
const fs = require('fs');
const path = require('path');

const DIR = __dirname;
const SYSTEM_PROMPT = fs.readFileSync(path.join(DIR, 'clary_prompt.txt'), 'utf8');
const SCHEMA = JSON.parse(fs.readFileSync(path.join(DIR, 'clary_schema.json'), 'utf8'));
const MODEL = process.env.CLARY_MODEL || 'gpt-4.1-mini';   // production model

function loadKey() {
  if (process.env.OPENAI_API_KEY) return process.env.OPENAI_API_KEY;
  const txt = fs.readFileSync(
    '/Users/federica/Documents/code/clarity/clarity-assistant/.env', 'utf8');
  const m = txt.match(/^OPENAI_API_KEY=(.+)$/m);
  if (!m) throw new Error('OPENAI_API_KEY not found in Clarity .env');
  return m[1].trim().replace(/^["']|["']$/g, '');
}
const OPENAI_API_KEY = loadKey();

async function clary(message, history) {
  const messages = [{ role: 'system', content: SYSTEM_PROMPT }];
  for (const h of (history || [])) {
    messages.push({ role: h.role === 'assistant' ? 'assistant' : 'user',
                    content: h.content ?? h.text ?? '' });
  }
  messages.push({ role: 'user', content: message });

  const resp = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: { Authorization: `Bearer ${OPENAI_API_KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      model: MODEL,
      temperature: 0.4,
      max_tokens: 8000,
      messages,
      response_format: {
        type: 'json_schema',
        json_schema: { name: 'clary_response', strict: true, schema: SCHEMA },
      },
    }),
  });
  if (!resp.ok) throw new Error(`openai ${resp.status}: ${(await resp.text()).slice(0, 300)}`);
  const data = await resp.json();
  const content = data.choices?.[0]?.message?.content || '{}';
  let parsed = {};
  try { parsed = JSON.parse(content); } catch (_) {}
  return parsed.chatReply || parsed.summary || '(no reply)';
}

const server = http.createServer((req, res) => {
  if (req.method === 'POST' && req.url === '/chat') {
    let body = '';
    req.on('data', c => (body += c));
    req.on('end', async () => {
      try {
        const { message, history } = JSON.parse(body || '{}');
        const reply = await clary(message || '', history || []);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ reply }));
      } catch (e) {
        res.writeHead(500, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: String(e && e.message || e) }));
      }
    });
  } else if (req.method === 'GET' && req.url === '/health') {
    res.writeHead(200); res.end('ok');
  } else {
    res.writeHead(404); res.end('not found');
  }
});

const PORT = process.env.PORT || 8799;
server.listen(PORT, () =>
  console.log(`clary proxy on :${PORT}  (model ${MODEL}, system prompt ${SYSTEM_PROMPT.length} chars)`));
