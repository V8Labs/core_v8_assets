# V8 Labs en puntos — para clientes de terminal (hall v8coders, V8-RMP-693)

## Los dos archivos
- `logo-dots-64.txt` — ~64 columnas (MacBook / Linux).
- `logo-dots-40.txt` — ≤40 columnas (Blink en iPhone vertical).

Braille U+2800, texto plano UTF-8, sin espacios a la derecha. Generados con el MISMO
algoritmo que ya tenía `remote` en `app_V8_CODERS/scripts/logo-braille.py` (threshold
de luminosidad a 2×4 px por carácter), pero alimentado de `wordmark-v8labs.svg` — el
wordmark vectorizado (paths, no Illustrator export) del que salen TODOS los wordmarks
por-app — en vez de `logo-hi.png`.

## Colores (SSOT: `branding/brand-tokens.json`)

| uso | hex | de dónde sale |
|---|---|---|
| **glyph del logo** (los puntos) | `#FFFFFF` | `wordmark-v8labs-blanco.svg` — la variante del wordmark para fondo oscuro |
| **acento** (cursor, líneas, indicador activo) | `#A2E771` | `color.acento` — el lima de marca |

⚠ **NO uses `ux.info` (`#679BE9`/`#0E4B8F`)** aunque también es "azul sobre oscuro" y
parece tentador para un acento de terminal. Ese color es FUNCIONAL — reservado para
marcar estado (mensajes esperando respuesta en XO) — y usarlo como decoración lo gasta:
el día que necesites señalar un estado de verdad, ya no significa nada. El acento de
identidad es el lima.

⚠ **`#8FB4FF` no era de marca** (lo dijiste vos mismo al pedir) — no lo sigas usando.

## ⚠ POR QUÉ NO TE DOY `logo-hi.png` NI TE PIDO QUE LE APUNTES AHÍ

`logo-hi.png` y `logo.png` (la raíz de `branding/`) **están en producción**: el edge
function `auth-send-email` (`core_v8_edge_functions`) los sirve en los correos
transaccionales de acceso, por URL cruda de GitHub pineada a `main`
(`raw.githubusercontent.com/V8Labs/core_v8_assets/main/branding/logo.png`). **Cualquier
cambio ahí sale a usuarios reales sin deploy.** No los toqué, y si tu script regenerador
necesita una fuente propia para "autoregenerar cuando cambie el logo", apuntalo a
**`logo-source.png`** (este directorio) — es una copia dedicada a terminal, no al email.
Si el wordmark de V8 Labs cambia alguna vez, branding actualiza ACÁ, no allá.

## Regenerar
El algoritmo es el tuyo (`logo-braille.py`); el único cambio es la `FUENTE`:

```python
FUENTE = Path.home() / "dev/core_v8_assets/branding/terminal/logo-source.png"
```

No duplico tu generador acá a propósito — una segunda copia del mismo algoritmo se
desincroniza con la primera el día que uno de los dos cambie (es tu repo, tu script).
