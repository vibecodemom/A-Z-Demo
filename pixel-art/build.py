import importlib, sys
import lib
mods = sys.argv[1].split(',')
for m in mods: importlib.import_module(m)
print(len(lib.ART), 'icons')
