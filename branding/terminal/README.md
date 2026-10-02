# Logos en puntos — para clientes de terminal (hall v8coders, V8-RMP-693)

## Coders y Roadmap (Andy, 2026-09-30) — el hall lleva SU nombre, no "V8 Labs"
Andy: «en vez de que diga V8 Labs, generar el logotipo de V8 Coders y ese sí volverlo
puntos. Un logo de puntos, a la esquina superior derecha; poner también en el mismo esquema
el logotipo de Roadmap». Mismo esquema = mismo generador, misma retícula, mismo umbral; los
wordmarks salen de `wordmarks/_generate.py` (Balgin Expanded Bold, pelados: el prefijo "V8"
solo lo lleva V8 Labs — LOGOMANIA §0).

**Lo que está EN PRODUCCIÓN (Andy fijó los tamaños, 2026-09-30, distintos de la propuesta):**
Roadmap chico — «presencia puntual» — y Coders mediano — «prudente, preciso». Roadmap a la
izquierda, Coders en la esquina superior derecha; los dos juntos desde 92 columnas, más
angosto solo Coders 48, y bajo 50 columnas Coders 40. V8 Labs salió del hall.

| archivo | col | filas | estado |
|---|---|---|---|
| `coders-dots-48.txt` | 48 | 5 | **en el hall** — esquina sup. derecha |
| `coders-dots-40.txt` | 40 | 4 | **en el hall** — terminales < 50 col |
| `roadmap-text-small.txt` | 13 | 1 | **propuesto para el hall** — ver §Roadmap más chico abajo |
| `roadmap-dots-40.txt` | 40 | 4 | asset, reemplazado como logo del hall (ver abajo) |
| `coders-dots-64.txt` | 64 | 6 | asset, no se usa hoy |
| `roadmap-dots-64.txt` | 64 | 5 | asset, no se usa hoy |
| `roadmap-dots-48.txt` | 48 | 4 | asset, no se usa hoy |

40 es el piso de legibilidad de Roadmap EN PUNTOS: a 32 ya degrada visiblemente y a 24 no se
lee (probado, confirmado de nuevo 2026-09-30 con preview PNG). Si estos archivos cambian,
avisar a `remote`: van embebidos con `go:embed` y la copia es a mano.

### V8CODERS en mayúscula (Andy, 2026-10-01) — excepción a LOGOMANIA §0
Andy, vía `remote`: «que v8coders salga en mayúscula el texto en terminal, listado título
V8CODERS». Va CON el V8 y en caja alta por orden directa suya — excepción a §0 (el V8 solo en
"V8 Labs"), acotada al hall. Wordmark: `wordmarks/wordmark-v8coders.svg` (`_generate.py V8CODERS`,
Balgin Expanded Bold, un peso).

| archivo | col | filas | para |
|---|---|---|---|
| `v8coders-dots-48.txt` | 48 | 3 | esquina sup. derecha, terminales ≥ 50 col |
| `v8coders-text-small.txt` | 15 | 1 | `V 8 C O D E R S` — terminales < 50 col (mismo estilo que `R O A D M A P`) |
| `v8coders-dots-64.txt` | 64 | 4 | asset para terminales anchas, no se pidió |

Por qué no hay `v8coders-dots-40`: V8CODERS es 10.7:1 (Coders era 6:1). A 40 col quedan 2
filas (~8 puntos de alto) y el 8 se lee como «9» — probado con preview. A 48 se lee; el 8 es
el glifo más débil (resolución, no umbral: 0.40 y 0.60 no lo mejoran). Sin descendentes:
la última fila de puntos es la línea base. `preview-v8coders-48.png` simula Terminal.app.

### Roadmap más chico que 40 (Andy, 2026-09-30) — por qué deja de ser puntos
Andy pidió Roadmap «mucho más chico» que el de 40 columnas, alineado abajo al nivel de la
línea base de Coders. 40 ya es el piso de legibilidad de los puntos (documentado arriba, y
reconfirmado con preview a 32/28/24 col: a 32 el trazo ya se degrada, a 24 es ruido). Achicar
el braille por debajo de eso no es "más pulido", es ilegible — así que la pieza deja de ser
braille y pasa a **texto versalitas espaciado**: `roadmap-text-small.txt` → `R O A D M A P`
(mayúsculas, 1 espacio entre letra, 13 columnas, 1 fila, sin espacio a la derecha).

Dos ventajas de este camino sobre forzar los puntos más chico:
1. **Resuelve solo la pregunta de la línea base.** El braille `roadmap-dots-40` lleva una «p»
   con descendente — por eso el hall compensaba 1 fila a mano. El texto en mayúsculas no tiene
   descendentes: no hay nada que compensar, la fila que imprime la cadena ES la línea base.
2. Es más angosto que cualquier versión en puntos que siga leyéndose (13 col vs. el piso de 40).

Estilo recomendado para el embebido: mismo blanco de los puntos (`#FFFFFF` sobre fondo
oscuro), sin negrita forzada — si la terminal soporta bold ANSI y se ve bien, úsalo; si no,
el tracking (el espacio entre letras) ya hace el trabajo de "versalita".

`preview-coders-64.png` y `preview-roadmap-64.png` simulan Terminal.app. Los `logo-dots-*`
de V8 Labs quedan como asset (sirven para cualquier otra terminal de la casa) pero **ya no
van en el hall**.

Generar: `core_v8_brand/scripts/logo-dots.py --svg wordmarks/wordmark-coders.svg --mono --cols 48`.
`--mono` = un solo peso (sin partir Bold/Regular como en V8 Labs).

---

## V8 Labs — los tres archivos (asset general, ya no es el header del hall)
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
