# AGENTS.md — `institute_website/assets/css`

## Scope

- Styling for the generated static site. One stylesheet, no preprocessor and
  no build step.

## Layout

- `styles.css` — all site styles: layout bands, cards, atlas rows, pager, and
  the responsive breakpoints. Linked by `src/build.mjs` from every page.

## Gotchas

- Class names are part of the generator contract: `build.mjs` emits
  `site-header`, `content-band`, `card-grid`, `atlas-row`, `source-grid`,
  `pager`, and similar hooks. Renaming a class requires updating `build.mjs`.
- `site.js` toggles the `data-scrolled` attribute on `.site-header`; style that
  attribute rather than adding scroll listeners.
