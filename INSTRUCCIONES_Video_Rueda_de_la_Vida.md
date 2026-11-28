# INSTRUCCIONES — Video "Rueda de la Vida · Dinero y finanzas" (@jeissonnr)

> Pega este documento completo en la sesión de Claude que tiene acceso a la carpeta de videos.
> Sigue los pasos **en orden**. No publiques nada sin que Jeisson apruebe el video final, la miniatura y los textos.

---

## 0. Contexto (léelo primero)

- **Marca:** Jeisson NR · @jeissonnr · marca personal de crecimiento personal ("píldoras de vida") + estrategia digital.
- **Objetivo del video:** viralizar y generar comentarios. Es la antesala del lanzamiento del **Reto RESET 30 días**.
- **Idea central:** la Rueda de la Vida tiene 10 áreas. Jeisson "toca" la rueda en pantalla, recorre varias áreas, vuelve y **selecciona Dinero y finanzas**. Aparecen 10 preguntas, cada persona se pone nota del 1 al 10, suma y descubre su **margen de mejora**.
- **Regla de lenguaje:** nunca decir "dónde estás peor". Decir siempre **"donde tienes más margen de mejora"**.

### Identidad de marca (obligatoria en todo)
| Elemento | Valor |
|---|---|
| Navy (fondo) | `#0A2240` |
| Lime (acento, palabra clave) | `#B8E92E` |
| Blanco | `#FFFFFF` |
| Titulares | **Syne ExtraBold** |
| Textos de apoyo | **DM Sans** |
| Firma | `@jeissonnr` + línea lime |
| Filtro de video JNR | contraste +8 %, saturación −12 %, sombras frías hacia navy, viñeta suave, grano fino |

### Herramientas ya hechas en el repositorio (úsalas si te sirven)
Repo `JeissonNr/Informe-de-cuenta-JNR-Digital-Unos-Tipos-Duros.html`, rama `claude/amazing-tesla-7kfrk9`, carpeta `.claude/skills/editor-reels-jnr/`:
- `SKILL.md` — reglas de marca, export y subida en máxima calidad.
- `render_reel.py` — reels con textos animados palabra por palabra, degradado navy, filtro JNR y loop.
- `rueda.py` — genera la Rueda de la Vida (10 áreas) en PNG transparente: base, cada área encendida y "Dinero y finanzas SELECCIONADO".
- `pack_rueda.py` — genera las 10 tarjetas de preguntas, la tarjeta de puntaje y la miniatura de YouTube (`--cara foto.png` para meter la cara de Jeisson).
- `fonts/` — Syne ExtraBold y DM Sans.

---

## 1. Revisa y organiza el material

1. Abre la carpeta `C:\Users\jeiss\Documents\Meta ads Manager- Agente\JEISSON NR\VIDEOS MARCA PERSONAL`.
2. Haz una lista de **todos** los videos e imágenes con: nombre, duración, orientación y qué se ve.
3. Mira cada clip (extrae un fotograma cada 0,5 s con ffmpeg) y clasifícalos en:
   - **A · Hook / a cámara:** Jeisson hablando o mirando a cámara.
   - **B · Tocando la pantalla:** el clip donde señala como si tocara una pantalla, recorre ~5 temas, devuelve el dedo y elige el primero.
   - **C · Cierre:** los clips que Jeisson grabó para el final.
   - **D · Imágenes de apoyo / transiciones:** fotos y recursos para pasar entre secciones.
4. **Antes de editar**, muéstrale a Jeisson la clasificación y el orden propuesto (inicio → medio → final) y espera su visto bueno.

---

## 2. Audio

1. Extrae el audio de todos los clips con voz.
2. Mejora la voz con **Adobe Podcast · Enhance Speech** (si está conectado el MCP de Adobe, usa `media_enhance_speech`; si no, súbelo a podcast.adobe.com/enhance).
3. Normaliza todo a **−14 LUFS, pico −1 dB**.
4. La música en tendencia **se elige dentro de cada app** (Instagram, TikTok, YouTube) al publicar, no se mete en el export. Si Jeisson quiere música de fondo fija, usar una sin derechos a −24 dB debajo de la voz.

---

## 3. Estructura del video (vertical 9:16, 60–75 s)

