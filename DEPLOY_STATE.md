# DEPLOY_STATE — FUGUEJUKEBOX

## Canonical production URL

**https://t3dy.github.io/FugueJukebox/**

## Host

GitHub Pages, served from `t3dy/FugueJukebox` via `.github/workflows/deploy.yml`
(Actions → Pages artifact, not a `gh-pages` branch). Every push to `main` runs
`npm ci` and `npm run build` inside `website/`, then publishes `website/out/`.

## Repo layout

- `website/` — the Next.js site. This is what gets deployed.
- `music/` — the render pipeline (Python, variation generation). Not part of
  the site and not built by the workflow.

## Migrated off Vercel — 2026-09-06

`fuguejukebox.vercel.app` is **gone**. The Vercel project was deleted to cut
deployment storage. The site had no API routes or server rendering, so it moves
to a Next.js static export unchanged.

## Gotchas

- **Base path.** Pages serves this under `/FugueJukebox`, so `next.config.js`
  sets `basePath` and `assetPrefix` only when `GITHUB_PAGES=true`. Building
  without that env var and uploading the result 404s every asset.
- **`/emblem/[id]` needs `generateStaticParams`.** Under `output: 'export'`
  Next has to be told which 50 pages to write. The view holds playback state so
  it must stay a client component, and a client component cannot export
  `generateStaticParams` — hence the split: `page.tsx` is a server shell that
  enumerates the ids, `EmblemView.tsx` is the client view. Adding an emblem to
  `data/emblems.json` is enough; the shell reads the same file.
- `trailingSlash: true` so `/emblem/1` resolves to `/emblem/1/index.html`,
  which is all Pages can serve.
- **Working copy.** `C:\Dev\FUGUEJUKEBOX-website` is an *unlinked* copy of
  `website/` with no git remote. Edit this repo, not that folder.
