// TalentScreen local server — runs the vulnerable, black-box HR screening agent behind
// the HTTP contract Rogue speaks:  POST /chat  {message, history}  ->  {reply}.
// Mirrors the clary proxy pattern. Zero deps (Node 18+). Run:
//   ANTHROPIC_API_KEY=... node server.js
// then point Rogue at  http://localhost:8788/chat
const http = require('http');
const { screen, MODEL, SYSTEM_PROMPT } = require('./agent');

function handleChat(body, res) {
  let parsed;
  try {
    parsed = JSON.parse(body || '{}');
  } catch (_) {
    parsed = {};
  }
  screen(parsed.message || '', parsed.history || [])
    .then((out) => {
      res.writeHead(200, {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      });
      res.end(JSON.stringify(out));
    })
    .catch((e) => {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: String((e && e.message) || e) }));
    });
}

const server = http.createServer((req, res) => {
  const path = req.url.split('?')[0];
  // Accept /chat and /api/chat so the same URL works locally and on Vercel.
  if (req.method === 'POST' && (path === '/chat' || path === '/api/chat')) {
    let body = '';
    req.on('data', (c) => (body += c));
    req.on('end', () => handleChat(body, res));
  } else if (req.method === 'GET' && path === '/health') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('ok');
  } else if (req.method === 'GET' && path === '/') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      agent: 'TalentScreen (AI CV-screening agent — EU AI Act Annex III, high-risk)',
      contract: 'POST /chat {message, history} -> {reply}',
    }));
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('not found');
  }
});

const PORT = process.env.PORT || 8788;
server.listen(PORT, () =>
  console.log(`talentscreen agent on :${PORT}  (model ${MODEL}, system prompt ${SYSTEM_PROMPT.length} chars)`));
