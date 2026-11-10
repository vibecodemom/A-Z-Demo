from lib import *
import math
# --- redraws from the review ---
add('💪', ["..yyyy..........",".yyyyyy.........",".yhyhyh.........",".yyyyyy.........","..yyyy....yyy...","..yyyy...yyyyybb",
           "..yyyyh.yyyyyybb","..yyyyyhyyyyyybb","..yyyyyyyyyyyybb","...yyyyyyyyyyybb","....yyyyyyyyyy.."])
add('🤸', [".y............y.","..y....yy....y..","...y..yyyy..y...","....y.yyyy.y....",".....bbbbbb.....","......bbbb......",
           "......bbbb......","......nnnn......",".....nn..nn.....","....nn....nn....","...nn......nn...","..kk........kk.."])
add('🧘', ["......yyyy......",".....yyyyyy.....",".....yyyyyy.....","......yyyy......",".....TTTTTT.....","....TTTTTTTT....",
           "...yTTTTTTTTy...","..y.TTTTTTTT.y..",".yy.TTTTTTTT.yy.","..nnnnnnnnnnnn..",".nnnnnnnnnnnnnn.",".nnnyy....yynnn."])
r = norm(["......yy",".....yyy",".....yyy","....yyyy","....yyyy","....yyyy","...hyyyy","...yyyyy","...yyyyy","....yyyy","...bbbbb","...bbbbb"])
r = [row[:8] + ('h' if 1 <= i <= 9 else row[8]) + row[9:] for i, row in enumerate(r)]
add('🙏', r)
g = blank()
for y in range(2, 12):
    for x in range(1, 11): g[y][x] = 'G'
put(g, [(4, 0), (5, 0), (6, 0), (4, 1), (5, 1), (6, 1)], 'G')
put(g, [(11, 5), (12, 5), (13, 5), (11, 6), (12, 6), (13, 6), (11, 7), (12, 7), (13, 7)], 'G')
put(g, [(4, 11), (5, 11), (6, 11), (4, 10), (5, 10), (6, 10)], '.')
put(g, [(1, 5), (1, 6), (1, 7), (2, 6)], '.')
put(g, [(3, 3), (4, 3), (3, 4)], 'L'); put(g, [(9, 9), (10, 9), (10, 8), (10, 10), (9, 11), (10, 11)], 'd')
add('🧩', rows_of(g))
add('👋', ["....yy.yy.yy....","....yy.yy.yy.yy.","....yyhyyhyyhyy.","....yyyyyyyyyyy.","yy..yyyyyyyyyyy.",".yy.yyyyyyyyyyy.",
           "..yyyyyyyyyyyy..","...yyyyyyyyyy...","....yyyyyyyy....",".....yyyyyy....."])

# --- sun, check, present, chick, calendar, gear, lock, briefcase ---
g = disc(3.9, 'y'); put(g, [(5, 6), (6, 5)], 'w')
for (x, y) in [(7, 0), (8, 0), (7, 1), (8, 1), (7, 14), (8, 14), (7, 15), (8, 15), (0, 7), (0, 8), (1, 7), (1, 8), (14, 7), (14, 8), (15, 7), (15, 8),
               (2, 2), (3, 3), (13, 2), (12, 3), (2, 13), (3, 12), (13, 13), (12, 12)]: g[y][x] = 'o'
add('☀', rows_of(g))
g = blank()
for y in range(1, 15):
    for x in range(1, 15):
        if (x, y) not in [(1, 1), (14, 1), (1, 14), (14, 14)]: g[y][x] = 'G'
for i, (x, y) in enumerate([(3, 7), (4, 8), (5, 9), (6, 10), (7, 9), (8, 8), (9, 7), (10, 6), (11, 5), (12, 4)]):
    put(g, [(x, y), (x, y + 1)], 'w')
