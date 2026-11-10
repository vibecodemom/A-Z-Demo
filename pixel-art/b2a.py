from lib import *
E = {
 'dot': [(5, 5), (5, 6), (10, 5), (10, 6)],
 'big': [(4, 5), (5, 5), (4, 6), (5, 6), (10, 5), (11, 5), (10, 6), (11, 6)],
 'happy': [(4, 6), (5, 5), (6, 6), (9, 6), (10, 5), (11, 6)],
 'closed': [(4, 6), (5, 6), (6, 6), (9, 6), (10, 6), (11, 6)],
 'down': [(4, 6), (5, 7), (6, 7), (9, 7), (10, 7), (11, 6)],
 'squeeze': [(4, 5), (5, 6), (4, 7), (11, 5), (10, 6), (11, 7)],
 'wide': [(4, 4), (5, 4), (4, 5), (5, 5), (4, 6), (5, 6), (10, 4), (11, 4), (10, 5), (11, 5), (10, 6), (11, 6)],
 'crazy': [(4, 5), (5, 5), (4, 6), (5, 6), (10, 4), (11, 4), (12, 4), (10, 5), (12, 5), (10, 6), (11, 6), (12, 6)],
}
B = {
 'angry': [(3, 3), (4, 3), (5, 4), (6, 4), (12, 3), (11, 3), (10, 4), (9, 4)],
 'worry': [(3, 4), (4, 4), (5, 3), (12, 4), (11, 4), (10, 3)],
}
M = {
 'smile': [(5, 10), (6, 11), (7, 11), (8, 11), (9, 11), (10, 10)],
 'small': [(6, 10), (7, 11), (8, 11), (9, 10)],
 'frown': [(5, 11), (6, 10), (7, 10), (8, 10), (9, 10), (10, 11)],
 'sfrown': [(6, 11), (7, 10), (8, 10), (9, 11)],
 'flat': [(5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10)],
 'o': [(7, 10), (8, 10), (7, 11), (8, 11)],
 'wavy': [(5, 11), (6, 10), (7, 11), (8, 10), (9, 11), (10, 10)],
}
GRIN = [(x, 9) for x in range(4, 12)] + [(4, 10), (11, 10), (5, 11), (10, 11), (6, 12), (7, 12), (8, 12), (9, 12)]
GRIN_W = [(x, 10) for x in range(5, 11)]
GRIN_R = [(6, 11), (7, 11), (8, 11), (9, 11)]
GRIM = [(x, 9) for x in range(4, 12)] + [(x, 11) for x in range(4, 12)] + [(4, 10), (11, 10), (6, 10), (8, 10), (10, 10)]
GRIM_W = [(5, 10), (7, 10), (9, 10)]
def F(fill='y', eyes=None, brows=None, mouth=None, extra=()):
    g = disc(7.1, fill)
    if eyes: put(g, E[eyes], 'k')
    if brows: put(g, B[brows], 'k')
    if mouth: put(g, M[mouth], 'k')
    for pts, c in extra: put(g, pts, c)
    return rows_of(g)
add('😠', F(eyes='dot', brows='angry', mouth='frown'))
add('😡', F('r', eyes='dot', brows='angry', mouth='frown'))
add('😢', F(eyes='dot', mouth='frown', extra=[([(4, 8), (4, 9), (3, 10), (4, 10)], 'b')]))
add('😟', F(eyes='dot', brows='worry', mouth='frown'))
add('😤', F(eyes='closed', brows='angry', mouth='sfrown', extra=[([(2, 11), (1, 12), (2, 12), (13, 11), (14, 12), (13, 12)], '&')]))
add('😳', F(eyes='wide', mouth='o', extra=[([(2, 8), (3, 8), (12, 8), (13, 8), (2, 9), (13, 9)], 'p')]))
add('🙁', F(eyes='dot', mouth='sfrown'))
add('🙂', F(eyes='dot', mouth='small'))
add('🤪', F(eyes='crazy', mouth='smile', extra=[([(8, 12), (9, 12), (8, 13)], 'r')]))
add('😫', F(eyes='squeeze', mouth=None, extra=[(GRIN, 'k'), (GRIN_W + GRIN_R, 'R')]))
add('😄', F(eyes='happy', extra=[(GRIN, 'k'), (GRIN_W, 'w'), (GRIN_R, 'r')]))
add('😀', F(eyes='big', extra=[(GRIN, 'k'), (GRIN_W, 'w'), (GRIN_R, 'r')]))
add('😔', F(eyes='down', brows='worry', mouth='sfrown'))
add('😬', F(eyes='dot', extra=[(GRIM, 'k'), (GRIM_W, 'w')]))
add('😌', F(eyes='happy', mouth='small', extra=[([(3, 8), (12, 8)], 'p')]))
add('😐', F(eyes='dot', mouth='flat'))
add('😕', F(eyes='dot', mouth='wavy'))
add('😖', F(eyes='squeeze', extra=[([(4, 11), (5, 10), (6, 11), (7, 10), (8, 11), (9, 10), (10, 11), (11, 10)], 'k'), ([(12, 2), (12, 3), (11, 3), (12, 4), (13, 4)], 'b')]))
add('🥵', F('o', eyes='squeeze', extra=[(GRIN, 'k'), (GRIN_W, 'R'), ([(7, 12), (8, 12), (7, 13), (8, 13)], 'r'), ([(13, 3), (13, 4), (12, 4)], '%')]))
add('🥶', F('b', eyes='wide', extra=[(GRIM, 'k'), (GRIM_W, 'w'), ([(4, 1), (5, 2), (10, 1), (11, 2), (3, 2)], 'c')]))
add('🤗', F(eyes='happy', mouth='smile', extra=[([(1, 10), (2, 10), (1, 11), (2, 11), (3, 11), (2, 12), (13, 10), (14, 10), (12, 11), (13, 11), (14, 11), (13, 12)], 'h')]))
g = disc(4.6, 'y'); put(g, [(6, 6), (9, 6), (6, 9), (7, 10), (8, 10), (9, 9)], 'k')
for (x, y) in [(7, 0), (8, 0), (7, 1), (8, 1), (7, 14), (8, 14), (7, 15), (8, 15), (0, 7), (0, 8), (1, 7), (1, 8), (14, 7), (14, 8), (15, 7), (15, 8),
               (2, 2), (3, 3), (13, 2), (12, 3), (2, 13), (3, 12), (13, 13), (12, 12)]: g[y][x] = 'o'
