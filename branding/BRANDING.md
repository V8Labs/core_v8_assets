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

## Colores

| Token | Hex | Uso |
|---|---|---|
| `color.primario` | `#262b39` | títulos, acentos, reglas |
| `color.texto` | `#1a1a1a` | texto cuerpo |
| `color.tenue` | `#6b7280` | metadatos, pies, secundario |
| `color.linea` | `#d1d5db` | reglas y bordes suaves |

### Paleta de estados — colores Notion vivos (`color.notion`)

Versión **viva y plana** (estética cartel suizo, ref. Musik Akademie Basel) de
los **10 colores nombrados de Notion**. Notion solo maneja estos 10 nombres (no
acepta hex arbitrario); cada opción de un select/status/tag en Notion lleva uno,
y la app lo **rinde vívido** con este hex. **Texto siempre negro** (`color.notion.texto_sobre`)
sobre el bloque. Sirve para estados de tareas, tags, y cualquier propiedad
coloreada de cualquier app del ecosistema.

| Nombre Notion | Hex |
|---|---|
| `default` | `#E8E5DD` |
| `gray` | `#9AA0AC` |
| `brown` | `#B0764A` |
| `orange` | `#F2872E` |
| `yellow` | `#FCE302` |
| `green` | `#3FBE83` |
| `blue` | `#3D7CD6` |
| `purple` | `#8E6BD4` |
| `pink` | `#F5BFCB` |
| `red` | `#F26159` |

> El mapeo *opción de estado → nombre de color* lo define cada base en Notion
> (lo ingiere Mirror a `notion_schema_registry.property_config`). Acá vive solo
> el hex por nombre. El rojo destructivo de UI (`#E11900`) NO es este `red`.

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