add('✅', rows_of(g))
add('🎁', ["..yyy...",".y...y.y","..yyyyyy","rrrrrrry","rrrrrrry","RRRRRRRy",".rrrrrry",".rrrrrry",".rrrrrry",".rrrrrry",".rrrrrry",".RRRRRRy"])
add('🐣', [".....yyy","....yyyy","....ykyy","....yyyo","...yyyyy",".wwyywwy","wwwwwwww","wwlwwwww","wwwwwlww",".wwwwwww","..wwwwww","....wwww"])
add('📅', ["....l......l....",".rrrlrrrrrrlrrr.",".rrrrrrrrrrrrrr.",".wwwwwwwwwwwwww.",".wllwllwllwllww.",".wwwwwwwwwwwwww.",".wllwllwllwllww.",
           ".wwwwwwwwwwwwww.",".wllwllwrrwllww.",".wwwwwwwwwwwwww.",".wllwllwllwllww.",".wwwwwwwwwwwwww."])
g = blank()
for y in range(16):
    for x in range(16):
        dx, dy = x - 7.5, y - 7.5; d = (dx * dx + dy * dy) ** .5; a = math.degrees(math.atan2(dy, dx)) % 45
        if d <= 5.2 or (d <= 7.4 and (a < 12 or a > 33)): g[y][x] = 'l'
        if d <= 2.1: g[y][x] = '.'
add('⚙', rows_of(g))
add('🔒', ["....llll","...ll...","...ll...","...ll...",".yyyyyyy",".ywyyyyy",".yyyyyyk",".yyyyyyk",".yyyyyyy",".hhhhhhh"])
add('💼', ["......MMMM......",".....M....M.....",".mmmmmmmmmmmmmm.",".mmmmmmmmmmmmmm.",".mmmmmmmmmmmmmm.",".MMMMMMyyMMMMMM.",
           ".mmmmmmmmmmmmmm.",".mmmmmmmmmmmmmm.",".mmmmmmmmmmmmmm.",".MMMMMMMMMMMMMM."])
# --- timer buddies ---
add('🐎', ["..........m.m...",".........mmmm...","........Mmkmmm..",".......MMmmmmmmm","......MMmm......","......Mmmm......",
           "M.mmmmmmmm......","MMmmmmmmmmm.....","M.mmmmmmmmm.....","M.mmmmmmmmm.....","..m.m....m.m....","..m.m....m.m....",
           ".MM.MM..MM.MM..."])
g = blank()
for k in range(3):
    line(g, 0 + k * 2, 2 + k * 0, 8, 9 - k * 0, '*' if k == 1 else 'o')
stamp(g, ["...y...", "...y...", "yyyyyyy", ".yyyyy.", "..yyy..", ".yy.yy.", ".y...y."], 8, 7)
add('🌠', rows_of(g))
add('🏎', ["rr.....yy.......","rr....yyyy......",".rrrrrrrrrrrrr..","rrrrwwrrrrrrrrrr","rrrrwwrrrrrrrrrr",".kkk......kkk...",
           "kklkk....kklkk..",".kkk......kkk..."])
add('👾', ["..v.....","...v....","....vvvv","..vvvvvv",".vvvvvvv",".vvwwvvv","vvvwkvvv","vvvvvvvv","vvvvvvvv",".vvvvvvv",".v.vv.vv","v..v..v."])
add('🐉', ["...........y.y..","..........GGGG..",".LL......GGkGG..",".LLL.....GGGGGGG","..LLL...GGGG....","..LLLLLGGGG.....",
           "...LLGGGGGG.....","G...GGGGGGGG....","GG.GGGGGGGGGG...",".GGGGGyyyyGGG...","..GGGGGGGGGG....","....GG...GG.....",
           "...dd...dd......"])
