# core_v8_assets

Repo de **assets estáticos compartidos V8Labs** — sirve PNG, SVG, PDFs, fonts y otros archivos vía `raw.githubusercontent.com` a apps internas y públicas.

## Para qué

- **CDN gratuito** vía GitHub raw URLs (sin necesidad de Cloudflare Images o S3 para assets simples).
- **Un solo lugar versionable** para activos compartidos entre múltiples apps/scripts (footers PDF, logos, plantillas, etc.).
- **Rotación trazable**: si cambia un logo, el commit deja constancia y los consumidores pueden pinear a un SHA específico si quieren estabilidad.

## Cómo consumirlo desde código

URL pattern:

```
https://raw.githubusercontent.com/V8Labs/core_v8_assets/<ref>/<path>
```

Donde `<ref>` puede ser:
- `main` — siempre la última versión (cambia con cada push)
- `<commit-sha>` — versión congelada (recomendado para producción crítica)
- `<tag>` — release fijo (ej. `v1.0.0`)

Ejemplos:

```javascript
// GAS / Apps Script
const footerUrl = "https://raw.githubusercontent.com/V8Labs/core_v8_assets/main/branding/footer_pdf.png";
const footer = UrlFetchApp.fetch(footerUrl).getBlob();

// Node / TypeScript
const logoUrl = "https://raw.githubusercontent.com/V8Labs/core_v8_assets/abc1234/branding/logo.svg";
```

## Estructura propuesta

```
core_v8_assets/
├── branding/        ← logos, colores, footers PDF
├── icons/           ← iconos SVG genéricos
├── templates/       ← templates HTML/PDF compartidos
├── fonts/           ← fonts custom
└── misc/            ← lo que no encaje
```

## Sistema de marca

La identidad de V8 Labs (logo, colores, tipografía) es un **sistema compartido**
que toda app debe seguir:

- **[`branding/BRANDING.md`](branding/BRANDING.md)** — guía legible + cómo consumirla.
- **[`branding/brand-tokens.json`](branding/brand-tokens.json)** — valores machine-readable (colores, fuentes, espaciados, logos).
- `branding/logo.svg` · `logo.png` · `logo-hi.png` — logos canónicos.

Estado actual: provisional. Se itera en `ops-admin-documentos` hasta aprobar el diseño.

## Reglas

- **Es público.** Cualquier cosa aquí es visible a todo el mundo. **NO subir nada confidencial** (NDAs, fotos privadas de clientes, info personal).
- **Optimizar antes de subir**: PNGs comprimidos (TinyPNG), SVGs minificados, PDFs sin metadata.
- **No binarios grandes**: si pesa >5 MB, considerá Cloudflare R2 o un bucket. Git no es bueno con binarios grandes.
- **Nombres kebab-case sin espacios** (constitución V8Labs §1).
- **Commit messages** describiendo el cambio: `feat(branding): add footer_pdf v2 with new logo`.

## Relación con otros assets V8Labs

- **Reemplaza progresivamente** a `andycoding1/fxckboy-assets` (legacy personal repo). Migrar asset por asset cuando convenga; actualizar URLs hardcoded en scripts consumidores en el mismo PR.
- **NO confundir** con assets ESPECÍFICOS de un proyecto (logos del theme Shopify viven en `app_V8_ECOMMERCE`, no acá).

## Consumidores conocidos (actualizar al agregar)

| App / Script | Asset usado |
|---|---|
| `ops-admin-documentos` | `branding/` (sistema de marca: tokens + logos) |
