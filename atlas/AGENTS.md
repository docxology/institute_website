# AGENTS.md — `institute_website/atlas`

## Scope

- Generated page-by-page coverage of the source PDF. Every HTML file here is
  written by `src/build.mjs`; the directory exists so that no extracted page is
  lost when the curated public pages are refactored.

## Layout

- `index.html` — searchable atlas index (uses `assets/js/atlas.js`).
- `page-NNN.html` — one page per PDF page, with extracted text, optional
  thumbnail, and previous/next pager.

## Gotchas

- Never hand-edit these files: change `src/build.mjs` or the source data and run
  `npm run build`.
- `README.md` in this directory is hand-written documentation and is not
  touched by the generator.
- Page count follows `pdf-pages.json`; a new source edition changes the set of
  files here, so commit the removals and additions together.
