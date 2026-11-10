from lib import *

def diag_tool(colors, start=(14, 1), length=13, width=3, shade=None):
    """Diagonal stick from top-right to bottom-left; colors = list of (rows_count, color)."""
    g = blank(); seq = []
    for c, n in colors: seq += [c] * n
    for i, col in enumerate(seq):
        x0 = start[0] - i; y = start[1] + i
        for j in range(width):
            x = x0 - (width // 2) + j
            c = col
            if col == 'TIP': c = 'k' if j == width // 2 else None
            if shade and j == width - 1 and col == shade[0]: c = shade[1]
            if c and 0 <= x < 16 and 0 <= y < 16: g[y][x] = c
    return g

# fix samples
add('🦄', [".......y",".......o",".......y",".......o",".p.....y",".ppwwwwy","pwwwwwww","pwwkwwww","wwwkwwww","wpwwwwww",
           "wwwwwwww",".wwppppp","..wpkppp","...ppppp"])
add('🎈', ["....rrrr","..rrrrrr",".rwwrrrr",".rwrrrrr",".rrrrrrr",".rrrrrrr","..rrrrrr","...rrrrr",".....rrr",".......r",
           "........l.......",".......l........","........l.......",".......l........"])

add('😊', over(face(), ["","","","",".....k....k.....","....k.k..k.k....","","...pp......pp...","....k......k....",".....kkkkkk....."]))
add('😴', over(face(), ["...........~~~..","............~...","...........~~~.","","","...kkk....kkk...","","","","......kkkk......","......kkkk......"]))
add('🛁', [".ll......c.c....",".l......ccccc...",".l....cccccccc..","wwwwwwwwwwwwwwww",".wwwwwwwwwwwwww.",".wwwwwwwwwwwwww.",
           "..wwwwwwwwwwww..","..llllllllllll..","..l..........l.."])
add('🚽', ["...wwwww","...wwwww","...wwwwl","...lllll",".wwwwwww","wwwwwwww",".wwwwwww","..wwwwww","...wwwww","....wwww",
           "...lllll","...lllll"])
add('🧼', ["...........cc...","........cc.cc...","........cc......","....pppppppppp..","..pppwwwppppppp.",".pppppppppppppp.",
           ".pppppppppppppp.",".qqqqqqqqqqqqqq.","..qqqqqqqqqqqq.."])
add('🦷', [".wwwww..","wwwwwwww","wcwwwwww","wwwwwwww","wwwwwwww","wwwwwwww",".wwwwwww",".wwwwwww",".wwwwwww",".wwwww..",
           "..www...","..ww...."])
add('💪', ["..yyy...........",".yyyyy..........",".yhhhy..........","..yyy...........","..yyy....yyy....","..yyy...yyyyy...",
           "..yyy..yyyhyyy..","..yyyyyyyhyyyyy.","..yyyyyyyyyyyyyy","...yyyyyyyyyyyyy","....yyyyyyyyyyy."])
add('🤸', ["..y..........y..","...n........n...","....n......n....",".....nnnnnn.....","......bbbb......","......bbbb......",
           ".....ybbbby.....","....y.yyyy.y....","...y..yyyy..y...","..y...yyyy...y..",".yy...........yy"])
add('🕺', ["............y...","......yyy..y....","......yyy.y.....","......yyyy......",".....vvvvv......","....yvvvvv......",
           "...y.vvvvv......","..y..vvvvv......","......nnnn......",".....nn..nn.....","....nn....nn....","....n......nn...",
           "...kk.......kk.."])
add('💃', ["............y...","......yyy..y....","......yyy.y.....","......yyyy......","......rrrr......","....yrrrrr......",
           "...y..rrrr......","......rrrr......",".....rrrrrr.....","....rrrrrrrr....","...rrrrrrrrrr...","..rrrrrrrrrrrr..",
           ".......y..y.....","......kk..kk...."])
add('🧘', [".......yy.......","......yyyy......","......yyyy......",".......yy.......",".....TTTTTT.....","....yTTTTTTy....",
           "...y.TTTTTT.y...","..y..TTTTTT..y..",".yy.nnnnnnnn.yy.","..nnnnnnnnnnnn..",".nnnnnnnnnnnnnn."])
add('🙏', [".......y","......yy","......yh",".....yyh",".....yyh","....yyyh","....yyyh","...yyyyh","...yyyyh","..yyyyyh",
           "..bbbbbb",".bbbbbbb"])
add('📖', [".wwww...","wwwwwww.","wllllwwg","wwwwwwwg","wllllwwg","wwwwwwwg","wllllwwg","wwwwwwwg","bbbbbbbb","...bbbbb"])
add('🍳', ["..DDDDDDDDD.....",".DDwwwwwDDDD....","DDwwwwwwwwDDD...","DDwwwyyywwwDDMMM","DDwwyyyyywwDDMMM",
           "DDwwwyyywwDDD...",".DDwwwwwwDDD....","..DDDDDDDDD....."])
add('🥪', ["..tttttttttttt..",".teeeeeeeeeeeet.",".tttttttttttttt.",".GLGGLGGLGGLGGL.",".rrrrrrrrrrrrrr.",".yyyyyyyyyyyyyy.",
           ".tttttttttttttt.",".teeeeeeeeeeeet.","..tttttttttttt.."])
add('🥦', ["...GGG.G",".GGGdGGG","GGdGGGdG","GGGGGGGG","GdGGdGGG",".GGGGGGd",".....LLL",".....LLL","......LL","......LL",".....LLL"])
g = disc(5.6, 'w', rim='l'); disc(2.6, 'l', g=g); disc(2.0, 'w', g=g)
put(g, [(0, 2), (0, 3), (2, 2), (2, 3), (1, 2), (1, 3), (1, 4)] + [(1, y) for y in range(4, 14)], 'g')
put(g, [(14, y) for y in range(2, 14)] + [(15, y) for y in range(2, 8)], 'g')
add('🍽', rows_of(g))
add('🥛', ["..cccccc","..clllll","..cwwwww","..cwwwww","..cwwwww","..cwwwww","..cwwwww","..cwwwww","..cwwwww","...cwwww",
           "...cwwww","...ccccc"])
add('💧', [".......b","......bb","......bb",".....bbb","....bbbb","...bbbbb","..bcbbbb","..bcbbbb",".bbcbbbb",".bbbbbbb",
           ".bbbbbbb","..bbbbbb","...bbbbb",".....bbb"])
add('👖', [".BBBBBBB",".bbbbbbb",".bbbbbbb",".bbbbbbb",".bbbbbb.",".bbbbb..",".bbbbb..",".bbbbb..",".bbbbb..",".bbbbb..",
           ".bbbbb..",".bbbbb..",".BBBBB.."])
add('🧦', ["....wwwww.......","....rrrrr.......","....wwwww.......","....rrrrr.......","....wwwww.......","....wwwww.......",
           "....wwwwww......","....wwwwwwww....","...rrwwwwwwwww..","...rrwwwwwwwwww.","....wwwwwwwrrrr.",".....wwwwwwrrr.."])
add('👟', ["...bbb..........","...bbbbbbb......","...bbbwbwbbb....","...bbbbwbwbbbb..","...bbbbbbbbbbbbb","...bbbbbbbbbbbbb",
           "..wwwwwwwwwwwwww","..llllllllllllll"])
add('👗', [".....p..",".....p..","....pppp","....pppp","....pppp",".....qqq","....pppp","...ppppp","...ppppp","..pppppp",
           "..pppppp",".ppppppp","pppppppp","qqqqqqqq"])
add('🎀', ["pp......","pppp....","ppppppqq","pppppqqq","ppppppqq","pppp....",".....pp.","....pp..","...pp..."])
add('🧥', ["..mmmmM.",".mmmmmM.","mmmmmmmy","mmmmmmmm","mmmmmmmy","mm.mmmmm","mm.mmmmy","mm.mmmmm","MM.mmmmy","...mmmmm","...MMMMM"])
add('🚌', ["yyyyyyyyyyyyyyy.","yccyccyccyccyccy","yccyccyccyccyccy","yyyyyyyyyyyyyyyy","DDDDDDDDDDDDDDDD","yyyyyyyyyyyyyyyo",
           "hhkkhhhhhhkkhhhh","..kk......kk...."])
add('🏫', [".......R","......RR",".....RRR","....RRRR","....rrww","....rrwk","RRRRrrww","rrrrrrrr","rccrrccr","rccrrccr",
           "rrrrrrrr","rccrrrmm","rrrrrrmm"])
g = blank()
for y in range(0, 15):
    for x in range(1, 11): g[y][x] = 'w'
for y in (3, 5, 7, 9, 11):
    for x in range(2, 9): g[y][x] = 'l'
pen = diag_tool([('p', 1), ('l', 1), ('y', 6), ('s', 1), ('TIP', 1)], start=(14, 1), width=2)
for y in range(16):
    for x in range(16):
        if pen[y][x] != '.': g[y][x] = pen[y][x]
add('📝', rows_of(g))
add('📚', ["..rrrrrrrrrrrr..","..ryyyyyyyyyyr..","..rrrrrrrrrrrr..",".bbbbbbbbbbbbb..",".bwwwwwwwwwwwb..",".bbbbbbbbbbbbb..",
           "...GGGGGGGGGGGG.","...GyyyyyyyyyyG.","...GGGGGGGGGGGG."])
FONT = {'A': [".w.", "w.w", "www", "w.w", "w.w"], 'B': ["ww.", "w.w", "ww.", "w.w", "ww."], 'C': [".ww", "w..", "w..", "w..", ".ww"],
        '1': [".w.", "ww.", ".w.", ".w.", "www"], '2': ["ww.", "..w", ".w.", "w..", "www"], '3': ["ww.", "..w", ".w.", "..w", "ww."]}
def tile(text, bg):
    g = blank()
    for y in range(3, 13):
        for x in range(0, 16): g[y][x] = bg
    for i, ch in enumerate(text):
        for yy, row in enumerate(FONT[ch]):
            for xx, c in enumerate(row):
                if c == 'w': g[5 + yy][2 + i * 4 + xx] = 'w'
    return rows_of(g)
add('🔤', tile('ABC', 'b'))
add('🔢', tile('123', 'v'))
add('🧩', [".....GG.........","....GGGG........","..GGGGGGGGG.....","..GGGGGGGGG.....","..GGGGGGGGGGG...","..GGGGGGGGGGGG..",
           "..GGGGGGGGGGGG..","..GGGGGGGGGGG...","..GGGGGGGGG.....","..GGG...GGG.....","..GG.....GG....."])
add('🖍', rows_of(diag_tool([('r', 2), ('w', 1), ('r', 1), ('w', 1), ('r', 5), ('R', 1), ('TIP', 1)], start=(13, 1), width=3)))
add('🧸', [".mm.....","mtmmmmmm","mmmmmmmm",".mmmkmmm",".mmmmmmm",".mmmtttt","..mmtttk","...mtttt","....mmmm"])
g = diag_tool([('m', 9)], start=(13, 0), width=1)
for y, (a, b) in enumerate([(4, 8), (3, 9), (2, 9), (1, 9), (1, 8), (0, 7)]):
    for x in range(a, b): g[9 + y][x] = 'h' if (x + y) % 3 else 'o'
put(g, [(4, 8), (5, 8), (6, 8), (7, 8)], 'R')
add('🧹', rows_of(g))
add('🧺', ["....MMMM","...M....","..M.....","..M.....","tttttttt",".tmtmtmt",".mtmtmtm",".tmtmtmt","..mtmtmt","..tmtmtm","...ttttt"])
g = disc(7.3, 'r'); disc(5.6, 'w', g=g)
for y in range(4, 12):
    for x in range(6, 10): g[y][x] = 'D'
for y in range(5, 10):
    for x in range(7, 9): g[y][x] = 'c'
for i in range(-5, 6): put(g, [(7 + i, 7 + i), (8 + i, 7 + i)], 'r')
add('📵', rows_of(g))
add('📱', ["....DDDDDDDD....","....DbbbbbbD....","....DbccbbbD....","....DbbbbbbD....","....DbbbbbbD....","....DbbbbbbD....",
           "....DbbbbbbD....","....DbbbbbbD....","....DbbbbbbD....","....DbbbbbbD....","....DbbbbbbD....","....DDDllDDD....",
           "....DDDDDDDD...."])
add('🎮', ["..llllllllllll..",".llkllllllllyll.",".lkkkllllllblrl.",".llkllllllllGll.",".llllllllllllll.",".llll......llll.","..ll........ll.."])
add('📺', ["....g......g....",".....g....g.....","......g..g......",".DDDDDDDDDDDDDD.",".DbbbbbbbbbbbbD.",".DbccbbbbbbbbbD.",
           ".DbcbbbbbbbbbbD.",".DbbbbbbbbbbbbD.",".DbbbbbbbbbbbbD.",".DbbbbbbbbbbbbD.",".DDDDDDDDDDDDDD.","..D..........D.."])
add('🐕', ["...........tt...","..........tMtt..","..........ttkt..","t.........tttttk",".t.......ttttt..","..ttttttttttt...",
           "..ttttttttttt...","..ttttttttttt...","..tt.tt...tt.tt.","..tt.tt...tt.tt."])
add('🐈', ["g..........g.g..","g..........ggg..",".g........ggkg..",".g........gggg..","..ggggggggggg...","..gggggggggg....",
           "..gggggggggg....","..gg.gg..gg.gg..","..gg.gg..gg.gg.."])
add('🌳', ["....GGGG","..GGGGGG",".GGLGGGG","GGLGGGGG","GGGGGGGG","GGGGGGdG","GGGGGdGG",".GGGGGGG","..dGGGGG","......mm",
           "......mm","......mm",".....mmm"])
g = disc(7.2, 'o')
put(g, [(7, y) for y in range(1, 15)] + [(x, 7) for x in range(1, 15)], 'k')
arc = [(3, 2), (4, 3), (4, 4), (5, 5), (5, 6), (5, 8), (5, 9), (4, 10), (4, 11), (3, 12)]
put(g, arc, 'k'); put(g, [(15 - x, y) for x, y in arc], 'k')
add('🏀', rows_of(g))
add('🎵', ["........vvv.....","........vvvvv...","........v..vvv..","........v....v..","........v.......","........v.......",
           "........v.......","........v.......",".....vvvv.......","....vvvvv.......","....vvvvv.......",".....vvv........"])
g = blank()
for y in range(2, 4):
    for x in range(0, 15): g[y][x] = 'r'
for y in range(4, 12):
    for x in range(0, 15): g[y][x] = 'w'
for x in (2, 5, 8, 11):
    for y in range(4, 12): g[y][x] = 'l'
for x0 in (1, 4, 10):
    for y in range(4, 8):
        g[y][x0 + 1] = 'k'; g[y][x0 + 2] = 'k'
add('🎹', rows_of(g))
HEART = ["........","..rrrr..",".rrrrrr.","rrwwrrrr","rrwrrrrr","rrrrrrrr","rrrrrrrr",".rrrrrrr","..rrrrrr","...rrrrr","....rrrr",
         ".....rrr","......rr",".......r"]
add('💚', [r.replace('r', 'G') for r in HEART])
add('💛', [r.replace('r', 'y') for r in HEART])
add('💗', [r.replace('r', 'p') for r in HEART])
g = blank()
disc(4.6, 'y', cx=7.5, cy=10, g=g)
for y in range(10, 16):
    for x in range(16): g[y][x] = '.'
put(g, [(6, 6), (7, 6), (8, 6), (9, 6)], 'o')
for y in range(10, 14):
    for x in range(0, 16): g[y][x] = 'b'
put(g, [(2, 11), (3, 11), (4, 11), (9, 12), (10, 12), (11, 12), (12, 12), (6, 11), (7, 11), (8, 11)], 'c')
put(g, [(7, 1), (8, 1), (7, 2), (8, 2), (2, 4), (3, 5), (13, 4), (12, 5), (0, 8), (1, 8), (14, 8), (15, 8)], 'o')
add('🌅', rows_of(g))
add('🏠', ["......rr",".....rrr","....rrrr","...rrrrr","..rrrrrr",".rrrrrrr","rrrrrrrr",".eeeeeee",".ecceeee",".ecceeee",
           ".eeeeemm",".eeeeemm",".eeeeemm"])
g = disc(6.3, 'w', cx=7.5, cy=8.5, rim='l')
put(g, [(7, 0), (8, 0)], 'D'); put(g, [(7, 1), (8, 1)], 'l'); put(g, [(12, 2), (13, 3), (13, 2)], 'l')
put(g, [(7, y) for y in range(5, 9)] + [(8, 8), (9, 8)], 'r'); put(g, [(7, 8)], 'k')
add('⏱', rows_of(g))
g = disc(7.1, 't')
put(g, [(4, 4), (5, 4), (9, 3), (11, 6), (12, 6), (5, 9), (6, 9), (9, 10), (10, 11), (3, 7), (7, 12), (8, 12), (12, 10)], 'M')
put(g, [(13, 2), (14, 3), (12, 1), (14, 4), (13, 3), (12, 2), (11, 1), (14, 5)], '.')
add('🍪', rows_of(g))
add('🧴', ["......DDDDDD....","........DD......",".......TTTT.....",".....TTTTTTTT...","....TTTTTTTTTT..","....TwwwwwwwwT..",
           "....TwwbbwwwwT..","....TwwwwwwwwT..","....TTTTTTTTTT..","....TTTTTTTTTT..","....TTTTTTTTTT..",".....TTTTTTTT..."])
add('👋', ["....y.y.y.......","....y.y.y.y.....","....yyyyyyy.....","yy..yyyyyyy.....",".yy.yyyyyyy.....","..yyyyyyyyy.....",
           "...yyyyyyyy.....","....yyyyyy......",".....yyyy......."])
