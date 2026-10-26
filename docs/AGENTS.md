# institute_website — Agent Notes

- The `.html` pages at the repo root are BUILD OUTPUTS of `src/build.mjs`;
  regenerate with `npm run build` rather than hand-editing rendered pages.
  Content-source changes go into `src/` (and `assets/`), then rebuild.
- `package.json` declares three scripts only: `build`, `extract`, `check`
  (see `docs/README.md`). There is no test suite or CI config in this repo.
- `npm run extract` re-runs the PDF pipeline against the committed
  `assets/source/AII.pdf`. It needs poppler on `PATH` and rewrites committed
  content (`src/content/pdf-pages.json`, `assets/img/*.png`), so run it only
  when adopting a new source PDF.
- No manuscript/publication track exists here; this is a website repo.
