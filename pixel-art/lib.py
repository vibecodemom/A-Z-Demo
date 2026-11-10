# Shared palette and helpers for the A-Z pixel pictures.
PAL = {
 'k':'#1A1C2C','w':'#FFFFFF','l':'#C2C3C7','g':'#7A7F8C','D':'#454A57','r':'#FF3B4E','R':'#B8213A','o':'#FFA300',
 'O':'#D9731F','y':'#FFE14D','h':'#E0A800','G':'#3DCC5A','L':'#A6F07A','d':'#1E8A4A','b':'#3BA7F5','B':'#1F64C8',
 'n':'#26355E','c':'#BDEBFF','T':'#2EC4B6','p':'#FF8FB8','q':'#E0609A','s':'#FFD2B0','t':'#E8A86A','m':'#9A5A33',
 'M':'#5E3420','e':'#F5E6C8','v':'#9B5DE5','P':'#5B2A86',
 '~':'#3BA7F5','*':'#FFE14D','^':'#FFFFFF','%':'#BDEBFF','!':'#FF3B4E','&':'#7A7F8C'   # never outlined
}
NO_OUTLINE = set('~*^%!&')
ART = {}

def norm(rows):
    rows = [r + r[::-1] if len(r) == 8 else r for r in rows]
    rows = [r.ljust(16, '.') for r in rows] + ['.' * 16] * (16 - len(rows))
    assert len(rows) == 16 and all(len(r) == 16 for r in rows), rows
    return rows

def center(rows):
    pts = [(x, y) for y, r in enumerate(rows) for x, ch in enumerate(r) if ch != '.']
    if not pts: return rows
    x0 = min(p[0] for p in pts); x1 = max(p[0] for p in pts); y0 = min(p[1] for p in pts); y1 = max(p[1] for p in pts)
    dx = (16 - (x1 - x0 + 1)) // 2 - x0; dy = (16 - (y1 - y0 + 1) + 1) // 2 - y0
    g = [['.'] * 16 for _ in range(16)]
    for (x, y) in pts: g[y + dy][x + dx] = rows[y][x]
    return [''.join(r) for r in g]

def add(e, rows, ctr=True):
    rows = norm(rows)
    for r in rows:
        for ch in r: assert ch == '.' or ch in PAL, (e, ch)
    ART[e.replace('️', '')] = center(rows) if ctr else rows

def blank(): return [['.'] * 16 for _ in range(16)]
def rows_of(g): return [''.join(r) for r in g]

def disc(r_out, fill, cx=7.5, cy=7.5, g=None, rim=None):
    g = g or blank()
    for y in range(16):
        for x in range(16):
            d = ((x - cx) ** 2 + (y - cy) ** 2) ** .5
            if d <= r_out: g[y][x] = rim if (rim and d > r_out - 1.1) else fill
    return g

def put(g, pts, c):
    for (x, y) in pts:
        if 0 <= x < 16 and 0 <= y < 16: g[y][x] = c
    return g

def over(base, top):
    base = norm(base) if isinstance(base[0], str) else rows_of(base)
    top = norm(top)
    return [''.join(t if t != '.' else b for b, t in zip(br, tr)) for br, tr in zip(base, top)]

# yellow smiley base
def face(fill='y'):
    g = disc(7.1, fill)
    return rows_of(g)

def line(g, x0, y0, x1, y1, c):
    dx = abs(x1 - x0); dy = -abs(y1 - y0); sx = 1 if x0 < x1 else -1; sy = 1 if y0 < y1 else -1; err = dx + dy
    while True:
        if 0 <= x0 < 16 and 0 <= y0 < 16: g[y0][x0] = c
        if x0 == x1 and y0 == y1: break
        e2 = 2 * err
        if e2 >= dy: err += dy; x0 += sx
        if e2 <= dx: err += dx; y0 += sy
    return g

def ring(g, cx, cy, r_in, r_out, c):
    for y in range(16):
        for x in range(16):
            d = ((x - cx) ** 2 + (y - cy) ** 2) ** .5
            if r_in < d <= r_out: g[y][x] = c
    return g

def stamp(g, rows, x0, y0):
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch != '.' and 0 <= x0 + x < 16 and 0 <= y0 + y < 16: g[y0 + y][x0 + x] = ch
    return g
