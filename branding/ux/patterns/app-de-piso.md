# Patrón: APP DE PISO — la interfaz que se opera de pie

> **Qué es:** el estándar para las superficies que NO se usan en un escritorio: el operario de
> pie en el taller, con el teléfono, entre máquinas, a veces con las manos sucias. Toca poco y
> mira rápido. Nace del formulario de flujo de Referencia (`produccion`, 2026-08-22) y gobierna
> por igual el modal de "Imprimir códigos" (`barcode`) — **son dos caras de la misma app y tienen
> que salir iguales, no parecidas.**
>
> **Dueño:** `branding`. Esto NO redefine nada: baja `brand-tokens.json` + `UX-PATTERNS.md` a un
> caso de uso. Ante cualquier diferencia, **manda el token**, no este doc.

---

## 1. El bloque de tokens — copiar TAL CUAL, no adaptar

Los valores salen de `brand-tokens.json → ux.superficie` + `ux.acento` + `ux.accion`. Si tu app
tiene un color que no está acá, no lo inventes: pedímelo.

```css
:root{                                   /* DARK es el default de la casa */
  --v8-bg:        #262b39;   /* slate V8 — la firma. Si no está, no es una app V8 */
  --v8-bg-deep:   #1a1d26;   /* inputs, modales internos, bloques hundidos */
  --v8-fg:        #f1f1f1;
  --v8-fg-mute:   #8a8f9c;   /* 4.36:1 sobre bg — el mínimo que pasa AA */
  --v8-line:      #3a3f4d;
  --v8-accent:    #A2E771;   /* lima: SOLO líneas, enlaces, indicador activo */
  --v8-danger:    #E11900;   /* EXCLUSIVO cancelar / rechazar / eliminar */
}
:root[data-theme="light"]{
  --v8-bg:        #D9DCE0;
  --v8-bg-deep:   #C5C9D0;
  --v8-fg:        #262b39;
  --v8-fg-mute:   #5B6371;   /* 4.40:1 sobre bg */
  --v8-line:      #A6ACB6;
  --v8-accent:    #355A10;   /* el lima NO sobrevive en claro — ver §2 */
  --v8-danger:    #E11900;
}

body{
  font-family:"IBM Plex Sans","Segoe UI",system-ui,"Helvetica Neue",Arial,sans-serif;
  background:var(--v8-bg); color:var(--v8-fg);
}
```

**Tipografía:** IBM Plex Sans, pesos 400/500/600. **NO Helvetica Condensed** — esa es de FXCKBOY,
y ponérsela a una app interna le pone la cara de la marca de producto a una herramienta de taller.
(`UX-PATTERNS.md §4` decía lo contrario hasta el 2026-08-22; estaba mal y ya está corregido.)

**Mono** para códigos y cantidades: correcto, es un tablero que se opera. `font-variant-numeric:
tabular-nums` siempre que haya cifras que se comparen en columna.

---

## 2. Las tres trampas que ya se cayeron (no las repitas)

**a) El lima no existe en tema claro.** `#A2E771` sobre fondo claro da **1.07:1** — invisible.
Ya está resuelto y asentado: en claro el acento de TEXTO es **`#355A10`** (5.82:1 sobre `--v8-bg`,
4.82:1 sobre `--v8-bg-deep`). No lo re-derives — cada quien que lo oscurece a ojo llega a un verde
distinto y la familia se desalinea. Para chips/badges en claro va el **pill invertido** (fondo
`--v8-bg` oscuro + texto lima), no el verde oscuro.

**b) El texto tenue es lo primero que se cae, y acá es lo que importa.** El texto de ayuda
("qué falta para avanzar") es justo lo que el operario necesita leer con reflejo, de pie y a un
brazo de distancia. **`--v8-fg-mute` es el piso, no un punto de partida para aclarar más.** Un gris
más claro que ese no pasa AA y en el taller directamente no se lee. Regla dura: **ningún texto de
esta app por debajo de 4.5:1**, y el de ayuda nunca por debajo de 12px.

**c) Sin gradients — tampoco para "desvanecer" una marca.** Prohibición absoluta
(`UX-PATTERNS §5`). Una línea que se desvanece se hace **sólida y corta**, no con
`linear-gradient(color,transparent)`. Sin sombras, sin glow, sin radius (0; el techo del sistema es
3px y esta app no lo necesita).

---

## 3. Layout: una sola app, tres anchos

El error a evitar es diseñar solo-móvil y dejar en desktop una columna flaca en el medio. **No se
diseña dos veces: se diseña una y se deja crecer.**

| Ancho | Qué hace |
|---|---|
| **< 640px** (el teléfono del taller — el caso real) | Una columna. Barra inferior fija de 2 botones. Línea temporal recortada a **3 etapas**: la actual y sus vecinas. |
| **640–1023px** | Una columna, más aire. Línea temporal completa. |
| **≥ 1024px** | **Dos columnas** (identidad + línea temporal a la izquierda, bloques del paso a la derecha) con `max-width:1100px`. Las acciones dejan de ser barra fija y se vuelven pie del contenido. |

