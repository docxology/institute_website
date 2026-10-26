# Active Inference Institute Website

This repository contains a GitHub Pages website for public Active Inference Institute information.

The site is source-driven:

- `src/content/site-data.json` contains curated public pages and navigation.
- `src/content/pdf-pages.json` is generated from the source PDF and powers the searchable source atlas.
- `src/build.mjs` generates static HTML into the repository root for GitHub Pages.
- `assets/` contains shared CSS, JavaScript, source thumbnails, and the source PDF download.

## Local Workflow

Requires Node >= 22 (`package.json` `engines`).

```bash
npm run build
npm run check
python3 -m http.server 4173
```

Then open `http://127.0.0.1:4173/`.

`npm run extract` re-runs the PDF pipeline (`scripts/extract_pdf.py`) against the
committed `assets/source/AII.pdf`. It needs poppler (`pdftotext`, `pdfinfo`,
`pdftoppm`) on `PATH`, and it rewrites the committed `src/content/pdf-pages.json`
and `assets/img/source-page-*.png`, so run it only when adopting a new source PDF.

## GitHub Pages

There is no CI workflow: GitHub Pages serves the repository root of `main`
directly, with `.nojekyll` disabling Jekyll processing. The site is published at
<https://docxology.github.io/institute_website/>.

## Source Contract

The public pages are refactored from `AII.pdf`. The source atlas keeps page-level coverage so that every extracted PDF page remains discoverable and auditable from the website.
