# UX/UI del canónico V8 Labs — cómo se cura

Hasta hoy el canónico (`core_v8_assets/branding/`) cubría **estática**: color,
tipografía, logo, datos de empresa. Pero las apps (`app_V8_NOTIFICATIONS`,
`ops-admin-documentos`, etc.) ya cocinan **patrones de interacción, componentes y
voz de UI** que se repetirían descoordinados si cada app los reinventa. Este
documento define **cómo eso entra al canónico sin caos**.

> 📕 **Manual de patrones canónico:** [`UX-PATTERNS.md`](UX-PATTERNS.md) — sistema de
> diseño completo (filosofía, tipografía, geometría, color, layouts, componentes, gestos,
> auth, anti-patterns). Origen: notifications; curado y asentado por branding (2026-06-01).

## Principio rector (regla de oro)

> **La app CONSUME, no REDEFINE.** Si una app necesita un token, patrón o
> componente que no existe en el canónico, **lo propone** (PR) — no lo inventa
> local y sigue. branding cura qué entra y en qué forma.

Esto preserva una sola fuente de verdad y evita la deriva (ej. tres "azules de
botón" distintos en tres apps).

## Las 3 capas de UX (qué vive dónde)

| Capa | Qué es | Dónde vive | Formato |
|---|---|---|---|
| **Tokens** | Valores: color, radii, motion, focus, escala, tonos semánticos | `brand-tokens.json` (bloque `ux`) | JSON machine-readable |
| **Patrones** | Convenciones de interacción reutilizables (swipe-armed, confirm modal, picker con buscador…) | `branding/ux/patterns/*.md` | 1 MD por patrón |
| **Componentes** | Implementación concreta (botón, input, card) | hoy **referencia/snippet** en el patrón; NO hay librería de código compartida todavía | snippet React de referencia |

> Honesto: **no existe un design system de código** (librería npm compartida) aún.
> Por ahora el canónico gobierna **decisiones** (tokens + patrones + reglas), y
> cada app implementa siguiéndolas. Si más adelante vale una librería, se decide
> aparte.

## El proceso de curación

```
1. La app cocina un patrón/token en su repo (resolviendo un problema real).
2. La app abre PR al canónico:
   - token  → propone entrada en brand-tokens.json (bloque ux)
   - patrón → propone branding/ux/patterns/<nombre>.md
3. branding CURA:
   - ¿es genérico y reutilizable? (si es específico de una app, no entra)
   - ¿respeta las reglas de marca? (ej. la regla del verde acento)
   - ¿pisa algo existente? → unificar, no duplicar
   → acepta / edita / rechaza con razón.
4. Mergeado a main → las apps lo CONSUMEN por raw URL / copia build-time.
```

**Canal:** PR a `core_v8_assets` + aviso por el bus de agentes (`branding/inbox/`).
Cambios chicos también pueden negociarse primero por inbox y luego PR.

## Formato de un patrón (`patterns/<nombre>.md`)

Cada patrón documenta, en orden:
1. **Cuándo usarlo** (y cuándo NO).
2. **Comportamiento** (el gesto/flujo, paso a paso).
3. **Reglas de marca que aplica** (tokens, color, motion).
4. **Snippet de referencia** (React u otro, ilustrativo — no es la implementación oficial).

## Reglas de color en UI (resumen — la ley completa en `../BRANDING.md`)

- **Fondo base:** `primario #262b39`. Negro/blanco = base.
- **Verde `acento` #A2E771:** acento VIVO (enlaces, subrayados, glow/animación de
  marcos). **NUNCA fondo de botón ni superficie extensa.** (Ver regla dura en BRANDING.md.)
- **Botones:** base o color semántico de acción — nunca el verde de marca.

## Pendientes de curar (cola)

### Tokens UX a canonizar (de `app_V8_NOTIFICATIONS`, vía PR)
- `radii`: 0 por default (V8 es de esquinas duras); excepciones a normalizar.
- `motion`: `swipeThreshold`, `longPressMs`.
- `iosInputMinFontSize`: 16px obligatorio (debajo, iOS hace zoom y rompe la UI).
- **Color semántico (estado, NO identidad)** — PROPUESTO, pendiente OK de Andy:
  `positivo #3FBE83` · `negativo #E11900` · `neutral #f1f1f1`. ⚠️ El verde
  semántico `#3FBE83` es OTRO verde, distinto del `acento #A2E771` de marca: el
  semántico SÍ puede rellenar un botón de confirmar; el de marca no. No confundirlos.

### Patrones (de notifications) — ✅ documentados en `UX-PATTERNS.md`
swipe-armed, confirm-modal, picker con buscador, AutoGrowTextarea, auth-gateway, card
system (kanban) y demás ya viven en [`UX-PATTERNS.md`](UX-PATTERNS.md). Si alguno crece a
necesitar su propio archivo detallado, se desglosa a `patterns/<nombre>.md` vía PR.

### Iconografía
Set minimal line de notifications (`src/components/icons/`). Decisión pendiente:
¿promover a `branding/icons/` como set canónico? Mientras tanto, por-app.

### Deuda de color a reconciliar
Las apps usan `bg #2f3547` (notifications, documentos) que **NO coincide** con
`primario #262b39`. **Resolución (regla de oro): la app se alinea al canónico.**
Migrar `#2f3547 → #262b39` en cada app. Si hay razón visual para mover el canónico
en vez de la app, se discute y se cambia el canónico (una vez), no cada app por su lado.

## Voz de UI

Distinta de la voz de cada marca de venta (FXCKBOY, etc.). La voz de las **apps
internas V8** (asistente, estados, microcopy) se define como parte de este sistema.
Pendiente: redactar `branding/ux/voz-ui.md` (tono del asistente V8, estados como
"V8 está revisando…", etc.). Hoy las apps improvisan ("Hola 👋 Soy el asistente") —
a canonizar.
