# Notes for Claude working in this repo

## The A-Z app in Claude must never be changed from here
- The A-Z app is a claude.ai artifact owned by the user. That artifact is the only place the app itself is changed.
- **Never publish, update, republish or delete that artifact (or any claude.ai artifact) from this repo, and never write to its data.** Reading it is fine. The artifact's link is in `private/ARTIFACT.txt` (kept off GitHub).
- This repo is one way, downstream only: artifact → `private/family-app.html` → `python3 build.py` → `index.html` (the demo) → GitHub Pages for `vibecodemom/A-Z-Demo`.

## "Update the demo from the artifact"
1. Read the artifact's page with the Artifact tool (`action: "read"`, `path: "index.html"`), saving it into `private/`, then move it to `private/family-app.html`.
2. Run `python3 build.py`. It stops and writes nothing if a family detail or Claude storage code is left, or if the artifact changed in a spot it edits. In that last case, make the smallest matching update to `build.py` (or to `private/make_public.py` for the family-details swaps).
3. Review `git diff index.html`, check the demo in the browser (Maya's code is 1 1 1 1; the grown-up passcode is 1 2 3 4), then commit.
4. Ask the user before pushing. The repo and its GitHub Pages site are public.

## What is published
- Only the demo (`index.html`). The full app for real families is intentionally not published right now. Don't add it unless the user asks.
- `.nojekyll` makes GitHub Pages serve files as they are.

## Privacy
- No children's names, ZIP code, city, or the user's real name or email in any tracked file, commit message or git author. `private/` is gitignored; `build.py` checks against `private/blocklist.txt`.
- Commits use the author name "A-Z" with the vibecodemom GitHub no-reply email (already set in this repo's git config).
