# AGENTS.md — `institute_website/assets/img`

## Scope

- Rendered previews of selected source PDF pages. All files here are generated;
  none are hand-authored.

## Layout

- `source-page-NNN.png` — one render per entry in `THUMBNAIL_PAGES` in
  `scripts/extract_pdf.py` (currently pages 1, 4, 12, 22, 58, 87, 121, 167,
  205), produced by `pdftoppm -png -singlefile -r 120`.

## Gotchas

- `src/build.mjs` links a thumbnail only when the file exists, so adding a new
  page number to `THUMBNAIL_PAGES` requires re-running `npm run extract`.
- The home page hardcodes `source-page-001/004/058/167.png` in `build.mjs`;
  those files must stay present or the hero art breaks.
