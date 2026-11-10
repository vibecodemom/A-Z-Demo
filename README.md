# A-Z

A calm routine, feelings and rewards app for kids, made for families with ADHD and autism in mind.

**Try the demo:** https://vibecodemom.github.io/A-Z-Demo/

The demo has a pretend family, Maya and Leo, so you can look around and see the features working without typing anything in. Tap Maya (code 1 1 1 1) or Leo (code 🍎 🐶 ⭐ 🚗). The grown-up passcode is 1 2 3 4. Everything you change stays in your own browser, and **Reset demo** puts the pretend family back.

## How this repo works

The A-Z app is made and changed in Claude, as a claude.ai artifact. This repo only builds the public demo from a copy of it. It works one way: nothing in this repo changes the app in Claude.

```
A-Z app in Claude  →  read-only copy in private/  →  python3 build.py  →  index.html (the demo)  →  GitHub Pages
```

Changes to the app don't reach GitHub by themselves. After changing the app, update the demo (see below).

| File or folder | What it is |
|---|---|
| `index.html` | The demo that GitHub Pages shows. Made by `build.py`, so don't edit it by hand. |
| `build.py` | Makes `index.html` from the copy of the app. It swaps out family details, disconnects the Claude storage code, adds the pretend family, and stops without writing anything if a family detail is left. |
| `demo-family.js` | The pretend family (Maya and Leo) and the demo welcome card. |
| `app-files/` | Icons, home-screen settings and the offline file for the full app. The full app (empty, for real families) isn't published yet. |
| `pixel-art/` | The 16x16 pixel pictures, drawn in Python. `python3 pixel-art/export_all.py` writes `pixel-art/pixel-art.js`, which replaces the "A-Z pixel pictures" section of the app in Claude. |
| `translations/` | Spanish words and phrases. `python3 translations/build_es.py` writes `translations/es.js`, which replaces the Spanish section of the app in Claude. |
| `reminder-service/` | The small service that will send phone notifications when the app is closed. Not set up yet. |
| `private/` | **Never on GitHub** (`.gitignore` keeps it off). The copy of the app (`family-app.html`), the script that swaps out family details, and the list of details to check for. |

## Updating the demo after the app changes

In Claude Code, in this folder, say: **"Update the demo from the A-Z artifact."** Claude reads a fresh copy of the app (read only), runs `python3 build.py`, checks the result, and asks before pushing to GitHub.

To do it by hand: save the app's page as `private/family-app.html`, run `python3 build.py`, then commit and push. GitHub Pages updates about a minute later.

If `build.py` stops and says the app changed in a spot it edits, the script needs a small update before the demo can be rebuilt. Nothing is written until every check passes.

## Privacy rule

Nothing with the children's names, our ZIP code or city goes anywhere outside `private/`. `build.py` swaps those details out and checks every file headed for GitHub against `private/blocklist.txt`. It stops if any are found.
