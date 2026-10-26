# assets

Static assets for the generated site: `css/styles.css` (the only stylesheet),
`js/site.js` and `js/atlas.js` (deferred classic scripts), `img/` (PDF page
thumbnails), and `source/AII.pdf` (the committed source document).

Nothing here is compiled — `src/build.mjs` only links to these files. The
`img/` and `source/` contents are produced by `npm run extract`; see
[AGENTS.md](AGENTS.md).
