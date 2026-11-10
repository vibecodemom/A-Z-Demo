import json, art
def js():
    pal = json.dumps(art.PAL, ensure_ascii=False)
    items = ',\n  '.join(f"{json.dumps(k.replace(chr(0xFE0F), ''), ensure_ascii=False)}: '{'|'.join(v)}'" for k, v in art.ART.items())
    return f"""/* ============================== A-Z pixel pictures (our own 16x16 art) ============================== */
const PXPAL = {pal};
const PXNO = '{''.join(sorted(art.NO_OUTLINE))}';
const PXART = {{
  {items}
}};
const PXC = {{}};
function pxURL(e) {{
  const key = String(e).replace(/\\uFE0F/g, '');
  if (key in PXC) return PXC[key];
  const a = PXART[key]; if (!a) return (PXC[key] = null);
  try {{
    const rows = a.split('|'), W = 18, cv = document.createElement('canvas'); cv.width = cv.height = W;
    const ctx = cv.getContext('2d'), img = ctx.createImageData(W, W), D = img.data, fill = new Uint8Array(W * W);
    const rgb = h => [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)];
    rows.forEach((r, y) => {{ for (let x = 0; x < r.length; x++) {{ const ch = r[x]; if (ch === '.' || !PXPAL[ch]) continue; const i = (y + 1) * W + x + 1, c = rgb(PXPAL[ch]); D.set([c[0], c[1], c[2], 255], i * 4); if (!PXNO.includes(ch)) fill[i] = 1; }} }});
    const o = rgb(PXPAL.k);
    for (let y = 0; y < W; y++) for (let x = 0; x < W; x++) {{ const i = y * W + x; if (D[i * 4 + 3]) continue; if ((x > 0 && fill[i - 1]) || (x < W - 1 && fill[i + 1]) || (y > 0 && fill[i - W]) || (y < W - 1 && fill[i + W])) D.set([o[0], o[1], o[2], 255], i * 4); }}
    ctx.putImageData(img, 0, 0);
    return (PXC[key] = cv.toDataURL());
  }} catch (err) {{ return (PXC[key] = null); }}
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
if __name__ == '__main__':
    import sys; open(sys.argv[1], 'w', encoding='utf-8').write(js())
