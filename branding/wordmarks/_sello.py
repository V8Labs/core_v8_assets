#!/usr/bin/env python3
"""
Sello de presencia V8 (familia de MindSeal): el nombre en Balgin Expanded REGULAR,
en contornos, con drop-cap — la inicial a 0.01595 y el resto a 0.01100 (altura x),
espaciado = avance natural del font (sin kerning), línea base 14.16, alto 19.9.
Aire lateral = el de Mind (7.73 a la izquierda de la tinta, 7.63 a la derecha), así
que dos sellos en el mismo hueco se leen del mismo sistema. fill=currentColor.

Uso:  python branding/wordmarks/_sello.py Pulse      (requiere fonttools)
Salida: branding/wordmarks/sello-<nombre-lower>.svg  + snippet de paths en stdout.
"""
import json, os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
tokens = json.load(open(os.path.join(ROOT, "branding", "brand-tokens.json")))
font = TTFont(os.path.join(ROOT, tokens["tipografia"]["wordmark"]["archivo_regular"]))
gs, cmap = font.getGlyphSet(), font.getBestCmap()

CAP, LOW, BL, H = 0.01595, 0.01100, 14.16, 19.9   # medidas de MindSeal
PAD_L, PAD_R = 7.73, 7.63                         # aire de Mind alrededor de la tinta

name = sys.argv[1] if len(sys.argv) > 1 else "Pulse"

def glyph(ch):
    g = gs[cmap[ord(ch)]]
    sp, bp = SVGPathPen(gs), BoundsPen(gs)
    g.draw(sp); g.draw(bp)
    return g.width, sp.getCommands(), bp.bounds

# 1ª pasada: avances desde x=0 para saber dónde arranca la tinta
glyphs, x, inkL, inkR = [], 0.0, None, None
for i, ch in enumerate(name):
    s = CAP if i == 0 else LOW
    w, d, (x0, _, x1, _) = glyph(ch)
    glyphs.append((s, x, d))
    inkL = x + x0 * s if inkL is None else min(inkL, x + x0 * s)
    inkR = x + x1 * s if inkR is None else max(inkR, x + x1 * s)
    x += w * s
shift = PAD_L - inkL
vb_w = (inkR + shift) + PAD_R

paths = "\n".join(
    f'    <path transform="matrix({s:.5f} 0 0 -{s:.5f} {gx + shift:.2f} {BL:.2f})" d="{d}"/>'
    for s, gx, d in glyphs)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w:.1f} {H}" role="img" aria-label="{name}" fill="none">
  <!-- Sello {name}: Balgin Expanded Regular en contornos, drop-cap, hermano de MindSeal.
       fill=currentColor (hereda el color del texto). Generado por branding/wordmarks/_sello.py. -->
  <g fill="currentColor">
{paths}
  </g>
</svg>
'''
out = os.path.join(HERE, f"sello-{name.lower()}.svg")
open(out, "w").write(svg)
print(f"OK -> {out}  viewBox 0 0 {vb_w:.1f} {H}")
