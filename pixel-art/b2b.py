from lib import *
import math
add('🕊', ["..........G.....",".........GdG....","...wwww....d....","..wwwwwww..d....",".wwwkwwwwwd.....","ooowwwwwwwww....",
           "..wwwwwwwwwwww..","...wwwlwwwwwwww.","....wwwllwwwwwww",".....wwwwwww....","......w..w......"])
g = blank()
stamp(g, [".......y.......", ".......y.......", "......yyy......", "......yyy......", ".....yywyy.....", "yyyyyyyyyyyyyyy", ".yyyyyyyyyyyyy.",
          "..yyyyyyyyyyy..", "...yyyyyyyyy...", "...yyyyyyyyy...", "..yyyyy.yyyyy..", "..yyy.....yyy..", ".yy.........yy."], 0, 2)
put(g, [(1, 1), (14, 1), (0, 9), (15, 9), (2, 0), (13, 0)], '*')
add('🌟', rows_of(g))
add('🌱', ["................","..GG......GG....",".GLLG....GLLG...",".GLLLG..GLLLG...","..GGLLGGLLGG....","....GGGGGG......",
           ".......dd.......",".......dd.......","...mmmmmmmmmm...","..mmMmmmmMmmmm..","...mmmmmmmmmm..."])
g = ring(blank(), 7.5, 7.5, 5.4, 7.2, 'v')
for y in range(1, 15): g[y][7] = 'v'; g[y][8] = 'v'
line(g, 7, 8, 3, 12, 'v'); line(g, 8, 8, 12, 12, 'v'); line(g, 7, 9, 4, 12, 'v'); line(g, 8, 9, 11, 12, 'v')
add('☮', rows_of(g))
add('🍃', ["...........GG...","........GGGGG...",".......GLGGGG...","......GLGGGd....",".....GLGGGd.....","....GLGGd.......",
           "...GGdd.........","..d.............","....GG..........","...GLGG.........","..GLGGd.........","..GGdd..........",".d.............."])
add('🐑', ["....wwwwwww.....","..wwwwwwwwwww...",".wwwwwwwwwwwwww.","DDwwwwwwwwwwwww.","DkDwwwwwwwwwwww.","DDDwwwwwwwwwwww.",
           ".DDwwwwwwwwwwww.","..wwwwwwwwwwww..","...D.D....D.D...","...D.D....D.D..."])
g = blank(); disc(3.6, 'y', cx=7.5, cy=7, g=g)
for y in range(16):
    for x in range(16):
        if y >= 6 and (abs(x - 4) <= (y - 6) * 0.9 or abs(x - 11) <= (y - 5) * 0.8): g[y][x] = 'd' if (x + y) % 5 else 'G'
for y in range(13, 16):
    for x in range(16): g[y][x] = '.'
put(g, [(4, 6), (11, 5), (3, 7), (5, 7), (11, 6)], 'w')
add('🌄', rows_of(g))
g = blank()
for y in range(6, 10):
    for x in range(1, 9): g[y][x] = 'D'
for y in range(5, 11):
    for x in range(9, 11): g[y][x] = 'l'
put(g, [(4, 6), (5, 6)], 'r')
for i, y in enumerate(range(3, 13)):
    w = abs(y - 7.5)
    for x in range(11, 16):
        if abs(y - 7.5) <= 1.2 + (x - 11) * 0.9: g[y][x] = '*'
add('🔦', rows_of(g))
g = blank()
for (cx, cy) in [(5, 6), (8, 6), (11, 6), (6.5, 8.5), (9.5, 8.5), (5, 11), (8, 11), (11, 11)] if False else [(5.5, 6), (9.5, 6), (3.5, 9), (7.5, 9), (11.5, 9), (5.5, 12), (9.5, 12), (7.5, 14.4)]:
    disc(1.6, 'v', cx=cx, cy=cy, g=g)
put(g, [(5, 5), (9, 5), (3, 8), (7, 8), (11, 8), (5, 11), (9, 11)], 'p')
put(g, [(7, 3), (8, 2), (8, 1)], 'd'); put(g, [(9, 2), (10, 2), (11, 1), (10, 1), (12, 1)], 'G')
add('🍇', rows_of(g))
add('🐢', [".....GGGGG......","....GdGdGdG.....","...GdGGdGGdG.yy.","..GGdGGdGGdGyyky","..GdGGdGGdGGyyyy",".LLLLLLLLLLLLyy.",
           "..yy.......yy...","..yy.......yy..."])
add('🛡', ["bbbbbbbb","bBBBBBBB","bBBBBBBy","bBBBBByy","bByyyyyy","bBByyyyy","bBBByyyy",".bBByyBy","..bBBBBB","...bBBBB","....bbbb",".....bbb","......bb"])
add('🌋', ["......r..r......",".....rr.rr.r....","......rrrr......",".....mrrrrm.....","....mmrrrmmm....","....mmmrrmmmm...",
           "...mmmmmrmmmmm..","...mmMmmmmmMmm..","..mmmmmmMmmmmmm.",".mmmMmmmmmmmMmmm","mmmmmmmmmmmmmmmm"])
