# Sistema de Marca — V8 Labs

Fuente única de la identidad de **V8 Labs** para **todas las apps** del ecosistema.
Los valores machine-readable están en [`brand-tokens.json`](brand-tokens.json);
este archivo es su versión legible.

> **Estado: provisional (en aprobación).** Mientras se aprueba el diseño, se
> itera en `V8Labs/ops-admin-documentos` (`marca/tema.typ`) y acá vive la copia
> publicada para que otras apps arranquen. Al aprobar, esto queda como SSOT.

## Cómo lo consume una app

Patrón base de URL (CDN vía GitHub raw):

```
https://raw.githubusercontent.com/V8Labs/core_v8_assets/main/branding/<archivo>
```

- **Apps online (web / Shopify / GAS / Node):** leé `brand-tokens.json` por raw URL
  (o pineá a un SHA) y mapeá a tus variables CSS / theme.
  ```js
  const t = await (await fetch(RAW + "branding/brand-tokens.json")).json();
  document.documentElement.style.setProperty("--color-primario", t.color.primario);
  ```
- **Apps build-time (Typst, generadores de PDF):** traé una **copia local** de los
  tokens y los logos (script de sync), porque no pueden hacer fetch en compilación.

## Logo

- Vector: `logo.svg` (wordmark "V8 Labs"). PNG transparente: `logo.png` (1724×240) y `logo-hi.png`.
- Color: **#262b39**. Fondo transparente. No deformar ni recolorear.
- Si no se puede usar imagen, fallback de texto: **V8 Labs**.

## Wordmark por-app

Cada app interna arma su propio wordmark combinando dos pesos de **Balgin
Expanded**:

- **"V8"** en **Bold** + **"<Nombre>"** en **Regular**, primera mayúscula y
  pegados. Ejemplos: **V8Metrics**, **V8Studio**.
- Fuentes en `fonts/balgin/` (`...boldexpanded.otf` / `...regularexpanded.otf`).
  Online: embebé por `@font-face`. Build-time: copia local por sync.
- Ejemplo de referencia implementado: `app_V8_METRICS`.

> ⚠️ La Balgin actual es **Fontspring DEMO** (versión de evaluación). Sirve como
> provisional mientras la marca está en aprobación; al aprobar el look hay que
> **licenciar Balgin Expanded** para producción/embedding.

**Wordmarks listos / generables:** `branding/wordmarks/`. Cada app tiene su SVG
vectorizado a paths (no requiere la fuente en el cliente). Generar uno nuevo:
`/tmp/fontvenv/bin/python branding/wordmarks/_generate.py <Nombre>` → `wordmark-v8<nombre>.svg`.
Existentes: `wordmark-v8studio.svg`. ⚠️ Por la licencia DEMO, **vectorizá el wordmark a
paths** (lo que hace el generador) en vez de embeber el `.otf` en una app desplegada.

## Favicons

`branding/favicons/` — un favicon por proyecto. Respetan la regla del verde
(acento solo como destello, nunca fondo).

**Sistema MONOGRAMA (default):** inicial(es) en Balgin Expanded Bold, blanco sobre
`primario #262b39`, esquinas duras, + punto `acento` abajo-derecha como firma de familia.
Generar: `/tmp/fontvenv/bin/python branding/favicons/_generate_monogram.py <app> <inicial>`.
Inicial vectorizada a paths (no embebe fuente). Iniciales por app:

| App | Inicial | · | App | Inicial |
|---|---|---|---|---|
| notifications | `V8` | | ecommerce | `E` |
| studio | `S` | | dialogue | `D` |
| metrics | `M` | | retailers | `R` |
| mind | `Mi` | | fashion | `F` |

> Colisión Mind/Metrics resuelta: Metrics=`M`, Mind=`Mi`.

**Excepción bespoke (concepto):** cuando el dominio pide un símbolo fuerte, favicon
conceptual en el mismo lenguaje (cuerpo `primario`, line-art blanco, punto `acento`):
- `firma-seguridad.svg` — caja fuerte (familia seguridad/legal, ej. `firma.v8labs.co`).

## Colores

### Paleta de marca (identidad)

