# institute_website — Agent Notes

- The `.html` pages at the repo root are BUILD OUTPUTS of `src/build.mjs`;
  regenerate with `npm run build` rather than hand-editing rendered pages.
  Content-source changes go into `src/` (and `assets/`), then rebuild.
- `package.json` declares three scripts only: `build`, `extract`, `check`
  (see `docs/README.md`). There is no test suite or CI config in this repo.
- `scripts/extract_pdf.py` embeds an owner-local input path
  (`/Users/4d/Downloads/AII.pdf`); treat it as a private workflow tool.
- No manuscript/publication track exists here; this is a website repo.
