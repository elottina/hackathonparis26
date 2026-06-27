// Faithfully extract Clary's real system prompt + response schema from the
// Clarity app source, so the proxy red-teams the REAL assistant (same prompt,
// same schema, same model). Read-only against the app; writes two artifacts.
const fs = require('fs');
const SRC = '/Users/federica/Documents/code/clarity/clarity-assistant/lib/clary/process-brain-dump.ts';
const OUT = __dirname;
const src = fs.readFileSync(SRC, 'utf8');

function sliceTemplate(afterIdx) {
  const open = src.indexOf('`', afterIdx);
  const close = src.indexOf('`', open + 1);
  return src.slice(open + 1, close);
}
function sliceObj(marker) {
  const i = src.indexOf(marker);
  const s = src.indexOf('{', i);
  let d = 0, j = s;
  for (; j < src.length; j++) {
    const c = src[j];
    if (c === '{') d++;
    else if (c === '}') { d--; if (d === 0) { j++; break; } }
  }
  return src.slice(s, j);
}

// ── system prompt (resolve the single ${languageInstructions} interpolation) ──
const lang = sliceTemplate(src.indexOf('const languageInstructions = `'));
let prompt = sliceTemplate(src.indexOf('return `', src.indexOf('function buildSystemPrompt')));
prompt = prompt.replace('${languageInstructions}', lang);
if (prompt.includes('${')) throw new Error('unresolved interpolation remains in prompt');
fs.writeFileSync(OUT + '/clary_prompt.txt', prompt);

// ── response schema (inline RECURRENCE_SCHEMA, drop the `as const`) ──
const recText = sliceObj('const RECURRENCE_SCHEMA =');
const claText = sliceObj('const CLARY_RESPONSE_SCHEMA =');
const RECURRENCE_SCHEMA = eval('(' + recText + ')');           // referenced by the schema below
const CLARY_RESPONSE_SCHEMA = eval('(' + claText + ')');
fs.writeFileSync(OUT + '/clary_schema.json', JSON.stringify(CLARY_RESPONSE_SCHEMA, null, 2));

console.log('prompt chars:', prompt.length, '| lines:', prompt.split('\n').length);
console.log('schema top-level props:', Object.keys(CLARY_RESPONSE_SCHEMA.properties).join(', '));
console.log('recurrence inlined ok:', !!CLARY_RESPONSE_SCHEMA.properties.reminders.items.properties.recurrence.properties.freq);
