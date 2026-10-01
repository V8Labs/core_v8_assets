# V8 Labs en puntos — para clientes de terminal (hall v8coders, V8-RMP-693)

## Los tres archivos
| archivo | columnas | filas | para |
|---|---|---|---|
| `logo-dots-96.txt` | 96 | 8 | MacBook / Linux con terminal ≥ 100 col — **el fiel al logo** |
| `logo-dots-64.txt` | 64 | 5 | terminales entre 66 y 99 col |
| `logo-dots-40.txt` | 40 | 3 | Blink en iPhone vertical |

Braille U+2800, UTF-8, sin espacios a la derecha. `preview-comparacion.png` muestra el logo
real contra la versión anterior y estas, simulando Terminal.app.

## Cómo se generan — y por qué cambió el método (2026-09-30, pedido de Andy)
Generador: **`core_v8_brand/scripts/logo-dots.py`** (de branding). Fuente:
`branding/wordmarks/wordmark-v8labs.svg`, el wordmark aprobado.

Andy vio el hall y dijo que el logo "se sentía distinto" al real. Tenía razón, y la causa
NO era el estiramiento que se sospechó primero — eran dos cosas del muestreo:

1. **Se muestreaba una grilla uniforme que no existe en pantalla.** Terminal.app dibuja
   el braille con la fuente *Apple Braille* (fallback) dentro de la celda de Menlo. Medido
   con fontTools: dentro de una celda los puntos van cada 484 unidades, pero entre celdas
   el salto es 1233 (el advance de Menlo) — el hueco entre celdas es **1.55×** el paso
   interno; verticalmente 490 vs 2384 de línea → **1.86×**. El generador nuevo muestrea el
   vector **en la posición real de cada punto** de esa retícula.
2. **Un solo umbral al 50% invertía el contraste de peso.** "V8" es Balgin Expanded BOLD y
   "Labs" REGULAR; con un umbral único el Regular se partía en trazos de 1 punto (casi
   contorno) y el Bold se empastaba cerrando los ojos del 8. Ahora cada tramo lleva su
   umbral de cobertura (Bold 0.50, Regular 0.32), y el tramo se detecta solo por el
   espacio de palabra entre el 8 y la L.

El límite que queda es de **resolución**: a 64 columnas el logo tiene 20 puntos de alto y
la mayúscula ~15. Por eso existe el de 96 (28 puntos de alto): ahí el vértice de la V, los
dos ojos del 8 y la panza de la 'a' se leen como en el logo. Si la terminal lo permite, es
el que debería verse.

**Supuesto declarado:** la retícula es la de Terminal.app/iTerm2 con Menlo + Apple Braille.
Otra fuente mono (JetBrains, Fira) cambia el paso entre celdas; el dibujo sigue leyéndose
pero no es la retícula exacta. Para Blink en iPhone no pude medir la fuente de fallback.

## Colores (SSOT: `branding/brand-tokens.json`)
| uso | hex | de dónde sale |
|---|---|---|
| glyph (los puntos) | `#FFFFFF` | `wordmark-v8labs-blanco.svg` — variante para fondo oscuro |
| acento (cursor, líneas, activo) | `#A2E771` | `color.acento`, el lima de marca |

⚠ No usar `ux.info` (`#679BE9`) como acento: es color FUNCIONAL de estado, no decoración.

## ⚠ `logo.png` / `logo-hi.png` (raíz de `branding/`) están en PRODUCCIÓN
`auth-send-email` los sirve en los correos de acceso por URL cruda de GitHub pineada a
`main`: cualquier cambio ahí sale a usuarios reales sin deploy. Este directorio no depende
de ellos. `logo-source.png` queda como raster de referencia; el generador ya no lo usa
(lee el SVG directo).
