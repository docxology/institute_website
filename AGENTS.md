# AGENTS.md — `institute_website`

## Scope

- Repository `docxology/institute_website`, default branch `main`; a GitHub
  Pages site for public Active Inference Institute information.
- Published at <https://docxology.github.io/institute_website/>. GitHub Pages
  serves the repository root of `main` directly — there is no CI workflow.
- Unlike the `projects/*` local-only areas, this checkout is committed and
  pushed to `origin`.

## Layout

- `src/build.mjs` — the static generator; writes every root `*.html`,
  `atlas/*.html`, `robots.txt`, `sitemap.xml`, and `404.html`.
- `src/content/` — `site-data.json` (hand-curated pages/nav) and
  `pdf-pages.json` (generated from the source PDF).
- `scripts/extract_pdf.py` — PDF → JSON + thumbnail pipeline (poppler).
- `assets/` — CSS, JS, thumbnails, and the committed source PDF.
- `atlas/` — generated page-by-page source atlas.
- `docs/` — repo documentation; `docs/manuscript/` is a template placeholder.

## Gotchas

- Root `*.html` and `atlas/*.html` are build outputs: change `src/` and run
  `npm run build`; never hand-edit rendered pages.
- `npm run build` rewrites every generated file — check `git diff --name-only`
  afterwards to confirm the change stayed scoped.
- `npm run extract` rewrites committed content and needs poppler on `PATH`.
- No test suite exists; `npm run check` is the only automated gate.
