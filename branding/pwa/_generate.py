#!/usr/bin/env python3
"""
Genera el ícono/splash PWA de V8 Labs: "V8" en Balgin Expanded Bold (vectorizado
a paths, self-contained), blanco sobre el gris primario de marca, en lienzo
cuadrado apto para icon mask de iOS (maskable: contenido dentro de la zona segura
central).

Fuente de verdad de marca: branding/brand-tokens.json
  - color.primario = fondo
  - tipografia.wordmark = Balgin Expanded Bold

Requiere fontTools. Uso:
  /tmp/fontvenv/bin/python branding/pwa/_generate.py
Salida: branding/pwa/v8-wordmark-splash.svg
"""
import json
import os

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))  # repo root

import sys
TEXT = sys.argv[1] if len(sys.argv) > 1 else "V8"           # monograma a centrar
OUTNAME = sys.argv[2] if len(sys.argv) > 2 else "v8-wordmark-splash"  # nombre de salida (sin ext)
CANVAS = 1024          # lienzo cuadrado (base PWA)
TARGET_FRAC = 0.62     # ancho/alto objetivo del monograma dentro del lienzo (zona segura iOS)

tokens = json.load(open(os.path.join(ROOT, "branding", "brand-tokens.json")))
BG = tokens["color"]["primario"]          # #262b39
FG = "#FFFFFF"
OTF = os.path.join(ROOT, tokens["tipografia"]["wordmark"]["archivo_bold"])

font = TTFont(OTF)
glyphset = font.getGlyphSet()
cmap = font.getBestCmap()

# Cadena de glifos con su offset horizontal acumulado (en unidades de fuente).
offsets, x = [], 0
for ch in TEXT:
    gname = cmap[ord(ch)]
    offsets.append((gname, x))
    x += glyphset[gname].width

def draw_into(pen):
    for gname, ox in offsets:
        glyphset[gname].draw(TransformPen(pen, (1, 0, 0, 1, ox, 0)))

# Path combinado (coords de fuente, Y hacia arriba).
svg_pen = SVGPathPen(glyphset)
draw_into(svg_pen)
path_d = svg_pen.getCommands()

# Bounding box real del lockup para centrar con precisión.
b = BoundsPen(glyphset)
draw_into(b)
xMin, yMin, xMax, yMax = b.bounds
gw, gh = xMax - xMin, yMax - yMin

# Escala: encajar el lado mayor del glifo en TARGET_FRAC del lienzo.
target = CANVAS * TARGET_FRAC
scale = target / max(gw, gh)
dw, dh = gw * scale, gh * scale
tx, ty = (CANVAS - dw) / 2, (CANVAS - dh) / 2

# Transform: font(Y-up) -> SVG(Y-down), escalado y centrado.
#   X = tx + scale*(px - xMin) ; Y = ty + scale*(yMax - py)
transform = (f"translate({tx:.3f},{ty:.3f}) "
             f"scale({scale:.6f},{-scale:.6f}) "
             f"translate({-xMin:.3f},{-yMax:.3f})")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS}" height="{CANVAS}" viewBox="0 0 {CANVAS} {CANVAS}">
  <!-- V8 Labs PWA icon/splash. Generado por branding/pwa/_generate.py.
       Fondo {BG} (color.primario), "V8" Balgin Expanded Bold vectorizado a paths. -->
  <rect width="{CANVAS}" height="{CANVAS}" fill="{BG}"/>
  <g transform="{transform}" fill="{FG}">
    <path d="{path_d}"/>
  </g>
</svg>
'''

out = os.path.join(HERE, f"{OUTNAME}.svg")
open(out, "w").write(svg)
print(f"OK -> {out}")
print(f"   glyph bbox font-units: {gw:.0f} x {gh:.0f}  scale={scale:.4f}  draw={dw:.0f}x{dh:.0f}px")