add('🌞', rows_of(g))
add('🌬', ["....wwwwww......","..wwwwwwwwww....",".wwwwkwwwkwww...","wwwwwwwwwwwwww..","wwwwwwwwwwkkw...","wwwwwwwwwwkkw.&&",
           ".wwwwwwwwwwww...","..wwwwwwwwww..&&","................",".........&&&&&&&"])
# people
HEAD = ["..yyyy..", ".yyyyyy.", ".yyyyyy.", "..yyyy.."]
add('🏃', [".........yyy....","........yyyyy...","........yyyyy...",".........yyy....",".......bbbb.....","......bbbbbyy...",
           "....yybbbbb..y..","...y..bbbb......","......nnnn......",".....nn..nnn....","....nn.....nn...","...nn......n....","..kk.......kk..."])
add('🚶', ["......yyyy......",".....yyyyyy.....",".....yyyyyy.....","......yyyy......","......bbbb......",".....bbbbbb.....",
           ".....ybbbby.....",".....ybbbby.....","......nnnn......",".....nn..nn.....",".....n....n.....","....kk....kk...."])
add('🙌', ["..y.y...",".yyyyy..",".yyyyy..","yyyyyy..",".yyyyy..","..yyyy..","..yyyy..","..bbbb..","..bbbb.."])
add('🤝', ["bb...yyyyy....rr","bbbyyyhyhyyyyrrr","bbbyyyyyyyyyyrrr","bbb.yyhyhyyy.rrr","bb...yyyyyy...rr"])
add('🤲', ["yy......","yyy.....",".yyy....",".yyyyyy.","..yyyyyy","...yyyyy","....yhhy"])
add('🫂', ["..yyy....yyy....",".yyyyy..yyyyy...",".yyyyy..yyyyy...","..yyy....yyy....",".bbbbbbvvvvvvv..","bbbbbbbbbvvvvvv.",
           "bbbbbbvvvvvvvvv.","bbbbbbvvvvvvvvv.",".bbbbbbvvvvvvv.."])
add('👨‍👩‍👧', [".MMM.......mmm..","yyyyy.....myyym.","yyyyy.....myyym.",".yyy...MM..yyy..","bbbbb.yyyy.pppp.",
               "bbbbb.yyyy.pppp.","bbbbb..yy..pppp.","bbbbb.rrrr.pppp.",".n.n..rrrr..n.n.",".n.n..y..y..n.n."])
add('🧑‍🤝‍🧑', ["..yyy......yyy..",".yyyyy....yyyyy.",".yyyyy....yyyyy.","..yyy......yyy..",".bbbbb....vvvvv.","bbbbbbyyyyvvvvvv",
               "b.bbb......vvv.v",".nnnn......nnnn.",".n..n......n..n.",".k..k......k..k."])
add('🗣', ["..ggggg.........",".ggggggg........","ggggggggg..&....","gggggggggg..&...","ggggggggggg..&..","gggggggggg..&...",
           "ggggggggg..&....",".gggggggg.......","..gggggg........","..gggggg........"])
add('✊', ["...yyyyyyy......","..yyhyyhyyy.....","..yyhyyhyyyy....","..yyyyyyyyyy....","..yyhyyyyyyy....","...yyyyyyyy.....",
           "....yyyyyy......","....yyyyyy......","....bbbbbb......","....bbbbbb......"])
