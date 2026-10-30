#!/usr/bin/env python3
"""
Sello MÍO: pareja apagada del ícono V8 (branding/app-icons/v8/v8-icon.svg),
mismo lockup/escala (misma placa 1024, mismo SCALE=0.295706, mismo tope de
caja de capitales) para que, uno al lado del otro, se lean del mismo sistema
apagado/encendido. "MIO" vectorizado desde Balgin Expanded Bold (paths, no
<text>). El font no trae glifos acentuados (ni Í ni ningún otro) ni un
componente de tilde reutilizable -- la tilde de la Í se compone a mano acá
como un paralelogramo rotado, mismo peso visual que el trazo de las letras.
Placa y letra son grises neutros (sin lima): #262B39 (= primario del token
de marca, misma placa que V8) / #9499A3, contraste 4.94:1 (pasa AAcontra
normal-text).

Uso:  python branding/seals/_generate_mio.py   (requiere fonttools)
Salida: branding/seals/mio.svg
"""
import math
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
FONT = os.path.join(ROOT, "fonts", "balgin", "Fontspring-DEMO-balgin-boldexpanded.otf")

SCALE = 0.295706  # mismo SCALE óptico de branding/app-icons/v8/v8-icon.svg
CANVAS = 1024.0
PLATE = "#262B39"   # = color.primario del brand-tokens.json, misma placa que V8
LETTER = "#9499A3"  # gris apagado, contraste 4.94:1 contra PLATE

f = TTFont(FONT)
gs = f.getGlyphSet()
cmap = f.getBestCmap()


def glyph(ch):
    g = gs[cmap[ord(ch)]]
    sp, bp = SVGPathPen(gs), BoundsPen(gs)
    g.draw(sp)
    g.draw(bp)
    return g.width, sp.getCommands(), bp.bounds


letters = "MIO"
x = 0.0
items = []  # (char, x_offset, path_d, bounds)
inkL = inkR = inkTop = inkBot = None
for ch in letters:
    w, d, (x0, y0, x1, y1) = glyph(ch)
    items.append((ch, x, d, (x0, y0, x1, y1)))
    L, R = x + x0, x + x1
    inkL = L if inkL is None else min(inkL, L)
    inkR = R if inkR is None else max(inkR, R)
    inkTop = y1 if inkTop is None else max(inkTop, y1)
    inkBot = y0 if inkBot is None else min(inkBot, y0)
    x += w

cap_top = inkTop  # 722 (tope de caja de capitales de M/I/O)

# ubicación de la I, para centrar la tilde encima
i_ch, i_xo, _, (i_x0, _, i_x1, _) = [it for it in items if it[0] == "I"][0]
i_cx = i_xo + (i_x0 + i_x1) / 2.0

# --- tilde compuesta a mano: paralelogramo rotado, mismo coord space que las letras ---
hw, hl = 70.0, 135.0          # semigrosor / semilargo, peso comparable al trazo de las letras
theta = math.radians(22)      # inclinación: sube de izquierda a derecha, como una tilde normal
cx = i_cx + 40                # corrida levemente a la derecha del asta de la I (uso tipográfico)
gap = 45.0                    # aire entre el tope de capitales y la base de la tilde
cy = cap_top + gap + hl


def rot(px, py, a):
    return (px * math.cos(a) - py * math.sin(a), px * math.sin(a) + py * math.cos(a))


pts = [(cx + rx, cy + ry) for rx, ry in (rot(px, py, theta) for px, py in
       [(-hw, -hl), (hw, -hl), (hw, hl), (-hw, hl)])]
accent_d = "M" + " L".join(f"{px:.2f} {py:.2f}" for px, py in pts) + " Z"

inkTop = max(inkTop, max(p[1] for p in pts))
inkBot = min(inkBot, min(p[1] for p in pts))
inkL = min(inkL, min(p[0] for p in pts))
inkR = max(inkR, max(p[0] for p in pts))

# centrado: mismo criterio que v8-icon.svg (ancho de tinta centrado en el cuadrado;
# el alto de referencia es el bloque de capitales, no la tilde, así "MIO" y "V8"
# quedan a la misma altura óptica)
ink_w_px = (inkR - inkL) * SCALE
cap_h_px = (cap_top - inkBot) * SCALE
TX = (CANVAS - ink_w_px) / 2.0
TY = (CANVAS - cap_h_px) / 2.0

group_transform = (
    f"translate({TX:.3f},{TY:.3f}) scale({SCALE:.6f},-{SCALE:.6f}) "
    f"translate({-inkL:.3f},{-cap_top:.3f})"
)

paths = [f'    <path transform="translate({xo:.3f},0)" d="{d}"/>' for _, xo, d, _ in items]
paths.append(f'    <path d="{accent_d}"/>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024" role="img" aria-label="MÍO">
  <!-- Sello MIO: pareja apagada del icono V8 (branding/app-icons/v8/v8-icon.svg), mismo
       lockup/escala. "MIO" vectorizado desde Balgin Expanded Bold (paths, no <text>); la
       tilde de la I se compuso a mano (el font no trae glifos acentuados). Generado por
       branding/seals/_generate_mio.py. -->
  <rect width="1024" height="1024" fill="{PLATE}"/>
  <g transform="{group_transform}" fill="{LETTER}">
{chr(10).join(paths)}
  </g>
</svg>
'''

OUT = os.path.join(HERE, "mio.svg")
open(OUT, "w").write(svg)
print(f"OK -> {OUT}")
