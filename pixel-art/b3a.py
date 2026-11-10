from lib import *
import math
# ---------- pet foods ----------
add('🍌', ["............M...","...........hy...","..........yyy...",".........yyyh...","........yyyyh...","......yyyyyh....",
           "....yyyyyyh.....",".yyyyyyyyh......","..hhhhhhh......."])
g = disc(6.2, 'o', cy=8.6); put(g, [(5, 5), (4, 6), (5, 6)], 'y'); put(g, [(7, 2), (8, 2), (8, 1), (9, 1), (10, 1), (9, 0)], 'G'); put(g, [(7, 3), (8, 3)], 'd')
add('🍊', rows_of(g))
add('🥕', ["...........G.G..","............GG.G","...........GGG..","..........ooo...",".........oooo...","........oOooo...",
           ".......oooOo....","......ooooo.....",".....oOooo......","....oooo........","...ooo..........","..oo............",".o.............."])
g = blank()
for y in range(16):
    for x in range(16):
        d = ((x - 7.5) ** 2 + (y - 3) ** 2) ** .5
        if y >= 4 and d <= 7.5: g[y][x] = 'd' if d > 6.6 else 'L' if d > 5.7 else 'r'
put(g, [(5, 6), (8, 7), (10, 6), (6, 8), (9, 9), (4, 5)], 'k')
add('🍉', rows_of(g))
add('🥗', ["...G.L.G",".GLGGLrG","GLGGLGGL","wwwwwwww",".wwwwwww","..wwwwww","...wwwww",".....lll"])
add('🍲', ["...&..&.","....&..&","..yoGoOo","DDDDDDDD",".DDDDDDD",".DDDDDDD",".DDDDDDD","..DDDDDD"])
add('🍚', ["....wwww","..wwwwww",".wwwlwww","bbbbbbbb",".bbbbbbb",".bwbbbbb","..bbbbbb","...bbbbb",".....BBB"])
add('🍟', ["..y..y.y","..yy.yyy",".yyyyyyy","rrrrrrrr","rrrrrrrr",".rrrrrrr",".rrrrrrr","..rrrrrr","..rrrrrr"])
add('🍔', ["...ttttt",".ttttttt","ttwtttwt","tttttttt","GLGLGLGL","yyyyyyyy","MMMMMMMM","MMMMMMMM","tttttttt",".ttttttt"])
add('🍗', ["......OOOOO.....",".....OOOOOOO....","....OOOoOOOOO...","....OOooOOOOO...","....OOOOOOOOO...",".....OOOOOOOO...",
           "......OOOOOO....","......wwOO......",".....www........","...www..........","..wwww..........",".ww.ww..........","..ww............"])
add('🥩', ["....rrrrrrr.....","..rrrrrrrrrrr...",".rrRrrrrrrrrrr..","wrrrrrrrRrrrrrw.","wrrrrwwrrrrrrrw.","wrrrrwwrrrrrrw..",
           ".wrrrrrrrrrrrw..","..wwwwwwwwwww..."])
add('🍱', ["DDDDDDDDDDDDDDDD","DwwwwwwDrrrrrrrD","DwwkwwwDrrrrrrrD","DwwwwwwDDDDDDDDD","DwwwwwwDGGGDyyyD","DwwwwwwDGGGDyyyD","DDDDDDDDDDDDDDDD"])
add('🥧', ["...ttttt",".trtrtrt","tttttttt","trtrtrtr","tttttttt","llllllll",".lllllll"])
add('🍰', [".........rr.....","........rrrr....","......wwwwwww...","...wwwwwwwwwww..","wwwwwwwwwwwwww..","eeeeeeeeeeeeeew.",
           "rrrrrrrrrrrrrrw.","eeeeeeeeeeeeeew.","eeeeeeeeeeeeeew."])
add('🎂', ["....o..o","....y..y","....p..p","....p..p",".wwwwwww",".ppppppp",".pwpwpwp","wwwwwwww","pppppppp","pppppppp","llllllll"])
add('🍓', ["...G.GGG","..GGGGGG",".rrrrrrr","rryrrrry","rrrrryrr",".ryrrrrr",".rrrryrr","..rrrrrr","...ryrrr","....rrrr","......rr"])
add('🌽', ["......yy",".....yhy",".....hyh","....Gyhy","...GGhyh","...GGyhy","..GGGhyh","..GGGyhy","..GGGGhh","...GGGGG","....GGGG",".....GGG"])
add('🥤', ["...........ww...","..........ww....",".........ww.....","...llllllllll...","..llllllllllll..","...rrrrrrrrrr...","...rrwrrrrrrr...",
           "....rrrrrrrr....","....rrrrrrrr....","....rrrrrrrr....",".....rrrrrr....."])
