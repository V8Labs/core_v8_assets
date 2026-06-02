#!/usr/bin/env python3
"""
Genera un wordmark por-app V8 Labs: "V8" en Balgin Expanded Bold + "<Nombre>" en
Balgin Expanded Regular, pegados, vectorizado a paths (self-contained, no depende
de que el cliente tenga la fuente), color primario #262b39, fondo transparente.

Patrón canónico: brand-tokens.json → logo.wordmark_por_app.
Uso:  /tmp/fontvenv/bin/python branding/wordmarks/_generate.py Studio
Salida: branding/wordmarks/wordmark-v8<nombre-lower>.svg
"""
import json, os, sys

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

name = sys.argv[1] if len(sys.argv) > 1 else "Studio"   # "V8" + este nombre
variant = sys.argv[2].lower() if len(sys.argv) > 2 else "dark"  # "dark" (#262b39) | "blanco" (#FFFFFF, fondos oscuros)
PAD = 40            # padding en unidades EM alrededor del lockup
tokens = json.load(open(os.path.join(ROOT, "branding", "brand-tokens.json")))
FILL = "#FFFFFF" if variant == "blanco" else tokens["color"]["primario"]
SUFFIX = "-blanco" if variant == "blanco" else ""
wm = tokens["tipografia"]["wordmark"]
BOLD = os.path.join(ROOT, wm["archivo_bold"])
REG  = os.path.join(ROOT, wm["archivo_regular"])

# (texto, fuente) por tramo. "V8" bold + ESPACIO + nombre regular (doctrina 2026-06-02).
segments = [("V8", BOLD), (" " + name, REG)]

fonts = {p: TTFont(p) for p in {BOLD, REG}}
EM = fonts[BOLD]["head"].unitsPerEm   # espacio común

def build(pen_factory):
    """Dibuja todos los tramos en el pen; devuelve el pen y el ancho total (EM)."""
    x = 0.0
    for text, path in segments:
        f = fonts[path]
        gs = f.getGlyphSet()
        cmap = f.getBestCmap()
        s = EM / f["head"].unitsPerEm          # normaliza a EM común
        for ch in text:
            g = gs[cmap[ord(ch)]]
            # escala del glifo + traslación x acumulada
            g.draw(TransformPen(pen_factory, (s, 0, 0, s, x, 0)))
            x += g.width * s
    return x

svg_pen = SVGPathPen(fonts[BOLD].getGlyphSet())
total_w = build(svg_pen)
path_d = svg_pen.getCommands()

b = BoundsPen(fonts[BOLD].getGlyphSet())
build(b)
xMin, yMin, xMax, yMax = b.bounds

vb_w = (xMax - xMin) + 2 * PAD
vb_h = (yMax - yMin) + 2 * PAD
# transform: font(Y-up) -> SVG(Y-down), con padding
transform = (f"translate({PAD - xMin:.2f},{PAD + yMax:.2f}) scale(1,-1)")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w:.0f} {vb_h:.0f}" role="img" aria-label="V8{name}">
  <!-- Wordmark V8{name}. V8=Balgin Expanded Bold, {name}=Balgin Expanded Regular.
       Vectorizado a paths. Color {FILL}. Generado por branding/wordmarks/_generate.py. -->
  <g transform="{transform}" fill="{FILL}"><path d="{path_d}"/></g>
</svg>
'''
out = os.path.join(HERE, f"wordmark-v8{name.lower()}{SUFFIX}.svg")
open(out, "w").write(svg)
print(f"OK -> {out}  ({vb_w:.0f}x{vb_h:.0f} EM, fill {FILL})")