| Tiempo | Sección | Clip | Superposición |
|---|---|---|---|
| 0–3 s | **Hook** | A | Texto grande: **"Ponle nota a tu vida del 1 al 10"** (palabra clave lime) |
| 3–5 s | Transición | D | Aparece la Rueda de la Vida con zoom-in |
| 5–14 s | **Recorrido por la rueda** | B | La rueda superpuesta junto al dedo. Cada vez que el dedo "toca" un área, **esa área se enciende** (ver paso 4) |
| 14–16 s | **Selección** | B | El dedo vuelve: se enciende **Dinero y finanzas** + etiqueta **SELECCIONADO**. Texto: "Hoy vamos con **Dinero y finanzas**" |
| 16–18 s | Instrucción | A o D | "Ponte una nota del 1 al 10 en cada pregunta" |
| 18–53 s | **10 preguntas** | A, B o D de fondo (difuminado) | Una tarjeta por pregunta, **3,5 s cada una**, con contador 1/10…10/10 y transición rápida entre tarjetas |
| 53–60 s | **Puntaje** | A | Tarjeta: "Suma tus 10 notas. 100 − tu total = **TU MARGEN DE MEJORA**" |
| 60–65 s | **3 áreas** | A | "Elige las 3 preguntas con **más margen de mejora**: ahí empieza tu cambio" |
| 65–75 s | **Cierre / CTA** | C | "Comenta tu margen de mejora y te digo por dónde empezar. **Guárdalo.**" + `@jeissonnr` |

Reglas:
- Algo nuevo en pantalla **cada 2–3 s**. Sin silencios ni pausas muertas.
- Subtítulos de la voz siempre (Syne o DM Sans, palabra clave en lime).
- Transiciones con sentido (zoom a la rueda, barrido lime), no transiciones genéricas.
- Último fotograma debe enlazar con el primero (loop) para que la gente lo vea dos veces.

---

## 4. Rueda de la Vida sincronizada con el dedo

**Las 10 áreas (en este orden, empezando arriba y en sentido horario):**
1. Salud y energía
2. Mente y emociones
3. **Dinero y finanzas**
4. Trabajo y propósito
5. Familia y relaciones
6. Amor y pareja
7. Crecimiento personal
8. Fe y espiritualidad
9. Diversión y ocio
10. Entorno y hogar

**Diseño:** círculo dividido en 10 porciones como una pizza, porciones navy alternando dos tonos, separadores blancos, centro con "RUEDA DE LA VIDA". El área activa se pinta **lime con resplandor** (como si se encendiera una luz).

**Sincronización paso a paso:**
1. En el clip B, extrae fotogramas cada 0,1 s.
2. Anota el **momento exacto** y la **posición en pantalla** de cada toque del dedo (cuando el dedo se detiene o "presiona").
3. Coloca la rueda (PNG transparente, `rueda.py`) de modo que cada toque caiga **sobre una porción** distinta.
4. En cada toque, cambia la rueda base por la versión con esa porción encendida (`rueda_01.png` … `rueda_10.png`) durante 0,4–0,6 s, con un destello corto.
5. En el toque final (cuando devuelve el dedo al primero), usa `rueda_dinero_seleccionado.png` y mantenla 1,5 s.
6. Opcional: un pequeño "pulso" de luz lime donde toca el dedo.
7. Revisa el resultado cuadro a cuadro: la luz debe encenderse **justo** cuando el dedo toca, no antes ni después.

---

## 5. Las 10 preguntas · Dinero y finanzas

Cada persona responde con una **nota del 1 al 10** (10 = está perfecto).

1. ¿Sé exactamente cuánto gano y cuánto gasto cada mes?
2. ¿Llevo un control escrito de mis finanzas: app, Excel o libreta?
3. ¿Tengo mis deudas bajo control y un plan claro para pagarlas?
4. ¿Tengo identificados y frenados mis gastos hormiga?
5. ¿Ahorro una parte fija de lo que gano antes de gastar?
6. ¿Tengo un fondo de emergencia para al menos 3 meses?
7. ¿Llego a fin de mes sin angustia por el dinero?
8. ¿Hablo de dinero con mi pareja o familia sin peleas ni secretos?
9. ¿Invierto en mí o en algo que me genere ingresos a futuro?
10. ¿Tengo una relación sana y tranquila con el dinero?

**Cómo se calcula:**
- Suma las 10 notas → máximo posible **100**.
- **Margen de mejora = 100 − tu total.** Ejemplo: sumaste 62 → tienes 38 puntos para crecer.
- Elige las **3 preguntas con la nota más baja**: esas son las de **más margen de mejora** y por ahí empiezas.

**Tarjeta de cada pregunta:** caja navy con borde lime en la mitad inferior, etiqueta "DINERO Y FINANZAS · 3/10", la pregunta en Syne ExtraBold blanca, debajo "Ponte nota del 1 al 10" y 10 casillas numeradas. Entra con un deslizamiento corto hacia arriba.

---

## 6. Export en máxima calidad

- **Reel / Short / TikTok:** 1080×1920, 30 fps, H.264 High, CRF 16 (máx. 20 Mbps), BT.709, AAC 320 kbps 48 kHz, `+faststart`.
- **Versión YouTube horizontal (opcional):** 1920×1080 con el video vertical al centro y fondo navy difuminado.
- Revisa el export con ffprobe (resolución, fps, duración) y mira 5 fotogramas clave antes de entregarlo.

---