| Token | Hex | Uso |
|---|---|---|
| `color.primario` | `#262b39` | fondo base de apps, títulos, reglas |
| `color.texto` | `#1a1a1a` | texto cuerpo |
| `color.tenue` | `#6b7280` | metadatos, pies, secundario |
| `color.linea` | `#d1d5db` | reglas y bordes suaves |
| `color.acento` | `#A2E771` | **acento vivo** — ver regla dura abajo |
| `color.acento_texto` | `#163309` | texto sobre verde, **solo** en el caso raro de que el verde sea fondo (evitar) |

### ⚠️ Regla dura del verde `acento` (#A2E771)

El verde es **acento de vida, no superficie**. Le da luz y energía a la interfaz;
nunca la estructura. Es el destello, no el relleno.

- ✅ **Permitido:** subrayado de enlaces · líneas vivas bajo palabras clave ·
  glow / animación de marcos y bordes · micro-acentos que "encienden" un frame.
- ❌ **Prohibido:** fondo de botón · relleno de bloques o tarjetas · fondo de
  tab/sección activa · cualquier área extensa. **El verde nunca es la superficie.**

Los **botones** usan la base (`primario` / negro / blanco) o el color **semántico**
de la acción (ver UX), **nunca** el verde de marca. Negro y blanco son la base;
el verde solo acentúa (enlaces, subrayados, animaciones vivas).

> Origen del verde: app de firma (Documenso). Nota: fue Documenso quien lo usó
> primero como fondo de botón — eso es el antipatrón que esta regla corrige.

### Resolución del acento contra fondos claros (modo light)

Sobre fondo oscuro (modo default), el lime `#A2E771` tiene contraste perfecto.
Sobre fondo claro (modo light, gris-azulado templado o blanco), el lime puro se
diluye y se vuelve ilegible. **No se sustituye el lime por otro verde** — el hex
del acento es el hex del acento.

**Patrón sancionado: pill oscuro invertido.** Donde el acento deba aparecer como
texto sobre superficie clara, se envuelve en un fondo `color.primario` con texto
`color.acento`. Es el dark invertido localmente: cero pérdida de fidelidad al
token, máximo contraste preservado.

- ✅ Aplica en: chips de slot vacío (PENDIENTE, SIN FECHA), score ≥80 de
  operador, ack inline de Mind, botón LIMPIAR filtros, badge de audio listo.
- ❌ No aplica para líneas/bordes/glows — esos siguen siendo lime suelto en
  ambos modos (ya tienen contraste por trazo, no por fill).
- Glyphs decorativos sueltos (flechas, ⤷): caen al `color.texto` en light en
  vez de pillarse, porque el pill sobre un solo carácter rompe la lectura.

Implementación de referencia: utility CSS `v8-accent-chip` en
`app_V8_NOTIFICATIONS/src/index.css`.

## Geometría

**V8 industrial: sin redondeo.** Las esquinas rectas dan al sistema su lectura
técnica de maquila/herramienta interna. Esquinas redondeadas pertenecen al
lenguaje de consumer apps, no al de V8.

| Token | Valor | Aplica a |
|---|---|---|
| `geometria.radio_chip` | `0` | chips, badges, pills, tags |
| `geometria.radio_modal` | `0` | modales, drawers, sheets |
| `geometria.radio_boton` | `0` | botones, controles táctiles |
| `geometria.radio_input` | `0` | inputs, textareas, selects |

Cualquier redondeo requiere justificación explícita (ej. avatares circulares de
operadores — caso documentado aparte) y vive en este archivo como excepción.

## Tipografía

| Token | Familia | Fallback |
|---|---|---|
| `tipografia.titulos` | Helvetica Neue | Arial, Helvetica, sans-serif |
| `tipografia.cuerpo` | PT Serif | Georgia, Times New Roman, serif |

Tamaños (pt): título 22 · h1 13 · base 11 · pie 8. Interlineado `0.8em`, separación de párrafo `1.1em`.

## Identidad legal

V8 Labs S.A.S. · NIT 901920939-6 · Calle 48 # 57-87, Medellín · info@v8labs.co

## Cambios

Editá `brand-tokens.json` (valores) y este `BRANDING.md` (prosa) en el mismo commit.
Los consumidores que necesiten estabilidad pinean a un commit-SHA, no a `main`.
