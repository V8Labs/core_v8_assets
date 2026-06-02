# V8 Labs — UX/UI Patterns para apps del ecosistema

> **Estado: CANÓNICO.** Curado por `branding` y asentado en `core_v8_assets/branding/ux/`
> el 2026-06-01. Origen: escrito por `notifications` (`app_V8_NOTIFICATIONS`). Gobierno =
> igual que `BRANDING.md`: cambios estructurales requieren commit a `core_v8_assets` con
> aprobación de branding; patrones nuevos validados en producción se proponen por PR.
>
> **Audiencia:** agentes y devs armando apps `*.v8labs.co` (dealer, studio, metrics, boletín…).
>
> ### ⚠️ Cómo leer este doc (nota de curación)
> Dos niveles, no confundir:
> - **LEY UNIVERSAL V8** (aplica a TODA app): consumir tokens del SSOT (§2-3), tipografía y
>   tracking (§4), geometría radius ≤3px / sin shadows-gradients-glow (§5), reglas de color
>   incl. **verde acento solo líneas/enlaces, nunca relleno** (§6 — coincide con `BRANDING.md`),
>   estados/optimistic (§11), auth SSO cross-subdominio (§12), anti-patterns (§15).
> - **REFERENCIA de notifications** (ilustrativa, NO obligatoria para otras apps): el fondo malla
>   de información (§7), los layouts capa1/capa2/kanban (§8), el catálogo de componentes con paths
>   `src/...` (§9), gestos concretos (§10). Adoptá el **principio**, no la estructura literal de esa app.
>
> **Tokens:** la fuente de verdad sigue siendo `brand-tokens.json` + `BRANDING.md`. Este doc NO
> los redefine. ⚠️ Pendiente de canonizar a `brand-tokens.json` (cola en `ux/README.md`): los tokens
> UX referidos como `--v8-*` (`bg-deep`, `fg-mute`, `line`, `danger #E11900`) y la **paleta de estados
> kanban** (§6) — hoy viven en la app; deben subir al SSOT para ser ley, no solo referencia.

---

## 0. Lectura mínima de 30 segundos

Si solo tenés 30s, llevate esto:

1. **Consumí tokens del SSOT**, no inventes valores. Repo:
   `V8Labs/core_v8_assets/branding/brand-tokens.json` + `BRANDING.md`.
2. **Helvetica Condensed** (con fallbacks), **3 pesos**, mayúsculas con tracking
   generoso en metadata.
3. **Radius ≤ 3px** en TODO. Sin gradients. Sin shadows. Sin glow. Sin
   glassmorphism. Sin neón.
4. **bg primario** `#262b39`, **fg primario** `#f1f1f1`, **destructivo** `#E11900`
   (rojo SOLO para cancelar/rechazar).
5. **Fondo = información ambiente** (malla de píxeles + datos macro reales),
   NO decorativo.
6. **Capa 1** = bottom-nav 2 botones (KANBAN + INBOX). **Capa 2** = (DETALLE
   + CHAT) o solo CHAT (notif sin Notion source).
7. **Gestos > botones**. Swipe horizontal cambia columna, drag-drop mueve
   estados, two-finger trackpad swipe cambia entre detalle y chat.
8. **Optimistic UI**: el cliente pinta el cambio inmediato, el server (Mirror)
   reconcilia.

---

## 1. Filosofía

La marca es **laboral industrial**, NO consumer-redondito. El operador es la
unidad central; la app es su "terminal" — no un panel decorativo. Decisiones
load-bearing:

- **El operador es dios** — presencia activa, suscripción explícita, anti-push
  agresivo. La app no notifica de más; el operador decide qué ve.
- **La app es thin client** — captura gestos, renderiza estado. La lógica de
  negocio vive en el server (Supabase Mirror + Mind/Edge Functions). Doctrina
  formal:
  `core_v8_doctrine/empresa/0003-reglas-negocio-server-side.md`.
- **Cero over-engineering de UI** — Tailwind sobre Material/Chakra por control
  visual estricto. SVGs inline propios en lugar de librerías de íconos.
- **Tipografía como identidad** — Helvetica Condensed única, tracking generoso,
  mayúsculas. Es la pieza más visible del branding después del color.

