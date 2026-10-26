# src

The source of truth for the site. `build.mjs` is a dependency-free Node ESM
generator that reads `content/site-data.json` and `content/pdf-pages.json` and
writes every generated file in the repository root and `atlas/`.

Run it with `npm run build`. See [AGENTS.md](AGENTS.md) for the contract and
`content/README.md` for the input data.
