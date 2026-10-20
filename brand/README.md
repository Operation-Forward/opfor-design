# Operation Forward logo

The charity's logo: two forward chevrons (teal and clay) and the name set in Fraunces. It started as
the Operation Forward Learning header mark and is now the organization's logo. All text is converted
to outlines, so no font is needed to use these files.

## Files

| File | Use |
|---|---|
| `svg/logo-horizontal.svg` (+ `png/logo-horizontal-1200.png`, `-600.png`) | Default logo on light backgrounds: websites, documents, email signatures |
| `svg/logo-horizontal-reversed.svg` | Same, on dark backgrounds |
| `svg/logo-horizontal-ink.svg` / `-white.svg` | One-colour printing, stamps, embroidery, overlays on photos |
| `svg/logo-stacked.svg` / `-reversed.svg` | Square-ish spaces: event banners, social posts, merchandise |
| `svg/mark.svg` / `-reversed.svg` / `-ink.svg` / `-white.svg` | The arrows alone, when the name is already nearby or space is tight |
| `svg/app-icon.svg`, `png/app-icon-{16…1024}.png`, `favicon.ico` | Profile pictures, app and browser icons (180 = Apple touch icon, 192/512 = web app) |
| `png/social-card-1200x630.png` | Link previews (Open Graph / social sharing) |

Prefer the SVGs; use PNGs where a tool cannot take SVG.

## Colours

| Name | Hex | RGB | Where |
|---|---|---|---|
| Forward Teal | `#1F5E5B` | 31, 94, 91 | First chevron, light backgrounds |
| Forward Clay | `#B4532A` | 180, 83, 42 | Second chevron, light backgrounds |
| Ink | `#1F2A33` | 31, 42, 51 | Name, one-colour logo, icon tile |
| Light Teal | `#7FC6BF` | 127, 198, 191 | First chevron, dark backgrounds |
| Light Clay | `#E58E6C` | 229, 142, 108 | Second chevron, dark backgrounds |
| Bone | `#ECE7E0` | 236, 231, 224 | Name on dark backgrounds |
| Paper | `#FBF8F3` | 251, 248, 243 | Preferred light background |

## Using it well

- **Clear space:** keep at least the width of one chevron's arm (about a quarter of the mark's
  height) empty around the logo.
- **Minimum size:** horizontal logo 120 px / 30 mm wide; mark alone 16 px / 5 mm tall.
- The teal chevron always comes first (left), the clay one second: the pair reads "moving forward".
- Don't recolour the chevrons outside the palette, stretch, rotate, add effects, or set the name in
  another typeface. On busy photos use the white version.

## Typeface

Fraunces (SemiBold, soft), © The Fraunces Project Authors, SIL Open Font License 1.1, which allows
its use in logos. The web app uses the same font for headings.

## Rebuilding

`source/build.py` regenerates every file from the mark geometry and the Fraunces font file in this
repository (`design-system/system/fonts/fraunces-latin.woff2`). It needs Python 3 with `fonttools` and
`uharfbuzz` (build-time only) and `rsvg-convert`:

    python3 source/build.py <dir with fonttools+uharfbuzz> ../design-system/system/fonts/fraunces-latin.woff2 <output dir>
