// Vercel serverless entrypoint:  POST /api/chat {message, history} -> {reply}
// Set ANTHROPIC_API_KEY in the Vercel project env. Shares the agent brain in ../agent.js.
const { screen } = require('../agent');

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  if (req.method === 'GET') {
    res.status(200).json({ agent: 'TalentScreen', contract: 'POST {message,history} -> {reply}' });
    return;
  }
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'POST only' });
    return;
  }
  try {
    let body = req.body;
    if (typeof body === 'string') {
      try { body = JSON.parse(body || '{}'); } catch (_) { body = {}; }
    }
    if (!body || typeof body !== 'object') body = {};
    const out = await screen(body.message || '', body.history || []);
    res.status(200).json(out);
  } catch (e) {
    res.status(500).json({ error: String((e && e.message) || e) });
  }
};
