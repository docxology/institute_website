# AGENTS.md — `institute_website/assets/js`

## Scope

- Browser-side enhancements only. The site is fully readable with JavaScript
  disabled; nothing here generates content.

## Layout

- `site.js` — toggles `data-scrolled` on `.site-header` while scrolling.
  Loaded on every page.
- `atlas.js` — client-side search and section filter for the atlas index.
  Loaded only on `atlas/index.html`, and only useful there.

## Gotchas

- Both files are classic scripts (`<script defer>`), not ES modules; they are
  not bundled and share no imports.
- `atlas.js` reads `data-search` and `data-section` attributes emitted by
  `build.mjs`; changing those attribute names breaks filtering silently.
- `atlas.js` runs its filter once on load to sync the visible count.
