"""Builds the A-Z demo (index.html, the page GitHub Pages shows) from your copy of the A-Z artifact.

    python3 build.py

One way only: it READS private/family-app.html (a copy of the artifact) and WRITES index.html here.
It never changes, uploads or publishes the artifact on claude.ai.

Steps:
  1. Swap out family details with private/make_public.py (kept private because it lists them).
  2. Disconnect the Claude storage code, so the demo only ever saves in the visitor's browser.
  3. Add the pretend family (demo-family.js) and the demo wording.
  4. Stop, without writing anything, if any family detail or Claude storage code is left.

If the artifact's code changed in a spot this script edits, it stops and names the spot.
Then this script needs a small update before the demo can be rebuilt."""
import hashlib, importlib.util, os, sys, time

ROOT = os.path.dirname(os.path.abspath(__file__))
PRIVATE = os.path.join(ROOT, 'private')
SOURCE = os.path.join(PRIVATE, 'family-app.html')
OUT = os.path.join(ROOT, 'index.html')
BLOCKLIST = os.path.join(PRIVATE, 'blocklist.txt')
CLAUDE_CODE = ['window.claude', 'claude.use(']


def fail(msg):
    sys.exit('build.py stopped, nothing was written: ' + msg)


def need(path, what):
    if not os.path.exists(path):
        fail(f'{os.path.relpath(path, ROOT)} is missing ({what}).')


need(SOURCE, 'the copy of the A-Z artifact; ask Claude Code to "copy the A-Z artifact into private/"')
need(os.path.join(PRIVATE, 'make_public.py'), 'the private script that swaps out family details')
need(BLOCKLIST, 'the private list of family details to check for')

spec = importlib.util.spec_from_file_location('make_public', os.path.join(PRIVATE, 'make_public.py'))
make_public = importlib.util.module_from_spec(spec)
spec.loader.exec_module(make_public)

raw = open(SOURCE, encoding='utf-8').read()
print(f'Artifact copy: {len(raw) // 1024} KB, saved {time.strftime("%Y-%m-%d %H:%M", time.localtime(os.path.getmtime(SOURCE)))}, '
      f'fingerprint {hashlib.sha256(raw.encode()).hexdigest()[:12]}')

try:
    s = make_public.scrub(raw, 'demo')
except AssertionError as e:
    fail(f'the family-details swap did not match the artifact ({e}). private/make_public.py needs an update.')


def rep(old, new, where):
    global s
    n = s.count(old)
    if n != 1:
        fail(f'expected one match for {where}, found {n}. The artifact changed here; build.py needs an update.')
    s = s.replace(old, new)


# ---------- 2. Disconnect the Claude storage code ----------
rep("""  let db = null, user = null, assets = null, downloads = null;
  try {
    if (window.claude && typeof window.claude.use === 'function') {
      [db, user, assets, downloads] = await Promise.all(['db', 'user', 'assets', 'downloads'].map(n => window.claude.use(n).catch(() => null)));
    }
  } catch (e) { db = null; }
  S.downloads = downloads;
  if (db && user) {
    let canEdit = true;
    try { canEdit = await user.canEdit(); } catch (e) {}
    if (!canEdit) { S.phase = 'private'; UI.view = 'private'; render(); return; }
  }
  S.store = db ? new CloudStore(db) : new LocalStore();
  S.assets = db ? assets : null;
""", """  /* Demo website: saved only in this browser. Never connects to Claude. */
  S.downloads = null;
  S.store = new LocalStore();
  S.assets = null;
""", 'the start-up code that connects to Claude storage (boot)')
rep("""const onOwnSite = () => !(window.claude && typeof window.claude.use === 'function');""",
    """const onOwnSite = () => true; /* the demo website never runs inside Claude */""",
    'the "running inside Claude?" check (onOwnSite)')

# ---------- 3. Demo: pretend family and demo wording ----------
rep("""    ${whoNudges()}\n    <div class="pickrow">""", """    ${demoBanner()}\n    ${whoNudges()}\n    <div class="pickrow">""", 'the start screen (whoNudges)')
rep("""    ${S.store && S.store.kind === 'local' ? `<p class="note small">${onOwnSite() ? 'Saved on this device only. Grown-ups can save a backup in Settings.' : `Saved on this device only. Open ${esc(appName())} from your Claude account to save across devices.`}</p>` : ''}\n""", "",
    'the start screen "Saved on this device only" note')
rep("""  h += backupNudge();""", """  if (S.store.kind === 'local') h += `<div class="banner">Demo: a pretend family. Everything you change is saved only in this browser.</div>`;""",
    'the grown-up home backup reminder (backupNudge)')
rep("""      : onOwnSite() ? 'Saved on this device only, inside this browser. To move to a new phone or tablet, save a backup here and restore it there.' : 'Saved on this device only. Open the app from your Claude account to keep it in sync across devices.'}</p></div>""",
    """      : 'This demo saves only in this browser on this device. Nothing is sent anywhere, and other people who open the demo get their own copy.'}</p></div>""",
    'the Settings "Where your data is saved" card')
demo_js = open(os.path.join(ROOT, 'demo-family.js'), encoding='utf-8').read().rstrip('\n')
rep("\nboot();\n\n</script>", "\n" + demo_js + "\n\nboot();\n\n</script>", 'the end of the app script (boot)')
rep("</style>\n<div id=\"app\"></div>", ".card.demo { background: var(--star-soft); box-shadow: none; }\n</style>\n<div id=\"app\"></div>", 'the end of the styles')
rep('<div id="app"></div>', '<div id="app"></div><script>window.AZ_LS_KEY = "a-z-demo-data";</script>', 'the app container')
rep('<meta name="claude:viewport-fit-sides" content="cover">',
    '<meta name="description" content="A-Z: picture routines, timers, reminders, rewards and calm-down tools for kids and families. Demo with a pretend family.">',
    'the Claude page setting in the head')

# ---------- 4. Checks ----------
problems = [f'Claude storage code is still in the demo ({c})' for c in CLAUDE_CODE if c in s]
terms = [t.strip() for t in open(BLOCKLIST, encoding='utf-8').read().splitlines() if t.strip() and not t.strip().startswith('#')]
low = s.lower()
problems += [f'a family detail from private/blocklist.txt is in the demo (starts with "{t[:2]}")' for t in terms if t.lower() in low]
for d, dirs, files in os.walk(ROOT):
    dirs[:] = [x for x in dirs if x not in ('.git', 'private', '__pycache__', '.claude')]
    for f in files:
        p = os.path.join(d, f)
        if p == OUT or f.endswith(('.png', '.jpg', '.ico', '.woff2')) or f == '.DS_Store':
            continue
        try:
            text = open(p, encoding='utf-8').read().lower()
        except UnicodeDecodeError:
            continue
        problems += [f'{os.path.relpath(p, ROOT)} has a family detail (starts with "{t[:2]}")' for t in terms if t.lower() in text]
if problems:
    fail('\n  ' + '\n  '.join(problems))

open(OUT, 'w', encoding='utf-8').write(s)
print(f'index.html written, {len(s.encode()) // 1024} KB. Checked: {len(terms)} family details, none found; no Claude storage code.')