add('🖐', ["....yy.yy.yy....","....yy.yy.yy.yy.","....yyhyyhyyhyy.","....yyyyyyyyyyy.","yy..yyyyyyyyyyy.",".yy.yyyyyyyyyyy.",
           "..yyyyyyyyyyyy..","...yyyyyyyyyy...","....yyyyyyyy....",".....yyyyyy....."])
add('✋', ["....yyyyyyy.....","....yhyhyhy.....","....yhyhyhy.....","y...yhyhyhy.....","yy..yyyyyyy.....",".yy.yyyyyyy.....",
           "..yyyyyyyyy.....","...yyyyyyyy.....","....yyyyyy......",".....yyyy......."])
add('👀', [".wwww....wwww...","wwwwww..wwwwww..","wwwkkw..wwwkkw..","wwwkkw..wwwkkw..","wwwwww..wwwwww..",".wwww....wwww..."])
add('👃', [".......yy.......","......yyy.......","......yyy.......",".....yyyy.......",".....yyyy.......","....yyyyyy......",
           "...yyyyyyyy.....","...yyyhyhyyy....","....yyyyyy......"])
add('👅', ["..pppppp",".ppppppq",".ppppppq",".ppppppq",".ppppppp","..pppppp","...ppppp",".....ppp"])
add('👂', [".....yyyy.......","....yyyyyy......","...yyhhhyyy.....","...yhyyyhyy.....","...yhyyyyyy.....","...yyhhyyy......",
           "....yyyhyy......","......yyy.......",".....yyy........",".....yy........."])
add('🙋', ["............y...","......yyyy..y...",".....yyyyyy.y...",".....yyyyyy.y...","......yyyy.y....",".....rrrrrr.....",
           "....yrrrrrr.....","....yrrrrrr.....","......nnnn......","......n..n......",".....kk..kk....."])
add('🙆', ["......yyyy......","....yy....yy....","...y..yyyy..y...","...y.yyyyyy.y...","...y.yyyyyy.y...","....y.yyyy.y....",
           ".....pppppp.....",".....pppppp.....",".....pppppp.....","......nnnn......","......n..n......",".....kk..kk....."])
add('🙇', ["................","...yyyy.........","..yyyyyy........","..yyyyyybbbb....","...yyyybbbbbb...",".....yybbbbbb...",
           "......y..nnnn...","..........nnnn..","..........n..n..",".........kk..kk."])
add('🧑‍🏫', ["dddddddd........","dwwddwwd........","ddddddd...yyyy..","dwwwdddd.yyyyyy.","dddddddd.yyyyyy.","....l.....yyyy..",
               "....l...yvvvvvv.","....l..y.vvvvvv.","....l....vvvvvv.","..........nnnn..","..........n..n..",".........kk..kk."])
add('🧗', ["llllllllllllllll","lllolllllllollll","llllllyyyllllll","llllllyyyylllol","lllllyybbbbllll","llllyllbbbllll",
           "lolllllbbbllllll","llllllnnnnyllll","lllllnnllnnllll","llllnnlllllnlll","llllklllllllkll"])
g = blank(); ring(g, 3.5, 11.5, 2.4, 3.5, 'D'); ring(g, 12, 11.5, 2.4, 3.5, 'D')
for a, b in [((3, 11), (7, 11)), ((7, 11), (12, 11)), ((7, 11), (6, 8)), ((6, 8), (10, 8)), ((10, 8), (12, 11))]: line(g, a[0], a[1], b[0], b[1], 'r')
stamp(g, ["..yyy", ".yyyy", "..yy.", ".bbbb", "bbbby", "nnn.y", ".nn.."], 5, 1)
add('🚴', rows_of(g))
add('🤾', ["........yyy..oo.","........yyy.oooo","........yyy.oooo","........yyy..oo.",".......bbbbyy...","......bbbbb.....",
           ".....ybbbbb.....","....y.bbbb......","......nnnn......",".....nn..nn.....","....nn....nn....","...kk......kk..."])
add('🦸', ["......yyyy......",".....kkkkkk.....",".....yyyyyy.....","......yyyy......","...rrbbbbbbrr...","..rrybbbbbbyrr..",
           "..rry.byyb.yrr..","..rr..bbbb..rr..","..rr..rrrr..rr..","..r...b..b...r..","......b..b......",".....rr..rr....."])
add('🧖', [".....&...&......","......&...&.....",".....wwwwww.....","....wwwwwwww....","....wwwwwwww....","....yyyyyyyy....",
           "....ykkyykky....","....yyyyyyyy....",".....yykkyy.....","......yyyy......","....wwwwwwww....","...wwwwwwwwww..."])
add('🦵', ["...yyyy.........","...yyyy.........","...yyyy.........","...yyyyy........","....yyyy........","....yyyy........",
           "....yyyyy.......",".....yyyy.......",".....yyyy.......",".....yyyyyyy....",".....yyyyyyyy...","......yyyyyyy..."])
