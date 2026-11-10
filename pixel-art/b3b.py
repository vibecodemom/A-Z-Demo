from lib import *
import math
add('🏝', ["....GGG.GGG.....","..GGGGGGGGGGG...",".GG...GmG...GG..",".......m........",".......m........","......m.........",
           "......m.........","...eeemeeee.....",".eeeeeeeeeeeee..","bbbbbbbbbbbbbbbb","bcbbbbcbbbbbcbbb"])
add('🦕', ["..........GGG...",".........GGkG...",".........GG.....","........GG......","........GG......",".......GG.......",
           "...GGGGGGG......",".GGGGGGGGGG.....","GGGGGGGGGGG.....","G.GGGGGGGGG.....","...GG...GG......","...dd...dd......"])
g = ring(blank(), 7.5, 7.5, 5.4, 7.2, 'r')
for i in range(-4, 5): put(g, [(7 + i, 7 - i), (8 + i, 7 - i), (7 + i, 8 - i)], 'r')
add('🚫', rows_of(g))
g = blank()
for y in range(16):
    lx = int(round(6 - y * 0.35)); rx = int(round(9 + y * 0.35))
    if y % 3 == 1:
        for x in range(lx - 1, rx + 2): g[y][x] = 'm'
    g[y][lx] = 'l'; g[y][rx] = 'l'
add('🛤', rows_of(g))
g = blank()
for y in range(0, 16): g[y][7] = 'b'; g[y][8] = 'b'
line(g, 1, 3, 14, 12, 'b'); line(g, 1, 12, 14, 3, 'b')
put(g, [(5, 1), (6, 2), (10, 1), (9, 2), (5, 14), (6, 13), (10, 14), (9, 13), (1, 6), (2, 5), (14, 6), (13, 5), (1, 9), (2, 10), (14, 9), (13, 10)], 'b')
put(g, [(7, 7), (8, 7), (7, 8), (8, 8)], 'w')
add('❄', rows_of(g))
add('🔥', ["........r.......",".......rr.......",".......rrr......","......rrrr..r...",".....rrrorr.rr..","....rrrooorrrr..",
           "...rrroooooorr..","...rroooyyooorr.","..rrooyyyyyoorr.","..rrooyyyyyyorr.","...rroyyyyyorr..","....rrooooorr...","......rrrrr....."])
add('🪨', ["....llll","..llllll",".lwlllll","llllllgl","lllglllg","llllllgg",".lllgggg","..gggggg"])
g = blank()
for y in range(16):
    for x in range(16):
        tx, ty = (x - 7.5) / 7, (y - 4.5) / 3.5
        if abs(tx) + abs(ty) <= 1 and y <= 8: g[y][x] = 'w' if (x + y) % 5 else 'c'
        elif 5 <= y <= 13 and abs(x - 7.5) <= 7 and y <= 13 - abs(x - 7.5) * 0.5 + 0.5 and y >= 4.5 + 3.5 * (1 - abs(x - 7.5) / 7):
            g[y][x] = 'c' if x < 8 else 'b'
put(g, [(4, 7), (5, 8), (11, 9), (12, 8)], 'w')
add('🧊', rows_of(g))
add('💎', ["...ccccc","..cwcccc","cccccccc",".bcbbcbb","..bcbbcb","...bbcbb","....bbcb",".....bbb","......bb",".......b"])
add('🌷', ["....r..r","....rrrr","....rrrr","....rrrr",".....rrr",".......G","...GG..G","...GGG.G","....GGGG",".......G",".......G"])
add('🌲', [".......d","......dd",".....ddd","....dddd",".....ddd","...ddddd","....dddd","..dddddd","...ddddd",".ddddddd","......mm","......mm"])
add('🍄', ["....rrrr","..rrrrrr",".rrwwrrr","rrrrrrww","rwwrrrww","rrrrrrrr","....eeee","....eeee","....eeee","...eeeee"])
add('⛺', [".......o","......oo",".....ooo","....oooo","...ooooo","..oooooM","..ooooMM",".ooooMMM","oooooMMM","ooooMMMM"])
add('🐔', ["....rr..........","...wwww.........","..wkwww.........","oowwwww......w..","..rwwwww...www..","...wwwwwwwwwww..",
           "...wwwwwwwwwww..","....wwwwwwwww...",".....wwwwwww....",".......o..o.....","......oo.oo....."])
