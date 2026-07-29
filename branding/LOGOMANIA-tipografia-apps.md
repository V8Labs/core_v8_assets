# Logomanía + tipografía de apps V8 — doctrina (asentado 2026-06-28)

> Sienta la **línea gráfica de las apps V8** (Metrics, Boletín, Studio, Fashion…): qué logo usa
> cada app, **tamaños límite** por contexto, y el **stylism tipográfico** (escala + estados).
> SSOT de consumo: `brand-tokens.json` + este doc. Gobierna diseno/0007 (branding = dueño del estándar).

## 0. Nombre de las apps — el prefijo V8 (decisión Andy 2026-07-27)

**El prefijo "V8" NO se usa en el nombre de las apps. Queda reservado a UNA sola.**

- **App de entrada a la gestión = "V8 Labs"** — es la que hoy se llama *Notifications*. Se
  renombra a **V8 Labs** y es la ÚNICA que lleva V8 en el nombre. Es la puerta al ecosistema:
  por eso carga la marca de la casa.
- **Todas las demás van con su nombre pelado:** **Metrics · Studio · POS · Boletín · Fashion ·
  Dialogue · Media · Rooms · Lounge · Ecommerce**. Sin "V8" adelante, en ningún lado visible.

**Dónde aplica (nombre VISIBLE):** `manifest.webmanifest` (`name` y `short_name` — es el nombre
con que la PWA se **graba** en la pantalla de inicio), `<title>` del HTML, wordmark del
header/login/splash, ícono, y cualquier rótulo de la app hacia el usuario.

**Dónde NO aplica:** los repos y carpetas siguen llamándose `app_V8_*`, y los `.agent-name`,
alias de comms y remotes de GitHub **no se tocan** (Andy 2026-07-27: renombrarlos rompería
comms, launchers y rutas del ecosistema entero, sin ganancia visible para nadie).

## 1. Estrategia de logo por app (jerarquía del ecosistema)
- **App insignia = V8 Labs** (ex-Notifications): lleva el nombre **V8** (es el punto clave del
  negocio: conectar talentos / ecosistema; y es la entrada a la gestión). Tiene ícono propio.
- **Apps secundarias** (Metrics, Boletín, Studio, POS, Fashion, Dialogue…): **SOLO LETRAS / nombre**
  (decisión Andy 2026-06-28 — NO símbolos propios). El nombre ES el logo:
  - **Logo en header/login/splash:** el **wordmark con el nombre PELADO** (Balgin, blanco sobre
    fondo V8 #262b39) — ej. `wordmark-metrics-blanco.svg`. Consumir el SVG, no dibujar texto.
    ⚠️ Los wordmarks viejos con prefijo (`wordmark-v8metrics-*`) quedan **deprecados** por §0.
  - **Ícono cuadrado (home-screen PWA) = la PALABRA de la app** (Andy 2026-06-29; supersede el
    monograma-inicial). Receta CANÓNICA (generador `core_v8_brand/scripts/app-icon.py`, mismo trato
    que el ícono "V8" de notifications):
    - Balgin Expanded **BOLD** · texto **blanco #FFFFFF** sobre **#262b39** · cuadrado · palabra
      centrada (H+V) · **proporción NATURAL del font** (no deformar / no textLength) · font-size tal
      que el ancho natural ocupe **~75%** del cuadro (any) / **~60%** (maskable, safe-area 10-12%).
    - Salidas: SVG vectorizado + PNG **1024(master)** · 512(any) · 512(maskable) · 192 · 180(apple-touch).
    - Ej.: `app-icons/metrics/metrics-icon-*`, `app-icons/boletin/boletin-icon-*`,
      `app-icons/studio/studio-icon-*`.
    - ⚠️ El fondo va **SÓLIDO** (#262b39), nunca transparente: iOS no respeta alpha en
      `apple-touch-icon` y el redondeo de esquina lo dibuja el sistema — no lo dibujes vos.
    - 🗑️ **Deprecado el monograma-inicial** (`pwa/studio-st.*` = "St"): lo supersede la palabra
      literal. No consumir esos archivos.
    - ⚠️ Balgin DEMO no trae acentuadas (í/é…) → el render normaliza ("Boletín"→"Boletin"); la tilde
      requiere la Balgin licenciada.
  - **Sin símbolo gráfico** — el sistema es la palabra (wordmark + ícono-palabra). (Símbolo propio:
    branding propone y Andy aprueba; hoy NO.)
  - **Variante "cara pública" con dominio** (Andy 2026-07-27, primer caso: Boletin.app): para
    landing / redes / firma / splash, el nombre puede armarse como **lockup de DOS LÍNEAS
    apiladas y justificadas al mismo ancho** — nombre arriba, `.app` abajo **escalado hasta
    igualar EXACTAMENTE el ancho de la línea de arriba** (ambos bordes coinciden). Las dos
    líneas en Balgin Expanded Bold. Generador: `core_v8_brand/scripts/boletin-app-lockup.py`.
    Assets: `wordmark-boletin-app[-blanco].svg`. El header/nav interno sigue usando el
    wordmark de UNA línea.
    ⚠️ En esta variante el nombre va **sin tilde** por ser un dominio (boletin.app), no por
    la limitación de la Balgin DEMO.
  - **Ícono de app CUANDO la app tiene lockup con dominio** (Andy 2026-07-28, a raíz de que el
    ícono de Boletin.app no sobrevivía a 48px): el ícono lo arma el **lockup de dos líneas**, no
    la palabra suelta — el apilado le da ~2,4× más altura de letra en el mismo cuadro, y es lo
    único que se lee en la home screen. Generador: `core_v8_brand/scripts/app-icon-lockup.py`.
    - El lockup se escala hasta **TOCAR el círculo** de 94% del lado (any) / **80%** (maskable,
      la zona que Android garantiza) — no contra el cuadrado. Se descuenta el PAD del viewBox
      del lockup: si no, ese aire se suma al margen y el ícono queda chico y flotando.
    - **Sin contorno.** A 48px el trazo oscuro cierra los huecos de la "o" y la "p" y el ícono
      se vuelve mancha. El contorno es para tamaños grandes, no para el ícono.
    - Fondo sólido y **sin esquinas redondeadas propias** (las dibuja el sistema).
    - **Paleta = la del sistema V8**: blanco #FFFFFF sobre #262b39, igual que el ícono-palabra
      (Andy 2026-07-28). El ícono de app es superficie de ecosistema, no de la marca suelta:
      en la home screen las apps V8 se reconocen entre sí por el fondo. La paleta propia de la
      app (ej. crema/oro de Boletín) vive en el logo y en la foto de perfil, no acá.
    - Ej.: `app-icons/boletin/boletin-app-icon-*`.
    - 🗑️ Queda fuera de uso como ícono `boletin-app-avatar-oro-1024.png` (era un avatar de
      perfil, apaisado y con aire muerto arriba y abajo); sigue sirviendo de foto de perfil.

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
- ✅ Nombre sin prefijo V8 en todas las apps salvo **V8 Labs** (ex-Notifications) — Andy 2026-07-27.
  Pendiente de aplicación por cada app: manifest, title, wordmark, ícono.
- ✅ Estado "en vivo" codificado (§3) desde el código real de Notifications.
- ✅ Apps secundarias = SOLO LETRAS (sin símbolos propios) — decisión Andy 2026-06-28.
- ✅ Review por-marca (`core_v8_brand/scripts/brand-audit.py`) corriendo desde branding (diseno/0007).
- Cada app aplica esta doctrina por su cuenta (auto-aplicación); branding arbitra por excepción.
