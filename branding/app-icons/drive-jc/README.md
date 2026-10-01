# drive-jc — la cara de Drive en drive.jeanscolombianos.com

> ⚠ **PROVISIONAL — pendiente de bendición de Andy.** Jeans Colombianos NO tiene manual de
> marca ni tokens en este SSOT (2026-09-30). Los colores de abajo no son inventados pero
> tampoco son ley: están **medidos del sitio vivo jeanscolombianos.com** (CSS del tema
> Shopify, 558 KB: `#043b59` aparece 100 veces, es el color de la casa; `#56cfe1` es su
> acento). Cuando Andy los bendiga —o entregue el manual real de JC— esto pasa a
> `brand-tokens.json` como paleta de host y se quita este aviso.

## Construcción — la MISMA que V8, otra placa
Andy pidió «la misma iconografía de los íconos V8 (Balgin Bold, monograma, punto de firma)
adaptada al lenguaje de Jeans Colombianos». Eso es exactamente lo que hay: misma geometría,
mismos generadores, otra placa y otro punto. **Nunca otra geometría.**

| pieza | V8 (drive.v8labs.co) | JC (drive.jeanscolombianos.com) |
|---|---|---|
| placa | `#262b39` | `#043b59` — azul petróleo/denim de JC |
| tinta | `#FFFFFF` (14.1:1) | `#FFFFFF` (11.9:1) |
| punto de firma (favicon) | lima `#A2E771` | cian `#56cfe1` |
| `theme-color` del manifest | `#262b39` | `#043b59` |
| ícono de lanzador (PWA) | palabra **Drive** | palabra **Drive** (misma) |
| favicon de pestaña | monograma **Dr** | monograma **JC** |
| wordmark del header | `wordmark-drive-blanco.svg` | el mismo, sobre `#043b59` |

## Archivos
- `drive-jc-icon-192.png`, `drive-jc-icon-512.png` → manifest `purpose: "any"`
- `drive-jc-icon-maskable-512.png` → manifest `purpose: "maskable"` (declarar APARTE del any)
- `drive-jc-apple-touch-180.png` → `<link rel="apple-touch-icon">` (fondo sólido, sin alpha)
- `drive-jc-icon.svg` / `-maskable.svg` → fuentes vectoriales
- favicon: `branding/favicons/drive-jc.svg`

## Por qué el lanzador lleva la PALABRA y no el monograma (LOGOMANIA §1, lord 2026-08-02)
El monograma-inicial murió como ícono de home-screen: lo supersede la palabra literal.
**Sigue vigente solo como favicon de pestaña**, donde a 16–32 px la palabra no se lee.
Dos superficies, dos reglas: home = palabra · pestaña = monograma. Vale para los dos hosts.

Generadores: `core_v8_brand/scripts/app-icon.py "Drive" <out> --bg "#043b59" --slug drive-jc`
y `branding/favicons/_generate_monogram.py drive-jc JC --bg "#043b59" --accent "#56cfe1"`.