Bitácora histórica con el "por qué" de cada decisión:
`V8Labs/app_V8_NOTIFICATIONS/docs/BITACORA.md`.

---

## 2. SSOT del branding (NO duplicar)

Repo canónico: `V8Labs/core_v8_assets/branding/`.

| Archivo | Qué tiene | Cómo consumir |
|---|---|---|
| `brand-tokens.json` | colores, tipografía, geometría, datos legales | fetch raw URL (runtime) o import build-time, mapear a CSS vars |
| `BRANDING.md` | versión prosa del sistema | leer una vez, no duplicar |
| `favicons/<app>.svg` | favicon por-app (V8 + acento verde) | `<link rel="icon" type="image/svg+xml" href="/favicon.svg">` |
| `logo.svg` / `logo.png` | logo principal | NO deformar, NO recolorear |

Raw URL para fetch runtime:

```
https://raw.githubusercontent.com/V8Labs/core_v8_assets/main/branding/<archivo>
```

> Pineá a un commit-SHA si necesitás estabilidad determinística.

Skill consultivo para todo agente que toque marca:
`~/.claude/skills/v8labs-branding/SKILL.md`.

---

## 3. Tokens (CSS vars + Tailwind)

Patrón: **definir CSS vars en `src/index.css`** desde `brand-tokens.json`, y
**mapear en `tailwind.config.js`** vía `colors.v8.<token>` para que las clases
Tailwind se resuelvan a vars. Beneficios: light/dark sin reescribir clases.

Ejemplo del config vivo (`tailwind.config.js`):

```js
colors: {
  v8: {
    bg:       'rgb(var(--v8-bg) / <alpha-value>)',
    'bg-deep':'rgb(var(--v8-bg-deep) / <alpha-value>)',
    fg:       'rgb(var(--v8-fg) / <alpha-value>)',
    'fg-mute':'rgb(var(--v8-fg-mute) / <alpha-value>)',
    danger:   'rgb(var(--v8-danger) / <alpha-value>)',
    line:     'rgb(var(--v8-line) / <alpha-value>)',
    accent:   'rgb(var(--v8-accent) / <alpha-value>)',
  },
  // estados kanban + sub-paleta mesh — ver tailwind.config.js
}
```

CSS vars en `:root` y override en `[data-theme="light"]`. Toggle vía
`document.documentElement.dataset.theme = 'light' | 'dark'`.

**Acento (verde lima brand):** SOLO líneas, enlaces e indicadores activos.
**NUNCA** rellenos grandes. En light mode el accent visible se invierte a
"v8-accent-chip" (píldora oscura sobre fondo claro). Convención:
`geometria.radio_chip = 0` en tokens — los chips de marca son **rectángulos
duros**, no píldoras redondeadas.

---

## 4. Tipografía

**Familia única:** Helvetica Condensed con fallbacks.

```css
font-family: "Helvetica Neue Condensed", "Helvetica Neue", Helvetica,
             "Inter Condensed", Inter, system-ui, sans-serif;
```

**Pesos:** Light / Regular / Bold (3, no más).

**Escala** (Tailwind `text-*`):

| Token | Tamaño | Line-height | Tracking | Uso |
|---|---|---|---|---|
| `text-meta` | 12px | 1.4 | 0.08em | metadata, labels, tabs |
| `text-body` | 15px | 1.5 | — | cuerpo de texto |
| `text-h2` | 18px | 1.3 | 0.02em | títulos secundarios |
| `text-h1` | 24px | 1.2 | — | títulos primarios |
| `text-display-l` | 32px | 1.1 | — | display |
| `text-display-xl` | 48px | 1.05 | -0.01em | hero/wordmark |

**Tracking semántico** (no inventar más):

| Clase | Tracking | Cuándo |
|---|---|---|
| `tracking-tag` | 0.08em | metadata uppercase, tabs, props |
| `tracking-action` | 0.10em | botones uppercase (`ARRANCAR`, `CANCELAR`) |
| `tracking-wide` | 0.05em | uso general "esto va en mayúsculas" |

**Mayúsculas + tracking** son el sello tipográfico. La regla de oro:

> Si vas a poner texto en MAYÚSCULAS, va con `tracking-tag` o
> `tracking-action`. Mayúsculas SIN tracking se ven como error.

---

## 5. Geometría

- **Border radius:** máximo **3px** en TODOS los contenedores. Tailwind
  override:
  ```js
  borderRadius: {
    DEFAULT: '3px', sm: '2px', md: '3px', lg: '3px', xl: '3px', none: '0',
  }
  ```
  Las clases tipo `rounded-2xl` siguen aceptadas en el lint pero resuelven a
  3px. Esto es a propósito — preferí no editar líneas existentes.

- **Sin shadows.** No usamos `shadow-*`. Si necesitás separar visualmente,
  usá `border-v8-line` o `bg-v8-bg-deep` (un nivel más oscuro/claro).

- **Sin gradients ni glow.** Prohibido absoluto. Si Andy te lo pide,
  contrapropone con paleta plana.

- **Líneas duras:** divisores con `border-b border-v8-line`. 1px puro, no
  gradient borders.

---

## 6. Color — reglas duras

| Color | CSS var | Uso |
|---|---|---|
| `v8-bg` (`#262b39` dark) | `--v8-bg` | fondo primario |
| `v8-bg-deep` | `--v8-bg-deep` | fondo secundario (un nivel más profundo) |
| `v8-fg` (`#f1f1f1`) | `--v8-fg` | texto primario |
| `v8-fg-mute` | `--v8-fg-mute` | texto secundario, metadata |
| `v8-danger` (`#E11900`) | `--v8-danger` | **EXCLUSIVO cancelar/rechazar/eliminar** |
| `v8-line` | `--v8-line` | bordes, divisores |
| `v8-accent` (lima brand) | `--v8-accent` | **SOLO líneas + enlaces + indicadores activos** |

**Estados kanban** — paleta semántica para `Estado`:

```
borrador:    #9AA0AC (gris acero)
sin-empezar: #F5D800 (amarillo brillante)
en-progreso: #7CC832 (verde lima)
verificar:   #F08019 (naranja)
programado:  #32C8B4 (teal)
retrasada:   #E53019 (coral-rojo)
terminada:   #2B9A2B (verde oscuro)
cancelada:   #B0764A (marrón)
```

Helper para mapear estado → color (bg + text):
`src/lib/notionColors.ts` → `estadoNotionColor(estado: string)`.

---

## 7. Background — malla de información ambiente

**El fondo NO es decorativo.** Es una malla de píxeles 16×16 que renderiza
**datasets macroeconómicos reales** rotando cada 12h vía
`/macro-snapshot`. Cinco-seis colores **desaturados industriales**
(`mesh-steel`, `mesh-mustard`, `mesh-olive`, `mesh-slate`, `mesh-sand`,
`mesh-charcoal`).

**Render:** Canvas2D + Web Worker (`src/components/MeshBackground.tsx` y
worker en `src/workers/`). Aplica a TODAS las rutas excepto explícitamente
listadas en `MeshGate` (login, off, callback).

**PROHIBIDO ABSOLUTO** en el fondo:

- Halos, glow, neón.
- Glassmorphism (backdrop-blur).
- Blur ondulante.
- Gradientes radiales.

> Eventualmente el fondo va a alimentar un modelo de predicción
> macroeconómica — gamificación silenciosa de la intuición del operador. Por
> eso el "ambient information", no la decoración.

---

## 8. Layouts canónicos

### 8.1. Capa 1 (entry points)

Bottom-nav con **2 botones** únicamente:

```
[ KANBAN ]   [ INBOX (N) ]
```

CHAT NO es función de capa 1 — vive dentro de cada objeto en capa 2. Esto
es load-bearing (decisión 1 del MVP-SCOPE).

### 8.2. Capa 2 (dentro del objeto)

Bottom-nav contextual:

- Si el objeto viene de Notion (tarea): `[ DETALLE ]   [ CHAT ]`.
- Si el objeto es una notif de Mind (sin Notion source): **solo CHAT**.

### 8.3. Header pattern

Todas las páginas comparten estructura:

```
┌──────────────────────────────────────────────────────────────┐
│  ← (back)    DISPLAY_ID centrado    (icon icon icon)         │ ← sticky
└──────────────────────────────────────────────────────────────┘
```