add('🥨', ["..mmmm..",".mmmmmmm","mm....mm","mm...mm.","mm..mm..",".mmmm...","..mmm...",".mm.mm..","mm...mmm",".mmmmmmm","..mmmmm."])
add('🥞', ["......yy","......yy",".OOOOOOO","tttttttt","OttttOtt","tttttttt","MMMMMMMM","tttttttt","MMMMMMMM",".lllllll"])
g = blank()
for y in range(1, 15):
    for x in range(1, 15):
        if (x, y) in [(1, 1), (14, 1), (1, 14), (14, 14)]: continue
        g[y][x] = 'O' if x % 3 == 1 or y % 3 == 1 else 'o'
add('🧇', rows_of(g))
add('🌮', [".....GrGGrG.....","...GGMMMMMMGG...","..yyyyyyyyyyyy..",".yyyyhyyyhyyyyy.","yyyyyyyyyyyyyyyy","yyhyyyyyyyhyyyyy",".yyyyyyyyyyyyyy.","...yyyyyyyyyy..."])
add('🍝', ["....yyyy","..yyhyyy",".yyyrrrr","yyhyrrry","yyyyyyhy","llllllll",".lllllll"])
add('🥟', ["......le","....elel","..eeeeee",".eeeeeee","eeeeeeee","eeeeeeee",".eeeeeee","..llllll"])
g = blank()
for y in range(16):
    for x in range(16):
        d = ((x - 7.5) ** 2 + (y - 7.5) ** 2) ** .5
        if 2.3 < d <= 7.2: g[y][x] = 'p' if d < 6.2 and y < 10 else 't'
put(g, [(4, 4), (10, 3), (12, 7), (3, 8), (6, 2), (11, 5)], '*'); put(g, [(5, 3), (9, 4), (12, 5), (4, 7)], '%')
add('🍩', rows_of(g))
add('🍣', ["...oooooooooo...","..oeoooeoooeoo..","..oooooooooooo..","..wwwwwwwwwwww..","..wwwwwwwwwwww..","..wwwwwwwwwwww..","...llllllllll..."])
add('🥚', ["......ee","....eeee","...eeeee","..eweeee","..eeeeee",".eeeeeee",".eeeeeee",".eeeeeee",".eeeeeee","..eeeeee","...eeeee",".....eee"])
# ---------- pet outfits ----------
add('🧢', [".....bbbbb......","...bbbbbbbbb....","..bbbbwbbbbbb...","..bbbbbbbbbbbb..","..BBBBBBBBBBBBBB","..........BBBBBB"])
add('🎩', ["....DDDDDDDD...."] * 6 + ["....rrrrrrrr....","....DDDDDDDD....",".DDDDDDDDDDDDDD.","..DDDDDDDDDDDD.."])
add('🕶', ["DDDDDDDDDDDDDDDD","DkkkkkD..DkkkkkD","DkgkkkD..DkgkkkD",".DkkkD....DkkkD.","..DDD......DDD.."])
add('👑', ["y..y...y","yy.yy.yy","yyyyyyyy","yyryyyby","yyyyyyyy","hhhhhhhh"])
add('🎄', [".......y","......yy","......GG",".....GGG","....GGrG","...GGGGG","....GGGG","...GGbGG","..GGGGGG",".GGyGGGG","GGGGGGGG","......mm","......mm"])
add('💐', ["...rr...pp......","..rrrr.pppp.yy..","..rrrr.pppp.yyy.","...rr.vv.pp.yy..","....vvvv..GG....","....GvvG.GG.....",
           ".....GGGGG......","....bbGGGbb.....","....bbbbbbb.....",".....bbbbb......","......bbb......."])
