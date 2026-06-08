# Active Inference Institute Website

This repository contains a GitHub Pages website for public Active Inference Institute information.

The site is source-driven:

- `src/content/site-data.json` contains curated public pages and navigation.
- `src/content/pdf-pages.json` is generated from the source PDF and powers the searchable source atlas.
- `src/build.mjs` generates static HTML into the repository root for GitHub Pages.
- `assets/` contains shared CSS, JavaScript, source thumbnails, and the source PDF download.

## Local Workflow

```bash
npm run extract
npm run build
python3 -m http.server 4173
```

Then open `http://127.0.0.1:4173/`.

## GitHub Pages

The workflow in `.github/workflows/pages.yml` deploys the static root on every push to `main`.

## Source Contract

The public pages are refactored from `AII.pdf`. The source atlas keeps page-level coverage so that every extracted PDF page remains discoverable and auditable from the website.