add('🌊', ["........wwww....","......wwbbbbw...",".....wbbbbbbbw..","....wbbbbw.wbb..","...wbbbbbw..wb..","..wbbbbbbbw.....",
           ".wbbbbbbbbbw....","wbbbbbbbbbbbw..w","bbbbbbbbbbbbbbbb","BBBBBBBBBBBBBBBB"])
add('⛈', ["....llll........","..llllllll.ll...",".lllllllllllll..","llllllllllllllll","gggggggggggggggg",".gggggggggggggg.",
           "...~..yy..~.....","..~..yy..~...~..",".....yyyy.......","......yy..~.....","......y.........","...~.....~......"])
add('🌸', ["......pp","....pppp","....pqpp",".pp.pppp","ppppppqy","pqppppyy",".ppppppy","..pppppp","...ppppq","...pppp.","....pp.."])
FONT = {'1': [".w.", "ww.", ".w.", ".w.", "www"], '0': ["www", "w.w", "w.w", "w.w", "www"]}
g = blank()
for y in range(1, 15):
    for x in range(1, 15): g[y][x] = 'b'
for i, ch in enumerate('10'):
    for yy, row in enumerate(FONT[ch]):
        for xx, c in enumerate(row):
            if c == 'w': g[5 + yy][4 + i * 5 + xx] = 'w'
add('🔟', rows_of(g))
add('🧱', ["rrrrrRrrrrrRrrrr","rrrrrRrrrrrRrrrr","RRRRRRRRRRRRRRRR","rrRrrrrrRrrrrrRr","rrRrrrrrRrrrrrRr","RRRRRRRRRRRRRRRR",
           "rrrrrRrrrrrRrrrr","rrrrrRrrrrrRrrrr","RRRRRRRRRRRRRRRR","rrRrrrrrRrrrrrRr","rrRrrrrrRrrrrrRr"])
g = blank()
for y in range(16):
    for x in range(16):
        if abs(x - 7.5) + abs(y - 7.5) <= 10.5 and abs(x - 7.5) <= 7.5 and abs(y - 7.5) <= 7.5: g[y][x] = 'r'
for y in range(7, 9):
    for x in range(3, 13): g[y][x] = 'w'
add('🛑', rows_of(g))
add('🛋', ["..vvvvvvvvvvvv..",".vvvvvvvvvvvvvv.",".vvvvvvvvvvvvvv.","vvvPPPPPPPPPPvvv","vvvvvvvvvvvvvvvv","vvvvvvvvvvvvvvvv",
           "PPPPPPPPPPPPPPPP",".M............M."])
add('🎧', ["....DDDD",".DDD....",".D......","D.......","D.......","D.......","rrr.....","rrrr....","rrrr....","rrrr....","rrr....."])
add('📓', ["..lPPPPPPPPPPP..","..PPPPPPPPPPPPP.","..lPPPPPPPPPPP..","..PPPwwwwwwPPPP.","..lPPPPPPPPPPP..","..PPPPPPPPPPPPP.",
           "..lPPPPPPPPPPP..","..PPPPPPPPPPPPP.","..lPPPPPPPPPPP..","..PPPPPPPPPPPPP.","..lPPPPPPPPPPP..","..PPPPPPPPPPPPP."])
add('🦘', ["..........tt....","..........ttt...",".........ttkt...",".........tttttk.","........ttt.....","......tttt.yy...",
           ".....tttttt.....","....tttttttt....","...ttttttttt....","..tt..tttttt....",".t.....tt..tt...","t......tttt.ttt."])
add('🪵', ["...mmmmmmmmmeee.","..mmMmmmmmmetteM",".mmmmmmmMmmettte",".mmmMmmmmmmetmte","..mmmmmmMmmettte","...mmmmmmmmmeee."])
add('🐻', [".mm.....","mMmmmmmm","mmmmmmmm",".mmkmmmm",".mmmmmmm",".mmmtttt","..mmtttk","...mtttt","....mmmm"])
g = blank()
for y in range(1, 15):
    for x in range(1, 15): g[y][x] = 'b'
ring(g, 7.5, 7.5, 3.0, 4.6, 'w')
put(g, [(11, 3), (12, 3), (12, 4), (11, 5), (11, 4)], 'b'); put(g, [(12, 2), (13, 3), (12, 3)], 'w')
put(g, [(4, 11), (3, 11), (3, 10), (4, 9), (4, 10)], 'b'); put(g, [(3, 12), (2, 11), (3, 11)], 'w')
add('🔄', rows_of(g))
g = blank()
for y in range(1, 15):
    for x in range(1, 15): g[y][x] = 'b'
for i, h in enumerate([2, 4, 6, 8]):
    for y in range(12 - h, 12):
        for x in (3 + i * 3, 4 + i * 3): g[y][x] = 'w'
add('📶', rows_of(g))
g = blank()
for y in range(1, 15):
    for x in range(16):
        if abs(x - 7.5) <= (y - 1) * 0.58: g[y][x] = 'y'