add('🦆', [".....yyy........","....yyyyy.......","...yykyyy.......","..ooyyyyy.......","...ooyyy........","....yyyyyyyy..y.",
           "...yyyyyyyyyyyy.","...yyyyhhhyyyy..","....yyyyyyyyy...",".....yyyyyyy...."])
add('🐄', ["...........k.k..","..........wwwww.","..........wkwww.","w.........wwwpp.","wwwwwwwwwwwwwpp.",".wwkkwwwwkkwww..",
           ".wkkkwwwwwkkww..",".wwwwwwwwwwwww..",".wwwpwwwwwwwww..",".ww.ww....ww.ww.",".kk.kk....kk.kk."])
add('⛵', [".......w........","......ww........",".....www.w......","....wwww.ww.....","...wwwww.www....","..wwwwww.wwww...",
           ".wwwwwww.wwwww..","........m.......","mmmmmmmmmmmmmmmm",".mmmmmmmmmmmmmm.","..mmmmmmmmmmmm..","~~~~~~~~~~~~~~~~"])
add('🏰', ["..r.........r...","..l.........l...",".l.l.......l.l..",".lll.l.l.l.lll..",".lllllllllllll..",".lDlllllllllDl..",
           ".lllllllllllll..",".lllllDDDlllll..",".llllDDDDDllll..",".llllDDDDDllll.."])
g = blank(); ring(g, 7.5, 7, 5.2, 6.3, 'l')
for a in range(0, 360, 45):
    line(g, 7, 7, int(round(7.5 + 5 * math.cos(math.radians(a)))), int(round(7 + 5 * math.sin(math.radians(a)))), 'l')
for i, a in enumerate(range(0, 360, 45)):
    x = int(round(7.5 + 6.6 * math.cos(math.radians(a)))); y = int(round(7 + 6.6 * math.sin(math.radians(a))))
    put(g, [(x, y)], 'rybGvpor'[i])
put(g, [(7, 7), (8, 7)], 'D'); line(g, 7, 8, 4, 15, 'D'); line(g, 8, 8, 11, 15, 'D')
add('🎡', rows_of(g))
add('🌵', ["......GG........",".....GGGG.......",".....GdGG.......",".GG..GGGG..GG...",".GG..GdGG..GG...",".GGGGGGGG..GG...",
           "..GGGGGdGGGGG...",".....GGGGGGG....",".....GdGG.......",".....GGGG.......",".....GGGG.......","...eeeeeeee....."])
add('⛄', [".....DDD",".....DDD","...DDDDD","....wwww","....wkwo","....wwww","...rrrrr","..wwwwww",".wwwwwwk","wwwwwwww","wwwwwwwk",".wwwwwww","..wwwwww"])
add('⛲', ["......bb",".....b.b","....b..b","...b...b","...b..ll","..b.llll","..b...ll",".bb...ll","llllllll","lbbbbbbb","llllllll"])
add('🐖', ["...........pp...","..........pppp..","..pppppppppkppp.",".pppppppppppppqq",".pppppppppppppqq","q.pppppppppppp..",
           ".ppppppppppppp..","..pp.pp...pp.pp.","..qq.qq...qq.qq."])
add('🎠', [".......y........",".......y........","...w...y........","..wwww.y........",".wkww..y........","..ppwwwwwwww....",
           "....wwwwrrwwww..","....wwwwwwwwwwp.",".....ww.y..ww...","....ww..y...ww..","........y......."])
