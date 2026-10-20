# Operation Forward

The charity's design system, taken from the Operation Forward Learning frontend (`Operation-Forward/opfor-lms-frontend@8ac8485`) and the logo kit: Paper and Ink, Forward Clay and Forward Teal, Fraunces headings, Atkinson Hyperlegible for reading, soft 16px cards. Use it for the learning platform, the website, emails, certificates, slides and print.

- Brand book: [`system/README.md`](system/README.md)
- Tokens: [`system/tokens.json`](system/tokens.json) → [`dist/tokens.css`](dist/tokens.css) (the same `--lms-*` names the LMS uses)
- Logos and icons: [`system/assets/`](system/assets/)
- Components (13): [`system/components/`](system/components/); open [`previews/index.html`](previews/index.html) through a web server
- Live previews: https://operation-forward.github.io/opfor-design/design-system/previews/

```html
<link rel="stylesheet" href="dist/tokens.css">
<link rel="stylesheet" href="system/components/bundle.css">
```

The Angular app keeps its own theme (`src/styles/_theme.scss`) and Material components; this folder is for everything built without Angular.
