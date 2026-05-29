#!/usr/bin/env python3
"""
Genera sellos SVG por app/servicio interno V8Labs.
Sello = pastilla (marco redondeado) + nombre en Balgin Expanded Regular,
con INICIAL CAPITULAR (primera letra más grande) y el resto Title-case,
glifos OUTLINEADOS (trazos) → portable sin la fuente.

SSOT: salida a core_v8_assets/branding/seals/ (la app consume una copia).
Fuente: Balgin Expanded Regular (DEMO/provisional — licenciar para prod).
"""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

OTF = os.path.expanduser(
    "~/dev/core_v8_assets/fonts/balgin/Fontspring-DEMO-balgin-regularexpanded.otf"
)
OUT_DIR = os.path.expanduser("~/dev/core_v8_assets/branding/seals")
os.makedirs(OUT_DIR, exist_ok=True)

NAMES = ["Dialogue", "Ecommerce", "Fashion", "Metrics", "Notifications",
         "Retailers", "Studio", "Mind"]

EM_PX = 11.0        # em del resto (minúsculas)
CAP_RATIO = 1.45    # la inicial es 1.45× → capitular
PAD_X = 7.0
PAD_Y = 3.0
COLOR = "#8a8f9c"   # v8-fg-mute
STROKE_OP = 0.4
FILL_OP = 0.7

font = TTFont(OTF)
glyphSet = font.getGlyphSet()
cmap = font.getBestCmap()
upm = font["head"].unitsPerEm
hmtx = font["hmtx"]
os2 = font["OS/2"]
asc, desc = os2.sTypoAscender, os2.sTypoDescender   # desc < 0
cap_h = getattr(os2, "sCapHeight", 0) or round(0.7 * upm)
s = EM_PX / upm
s_cap = s * CAP_RATIO

# Extentes verticales constantes → todos los sellos misma altura
TOP = max(cap_h * s_cap, asc * s)   # px por encima de la baseline (domina la capital)
BOT = -desc * s                     # px por debajo (descendentes: g, y, p)
BASELINE = PAD_Y + TOP
HEIGHT = round(PAD_Y + TOP + BOT + PAD_Y, 1)

def seal(name: str) -> str:
    glyphs, x = [], PAD_X
    for i, ch in enumerate(name):
        gname = cmap.get(ord(ch))
        if not gname:
            continue
        sc = s_cap if i == 0 else s
        pen = SVGPathPen(glyphSet)
        glyphSet[gname].draw(pen)
        d = pen.getCommands()
        if d:
            glyphs.append(
                f'<path transform="matrix({sc:.5f} 0 0 {-sc:.5f} {x:.2f} {BASELINE:.2f})" d="{d}"/>'
            )
        x += hmtx[gname][0] * sc
    w = round(x + PAD_X, 1)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {HEIGHT}" fill="none">\n'
        f'  <rect x="0.5" y="0.5" width="{round(w-1,1)}" height="{round(HEIGHT-1,1)}" rx="2.5" '
        f'stroke="{COLOR}" stroke-opacity="{STROKE_OP}"/>\n'
        f'  <g fill="{COLOR}" fill-opacity="{FILL_OP}">{"".join(glyphs)}</g>\n'
        f'</svg>\n'
    )

for name in NAMES:
    svg = seal(name)
    with open(os.path.join(OUT_DIR, f"{name.lower()}.svg"), "w") as f:
        f.write(svg)
    vb = svg.split('viewBox="')[1].split('"')[0]
    print(f"{name:14s} -> {name.lower()}.svg   viewBox={vb}")
