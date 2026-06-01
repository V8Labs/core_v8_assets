#!/usr/bin/env python3
"""
Genera favicons MONOGRAMA por-app V8 Labs: inicial(es) en Balgin Expanded Bold,
blanco sobre #262b39 (primario), esquinas duras (cero radius), + punto verde
`acento` abajo-derecha como firma de familia (destello, no fondo).

Inicial(es) vectorizadas a paths (self-contained). Color de marca desde brand-tokens.json.

Uso:  /tmp/fontvenv/bin/python branding/favicons/_generate_monogram.py <app> <inicial>
  ej: ... studio S   |   ... mind Mi
Salida: branding/favicons/<app>.svg
"""
import json, os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

app = sys.argv[1]
initial = sys.argv[2]

CANVAS = 64
FRAC = 0.56          # alto/ancho objetivo de la inicial dentro del lienzo
tokens = json.load(open(os.path.join(ROOT, "branding", "brand-tokens.json")))
BG = tokens["color"]["primario"]
ACENTO = tokens["color"]["acento"]
FG = "#FFFFFF"
OTF = os.path.join(ROOT, tokens["tipografia"]["wordmark"]["archivo_bold"])

font = TTFont(OTF)
gs = font.getGlyphSet()
cmap = font.getBestCmap()

offsets, x = [], 0.0
for ch in initial:
    g = gs[cmap[ord(ch)]]
    offsets.append((cmap[ord(ch)], x))
    x += g.width

def draw(pen):
    for gname, ox in offsets:
        gs[gname].draw(TransformPen(pen, (1, 0, 0, 1, ox, 0)))

svg_pen = SVGPathPen(gs)
draw(svg_pen)
path_d = svg_pen.getCommands()

b = BoundsPen(gs)
draw(b)
xMin, yMin, xMax, yMax = b.bounds
gw, gh = xMax - xMin, yMax - yMin

scale = (CANVAS * FRAC) / max(gw, gh)
dw, dh = gw * scale, gh * scale
tx, ty = (CANVAS - dw) / 2, (CANVAS - dh) / 2
transform = (f"translate({tx:.2f},{ty:.2f}) scale({scale:.5f},{-scale:.5f}) "
             f"translate({-xMin:.2f},{-yMax:.2f})")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CANVAS} {CANVAS}" role="img" aria-label="V8 {app}">
  <!-- Favicon monograma V8 {app}. Inicial "{initial}" Balgin Bold vectorizada.
       Fondo {BG}, inicial {FG}, punto {ACENTO} (acento de familia). Generado por _generate_monogram.py. -->
  <rect width="{CANVAS}" height="{CANVAS}" fill="{BG}"/>
  <g transform="{transform}" fill="{FG}"><path d="{path_d}"/></g>
  <circle cx="{CANVAS-11}" cy="{CANVAS-11}" r="4" fill="{ACENTO}"/>
</svg>
'''
out = os.path.join(HERE, f"{app}.svg")
open(out, "w").write(svg)
print(f"OK -> {out}  (inicial '{initial}', scale {scale:.3f})")
