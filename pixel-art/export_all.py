"""Makes pixel-art/pixel-art.js from the pictures in b1a.py to b3c.py.
Run from the repo folder:  python3 pixel-art/export_all.py
The A-Z artifact on claude.ai is where the app is changed: pixel-art.js replaces its
"A-Z pixel pictures" section there. This repo never changes the artifact itself."""
import json, importlib, sys, os
import lib
for m in ['b1a','b1b','b1c','b2a','b2b','b3a','b3b','b3c']: importlib.import_module(m)
def pack(rows):
    rows = [r.rstrip('.') for r in rows]
    while rows and not rows[-1]: rows.pop()
    return '|'.join(rows)
items = ',\n'.join(f"  {json.dumps(k, ensure_ascii=False)}: '{pack(v)}'" for k, v in lib.ART.items())
pal = json.dumps(lib.PAL, ensure_ascii=False)
js = f"""/* ============================== A-Z pixel pictures ==============================
   Our own 16x16 pixel art, drawn for A-Z. Every emoji on screen is swapped for its pixel picture;
   the emoji stays as the picture's alt text, and in copied reports. '.' = empty; rows are 16 wide. */
const PXPAL = {pal};
const PXNO = {json.dumps(''.join(sorted(lib.NO_OUTLINE)))};
const PXART = {{
{items}
}};
const PXCELL = {{}}, PXC = {{}};
const pxKey = e => String(e).replace(/\\uFE0F/g, '');
function pxCells(e) {{
  const key = pxKey(e);
  if (key in PXCELL) return PXCELL[key];
  const a = PXART[key]; if (!a) return (PXCELL[key] = null);
  const W = 18, col = new Array(W * W).fill(null), fill = new Uint8Array(W * W);
  a.split('|').forEach((r, y) => {{ for (let x = 0; x < r.length; x++) {{ const ch = r[x]; if (ch === '.' || !PXPAL[ch]) continue; const i = (y + 1) * W + x + 1; col[i] = PXPAL[ch]; if (!PXNO.includes(ch)) fill[i] = 1; }} }});
  for (let y = 0; y < W; y++) for (let x = 0; x < W; x++) {{
    const i = y * W + x; if (col[i]) continue;
    if ((x > 0 && fill[i - 1]) || (x < W - 1 && fill[i + 1]) || (y > 0 && fill[i - W]) || (y < W - 1 && fill[i + W])) col[i] = PXPAL.k;
  }}
  const runs = [];
  for (let y = 0; y < W; y++) {{ let x = 0; while (x < W) {{ const c = col[y * W + x]; if (!c) {{ x++; continue; }} let x2 = x; while (x2 + 1 < W && col[y * W + x2 + 1] === c) x2++; runs.push([x, y, x2 - x + 1, c]); x = x2 + 1; }} }}
  return (PXCELL[key] = runs);
}}
function pxURL(e) {{
  const key = pxKey(e);
  if (key in PXC) return PXC[key];
  const runs = pxCells(key); if (!runs) return (PXC[key] = null);
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 18" shape-rendering="crispEdges">${{runs.map(([x, y, w, c]) => `<rect x="${{x}}" y="${{y}}" width="${{w}}" height="1" fill="${{c}}"/>`).join('')}}</svg>`;
  return (PXC[key] = 'data:image/svg+xml,' + encodeURIComponent(svg));
}}
/* Draw a pixel picture on a canvas, centred on (cx, cy), size = width in canvas units. Returns false if there is no picture. */
function pxDraw(ctx, e, cx, cy, size) {{
  const runs = pxCells(e); if (!runs) return false;
  const u = size / 18, x0 = cx - size / 2, y0 = cy - size / 2;
  ctx.save(); ctx.globalAlpha = 1;
  for (const [x, y, w, c] of runs) {{ ctx.fillStyle = c; ctx.fillRect(x0 + x * u, y0 + y * u, w * u + 0.04, u + 0.04); }}
  ctx.restore(); return true;
}}
let PXRE = null;
function pxRe() {{
  if (!PXRE) PXRE = new RegExp(Object.keys(PXART).sort((a, b) => b.length - a.length).map(k => k.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&') + '\\uFE0F?').join('|'), 'gu');
  PXRE.lastIndex = 0; return PXRE;
}}
function pxify(root) {{
  if (!root) return;
  const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {{ acceptNode: n => (n.parentNode && /^(SCRIPT|STYLE|TEXTAREA|OPTION|TITLE)$/.test(n.parentNode.nodeName) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT) }});
  const hits = [];
  for (let n = w.nextNode(); n; n = w.nextNode()) if (pxRe().test(n.nodeValue)) hits.push(n);
  for (const n of hits) {{
    const s = n.nodeValue, frag = document.createDocumentFragment(); let last = 0;
    s.replace(pxRe(), (m, i) => {{
      if (i > last) frag.append(s.slice(last, i));
      const u = pxURL(m);
      if (u) {{ const im = document.createElement('img'); im.className = 'px'; im.src = u; im.alt = m; im.draggable = false; frag.append(im); }} else frag.append(m);
      last = i + m.length; return m;
    }});
    if (last < s.length) frag.append(s.slice(last));
    n.parentNode.replaceChild(frag, n);
  }}
}}
"""
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pixel-art.js')
open(out, 'w', encoding='utf-8').write(js)
print(len(lib.ART), 'pictures,', len(js) // 1024, 'KB ->', os.path.relpath(out))
