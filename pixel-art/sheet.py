import sys, importlib, unicodedata
from PIL import Image, ImageDraw, ImageFont
import lib
def hexrgb(h): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def icon(rows):
    W = 18; im = Image.new('RGBA', (W, W), (0, 0, 0, 0)); px = im.load(); filled = set()
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch == '.': continue
            px[x + 1, y + 1] = hexrgb(lib.PAL[ch]) + (255,)
            if ch not in lib.NO_OUTLINE: filled.add((x + 1, y + 1))
    o = hexrgb(lib.PAL['k'])
    for y in range(W):
        for x in range(W):
            if px[x, y][3]: continue
            if any((x + dx, y + dy) in filled for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))): px[x, y] = o + (255,)
    return im
def nm(e):
    try: return unicodedata.name(e[0]).lower().replace('face', '').replace('with ', '')[:16]
    except Exception: return e
if __name__ == '__main__':
    mods = sys.argv[2].split(',')
    before = set(lib.ART)
    for m in mods[:-1]: importlib.import_module(m)
    before = set(lib.ART)
    importlib.import_module(mods[-1])
    keys = [k for k in lib.ART if k not in before] if len(sys.argv) < 4 else list(lib.ART)
    sc = 4; cell = 18 * sc; cols = 10; padx = 18; lab = 18
    f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
    rows = (len(keys) + cols - 1) // cols
    W = cols * (cell + padx) + padx; H = rows * (cell + lab + 10) + 14
    sh = Image.new('RGB', (W, H), (247, 248, 252)); d = ImageDraw.Draw(sh)
    for i, k in enumerate(keys):
        cx = padx + (i % cols) * (cell + padx); cy = 10 + (i // cols) * (cell + lab + 10)
        im = icon(lib.ART[k]).resize((cell, cell), Image.NEAREST); sh.paste(im, (cx, cy), im)
        t = f"{i}:{nm(k)}"; tw = d.textlength(t, font=f); d.text((cx + (cell - tw) / 2, cy + cell + 2), t, fill=(70, 80, 100), font=f)
    sh.save(sys.argv[1]); print(len(keys), 'drawn')