add('🧽', ["..GGGGGGGGGGGG..","..GGGGGGGGGGGG..","..yyyyyyyyyyyy..","..yhyyyyhyyyyy..","..yyyyhyyyyyhy..","..yyhyyyyyhyyy..",
           "..yyyyyyyyyyyy..","..hhhhhhhhhhhh.."])
add('🪑', ["...mmmmmmmmm....","...mMMMMMMMm....","...mmmmmmmmm....","...m.......m....","...m.......m....","..mmmmmmmmmmm...",
           "..MMMMMMMMMMM...","..m.........m...","..m.........m...","..m.........m..."])
add('🍂', ["...........oo...",".........oooo...",".......ooooooo..","......oooOoooo..",".....oooOooooo..","....rooOoooooo..",
           "...rroOooooo....","...rOoooo.......","..rOooo.........","..Oo............",".O.............."])
CLOUD = ["......wwww......", "....wwwwwwww....", "...wwwwwwwwww...", ".wwwwwwwwwwwwww.", "wwwwwwwwwwwwwwww", "wwwwwwwwwwwwwwww", ".wllllllllllllw."]
add('☁', CLOUD)
add('🌧', [r.replace('w', 'l').replace('l', 'l') for r in CLOUD[:6]] + [".gggggggggggggg.", "", "..~...~...~...~.", ".~...~...~...~..", "...~...~...~....", "..~...~...~....."])
add('🌫', ["................", ".llllllllllll...", "................", "...llllllllllll.", "................", ".llllllllllll...", "................", "...llllllllllll.", "................", ".lllllllll......"])
g = blank(); disc(4.2, 'y', cx=10, cy=5, g=g); stamp(g, CLOUD, 0, 7)
add('⛅', rows_of(g))
g = blank(); disc(3.6, 'y', cx=11, cy=4, g=g); stamp(g, [r.replace('w', 'l') for r in CLOUD[:6]], 0, 5)
put(g, [(3, 12), (7, 12), (11, 12), (2, 14), (6, 14), (10, 14)], '~')
add('🌦', rows_of(g))
add('🪟', ["mmmmmmmmmmmmmm","mccccccmccccccm","mcwccccmcwccccm","mccccccmccccccm","mccccccmccccccm","mmmmmmmmmmmmmmm",
           "mccccccmccccccm","mccccccmccccccm","mccccccmccccccm","mmmmmmmmmmmmmmm"])
add('🌡', ["......www.......",".....wwlww......",".....wwrww......",".....wwrwwl.....",".....wwrww......",".....wwrwwl.....",
           ".....wwrww......",".....wwrwwl.....","....wwrrrww.....","....wrrrrrw.....","....wrrrrrw.....",".....wrrrw......"])
def arrow_tile(up):
    g = blank()
    for y in range(1, 15):
        for x in range(1, 15): g[y][x] = 'b'
    shape = [".......ww.......", "......wwww......", ".....wwwwww.....", "....wwwwwwww....", ".......ww.......", ".......ww.......", ".......ww.......", ".......ww......."]
    if not up: shape = shape[::-1]
    stamp(g, shape, 0, 4)
    return rows_of(g)
add('⬆', arrow_tile(True)); add('⬇', arrow_tile(False))
g = blank()
for (x0, y0) in [(2, 3), (8, 1), (6, 8)]:
    stamp(g, ["..b..", ".bbb.", "bbbbb", "bcbbb", ".bbb."], x0, y0)
add('💦', rows_of(g))
g = blank()
for y in range(1, 15):
    for x in range(1, 15): g[y][x] = 'b'
stamp(g, ["wwwwwww.", "wwwwwwww", ".....ww.", ".....ww."], 2, 3); stamp(g, ["..w..", ".www.", "wwwww", ".www."], 7, 9)
add('🚰', rows_of(g))
