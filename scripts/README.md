# scripts

Build-time helper scripts for the institute_website static site. The site itself is
plain HTML rendered by `src/build.mjs`; this folder contributes the PDF extraction
step that produces the source-atlas content under `src/content/`.

## Inventory

| Script | Purpose | Delegates to | Run command |
|--------|---------|--------------|-------------|
| `extract_pdf.py` | Splits the Active Inference Institute source PDF into per-page JSON, copies the PDF into `assets/source/`, and renders page thumbnails into `assets/img/` | Self-contained CLI over poppler tools (`pdftotext`, `pdfinfo`, `pdftoppm`); its JSON output is consumed downstream by `src/build.mjs` | `python3 scripts/extract_pdf.py /path/to/AII.pdf` (npm alias: `npm run extract`) |

## Related commands (defined in `package.json`)

- `npm run build` — `node src/build.mjs` renders the root HTML pages and `atlas/` pages from `src/content/*.json`.
- `npm run check` — `node --check src/build.mjs && python3 -m py_compile scripts/extract_pdf.py`.

See [AGENTS.md](AGENTS.md) for the scripts/ contract and gotchas.
