# institute_website — Documentation

GitHub Pages website for public Active Inference Institute information.
Source-driven static site: `src/build.mjs` generates the HTML pages from source
data; `scripts/extract_pdf.py` extracts publication content. See root
[`README.md`](../README.md).

## How it works

- `npm run build` → `node src/build.mjs` (regenerates the site HTML).
- `npm run extract` → `python3 scripts/extract_pdf.py /Users/4d/Downloads/AII.pdf`
  (owner-local input path; not portable).
- `npm run check` → syntax-checks `src/build.mjs` and `extract_pdf.py`.
- Requires Node >= 20 (`package.json` `engines`).

## Layout

- `*.html` — generated pages (index, about, programs, learning, projects, ...).
- `src/` — build script(s); `assets/` — site assets; `scripts/` — extraction
  tooling; `atlas/` — atlas content; `sitemap.xml`, `robots.txt`, `404.html`.
