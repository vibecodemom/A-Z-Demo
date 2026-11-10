from lib import *
import art as _s
for k, v in _s.ART.items(): add(k, v)

add('🐼', [".kkk....","kkkkwwww","kkwwwwww",".wwwwwww","wwkkkwww","wkkwkwww","wkkkkwww","wwkkwwww",
           "wwwwwwwk",".wwwwwwk","..wwwwkw","...wwwww",".....www"])
add('🐯', [".oo.....","opoooook","ooooookk","kooooooo","okookooo","ooookooo","kooooooo","oooowwww",
           ".koowwwk","..oowwkw","...owwww",".....www"])
add('🦁', ["...OOOOO",".OOOOOOO","OOOooooo","OOoooooo","OOookooo","OOookooo","OOoooooo","OOoooeee",
           ".OOooeek","..OOoeke","...OOeee","....OOOO"])
add('🐸', ["..www...",".wwkkw..",".wwkkwGG","GGwwwGGG","GGGGGGGG","GGGGGGGG","GpGGGGGG","GGkGGGGG",
           ".GGkkkkk","..GGGGGG","...ddddd"])
add('🐵', ["...mmmmm",".mmmmmmm","tmmeeemm","tmeekeee","tmeekeee",".meeeeee",".meeeeke","..meeeee",
           "..meekkk","...meeee","....mmmm"])
add('🦄', [".......y",".......o",".p.....y",".ppwwwwy","pwwwwwww","pwwkwwww","wwwkwwww","wpwwwwww",
           "wwwwwwww",".wwppppp","..wpkppp","...ppppp"])
add('🐲', [".y......",".yG.....","..GGGGGG",".GGGGGGG","GGyykGGG","GGGGGGGG","GGGGLLLL",".GGLLLLL",
           ".GLLkLLL","..LLLLLL","..dkkkkk","...LwLwL"])
add('🦖', ["........GGGGGG..",".......GGGkGGGG.",".......GGGGGGGGG",".......GGGGkkkkk",".......GGGGwGwG.",
           "......GGGGGGG...","G....GGGGGG.....","GG..GGGGGGGGG...",".GGGGGGGGGG.G...","..GGGGGGGGG.....",
           "...GGLLLLG......","....GGG.GG......","....GG..GG......","...ddd.ddd......"])
add('🐙', ["...ppppp",".ppppppp",".ppwpppp","pppppppp","pppkpppp","pppkpppp","pppppppp",".ppppppp",
           "pppppppp","p.pp.pp.","p.p..p..",".p..p..."])
add('🦋', [".....k..",".bb...k.","bbbbb..k","bwbbbb.k","bbbbbbbk","bbbBbbbk",".bbbbbbk","..bbbbbk",
           "..vvvvvk",".vvvvvvk",".vvpvvvk","..vvv..k"])
add('🐝', ["......ww.ww.....",".....wccwccw....",".....wccwccw....","......ww.ww.....","...yyykkyykky...",
           "..yyyykkyykkyy..","..ykyykkyykkyyk.","..yyyykkyykkyy..","...yyykkyykky..."])
g = disc(7.2, 'w')
put(g, [(6,6),(7,6),(8,6),(9,6),(6,7),(7,7),(8,7),(9,7),(7,8),(8,8),(7,5),(8,5)], 'k')
put(g, [(7,1),(8,1),(6,1),(9,1),(7,2),(8,2)], 'k')
put(g, [(1,6),(1,7),(2,7),(1,8),(2,6)], 'k'); put(g, [(14,6),(14,7),(13,7),(14,8),(13,6)], 'k')
put(g, [(4,12),(5,12),(4,13),(5,13),(3,12)], 'k'); put(g, [(11,12),(10,12),(11,13),(10,13),(12,12)], 'k')
put(g, [(4,4),(5,3)], 'l'); add('⚽', rows_of(g))
g = blank()
for y in range(16):
    for x in range(16):
        d = ((x - 7.5) ** 2 + (y - 13) ** 2) ** .5
        if y <= 12:
            for rr, c in [(8, 'r'), (7, 'o'), (6, 'y'), (5, 'G'), (4, 'b'), (3, 'v')]:
                if rr - 1 < d <= rr: g[y][x] = c
put(g, [(0,12),(1,12),(2,12),(1,11),(2,11),(3,12),(0,13),(1,13),(2,13),(3,13),(4,13)], 'w')
put(g, [(12,12),(13,12),(14,12),(13,11),(14,11),(15,12),(11,13),(12,13),(13,13),(14,13),(15,13)], 'w')
add('🌈', rows_of(g))
add('🎨', ["................",".....eeeeee.....","...eeeeeeeeee...","..eerreeyyeeee..",".eeerreeyyeeGGe.",
           ".eeeeeeeeeeeGGe.","eebbeeee..eeeeee","eebbeeee..eeee..",".eeeeeeeeeeee...",".eevveeeeeeee...",
           "..evveeeeeee....","...eeeeeee......"])
add('🎸', ["..............MM",".............MM.","............M...","...........M....","..........M.....",
           ".....rr..M......","....rrrrM.......","...rrrrMrr......","..rrrrkkrr......",".rrrrkkrrr......",
           ".rrrrrrrrr......","rrrrrrrrrr......","rrrwrrrrr.......",".rrrrrrr........","..rrrr.........."])
add('🐬', ["........b.......",".......bb.......",".....bbbbbb.....","...bbbbbbbbbb...","..bkbbbbbbbbbb..",
           "bbbbbbbbbbbbbbb.",".cccbbbbbbbbbbbb","...ccccbbbbbbbbb","......cccbbbb.bb",".........bbb..bb",
           "..............b."])
add('🦉', [".m......",".mm.mmmm",".mmmmmmm","mmmwwmmm","mwwwwwmm","mwwkkwmm","mwwkkwmo","mmwwwmmo",
           "mmmmmmmm","mmmeeeee",".mmeeeee",".mmeMeeM","..mmeeee","...oo..."])
add('🚗', [".....rrrrrr.....","....rccrrccr....","...rcccrrcccr...",".rrrrrrrrrrrrrr.","rrrrrrrrrrrrrryy",
           "rrrrrrrrrrrrrrrr","RRkkkkRRRRkkkkRR","..kllk....kllk..","...kk......kk..."])
add('🐱', [".g......",".gg.....",".gpg....",".gppgggg","gggggggg","gggGkggg","gggGkggg","gggggggp",
           "gggggkgk","..gggggg","....gggg"])
add('🎈', ["....rrrr","..rrrrrr",".rrwwrrr",".rwwrrrr","rrwrrrrr","rrrrrrrr","rrrrrrrr",".rrrrrrr",
           ".rrrrrrr","..rrrrrr","....rrrr",".......r","........l.......",".......l........","........l......."])
add('🐟', ["......bbb.......","....bbbbbbb...bb","...bbbbbbbbb.bbb","..bkbbbBbbbbbbb.",".bbbbbBbbbbbbb..",
           "..cccccccbbbbbb.","...ccccccbb.bbb","....bbbbbbb...bb","......bbb......."])
add('🌻', ["....y.yy","..yyyyyy",".yyymmmm","..yymMmM",".yyymmmm","..yyyyyy","....y.yy",".......d",
           "...GG..d","..GGGGdd","...GGG.d",".......d",".......d"])
add('🍦', [".......w","......ww","....wwww","...lllll","..wwwwww","..wwwwww",".lllllll",".wwwwwww",
           "..tttttt","..tmtttm","...ttmtt","...tttmt","....tttt",".....ttt","......tt",".......t"])
