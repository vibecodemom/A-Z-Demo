import sys
from PIL import Image, ImageDraw, ImageFont
import art

def hexrgb(h): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
LCD = [(26, 48, 26), (74, 104, 46), (139, 172, 15), (205, 222, 150)]

def lum(c): return (0.3 * c[0] + 0.59 * c[1] + 0.11 * c[2]) / 255

def icon(rows, style):
    W = 18
    im = Image.new('RGBA', (W, W), (0, 0, 0, 0))
    px = im.load()
    filled = set()
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch == '.': continue
            c = hexrgb(art.PAL[ch])
            if style == 'retro':
                L = lum(c); c = LCD[0] if ch == 'k' or L < .3 else LCD[1] if L < .55 else LCD[2] if L < .8 else LCD[3]
            px[x + 1, y + 1] = c + (255,)
            if ch not in art.NO_OUTLINE: filled.add((x + 1, y + 1))
    if style in ('bright', 'retro'):
        out = LCD[0] if style == 'retro' else hexrgb(art.PAL['k'])
        for y in range(W):
            for x in range(W):
                if px[x, y][3]: continue
                if any((x + dx, y + dy) in filled for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    px[x, y] = out + (255,)
    return im

NAMES = {'⏰': 'Wake up', '🪥': 'Brush teeth', '🚿': 'Shower', '🥣': 'Breakfast', '👕': 'Get dressed', '🎒': 'Backpack',
         '✏️': 'Homework', '🛏️': 'Bed', '⭐': 'Star', '🪙': 'Coin', '❤️': 'Heart', '🍎': 'Apple', '🦊': 'Fox',
         '🐶': 'Puppy', '🚀': 'Rocket', '🌙': 'Moon'}

def sheet(path, styles, scale=4):
    keys = list(art.ART)
    cols = 8; cell = 18 * scale; padx = 26; lab = 34
    try:
        f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
        fs = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
    except Exception:
        f = fs = ImageFont.load_default()
    titles = {'bright': 'A.  Bright, with outline', 'soft': 'B.  Soft, no outline', 'retro': 'C.  Old-school handheld (like the pixel pet)'}
    rows_per = (len(keys) + cols - 1) // cols
    block = 30 + rows_per * (cell + lab) + 14
    W = cols * (cell + padx) + padx
    H = len(styles) * block + 10
    sh = Image.new('RGB', (W, H), (247, 248, 252))
    d = ImageDraw.Draw(sh)
    for si, st in enumerate(styles):
        y0 = si * block + 10
        if st == 'retro': d.rounded_rectangle([8, y0 - 4, W - 8, y0 + block - 16], 14, fill=(214, 228, 170))
        d.text((padx, y0), titles[st], fill=(26, 34, 51), font=f)
        for i, k in enumerate(keys):
            cx = padx + (i % cols) * (cell + padx); cy = y0 + 30 + (i // cols) * (cell + lab)
            im = icon(art.ART[k], st).resize((cell, cell), Image.NEAREST)
            sh.paste(im, (cx, cy), im)
            t = NAMES.get(k, ''); tw = d.textlength(t, font=fs)
            d.text((cx + (cell - tw) / 2, cy + cell + 4), t, fill=(88, 98, 118), font=fs)
    sh.save(path)

if __name__ == '__main__':
    sheet(sys.argv[1], sys.argv[2].split(','), int(sys.argv[3]) if len(sys.argv) > 3 else 4)