Iconos del header son **icon-only** (size=14, p-1, text-v8-fg-mute con
active:text-v8-fg). Sin marco, sin texto. La identidad la da el ícono.
Referencia: `src/components/shells/AppShell.tsx` y el header de
`TareaDetalle.tsx`.

### 8.4. Modal full-screen

Cuando un modal necesita más de 2 acciones, **NO** flotar. Usar pantalla
completa con header limpio:

```
┌──────────────────────────────────────────────────────────────┐
│  TÍTULO          (X cerrar / ✓ aplicar a la derecha)         │ ← shrink-0
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  contenido scrolleable (flex-1 overflow-y-auto)              │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  acciones secundarias (shrink-0) — opcional                  │
└──────────────────────────────────────────────────────────────┘
```

`paddingTop: 'env(safe-area-inset-top)'` y `paddingBottom:
'env(safe-area-inset-bottom)'` siempre. Compatible con notch + barra inferior
iOS/Android.

Ejemplo: el modal VISTA y FILTROS de Kanban (`src/routes/Kanban.tsx`
líneas ~466-579).

### 8.5. Carrusel de columnas (kanban gestual)

Pista única que se mueve con `transform: translateX(-idx * containerW)`.
Las columnas vecinas asoman. Drag horizontal con `onPointerMove` engancha
swipe; wheel horizontal (trackpad) hace saltos discretos.

**Umbral horizontal** que andó bien en Android:

```js
absDx >= 24 && absDx >= absDy * 1.5
```

(24px + ratio 1.5x). Más permisivo rompe el scroll vertical de columnas vacías.

Referencia: `src/routes/Kanban.tsx` y `src/components/kanban/ColumnScroll.tsx`.

---

## 9. Componentes patrones (catálogo)

### 9.1. Chip / Pill

NO redondeado (radio_chip=0). Bordes 1px, padding compacto, uppercase
metadata.

```tsx
<span className="border border-v8-line px-2 py-1 text-meta uppercase tracking-tag text-v8-fg-mute">
  {label}
</span>
```

Variante "activo" (para filtros, vistas, etc.):

```tsx
<span className="bg-v8-fg text-v8-bg border border-v8-fg px-2 py-1 text-meta uppercase tracking-tag font-bold">
  {label}
</span>
```

### 9.2. Accent chip (acento brand en light mode)

`v8-accent-chip` — píldora oscura invertida con el lima brand como detalle.
Útil para "LIMPIAR FILTROS", links inline. Definida en CSS, ver clase
`v8-accent-chip` en `src/index.css`.

### 9.3. NextAction button (icon-only del header)

Cuando una acción contextual va al header (cancelar, arrancar, programar):

```tsx
<button
  onClick={openDialog}
  className="-mr-1 p-1 text-v8-fg-mute active:text-v8-fg shrink-0"
  aria-label={action.label}
>
  <Icon size={14} />
</button>
```

Mismo size y comportamiento que los light/dark/power del AppShell.
**Sin marco, sin texto**, identidad por ícono.

### 9.4. Card (tarjeta kanban)

`src/components/kanban/TaskCard.tsx`. Características:

- Border `border-v8-line`, bg `v8-bg`.
- Title bold + meta line con `text-meta uppercase tracking-tag text-v8-fg-mute`.
- Expandible inline (no modal): click → estado `editing=id`, el card se
  estira en el track. ESC cierra; flechas mueven columna.
- Swipe horizontal sobre la card cambia estado (transitions del registry).

### 9.5. Picker relacional

`src/components/tarea/PropertyEditor.tsx`. Soporta single / multi. Opciones
ordenadas por `updated_at` desc (recientes primero), con "pin" del propio
operador al top para el caso "asignarme yo mismo".

### 9.6. AudioRecorderButton

`src/components/kanban/AudioRecorderButton.tsx`. MediaRecorder API con
fallback a webm. Sube a Storage como blob privado.

### 9.7. ChatInput / Comment input

`src/components/chat/ChatInput.tsx` y el ribbon de comments en
`src/routes/TareaDetalle.tsx`. Patrón:

```
[ AutoGrowTextarea (flex-1) ] [📎 attach] [🎙️ rec] [↑ send]
```

