# Logomanía + tipografía de apps V8 — doctrina (asentado 2026-06-28)

> Sienta la **línea gráfica de las apps V8** (Metrics, Boletín, Studio, Fashion…): qué logo usa
> cada app, **tamaños límite** por contexto, y el **stylism tipográfico** (escala + estados).
> SSOT de consumo: `brand-tokens.json` + este doc. Gobierna diseno/0007 (branding = dueño del estándar).

## 1. Estrategia de logo por app (jerarquía del ecosistema)
- **App insignia = V8 Notifications:** lleva el nombre **V8** (es el punto clave del negocio: conectar
  talentos / ecosistema). Tiene ícono propio.
- **Apps secundarias** (Metrics, Boletín, Studio, Fashion, Dialogue…): **SOLO LETRAS / nombre**
  (decisión Andy 2026-06-28 — NO símbolos propios). El nombre ES el logo:
  - **Logo en header/login/splash:** el **wordmark "V8 <Nombre>"** (Balgin, blanco sobre fondo V8
    #262b39) — ej. `wordmark-v8metrics-blanco.svg`. Consumir el SVG, no dibujar texto.
  - **Ícono cuadrado (home-screen PWA) = la PALABRA de la app** (Andy 2026-06-29; supersede el
    monograma-inicial). Receta CANÓNICA (generador `core_v8_brand/scripts/app-icon.py`, mismo trato
    que el ícono "V8" de notifications):
    - Balgin Expanded **BOLD** · texto **blanco #FFFFFF** sobre **#262b39** · cuadrado · palabra
      centrada (H+V) · **proporción NATURAL del font** (no deformar / no textLength) · font-size tal
      que el ancho natural ocupe **~75%** del cuadro (any) / **~60%** (maskable, safe-area 10-12%).
    - Salidas: SVG vectorizado + PNG 512(any) · 512(maskable) · 192 · 180(apple-touch).
    - Ej.: `app-icons/metrics/metrics-icon-*`, `app-icons/boletin/boletin-icon-*`.
    - ⚠️ Balgin DEMO no trae acentuadas (í/é…) → el render normaliza ("Boletín"→"Boletin"); la tilde
      requiere la Balgin licenciada.
  - **Sin símbolo gráfico** — el sistema es la palabra (wordmark + ícono-palabra). (Símbolo propio:
    branding propone y Andy aprueba; hoy NO.)

## 2. Tamaños límite (logomanía) — por contexto de uso
| Uso | Tamaño (alto) | Nota |
|---|---|---|
| **Marcador / puntual** (estilo Mind en Notifications) | **16–20 px** | solo ícono, muy chico |
| **Footer** | **18–24 px** | wordmark o ícono, discreto |
| **Header / nav** | **24–32 px** | wordmark chico o ícono 28–32 |
| **Login / splash / central** | **40–56 px** | el grande pero CONTENIDO; ref = login de Notifications. NO gigante. En móvil ≤ ~12% del alto del viewport |
| **PWA app icon** (home screen) | **512×512** | safe-area ~10–12% margen, maskable |
| **Foto de perfil** (WhatsApp/social) | **1024×1024** | logo/ícono centrado, margen para crop circular |
- **Zona de exclusión:** ≥ la altura de la "8"/X del wordmark, libre alrededor.
- ⚠️ FIX Metrics: el logo del login estaba GIGANTE → bajarlo al rango **login 40–56 px** (como Notifications).

## 3. Tipografía — stylism (escala + pesos + estados)
**Familias (apps/UI):** IBM Plex Sans = sistema/UI (la voz funcional). Balgin Expanded = wordmark.
(Documentos: Helvetica Neue títulos + PT Serif cuerpo — no aplica a UI de app.)

**Escala (IBM Plex Sans, apps):**
| Rol | Peso | Tamaño ref | Uso |
|---|---|---|---|
| Título (h1) | 600 | 28–34 px | encabezado de pantalla |
| Título secundario (h2) | 600 | 20–24 px | secciones |
| Subtítulo (h3) | 500 | 16–18 px | sub-secciones |
| Frase destacada | 500/600 | 16–20 px | callouts |
| Párrafo (body) | 400 | 14–16 px | texto corrido |
| Utility / label | 500 | 11–13 px | labels, ejes, captions |

**Estado "EN VIVO / ATENCIÓN"** — receta CANÓNICA (leída de `app_V8_NOTIFICATIONS/src/index.css`,
clases `.v8-accent-chip` / `.v8-accent-soft`). El destaque lo da el **acento lima `#A2E771` como
DESTELLO, nunca relleno de área**:
- **Fondo CLARO (light):** **pill oscuro `#262b39`** (token `--v8-accent-on`) **+ texto lima `#A2E771`**.
  (= "si el fondo es blanco, el fondo de la letra va azul-grafito con la letra verde".)
- **Fondo OSCURO (dark):** **texto lima `#A2E771`** solo, **sin pill** (`--v8-accent-on` es no-op en dark).
- **Pulso de atención** (algo llega/sucede ahora): keyframe con lima a baja opacidad — `bg rgb(accent/0.16)`,
  `border rgb(accent/0.7)`, `border-left rgb(accent/0.9)`. Un parpadeo sutil, no un relleno.
- Variante suave: `.v8-accent-soft` (texto lima, sin chip).
- Tokens a consumir: `--v8-accent` (#A2E771) y `--v8-accent-on` (#262b39). Misma clase para TODAS las
  apps (Metrics, Boletín…) → coherencia del "en vivo" en el ecosistema.

## 4. Estado
- ✅ Estado "en vivo" codificado (§3) desde el código real de Notifications.
- ✅ Apps secundarias = SOLO LETRAS (sin símbolos propios) — decisión Andy 2026-06-28.
- ✅ Review por-marca (`core_v8_brand/scripts/brand-audit.py`) corriendo desde branding (diseno/0007).
- Cada app aplica esta doctrina por su cuenta (auto-aplicación); branding arbitra por excepción.
