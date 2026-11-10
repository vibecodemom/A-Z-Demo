# A-Z pixel icons: our own 16x16 art. '.' = empty. Rows of 8 chars are mirrored to 16.
PAL = {
 'k':'#1A1C2C','w':'#FFFFFF','l':'#C2C3C7','g':'#7A7F8C','r':'#FF3B4E','R':'#B8213A','o':'#FFA300','y':'#FFE14D',
 'G':'#3DCC5A','d':'#1E8A4A','b':'#3BA7F5','B':'#1F64C8','n':'#26355E','p':'#FF8FB8','s':'#FFD2B0','m':'#9A5A33',
 'M':'#5E3420','t':'#E8A86A','v':'#8E44AD','c':'#BDEBFF',
 '~':'#3BA7F5','*':'#FFE14D','^':'#FFFFFF'   # these never get an outline (water drops, sparkles, shine)
}
NO_OUTLINE = set('~*^')

def mirror(rows):
    return [r + r[::-1] if len(r) == 8 else r for r in rows]

def circle(r_out, fill, rim=None, inner=None, hi=True):
    g = [['.'] * 16 for _ in range(16)]
    for y in range(16):
        for x in range(16):
            d = ((x - 7.5) ** 2 + (y - 7.5) ** 2) ** .5
            if d <= r_out:
                c = fill
                if rim and d > r_out - 1.2: c = rim
                if inner and abs(d - (r_out - 3)) < .5: c = inner
                g[y][x] = c
    if hi:
        for (x, y) in [(4, 4), (5, 3), (4, 5)]:
            if g[y][x] == fill: g[y][x] = 'w'
    return [''.join(r) for r in g]

def moon():
    g = [['.'] * 16 for _ in range(16)]
    for y in range(16):
        for x in range(16):
            if ((x - 7.5) ** 2 + (y - 7.5) ** 2) ** .5 <= 6.8 and ((x - 11) ** 2 + (y - 5) ** 2) ** .5 > 5.6:
                g[y][x] = 'y'
    g[11][5] = 'o'; g[12][7] = 'o'; g[10][4] = 'o'
    return [''.join(r) for r in g]

def pencil():
    g = [['.'] * 16 for _ in range(16)]
    for r in range(1, 15):
        c0 = 14 - r
        cols = [c0 - 1, c0, c0 + 1]
        col = 'p' if r <= 2 else 'l' if r == 3 else 'y' if r <= 10 else 's' if r <= 12 else 'k'
        for i, x in enumerate(cols):
            if 0 <= x < 16:
                c = col
                if col == 'y' and i == 2: c = 'o'
                if r >= 13 and i != 1: c = 's' if r == 13 else '.'
                g[r][x] = c
    return [''.join(r) for r in g]

ART = {
 '⏰': [
  "................",".rr..........rr.","rrrr..kkkk..rrrr","rrr.rrrrrrrr.rrr","...rrwwwwwwrr...","..rwwwwkwwwwwr..",
  "..rwwwwkwwwwwr..",".rwwwwwkwwwwwwr.",".rwwwwwkkkkwwwr.",".rwwwwwwwwwwwwr.","..rwwwwwwwwwwr..","..rwwwwwwwwwwr..",
  "...rrwwwwwwrr...","....rrrrrrrr....","...rr......rr...","................"],
 '🪥': [
  "................","................","................",".........cwwc...","........cwwwwwc.","........wlwlwlw.",
  "........wlwlwlw.","........wlwlwlw.",".bbbbbbbbbbbbbb.","bwbbbbbbbbbbbbbb",".BBBBBBBBBBBBBB.","................",
  "................","................","................","................"],
 '🚿': [
  ".......ll.......",".......ll.......","......llll......","....llllllll....","...llwllllllg...","..gggggggggggg..",
  "................","...~...~...~....","...~...~...~....",".....~...~...~..",".....~...~...~..","...~...~...~....",
  "...~...~...~....",".....~...~...~..",".....~...~...~..","................"],
 '🥣': [
  "...........ll...","..........ll....",".........ll.....","...oy.yoll.oy...","..yoyoyoyoyyoy..",".wwwwwwwwwwwwww.",
  "bbbbbbbbbbbbbbbn","bwbbbbbbbbbbbbbn",".bbbbbbbbbbbbbn.",".bbbbbbbbbbbbbn.","..bbbbbbbbbbbn..","...bbbbbbbbbn...",
  ".....nnnnnn.....","................","................","................"],
 '👕': mirror([
  "........","....bbb.","..bbbbbn",".bbbbbbb","bbbbbbbb","bbbbbbbb","BBB.bbbb","....bbbb",
  "....yyyy","....bbbb","....bbbb","....bbbb","....bbbb","....BBBB","........","........"]),
 '🎒': mirror([
  "......gg",".....g..","...rrrrr","..rrrrrr","..rwrrrr","..rRRRRR","..rrrrrr","..rrrrry",
  "..rrrrrr","..rroooo","..rroooo","..rroooo","..rrrrrr","...rrrrr","........","........"]),
 '✏️': pencil(),
 '🛏️': [
  "................","................","mm..............","mm..............","mm..............","mmwww.........mm",
  "mmwwwbbbbbbbbbmm","mmbbbcbbbcbbbbmm","mmBBBBBBBBBBBBmm","mmmmmmmmmmmmmmmm","mM............Mm","mM............Mm",
  "................","................","................","................"],
 '⭐': mirror([
  ".......y",".......y","......yy","......yy",".....ywy","yyyyyyyy",".yyyyyyy","..yyyyyy",
  "...yyyyy","....yyyy","....yyyy","...yyyyy","...yyyy.","..yyy...","..yy....","........"]),
 '🪙': circle(7.2, 'y', rim='o', inner='o'),
 '❤️': mirror([
  "........","..rrrr..",".rrrrrr.","rrwwrrrr","rrwrrrrr","rrrrrrrr","rrrrrrrr",".rrrrrrr",
  "..rrrrrr","...rrrrr","....rrrr",".....rrr","......rr",".......r","........","........"]),
 '🍎': [
  "................","........m.GG....","........mGGG....","...rrrr.mrrrr...","..rrrrrrrrrrrr..",".rwwrrrrrrrrrrR.",
  ".rwrrrrrrrrrrrR.",".rrrrrrrrrrrrrR.",".rrrrrrrrrrrrrR.",".rrrrrrrrrrrrrR.","..rrrrrrrrrrrR..","..rrrrrrrrrrRR..",
  "...rrrrrrrrRR...","....rrr..rRR....","................","................"],
 '🦊': mirror([
  "........",".o......",".oo.....",".opo....",".oppoooo","oooooooo","ooookooo","ooookooo",
  "wooooooo",".wwwoooo","..wwwwww","...wwwww","....wwwk",".....www","........","........"]),
 '🐶': mirror([
  "........","....tttt","..tttttt","MMtttttt","MMtttttt","MMMtkttt","MMMtkttt","MMtttsss",
  ".Mttssss","..tssssk","..tsssks","...ssssp","....ssss","........","........","........"]),
 '🚀': mirror([
  ".......r","......rr",".....rrr",".....www",".....wwb",".....wbc",".....wbb",".....www",
  "....rwww","...rrwww","...rrwww","...r.lll","......oy",".......o","........","........"]),
 '🌙': moon(),
}

def check():
    for k, rows in ART.items():
        assert len(rows) == 16, (k, len(rows))
        for r in rows:
            assert len(r) == 16, (k, r, len(r))
            for ch in r:
                assert ch == '.' or ch in PAL, (k, ch)
check()
