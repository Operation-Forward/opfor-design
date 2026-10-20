"""Builds the Operation Forward brand kit from the LMS logo.

Mark geometry is the LMS header mark (src/app/layout/shell.scss .mark): two
chevrons in a 14x22 box, polygon (0,0) (45%,0) (100%,50%) (45%,100%) (0,100%)
(55%,50%), the second offset 11 units right. The wordmark is Fraunces at the
header's settings (wght 650, SOFT 100, optical size 20, -0.01em tracking),
shaped with HarfBuzz and converted to outlines.

usage: python3 -I build.py <pylibs> <fraunces.woff2> <out dir>
"""
import io
import struct
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, sys.argv[1])
from fontTools.pens.svgPathPen import SVGPathPen  # noqa: E402
from fontTools.pens.transformPen import TransformPen  # noqa: E402
from fontTools.ttLib import TTFont  # noqa: E402
from fontTools.varLib import instancer  # noqa: E402
import uharfbuzz as hb  # noqa: E402

FONT_SRC, OUT = Path(sys.argv[2]), Path(sys.argv[3])
NAME = "Operation Forward"

TEAL, CLAY, INK = "#1F5E5B", "#B4532A", "#1F2A33"
TEAL_D, CLAY_D, INK_D = "#7FC6BF", "#E58E6C", "#ECE7E0"
PAPER = "#FBF8F3"

# --- font: instance, shape, outline -------------------------------------------
font = TTFont(FONT_SRC)
font.flavor = None
inst = instancer.instantiateVariableFont(font, {"opsz": 20, "wght": 650, "SOFT": 100})
buf = io.BytesIO()
inst.save(buf)
blob = hb.Blob(buf.getvalue())
hbfont = hb.Font(hb.Face(blob))
upm = inst["head"].unitsPerEm
hb_buf = hb.Buffer()
hb_buf.add_str(NAME)
hb_buf.guess_segment_properties()
hb.shape(hbfont, hb_buf, {"kern": True, "liga": True})
glyph_set = inst.getGlyphSet()
order = inst.getGlyphOrder()
cap = inst["OS/2"].sCapHeight
track = -0.01 * upm


def wordmark_path(size, x0, baseline):
    """SVG path data for the wordmark at font size `size` px, origin (x0, baseline)."""
    s = size / upm
    pen = SVGPathPen(glyph_set, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    x = 0.0
    for info, pos in zip(hb_buf.glyph_infos, hb_buf.glyph_positions):
        g = order[info.codepoint]
        t = TransformPen(pen, (s, 0, 0, -s, x0 + (x + pos.x_offset) * s, baseline - pos.y_offset * s))
        glyph_set[g].draw(t)
        x += pos.x_advance + track
    return pen.getCommands(), (x - track) * s


def wordmark_width(size):
    return wordmark_path(size, 0, 0)[1]


# --- mark ----------------------------------------------------------------------
CHEVRON = [(0, 0), (6.3, 0), (14, 11), (6.3, 22), (0, 22), (7.7, 11)]


def chevrons(x, y, h, c1, c2):
    s = h / 22
    out = []
    for dx, color in ((0, c1), (11, c2)):
        pts = " ".join(f"{x + (px + dx) * s:.3f},{y + py * s:.3f}" for px, py in CHEVRON)
        out.append(f'<polygon points="{pts}" fill="{color}"/>')
    return "".join(out)


MARK_W = 25  # units, at height 22


def svg(w, h, body, title, bg=None):
    rect = f'<rect width="{w:g}" height="{h:g}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" width="{w:g}" height="{h:g}" role="img">'
            f"<title>{title}</title>{rect}{body}</svg>\n")


def mark_svg(c1, c2, pad=0):
    h = 22
    return svg(MARK_W + 2 * pad, h + 2 * pad, chevrons(pad, pad, h, c1, c2), "Operation Forward")


def horizontal_svg(c1, c2, ink, bg=None):
    # Header proportions: mark 22 tall, 12 gap, 20px type; cap height centred on the mark.
    pad, mh, gap, size = 11, 22, 12, 20
    capx = cap * size / upm
    d, tw = wordmark_path(size, pad + MARK_W + gap, pad + mh / 2 + capx / 2)
    w, h = pad + MARK_W + gap + tw + pad, mh + 2 * pad
    body = chevrons(pad, pad, mh, c1, c2) + f'<path d="{d}" fill="{ink}"/>'
    return svg(round(w, 2), h, body, NAME, bg)