```css
.app{max-width:none;margin:0;background:var(--v8-bg)}      /* NO 460px fijo */
@media (min-width:1024px){
  .app{max-width:1100px;margin:0 auto;display:grid;
       grid-template-columns:320px 1fr;gap:0;align-items:start}
  .barra-inf{position:static;max-width:none;height:auto}   /* deja de flotar */
}
```

**La línea temporal en móvil (3 etapas):** mostrá la actual y una a cada lado. No hace falta
inventar señales de "hay más": el rótulo `Paso 5 de 6` ya lo dice, y decirlo dos veces gasta el
espacio que necesitás para el dedo.

```css
.tramo{display:none}
.tramo.hoy,.tramo.hoy + .tramo,.tramo:has(+ .tramo.hoy){display:block}
@media (min-width:640px){ .tramo{display:block} }
```

---

## 4. La barra superior: qué se pega y qué se va

"Más cómoda" no es solo más padding — es **pegar menos**. Hoy viaja pegado todo el encabezado
(identidad + paso + línea temporal) y se come la pantalla del teléfono.

**Regla:** queda pegado SOLO lo que contesta la pregunta 1 del operario — *en qué paso estoy y
qué falta*. Eso es: **código de referencia · título del paso · cuántos obligatorios faltan.** La
línea temporal **scrollea y se va**: es orientación, se mira una vez al entrar, no se consulta
mientras se carga un campo.

- Alto de toque mínimo **44px** en todo lo que se toca (hoy los campos van en 10px de padding).
- Padding del encabezado: **16px** vertical, no 12/8.
- El contador de faltantes es **texto**, no un emoji de semáforo: 🔴 no se lee con reflejo, y en
  el sistema el rojo tiene un solo dueño (`--v8-danger` = cancelar/rechazar). Usá
  `4 OBLIGATORIOS PENDIENTES` en mayúsculas con `letter-spacing:.08em`.

---

## 5. Las tres que quedaron abiertas — criterio

**a) Dónde entra Cancelar/Rechazar.** Con 211 canceladas contra 145 listas, rechazar **no es un
caso raro: es el otro final del proceso.** Pero la barra de dos botones es orden de Andy y no se
toca. La salida no es meter un tercero: es entender que **la barra inferior es NAVEGACIÓN (avanzar
/ volver), y rechazar no es navegar — es un acto sobre el objeto.** Va arriba, junto a la
identidad de la referencia, como acción de texto en `--v8-danger`, con confirmación obligatoria.
Queda visible (no escondida en un menú), no compite con el botón de avanzar, y respeta la regla.
⚠️ La regla de los dos botones es de Andy: si querés moverla, se le pregunta a él, no se
reinterpreta.

**b) Rótulos de UI distintos del nombre del estado: NO.** Acortar sí, **renombrar no.** El
operario va a escuchar "está en Medición" de boca de otra persona y va a leer "Medición" en el
reporte: si su pantalla dice "Recibida", acaba de aparecer un diccionario que solo existe en su
teléfono. Si un nombre real no entra, se abrevia (`En muestra` → `Muestra`), nunca se sustituye
por otra palabra. El costo de un rótulo apretado es un rótulo apretado; el costo de un rótulo
inventado es una conversación que no cierra.

**c) El modal de impresión: no lo expliques, estructurálo.** La frase "cambiar esto no altera ese
dato" es correcta y aun así frágil — está en el color más tenue y en 11.5px, o sea justo donde
nadie mira. La distinción se resuelve con **jerarquía, no con una aclaración**: poné
`Producidas · 24` como una fila más del bloque de sólo-lectura (mono, alineada con las otras), y
etiquetá el campo editable como lo que es: **"Etiquetas a imprimir"**. Cuando los dos números
viven en lugares visiblemente distintos —uno en el preview inmutable, otro en el único campo con
borde— la diferencia deja de depender de que alguien lea una línea chiquita. La aclaración puede
quedarse, pero como refuerzo, no como el único mecanismo.

---

## 6. Lo que ya estaba bien (no lo toques al rehacer)

- Lima **solo en líneas e indicadores** (subrayado del botón activo, barra del paso hecho). Bien
  leído.
- **Esquinas rectas, sin sombras.** Correcto y es la mitad del carácter del sistema.
- **Mono con cifras tabulares** en códigos y cantidades.
- **El botón deshabilitado como gate**: que no se pueda avanzar se ve, no se explica. Es
  exactamente la doctrina de la casa.
- **Datos reales** (la V8-REF-573 con su estado de hoy). Un ejemplo inventado habría escondido
  justo el caso que la interfaz tiene que saber mostrar.
