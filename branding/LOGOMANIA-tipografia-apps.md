# Logomanía + tipografía de apps V8 — doctrina (asentado 2026-06-28)

> Sienta la **línea gráfica de las apps V8** (Metrics, Boletín, Studio, Fashion…): qué logo usa
> cada app, **tamaños límite** por contexto, y el **stylism tipográfico** (escala + estados).
> SSOT de consumo: `brand-tokens.json` + este doc. Gobierna diseno/0007 (branding = dueño del estándar).

## 1. Estrategia de logo por app (jerarquía del ecosistema)
- **App insignia = V8 Notifications:** lleva el nombre **V8** (es el punto clave del negocio: conectar
  talentos / ecosistema). Tiene ícono propio.
- **Apps secundarias** (Metrics, Boletín, Studio, Fashion, Dialogue…): por ahora, **INTERIM**:
  - **Logo en header/login/splash:** el **wordmark "V8 <Nombre>"** (Balgin, blanco sobre fondo V8
    #262b39) — ej. `wordmark-v8metrics-blanco.svg`. Consumir el SVG, no dibujar texto.
  - **Ícono cuadrado (home-screen PWA):** **monograma interino** (la inicial en Balgin, blanco sobre
    #262b39) hasta definir símbolo propio — ej. `app-icons/metrics-pwa-icon-interim-512.png`.
  - **Símbolo propio:** se diseña por app cuando se priorice (geométrico, estilo V8: rectas, trazo
    ~2px, sin bézier salvo círculo real, radius 0, lima solo destello). branding propone, Andy aprueba.

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

**Estado "EN VIVO / ATENCIÓN"** (el patrón de Notifications, codificado al canon):
- El destaque lo da **el acento lima `#A2E771` como DESTELLO, nunca relleno de superficie**:
  livedot, micro-label en lima, o subrayado/borde fino lima.
- Fondo oscuro (#262b39): texto base `#f1f1f1` + **acento lima** (dot/label/underline).
- Fondo claro (#D9DCE0): texto base `#262b39` + **acento lima** (o el azul-grafito como realce).
- ⚠️ A CONFIRMAR con notifications: la receta exacta del "texto verde sobre realce" que describe Andy
  (¿lima como TEXTO del micro-label? ¿pill con borde lima?) → codificar la versión final acá tras ver
  `app_V8_NOTIFICATIONS/src/index.css`. Regla dura mientras tanto: lima jamás como relleno de área.

## 4. Pendiente / plan
- Confirmar receta exacta del estado "en vivo" con notifications (ver index.css) → cerrar §3.
- Diseñar símbolos propios por app cuando se prioricen (3 propuestas Metrics ya enviadas).
- Review por-marca (`core_v8_brand/scripts/brand-audit.py`) corriendo desde branding (diseno/0007).
