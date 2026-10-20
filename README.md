<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="brand/svg/logo-horizontal-reversed.svg">
    <img src="brand/svg/logo-horizontal.svg" alt="Operation Forward" width="420">
  </picture>
</p>

# Operation Forward design

The charity's brand and design system in one place: use it for the learning platform, the website,
emails, certificates, slides and print.

| Folder | What it is |
|---|---|
| [`brand/`](brand/) | The logo kit: horizontal, stacked and mark-only logos in colour, reversed, ink and white (SVG + PNG), app icons, favicon and social card, with the [brand guide](brand/README.md) (colours, clear space, minimum sizes, misuse). |
| [`design-system/`](design-system/) | Tokens, fonts, icons and 13 UI components taken from the Operation Forward Learning frontend. Start with the [brand book](design-system/system/README.md). |

**Live previews:** https://operation-forward.github.io/opfor-design/

## Use it in a page

```html
<link rel="stylesheet" href="design-system/dist/tokens.css">
<link rel="stylesheet" href="design-system/system/components/bundle.css">
```

`tokens.css` follows the device's light or dark setting; `data-theme="light"` or `"dark"` on
`<html>` forces one. Each component's `README.md` shows its markup.

## Colours

| | Light backgrounds | Dark backgrounds |
|---|---|---|
| First chevron | Forward Teal `#1F5E5B` | Light Teal `#7FC6BF` |
| Second chevron | Forward Clay `#B4532A` | Light Clay `#E58E6C` |
| Name and text | Ink `#1F2A33` | Bone `#ECE7E0` |

Preferred light background: Paper `#FBF8F3`.

## Licences

The Operation Forward name and logo are the charity's; use them only to refer to Operation Forward.
Third-party parts keep their own licences: Fraunces, Atkinson Hyperlegible Next and Atkinson
Hyperlegible Mono are under the SIL Open Font License 1.1 (texts in
[`design-system/system/fonts/`](design-system/system/fonts/)); the icons are Material Symbols
(Apache 2.0).
