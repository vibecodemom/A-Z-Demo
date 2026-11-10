import sys, importlib
from PIL import Image, ImageDraw
import lib, sheet
for m in sys.argv[2].split(','): importlib.import_module(m)
keys = sys.argv[3].split(',')
sc = 5; cell = 18 * sc
im = Image.new('RGB', (len(keys) * (cell + 10) + 10, cell + 20), (247, 248, 252))
for i, k in enumerate(keys):
    ic = sheet.icon(lib.ART[k.replace('️', '')]).resize((cell, cell), Image.NEAREST); im.paste(ic, (10 + i * (cell + 10), 10), ic)
im.save(sys.argv[1])
