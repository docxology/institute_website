# AGENTS.md — `institute_website/scripts`

> Status: verified 2026-09-06 (scripts remediation pass).

## Scope

Build-time helper scripts for the static GitHub Pages site. Page rendering lives in
`src/build.mjs`; browser code lives in `assets/js/`. Nothing in `scripts/` runs at
page load — these are offline content-pipeline entrypoints only.

## Thin-orchestrator contract

- `scripts/` holds CLI entrypoints ONLY: argument parsing, path bootstrap, logging,
  and a single delegated call into importable logic under `src/<pkg>/`.
- Business/data/analysis logic must live in `src/` (importable and tested there),
  not in `scripts/`.
- Current state: `extract_pdf.py` predates this contract. It is a single-file tool —
  its extraction logic (text cleaning, section ranges, summaries) is inline rather
  than delegated, because `src/` holds the Node build (`build.mjs`) and no Python
  package to receive it. Do not add new logic here; new Python logic goes under
  `src/` and scripts/ calls into it.

## Inventory

| Script | Inputs | Outputs |
|--------|--------|---------|
| `extract_pdf.py` | Source PDF path (`argv[1]`); poppler `pdftotext`/`pdfinfo`/`pdftoppm` on PATH | `src/content/pdf-pages.json`, `assets/source/AII.pdf`, `assets/img/source-page-*.png` |

## Gotchas

- No flag parsing: `extract_pdf.py` requires exactly one positional PDF path; a wrong
  argument count or missing file exits 2 with a usage line (there is no `--help`).
- `npm run extract` passes the committed `assets/source/AII.pdf`. The script
  skips its copy step when the input already is that file, so a default run
  leaves `assets/source/AII.pdf` untouched.
- Poppler utilities (`pdftotext`, `pdfinfo`, `pdftoppm`) must be on PATH (Homebrew on
  this machine).
- `SECTION_RANGES` and `THUMBNAIL_PAGES` in `extract_pdf.py` are page-number maps tied
  to the current PDF edition; a new source edition requires re-checking both.
- Outputs are committed artifacts: rerunning extraction rewrites the 400+ KB
  `src/content/pdf-pages.json` and the `assets/img/source-page-*.png` thumbnails,
  and copies the input PDF over `assets/source/AII.pdf` unless it already is that
  file. Only rerun when adopting a new source edition; commit the results
  deliberately.
- `npm run check` compiles this script (`python3 -m py_compile`), which creates a
  gitignored `scripts/__pycache__/`; never commit it.
