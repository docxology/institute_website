# AGENTS.md — `institute_website/assets/source`

## Scope

- Holds the committed source document that the site is built from and offers
  for download. It is both pipeline input and published asset.

## Layout

- `AII.pdf` — the Active Inference Institute source PDF, 211 pages. Read by
  `scripts/extract_pdf.py`, downloaded via the footer and atlas "Source PDF"
  links, and referenced as `siteData.site.sourcePdf` in `build.mjs`.

## Gotchas

- `extract_pdf.py` copies its input PDF here unless the input already is this
  file, so `npm run extract` with no argument leaves it untouched.
- Adopting a new edition means replacing this file and re-running
  `npm run extract`; `SECTION_RANGES` and `THUMBNAIL_PAGES` in the script are
  page-number maps tied to the current edition.
