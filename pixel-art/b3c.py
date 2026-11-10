from lib import *
add('🕯', ["........o.......",".......oyo......",".......oyo......","........k.......","......pppp......","......pwpp......","......pwpp......",
           "......pppp......","......pppp......","......pppp......","......pppp......","....llllllll...."])
add('🧩', ["...GGGGG........","...GLGGG........","....GGG.........",".GGGGGGGGGG.....",".GLLGGGGGGG.....",".GLGGGGGGGG.GGG.",
           "...GGGGGGGGGGGGG","...GGGGGGGGGGGGG","...GGGGGGGGGGGdG",".GGGGGGGGGd.GdG.",".GGGGGGGGGd.....",".GGGGGGGGGd.....",
           ".GdddddddddG...."])
add('👍', ["......yy........",".....yyy........",".....yyy........","....yyyy........","bbyyyyyyyyyyy...","bbyyyyyyhyyyyy..",
           "bbyyyyyyyyyyy...","bbyyyyyyhyyyyy..","bbyyyyyyyyyyy...","bbyyyyyyhyyyy...","bb.yyyyyyyyy...."])
g = blank()
for y in range(1, 15):
    for x in range(1, 15): g[y][x] = 'b'
for y in range(4, 12):
    for x in (5, 6, 9, 10): g[y][x] = 'w'
add('⏸', rows_of(g))
add('🏈', ["......mmmm......","....mmmmmmmm....","..mmmmmmmmmmmm..",".mmwmmwmmwmmwmm.","mmmwmwwwwwwmwmmm",".mmwmmwmmwmmwmm.",
           "..mmmmmmmmmmmm..","....mmmmmmmm....","......mmmm......"])
add('🤖', [".......r",".......g","..llllll",".lllllll","gllbblll","gllbblll","glllllll",".llkwkwk",".lllllll","..gggggg"])
# floppy disk (save)
add('💾', ["BBBBBBBBBBBBB...","BBBlllllllBBBB..","BBBlllllllBlBBB.","BBBlllllllBlBBBB","BBBlllllllBBBBBB","BBBBBBBBBBBBBBBB",
           "BBwwwwwwwwwwwwBB","BBwwwwwwwwwwwwBB","BBwbbbbbbbbbbwBB","BBwwwwwwwwwwwwBB","BBwbbbbbbbbbbwBB","BBwwwwwwwwwwwwBB","BBBBBBBBBBBBBBBB"])
# globe (language)
g = disc(7.1, 'b')
land = [(4,3),(5,3),(6,3),(3,4),(4,4),(5,4),(6,4),(7,4),(3,5),(4,5),(5,5),(6,5),(4,6),(5,6),(5,7),(6,7),(6,8),(6,9),(7,9),
        (10,3),(11,3),(10,4),(11,4),(12,4),(9,6),(10,6),(11,6),(12,6),(9,7),(10,7),(11,7),(12,7),(13,7),(10,8),(11,8),(12,8),(11,9),(12,9),(10,11),(11,11),(9,12),(10,12)]
put(g, land, 'G')
add('🌐', rows_of(g))
# trash can (delete)
add('🗑', ["......llll......","..llllllllllll..","..gggggggggggg..","...llllllllll...","...lglglglgll...","...lglglglgll...",
           "...lglglglgll...","...lglglglgll...","...lglglglgll...","...lglglglgll...","...lglglglgll...","....llllllll...."])
# multiplication sign
g = blank()
for i in range(3, 13):
    for d in (0, 1):
        if 0 <= i + d < 16: g[i][i + d] = 'v'; g[i][15 - i - d] = 'v'
add('✖', rows_of(g))
# mountain
add('🏔', [".......w........","......www.......",".....wwgww......","....wwggggg.....","...gggggggggg...","..gggDgggggggg..",
           ".ggggDDgggDggggg","ggggDDDggDDDgggg","gggDDDDDDDDDDggg","ddddddddddddddd."])
# plus and minus (math games)
g = blank()
for i in range(3, 13):
    for d in (7, 8):
        g[i][d] = 'G'; g[d][i] = 'G'
add('➕', rows_of(g))
g = blank()
for i in range(3, 13):
    for d in (7, 8):
        g[d][i] = 'b'
add('➖', rows_of(g))
# globe showing the Americas (Hispanic heritage)
g = disc(7.1, 'b')
put(g, [(x, 2) for x in range(5, 9)] + [(x, 3) for x in range(3, 10)] + [(x, 4) for x in range(3, 10)] + [(12, 4)] +
       [(x, 5) for x in range(4, 9)] + [(x, 6) for x in range(5, 8)] + [(6, 7), (7, 7)] + [(7, 8), (8, 8)] +
       [(x, 9) for x in range(8, 12)] + [(x, 10) for x in range(8, 12)] + [(x, 11) for x in range(9, 11)] + [(9, 12), (10, 12), (9, 13)], 'G')
put(g, [(4, 3), (4, 4), (8, 9), (8, 10)], 'L')
add('🌎', rows_of(g))
# history scroll (Black history)
add('📜', ["...ttttttttttt..","..tettttttttttt.","...ttttttttttt..","....eeeeeeeeee..","....egggggggge..","....eeeeeeeeee..",
           "....egggggggge..","....eeeeeeeeee..","....eggggggeee..","....eeeeeeeeee..","....egggggggge..","....eeeeeeeeee..",
           "...ttttttttttt..","..tettttttttttt.","...ttttttttttt.."])
# microscope (science)
add('🔬', ["...gg...........","...lgg..........","....lgg.........",".....lgg........","......lgg.DD....",".......lggDD....",
           "........lgDD....","........cDDD....","......kkkkDD....","...........DD...","..........DD....","..........DD....",
           ".....DDDDDDDD...","....DDDDDDDDDD.."])
# lipstick (beauty)
add('💄', ["......rr........",".....rrrr.......",".....rrrR.......",".....rrrR.......",".....rrrR.......","....hyyyyh......",
           "....hyyyyh......","....pqqqqq......","....pqqqqq......","....pqqqqq......","....pqqqqq......","....pqqqqq......","....qqqqqq......"])
# light bulb (fun facts)
add('💡', ["......yyyy......","....yyyyyyyy....","...ywwyyyyyyy...","...ywyyyyyyyy...","...yyyyyyyyyy...","...yyyyyyyyyy...",
           "....yyyyyyyy....",".....yyyyyy.....","......hyyh......",".....llllll.....",".....gggggg.....",".....llllll.....","......gggg......"])
# die (surprise me)
add('🎲', ["...wwwwwwwwww...","..wwwwwwwwwwww..","..wwkkwwwwkkww..","..wwkkwwwwkkww..","..wwwwwwwwwwww..","..wwwwwkkwwwww..",
           "..wwwwwkkwwwww..","..wwwwwwwwwwww..","..wwkkwwwwkkww..","..wwkkwwwwkkww..","..wwwwwwwwwwww..","..llllllllllll..","...llllllllll..."])