Multi-archivo soportado (`<input type="file" multiple>`). Audio + texto +
archivos co-existen como tipos de comment.

### 9.8. Mesh background gate

`<MeshGate>` decide cuándo renderizar la malla. Lista de exclusión por
`pathname`:

```ts
const excluded = pathname === '/login' || pathname.startsWith('/auth/') || pathname === '/off';
```

---

## 10. Interacciones / gestos

| Gesto | Acción | Where |
|---|---|---|
| Swipe horizontal sobre kanban | Cambia columna | `Kanban.tsx` onColPointerMove |
| Swipe horizontal sobre card | Estado próximo (transition) | `TaskCard.tsx` |
| Wheel horizontal | Salto discreto entre columnas (cooldown 420ms) | `Kanban.tsx` |
| Two-finger trackpad swipe en ficha | Cambia entre DETALLE y CHAT | `useTwoFingerSwipe` hook |
| ESC en card expandido | Cierra el editor inline | global key listener |
| Flechas ← → en kanban | Mueven entre columnas (no si hay input focus) | `Kanban.tsx` |
| Enter en NuevaTarea | Crea | `NuevaTarea.tsx` |
| Long press sobre card (en backlog) | Drag para mover | dnd-kit |

**Patrón anti-doble-disparo:** todo mutation crítico (post comment, create,
transition) guarda con `if (mutation.isPending || uploading) return` al
inicio del handler. Pasa con doble-tap del botón ↑.

---

## 11. Estados (loading / error / empty / optimistic)

### Loading
- Página completa: `<div className="p-6 text-v8-fg-mute">Cargando...</div>`.
- Inline en componente: spinner v8-pulse-ring (ver Tailwind animations).

### Error
- Soft inline: badge rojo con `text-v8-danger`.
- Toda la página: `<div className="p-6 text-v8-danger">Error: {msg}</div>`.

### Empty
- En columnas vacías:
  `<p className="text-meta uppercase tracking-tag text-v8-fg-mute py-8 text-center">Sin tareas en {estado}</p>`.

### Optimistic
- React Query `setQueriesData` para mover card antes del server.
- Optimistic + `setTimeout(invalidateQueries, 5000)` como red de seguridad.
- Rollback en `onError` filtrando por `optimisticId`.

Patrón completo en `TareaDetalle.tsx:nextActionMut.onSuccess` para
transitions, y en `sendComment` para multi-file.

---

## 12. Auth / SSO (cross-subdominio)

Hoy `notifications` es el **SSOT del SSO** del ecosistema.

- **Provider:** Supabase Auth + Google OAuth (PKCE).
- **Storage híbrido:** localStorage primario + cookies espejo `.v8labs.co`
  chunked (`v8auth`, `v8auth.0`, `v8auth.1`, ...). Ver
  `src/lib/supabase.ts`.
- **Gate:** edge function `me` de Mind valida 5 condiciones contra
  `mind.operators`. Para apps cliente-facing (ej. dealer), replicar con
  vista equivalente (`mind.clients`).
- **Login centralizado:** `on.v8labs.co/login`. Cualquier subdominio rebota
  con cortafuegos anti-loop.
- **Return after login:** `https://on.v8labs.co/login?return_to=https://<sub>.v8labs.co/<path>`.
  Filtro defensivo: solo `https://` + `.v8labs.co` o `v8labs.co` exacto.

Contrato `v8auth`:
- Cookie domain: `.v8labs.co`
- Encoding: `encodeURIComponent` sobre el JSON de la Session.
- Attrs: `path=/; domain=.v8labs.co; secure; samesite=lax; max-age=31536000`.
- **NO se modifica sin avisar por comms a `studio/dealer/etc.`** — es ley
  del ecosistema (decisión Andy 2026-06-01, registrada en
  `shared/decisions.md`).

Componentes reutilizables (copiá tal cual cambiando solo `storageKey` si
querés sesiones independientes):

- `src/lib/supabase.ts` — cliente + hybridStorage.
- `src/lib/host.ts` — helpers de subdominio + return_origin + cortafuegos.
- `src/components/shells/AuthShell.tsx` + `LoginRedirect.tsx` +
  `RequireAuth.tsx`.