## 7. Miniatura de YouTube (1280×720)

1. Recorta la cara de Jeisson de un fotograma expresivo (sorpresa o mirada directa) y quítale el fondo.
2. Composición: texto grande a la izquierda, rueda a la derecha con **Dinero y finanzas encendida**, cara de Jeisson delante de la rueda.
3. Texto principal (máximo 4 palabras, Syne ExtraBold): **"¿CUÁNTO VALE TU DINERO?"** con "DINERO?" en lime.
4. Etiqueta lime: **"Test de 10 preguntas"**.
5. Si hay Adobe Firefly / Express conectado, puedes mejorar el fondo con él, pero respetando colores y tipografías de la marca.
6. Entrega 2 versiones para que Jeisson elija.

### 10 ganchos para portada / primer segundo
1. ¿Cuánto vale tu relación con el dinero?
2. Ponle nota a tu dinero del 1 al 10
3. Este test te dice dónde se te va la plata
4. 10 preguntas que nadie se hace sobre su dinero
5. Si sacas menos de 70, mira este video
6. Tu margen de mejora financiero en 60 segundos
7. No es falta de dinero, es falta de estrategia
8. ¿Gastos hormiga? Haz este test
9. Descubre en qué área de tu vida tienes más margen
10. La rueda de la vida que cambia tu año

---

## 8. Textos para publicar

### Título de YouTube (Short)
**¿Cuánto vale tu dinero? Haz este test de 10 preguntas 💰 #RuedaDeLaVida**

### Descripción de YouTube
```
¿Cómo está de verdad tu relación con el dinero? 💰

Haz este test rápido de la Rueda de la Vida: ponte una nota del 1 al 10 en cada pregunta, suma tus 10 notas y resta el total a 100. Ese número es tu MARGEN DE MEJORA.

Las 10 preguntas:
1. ¿Sé exactamente cuánto gano y cuánto gasto cada mes?
2. ¿Llevo un control escrito de mis finanzas?
3. ¿Tengo mis deudas bajo control y un plan para pagarlas?
4. ¿Tengo identificados y frenados mis gastos hormiga?
5. ¿Ahorro una parte fija antes de gastar?
6. ¿Tengo un fondo de emergencia para al menos 3 meses?
7. ¿Llego a fin de mes sin angustia?
8. ¿Hablo de dinero con mi pareja o familia sin peleas ni secretos?
9. ¿Invierto en mí o en algo que me genere ingresos a futuro?
10. ¿Tengo una relación sana y tranquila con el dinero?

Elige las 3 preguntas con más margen de mejora: ahí empieza tu cambio.

👇 Comenta tu margen de mejora y te digo por dónde empezar.

Soy Jeisson, administrador de empresas y estratega digital. Aquí comparto estrategia real y píldoras de vida para crecer por fuera y por dentro.

#RuedaDeLaVida #FinanzasPersonales #CrecimientoPersonal
```

### Caption Instagram / Facebook / TikTok
```
¿Cuánto vale tu relación con el dinero? 💰

Ponte nota del 1 al 10 en cada pregunta, suma y resta a 100: ese es tu margen de mejora.

👇 Comenta tu número y te digo por dónde empezar.
📌 Guárdalo y hazlo con calma esta noche.

#crecimientopersonal
```
(Un solo hashtag principal; en TikTok se puede añadir #finanzaspersonales.)

---

## 9. Aprobación y publicación

1. Envía a Jeisson: video vertical final, miniatura (2 opciones), título, descripción y caption.
2. **No publiques hasta que Jeisson diga "aprobado".**
3. Publicación:
   - **Instagram + Facebook:** Meta Business Suite → Crear Reel → subir el video → caption → programar. Elegir la **música en tendencia dentro de la app**.
   - **YouTube Shorts:** YouTube Studio → subir → título, descripción, miniatura → programar.
   - **TikTok:** desde la app o TikTok Studio, con un sonido en tendencia.
   - Si la sesión no tiene conexión para publicar en alguna red, **díselo a Jeisson** y déjale el paquete listo para que lo suba él. No digas que quedó publicado si no lo está.
4. **Horario:** revisa en Instagram → Panel profesional → Estadísticas → Seguidores → "Horas de mayor actividad" y programa 15 min antes del pico. Si no hay datos, entre 7 y 9 p. m. hora Colombia.
5. **Calidad al subir:** Instagram → Configuración → Calidad de los medios → "Subir con la máxima calidad". Facebook → Contenido multimedia → Calidad HD. Nunca pasar el video por WhatsApp.

---

## 10. Al terminar

1. Guarda en `.claude/skills/editor-reels-jnr/SKILL.md` (sección "Historial de aprendizajes") lo que funcionó y lo que corregiste en este video.
2. Entrega a Jeisson un resumen: archivos generados, dónde quedaron y qué falta (si algo no se pudo publicar).