for y in range(5, 10): g[y][7] = 'k'; g[y][8] = 'k'
put(g, [(7, 11), (8, 11), (7, 12), (8, 12)], 'k')
add('⚠', rows_of(g))
g = blank(); disc(4.2, 'y', cx=6, cy=5.5, g=g)
stamp(g, ["....wwww....", "..wwwwwwww..", ".wwwwwwwwwww", "wwwwwwwwwwww", ".wwwwwwwwww."], 4, 8)
add('🌤', rows_of(g))
add('⭕', rows_of(ring(blank(), 7.5, 7.5, 4.6, 7.2, 'r')))
add('🕯', [".......o",".......y","......oy",".......k","....pppp","...pwppp","...pwppp","...ppppp","...ppppp","...ppppp","...ppppp","..llllll"])
add('📣', ["...........rr...",".........rrrr...","......rrrrrrr...","...wwrrrrrrrr...","..wwwrrrrrrrr...","..wwwrrrrrrrr...",
           "...wwrrrrrrrr...","....l.rrrrrrr...","....l....rrrr...","...ll......rr..."])
add('⬜', ["................",".wwwwwwwwwwwwww."] + [".wwwwwwwwwwwwww."] * 12 + [".wwwwwwwwwwwwww."])
g = blank()
for (cx, cy, r) in [(5, 9, 4.2), (12, 4.5, 2.6), (12.5, 12, 1.8)]:
    ring(g, cx, cy, r - 1.1, r, 'b')
    put(g, [(int(cx - r / 2), int(cy - r / 2))], 'w')
add('🫧', rows_of(g))
g = blank()
for y in range(16):
    for x in range(16):
        if abs(x - 9) + abs(y - 6) <= 5.5: g[y][x] = 'r' if x < 9 and y < 6 else 'y' if x >= 9 and y < 6 else 'b' if x < 9 else 'G'
line(g, 9, 1, 9, 11, 'k'); line(g, 4, 6, 14, 6, 'k')
put(g, [(8, 12), (7, 13), (6, 13), (5, 14), (4, 14)], 'l'); put(g, [(6, 12), (5, 15)], 'p')
add('🪁', rows_of(g))
g = blank(); disc(5, 'r', cx=7.5, cy=9.5, g=g)
for x in range(3, 13): g[9][x] = 'R'
put(g, [(7, 9), (8, 9)], 'l')
for y in range(0, 5): g[y][8] = 'l'
put(g, [(7, 0), (8, 0), (9, 0)], 'l')
add('🪀', rows_of(g))
add('🐰', ["..ww....","..wpw...","..wpw...","..wpw...","..wpw...","..wwwwww",".wwwwwww",".wwkwwww",".wwwwwww",".wpwwwwp","..wwwwwk","...wwwkw","....wwww"])
add('🐒', ["....mmmm........","...mmmmmm.......","..tmeeeemt......","...meekem.......","...meeeem.......","....meem........",
           "...mmmmmm....mm.","..mmmmmmmm...m..","..m.mmmm.m..m...","....mmmmmmmm....","....mm..mm......","...mm....mm....."])
add('📷', ["...DDD..........",".DDDDDDDDDDDDDD.",".DllllllllllllD.",".Dlll.....lllrD.",".Dll.DDDDD.lllD.",".Dl.DDbbbDD.llD.",
           ".Dl.DbbcbbD.llD.",".Dl.DDbbbDD.llD.",".Dll.DDDDD.lllD.",".DllllllllllllD.",".DDDDDDDDDDDDDD."])
add('🎙', ["......llll......",".....lDlDll.....",".....llDlDl.....",".....lDlDll.....",".....llllll.....","...l.llllll.l...",
           "...l..llll..l...","....l......l....",".....llllll.....",".......ll.......",".......ll.......","....llllllll...."])
add('🧠', ["...pppp.","..pqpppq",".ppppqpp","pqpppppq","ppqppqpp","pppppppq",".ppqpppp","..pppqpp","....pppp","......qq"])
add('💬', ["...wwwwwwwwww...","..wwwwwwwwwwww..",".wwwwwwwwwwwwww.",".wwllwwllwwllww.",".wwwwwwwwwwwwww.","..wwwwwwwwwwww..",
           "...wwwwwwwwww...","...www..........","..ww............",".w.............."])
g = blank()
pts = []
for i in range(260):
    t = i / 260 * 4.2 * math.pi; r = 0.4 + t * 0.53
    x = int(round(7.5 + r * math.cos(t))); y = int(round(7.5 + r * math.sin(t)))
    if 0 <= x < 16 and 0 <= y < 16: g[y][x] = 'b'
add('🌀', rows_of(g))
add('🧰', ["....DDDDDDDD....","....D......D....","rrrrrrrrrrrrrrrr","rrrrrrrrrrrrrrrr","RRRRRRyyRRRRRRRR","rrrrrrrrrrrrrrrr",
           "rrrrrrrrrrrrrrrr","rrrrrrrrrrrrrrrr","RRRRRRRRRRRRRRRR"])
