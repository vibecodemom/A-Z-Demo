"""Makes translations/es.js, the Spanish words and phrases, from es1.py to es5.py and es_rx.js.
Run from the repo folder:  python3 translations/build_es.py
The A-Z artifact on claude.ai is where the app is changed: es.js replaces the Spanish section
(from "const ES = " up to the pixel pictures) there. This repo never changes the artifact itself."""
import json, sys, os
here =os.path.dirname(os.path.abspath(__file__)); os.chdir(here); sys.path.insert(0, here)
from es1 import ES1; from es2 import ES2; from es3 import ES3; from es4 import ES4; from es5 import ES5
ES = {}
for d in (ES1, ES2, ES3, ES4, ES5):
    for k, v in d.items(): ES[k.strip()] = v
extra = {
 "Calm-down finished": "Calma terminada",
 "Grown-up Dino": "Dino grande", "Kid Dino": "Dino niño", "Baby Dino": "Dino bebé",
 "Kids · Numbers code": "Niños · código de números",
}
ES.update(extra)
js = 'const ES = ' + json.dumps(ES, ensure_ascii=False, indent=0) + ';\n' + open('es_rx.js', encoding='utf-8').read()
js += "\nconst BIBLE_ES = { John: 'Juan', Peter: 'Pedro', Thessalonians: 'Tesalonicenses', Timothy: 'Timoteo', Colossians: 'Colosenses', Ephesians: 'Efesios', Galatians: 'Gálatas', Isaiah: 'Isaías', James: 'Santiago', Joshua: 'Josué', Lamentations: 'Lamentaciones', Matthew: 'Mateo', Philippians: 'Filipenses', Proverbs: 'Proverbios', Psalm: 'Salmo', Romans: 'Romanos' };\nES_RX.push([/^([12] )?(John|Peter|Thessalonians|Timothy|Colossians|Ephesians|Galatians|Isaiah|James|Joshua|Lamentations|Matthew|Philippians|Proverbs|Psalm|Romans) (\\d+:[\\d-]+)$/, (m, n, b, v) => `${n || ''}${BIBLE_ES[b]} ${v}`], [/^Today's devotional$/, 'Devocional de hoy']);\n"
js += "\nES_RX.push([/^Checked in: (\\S+) (.+)$/u, (m, e, a) => `Registró: ${e} ${tIn(a)}`], [/^used (.+)$/, (m, a) => `usó ${tIn(a)}`]);\n"
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'es.js')
open(out, 'w', encoding='utf-8').write(js)
print('ES entries', len(ES), '->', os.path.relpath(out))