# --- day tags ---
g = blank()
for y in range(16):
    for x in range(16):
        d = ((x - 7.5) ** 2 + (y - 7) ** 2) ** .5
        if d <= 6.6 and y <= 6: g[y][x] = 'r' if int((math.degrees(math.atan2(7 - y, x - 7.5)) + 180) // 30) % 2 else 'w'
for y in range(7, 13): g[y][8] = 'l'
for y in range(12, 15):
    for x in range(16): g[y][x] = 'e'
put(g, [(2, 13), (6, 14), (11, 13), (14, 14)], 't')
add('🏖', rows_of(g))
add('🩺', ["..D........D....","..l........l....","..l........l....","...l......l.....","....l....l......",".....l..l.......",
           "......ll........","......ll........","......ll........",".......ll.......","........lll.....","..........lll...",
           ".........lccl...",".........lccl...","..........ll...."])
add('🤒', over(face(), ["","","","","","...kkk....kkk...","....k......k....","","","","......kkwwwwwwrr","",""]))
g = blank()
for y in range(16):
    for x in range(16):
        # triangle (1,14),(4,6),(9,11)
        def side(ax, ay, bx, by): return (bx - ax) * (y - ay) - (by - ay) * (x - ax)
        s1, s2, s3 = side(1, 14, 4, 6), side(4, 6, 9, 11), side(9, 11, 1, 14)
        if (s1 <= 0 and s2 <= 0 and s3 <= 0) or (s1 >= 0 and s2 >= 0 and s3 >= 0): g[y][x] = 'o' if (x + y) % 4 < 2 else 'y'
put(g, [(9, 3), (12, 2), (14, 5), (11, 6), (7, 1), (13, 8), (10, 0), (15, 2)], '!')
put(g, [(10, 4), (13, 4), (12, 7), (8, 4), (15, 6)], '*'); put(g, [(11, 1), (14, 1), (9, 6), (14, 9)], '%')
add('🎉', rows_of(g))
# --- rewards ---
add('🎬', ["..DDwwDDwwDDww..",".DDwwDDwwDDwwDD.","................",".DDDDDDDDDDDDDD.",".DwwDDwwDDwwDDD.",".DDDDDDDDDDDDDD.",
           ".DDDDDDDDDDDDDD.",".DDllllllllllDD.",".DDDDDDDDDDDDDD.",".DDllllllllDDDD.",".DDDDDDDDDDDDDD."])
add('🃏', ["...wwwwwwwwww...","...wrwwwwwwww...","...wwwwwwwwww...","...wwwrwrwrww...","...wwrrrrrrrw...","...wwwkkkkkww...",
           "...wwwwyyyyww...","...wwwwykyyww...","...wwwwyyyyww...","...wwwwwrwwww...","...wwwwwwwwkw...","...wwwwwwwwww..."])
g = blank()
for y in range(2, 14): g[y][1] = 'l'; g[y][4] = 'l'
for y in (4, 7, 10, 13):
    for x in (2, 3): g[y][x] = 'l'
for x in range(1, 6): g[2][x] = 'r'
for i in range(0, 11):
    x = 5 + i; y = 2 + i
    for t in range(3):
        if 0 <= y + t < 16 and x < 16: g[y + t][x] = 'b'
add('🛝', rows_of(g))
add('🍕', [".ttttttt","tttttttt",".yyyyyyy",".yyrryyy","..yrryyy","..yyyyyy","...yyyyr","...yyyyr","....yyyy","....yyyy",".....yyy",".....yyy","......yy",".......y"])
add('🎟', ["pppppppppppppppp","ppwwwwwppqpppppp","pppppppppppppppp",".pwwwwwpppqpppp.","..pppppppppppp..",".ppppppppqppppp.",
           "pppppppppppppppp","ppwwwwppqppppppp","pppppppppppppppp"])
add('💵', ["dddddddddddddddd","dLLLLLLLLLLLLLLd","dLGLLLLddLLLLGLd","dLLLLLdLLdLLLLLd","dLLLLLdLLdLLLLLd","dLGLLLLddLLLLGLd",
           "dLLLLLLLLLLLLLLd","dddddddddddddddd"])
add('☕', [".....&...&......","....&...&.......",".....&...&......","..wwwwwwwwww....","..wmmmmmmmmw....","..wwwwwwwwwwww..",
           "..wwwwwwwwww..w.","..wwwwwwwwww..w.","..wwwwwwwwwwww..","..wwwwwwwwww....","...wwwwwwww.....",".llllllllllll..."])
add('🛍', ["....qqqq","...q....","...q....",".ppppppp",".ppppppp",".pppwppp",".ppppppp",".ppppppp",".ppppppp",".ppppppp",".ppppppp",".qqqqqqq"])
add('🍿', ["..ww.www",".wwwwwww","wwewwwew",".wwwwwww","rrwwrrww",".rwwrrww",".rwwrrww",".rwwrrww","..wwrrww","..wwrrww","..wwrrww","...wrrww"])
add('🏊', ["....rrr.........","...rrrrr...yy...","...yyyyy..yy....","...ykyky.yy.....","...yyyyyyy......","..c...c...c...c.",
           ".bcb.bcb.bcb.bcb","bbbbbbbbbbbbbbbb","bcbbbcbbbcbbbcbb","bbbbbbbbbbbbbbbb"])
g = blank(); ring(g, 3.5, 10.5, 2.6, 3.7, 'D'); ring(g, 12, 10.5, 2.6, 3.7, 'D'); put(g, [(3, 10), (12, 10)], 'l')
for a, b in [((3, 10), (7, 10)), ((7, 10), (12, 10)), ((7, 10), (6, 6)), ((6, 6), (10, 6)), ((10, 6), (7, 10)), ((10, 6), (12, 10)), ((3, 10), (6, 6))]:
    line(g, a[0], a[1], b[0], b[1], 'r')
put(g, [(10, 5), (11, 4), (12, 4)], 'k'); put(g, [(5, 5), (6, 5), (7, 5)], 'k')
add('🚲', rows_of(g))
g = blank()
stamp(g, ["..ww..", ".wwww.", ".wwww.", "..ww..", ".rrrr.", ".wwww.", "wwwwww", "wwwwww", "wwwwww", "wwwwww", ".wwww.", ".wwww."], 0, 2)
disc(3.4, 'B', cx=11.5, cy=10, g=g); put(g, [(10, 8), (12, 8), (11, 10)], 'k'); put(g, [(10, 11), (9, 10)], 'b')
add('🎳', rows_of(g))
add('🧁', [".......r","......rr","....pppp","...ppppp","..pppppp",".ppqpppp",".ppppqpp","pppppppp",".bcbcbcb",".bcbcbcb","..bcbcbc","..bcbcbc","...bcbcb"])
# --- little UI pictures ---
add('🔔', [".......h","......yy",".....yyy","....yyyy","....yyyy","...wyyyy","...yyyyy","...yyyyy","..yyyyyy",".yyyyyyy","hhhhhhhh",".......o"])
add('🔊', ["......ll........",".....lll...&....","....llll.&..&...","llllllll..&..&..","llllllll..&..&..","llllllll..&..&..",
           "llllllll..&..&..","....llll.&..&...",".....lll...&....","......ll........"])
g = [list(r) for r in norm([".......h","......yy",".....yyy","....yyyy","....yyyy","...wyyyy","...yyyyy","...yyyyy","..yyyyyy",".yyyyyyy","hhhhhhhh",".......o"])]
for i in range(0, 14): put(g, [(1 + i, 1 + i), (2 + i, 1 + i)], 'r')
add('🔕', rows_of(g))
add('📍', [".....rrrr.......","....rrrrrr......","...rrwwrrrr.....","...rwrrrrrr.....","...rrrrrrrr.....","....rrrrrr......",
           ".....rrrr.......","......ll........","......ll........",".......l........",".......l........",".......l........"])
g = blank()
def spark(cx, cy, n):
    for i in range(-n, n + 1): put(g, [(cx + i, cy), (cx, cy + i)], 'y')
    put(g, [(cx - 1, cy - 1), (cx + 1, cy - 1), (cx - 1, cy + 1), (cx + 1, cy + 1)], 'y')
spark(5, 9, 4); spark(12, 3, 2); spark(12, 12, 2)
add('✨', rows_of(g))
add('🏆', ["..yyyyyy","yyyyyyyy","y.yyyyyy","y.ywyyyy",".yyyyyyy","..yyyyyy","...yyyyy",".....yyy","......yy","......yy","....hhhh","...mmmmm","...mmmmm"])
