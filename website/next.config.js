/** @type {import('next').NextConfig} */

// Hosted on GitHub Pages at https://t3dy.github.io/FugueJukebox/, which serves
// plain files from a repo subpath — hence the static export, the basePath, and
// the unoptimized images (the Next image optimizer needs a server).
// Local `next dev` keeps the root path and normal behaviour.
const onPages = process.env.GITHUB_PAGES === 'true'

const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  output: 'export',
  basePath: onPages ? '/FugueJukebox' : '',
  assetPrefix: onPages ? '/FugueJukebox/' : '',
  images: {
    unoptimized: true,
  },
  // Pages has no rewrite layer, so /emblem/1 must resolve to
  // /emblem/1/index.html.
  trailingSlash: true,
}

module.exports = nextConfig