- `src/store/auth.ts` — Zustand store `{ operator, initializing }`.
- `src/main.tsx` — bootstrap pattern (getSession FUERA de
  onAuthStateChange para evitar deadlock).

---

## 13. Iconografía

**Sin librerías**. SVGs inline propios en `src/components/icons/index.tsx`.
Cada ícono es un componente `({ size = 16, className }) => <svg ...>`.
Stroke `currentColor` para heredar `text-*`.

Por qué no librería: control visual estricto + bundle más chico. La lista
crece a demanda; nadie agregó "todos los Heroicons por las dudas".

> Para dealer: si necesitás un set inicial de íconos comerciales (cart,
> WhatsApp, package), avísame y los agrego al set compartido o te paso un
> patrón consistente. Mientras tanto, copiá el archivo y extendelo.

---

## 14. PWA + Service Worker

`vite-plugin-pwa` con Workbox. Manifest define `display: standalone`,
`theme_color: #262b39`, íconos 192/512.

**Service worker auto-destructivo durante development** — evitar SW caching
agresivo durante el bootstrap del MVP. Habilitalo cuando el dataset esté
estable.

---

## 15. Anti-patterns explícitos (NO HACER)

- ❌ Hardcodear colores (`#262b39`) en lugar de `text-v8-bg`.
- ❌ Inventar tracking sin clase semántica.
- ❌ Border radius > 3px.
- ❌ `shadow-xl`, `backdrop-blur-*`, gradientes.
- ❌ Usar `v8-danger` para algo que no sea cancelar/rechazar/eliminar.
- ❌ Usar `v8-accent` como background grande. Solo líneas/links/indicadores.
- ❌ Bottom-nav con 3+ botones en capa 1.
- ❌ Modal flotante para acción que necesita 3+ pickers — usar full-screen.
- ❌ Library de íconos genérica (Heroicons, Lucide, etc.).
- ❌ Material UI, Chakra, Mantine — Tailwind directo y componentes propios.
- ❌ Push notifications agresivas. El operador decide qué ve.
- ❌ "Skeleton loaders" elaborados — `Cargando...` directo es suficiente.

---

## 16. Stack referencia (lo que probé en producción)

- **Build:** Vite + React 18 + TypeScript.
- **Styling:** Tailwind v3 + CSS vars.
- **Router:** React Router v6.
- **State:** Zustand (local) + TanStack Query v5 (remoto/cache).
- **Auth/DB:** `@supabase/supabase-js` directo (sin `@supabase/ssr` —
  rompe cross-subdominio).
- **DnD:** dnd-kit.
- **Media:** MediaRecorder API.
- **PWA:** vite-plugin-pwa + Workbox.
- **Deploy:** Fly.io org v8labs, 2 machines shared-cpu-1x 256MB
  (dfw + gru).

---

## 17. Recursos rápidos

- Repo de marca (SSOT tokens + assets): `V8Labs/core_v8_assets`.
- Repo de doctrina (reglas universales): `V8Labs/core_v8_doctrine`.
- Repo de referencia (este UX/UI): `V8Labs/app_V8_NOTIFICATIONS`,
  branch `feature/mvp-night-builder` o `main` (post-merge).
- Memorias persistentes de notifications:
  `~/.claude/projects/-Users-andycoding-dev-app-V8-NOTIFICATIONS/memory/MEMORY.md`.
- Coordinación entre agentes: `comms` CLI + `~/.claude-agent-comms/`.

---

## 18. Cuándo actualizar este doc

- Cuando se añada un patrón visual NUEVO que otra app debería heredar.
- Cuando se DEPRECE algo (marcar con tachado + razón).
- Cuando una decisión doctrinal cambie el comportamiento (ej. nueva regla
  de gestos, cambio en bottom-nav).

NO actualizar para:

- Cambios de copy / textos.
- Bugfixes puntuales.
- Refactors que no cambian el contrato visual.

Mantener este doc < 1000 líneas. Si crece más, partirlo por capas
(`UX-COLOR.md`, `UX-LAYOUT.md`, `UX-COMPONENTS.md`).

---

**Última revisión:** notifications, 2026-06-01.