def stacked_svg(c1, c2, ink, bg=None):
    pad, mh, gap, size = 16, 44, 14, 20
    tw = wordmark_width(size)
    w = max(tw, MARK_W * mh / 22) + 2 * pad
    capx = cap * size / upm
    mw = MARK_W * mh / 22
    d, _ = wordmark_path(size, (w - tw) / 2, pad + mh + gap + capx)
    h = pad + mh + gap + capx + pad
    body = chevrons((w - mw) / 2, pad, mh, c1, c2) + f'<path d="{d}" fill="{ink}"/>'
    return svg(round(w, 2), round(h, 2), body, NAME, bg)


def app_icon_svg(size=512):
    # Rounded square in ink with the dark-mode chevrons, mark ~56% of the tile.
    mh = size * 0.5
    mw = MARK_W * mh / 22
    body = (f'<rect width="{size}" height="{size}" rx="{size * 0.22:g}" fill="{INK}"/>'
            + chevrons((size - mw) / 2, (size - mh) / 2, mh, TEAL_D, CLAY_D))
    return svg(size, size, body, NAME)


def social_svg(w=1200, h=630):
    inner = horizontal_svg(TEAL, CLAY, INK)
    # Reuse the horizontal lockup, scaled to ~62% of the card width.
    vb = inner.split('viewBox="0 0 ')[1].split('"')[0].split()
    iw, ih = float(vb[0]), float(vb[1])
    s = w * 0.62 / iw
    body_inner = inner.split("</title>", 1)[1].rsplit("</svg>", 1)[0]
    body = f'<g transform="translate({(w - iw * s) / 2:.2f},{(h - ih * s) / 2:.2f}) scale({s:.4f})">{body_inner}</g>'
    return svg(w, h, body, NAME, PAPER)


files = {
    "svg/mark.svg": mark_svg(TEAL, CLAY),
    "svg/mark-reversed.svg": mark_svg(TEAL_D, CLAY_D),
    "svg/mark-ink.svg": mark_svg(INK, INK),
    "svg/mark-white.svg": mark_svg("#FFFFFF", "#FFFFFF"),
    "svg/logo-horizontal.svg": horizontal_svg(TEAL, CLAY, INK),
    "svg/logo-horizontal-reversed.svg": horizontal_svg(TEAL_D, CLAY_D, INK_D),
    "svg/logo-horizontal-ink.svg": horizontal_svg(INK, INK, INK),
    "svg/logo-horizontal-white.svg": horizontal_svg("#FFFFFF", "#FFFFFF", "#FFFFFF"),
    "svg/logo-stacked.svg": stacked_svg(TEAL, CLAY, INK),
    "svg/logo-stacked-reversed.svg": stacked_svg(TEAL_D, CLAY_D, INK_D),
    "svg/app-icon.svg": app_icon_svg(),
    "svg/social-card.svg": social_svg(),
}
for rel, text in files.items():
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)


def png(src, dst, width=None, height=None):
    dst = OUT / dst
    dst.parent.mkdir(parents=True, exist_ok=True)
    args = ["rsvg-convert", "-o", str(dst)]
    if width:
        args += ["-w", str(width)]
    if height:
        args += ["-h", str(height)]
    subprocess.run(args + [str(OUT / src)], check=True)
    return dst


for name in ("mark", "mark-reversed", "mark-ink", "mark-white"):
    png(f"svg/{name}.svg", f"png/{name}-512.png", height=512)
for name in ("logo-horizontal", "logo-horizontal-reversed", "logo-horizontal-ink", "logo-horizontal-white"):
    png(f"svg/{name}.svg", f"png/{name}-1200.png", width=1200)
    png(f"svg/{name}.svg", f"png/{name}-600.png", width=600)
for name in ("logo-stacked", "logo-stacked-reversed"):
    png(f"svg/{name}.svg", f"png/{name}-800.png", width=800)
icons = {n: png("svg/app-icon.svg", f"png/app-icon-{n}.png", width=n, height=n) for n in (16, 32, 48, 180, 192, 512, 1024)}
png("svg/social-card.svg", "png/social-card-1200x630.png", width=1200, height=630)

# favicon.ico: ICO container with embedded PNGs (16, 32, 48).
entries = [(n, icons[n].read_bytes()) for n in (16, 32, 48)]
ico = struct.pack("<HHH", 0, 1, len(entries))
offset = 6 + 16 * len(entries)
blobs = b""
for n, data in entries:
    ico += struct.pack("<BBBBHHII", n, n, 0, 0, 1, 32, len(data), offset)
    offset += len(data)
    blobs += data
(OUT / "favicon.ico").write_bytes(ico + blobs)
print("built", len(files), "svg +", len(list((OUT / "png").glob("*.png"))), "png + favicon.ico in", OUT)
