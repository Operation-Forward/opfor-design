# Icons

A representative 32 of the LMS's 122 icons: Material Symbols Rounded (Apache 2.0), 24px grid, filled outlines. These files are drawn in Ink (`#1F2A33`) because an `<img>` cannot take the text colour; in pages, paste the path into an inline `<svg fill="currentColor">` or, in the Angular app, use `<mat-icon svgIcon="name" />` from `public/icons/symbols.svg`. Add new names to `scripts/build-icons.mjs` and run `npm run icons`; never load icons from a CDN at runtime.