add('🩰', ["..p........p....","...p......p.....","....p....p......","..pppp...pppp...",".pppppp.pppppp..",".pqqqpp.pqqqpp..",".pppppp.pppppp..","..pppp...pppp..."])
g = disc(7, 'w')
put(g, [(3, 2), (4, 3), (4, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (4, 10), (4, 11), (3, 12)], 'r')
put(g, [(12, 2), (11, 3), (11, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (11, 10), (11, 11), (12, 12)], 'r')
add('⚾', rows_of(g))
g = blank()
for i in range(8): put(g, [(13 - i, 1 + i), (14 - i, 1 + i)], 'l')
put(g, [(4, 7), (5, 8), (6, 9), (7, 10), (8, 11), (3, 6), (9, 12)], 'y')
for i in range(4): put(g, [(5 - i, 10 + i)], 'm')
put(g, [(1, 14), (2, 14), (1, 13)], 'y')
add('🗡', rows_of(g))
add('🥊', ["....rrrrrr......","...rrrrrrrr.....","..rrrrrrrrrr....","..rrwrrrrrrrr...","..rrrrrrrrrrr...","rr.rrrrrrrrrr...",
           "rrrrrrrrrrrrr...",".rrrrrrrrrrr....","...wwwwwwww.....","...wwwwwwww....."])
g = blank(); line(g, 12, 3, 3, 12, 'D'); line(g, 12, 4, 4, 12, 'D'); put(g, [(12, 3), (13, 2), (13, 3), (12, 2)], 'w')
put(g, [(14, 0), (15, 3), (10, 1), (14, 6), (11, 0)], '*')
add('🪄', rows_of(g))
add('🥾', ["...mmmmm........","...mwmwm........","...mmwmm........","...mwmwm........","...mmmmm........","...mmmmmmm......",
           "...mmmmmmmmmm...","...mmmmmmmmmmmm.","..MMMMMMMMMMMMMM","..DDDDDDDDDDDDDD"])
add('👒', [".....eeeeee.....","....eeeeeeee....","....eeeeeeee....","....pppppppprr..","eeeeeeeeeeeeeeee",".eeeeeeeeeeeeee."])
add('🎓', [".......DD.......",".....DDDDDD.....","...DDDDDDDDDD...",".DDDDDDDDDDDDDD.","...DDDDDDDDDD.y.",".....DDDDDD...y.",
           "....DDDDDDDD..y.","....DDDDDDDD.yy.","....DDDDDDDD...."])
add('⛑', ["....rrrr","..rrrrrr",".rrrrrrw","rrrrrrrw","rrrrrwww","rrrrrrrw","rrrrrrrw","RRRRRRRR"])
add('🎃', [".......d","...ooooo",".ooooooo","oooOoooO","oookkooO","ooookooO","oooOoooO","ookkkkkk","oooookko",".ooooooo","...ooooo"])
g = blank(); disc(5, 'p', cy=5.5, g=g); ring(g, 7.5, 5.5, 3.4, 4.3, 'w'); ring(g, 7.5, 5.5, 1.2, 2.2, 'w')
for y in range(11, 16): g[y][7] = 'l'; g[y][8] = 'l'
add('🍭', rows_of(g))
g = blank()
for y in range(16):
    for x in range(16):
        d = ((x - 7.5) ** 2 + (y - 7) ** 2) ** .5
        if d <= 7.2 and y <= 6: g[y][x] = 'v'
for x in range(16):
    if g[6][x] == 'v' and x % 4 in (1, 2): g[6][x] = '.'
for y in range(6, 13): g[y][8] = 'D'
put(g, [(7, 13), (6, 13), (6, 12)], 'D'); put(g, [(5, 2), (4, 3)], 'p')
add('☂', rows_of(g))
add('🟡', rows_of(disc(7, 'y')))
add('🟢', rows_of(disc(7, 'G')))
SQ = ["................"] + [".XXXXXXXXXXXXXX."] * 14
add('🟩', [r.replace('X', 'G') for r in SQ]); add('🟫', [r.replace('X', 'm') for r in SQ])
add('🟨', [r.replace('X', 'y') for r in SQ]); add('⬛', [r.replace('X', 'D') for r in SQ])
add('🛼', ["....pppp........","....pwpp........","....ppwp........","....pwpp........","....pppp........","....pppppppp....",
           "....pppppppppp..","...ppppppppppp..","...llllllllllll.","...yy....yy..yy.","...yy....yy..yy."])
g = disc(7, 'L')
put(g, [(2, 3), (3, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (3, 10), (2, 11)], 'w')
put(g, [(13, 3), (12, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (12, 10), (13, 11)], 'w')
add('🎾', rows_of(g))
add('🧤', ["....bb.bb.bb....","....bb.bb.bb.bb.","....bbBbbBbbBbb.","....bbbbbbbbbbb.","bb..bbbbbbbbbbb.",".bb.bbbbbbbbbbb.",
           "..bbbbbbbbbbbb..","...bbbbbbbbbb...","....BBBBBBBB....","....BBBBBBBB...."])
add('🧣', ["...rrrrrrrrrr...","..rwrrwrrwrrwr..","...rrrrrrrrrr...","........rrr.....","........rwr.....","........rrr.....",
           "........rwr.....","........rrr.....","........r.r....."])
add('🩴', [".....bbbb.......","....bbrbbb......","...bbrbrbbb.....","...brbbbrbb.....","...rbbbbbrb.....","...bbbbbbbb.....",
           "...bbbbbbbb.....","...bbbbbbbb.....","....bbbbbb......","....bbbbbb......",".....bbbb......."])
add('🩳', [".BBBBBBB",".bbbbbbb",".bbbbbbb",".bbbbbb.",".bbbbb..",".bbbbb..",".BBBBB.."])
