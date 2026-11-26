---
name: editor-reels-jnr
description: Edita Reels / Shorts / TikToks de la marca personal de Jeisson NR (@jeissonnr) con su identidad visual — textos animados palabra por palabra en Syne con palabra clave en lime, degradado navy arriba, filtro JNR, loop infinito y export en máxima calidad. Úsala cuando pidan editar un video para redes, hacer un reel con una frase, un short de YouTube o "el video con mi marca".
---

# Editor de Reels JNR

Herramienta: `render_reel.py` (en esta carpeta). Requiere ffmpeg, Pillow y las fuentes de `fonts/`.

## Identidad de marca (no cambiar sin que Jeisson lo pida)
- Navy `#0A2240` · Lime `#B8E92E` · Blanco
- Titulares: **Syne ExtraBold** · Firma/apoyo: **DM Sans**
- Degradado navy arriba (~56% de la altura) con un brillo lime sutil en la esquina.
- Texto aparece palabra por palabra (sube + fade, 0,45 s por palabra, 0,11-0,13 s de escalonado). La palabra clave va en lime con resplandor.
- Firma `@jeissonnr` + línea lime abajo, fuera de la zona de botones de IG/TikTok.
- Filtro JNR: contraste +8%, saturación −12%, sombras frías hacia navy, altas luces levemente cálidas, viñeta suave, grano fino.

## Retención (por qué funciona)
- **Loop infinito:** el final se funde con el propio inicio del fondo y la respiración de zoom vuelve al mismo punto, así la repetición no se nota → más vistas por persona.
- **Hook en el primer segundo:** el primer texto entra a los 0,15 s.
- **Cada 2-3 s pasa algo nuevo** (bloque de texto nuevo). Duración ideal 15-20 s, nunca más de 30.
- La última frase se va antes del final para que el loop vuelva directo al hook.

## Cómo usarla
1. Escribe el guion en `guiones/<nombre>.json` (ver `guiones/llamados.json`): bloques con `start`, `end`, `text`, `lime` (palabras en lime), `size`, `y`.
2. Previsualiza sin el video (fondo sintético): `python3 -I render_reel.py --demo --guion guiones/x.json --out preview.mp4`
3. Final: `python3 -I render_reel.py --bg "video de fondo.mp4" --guion guiones/x.json --out reel.mp4`
   - `--audio musica.mp3` para meter música (normaliza a −14 LUFS) · `--keep-audio` para conservar el audio original.
   - Si la música es una canción en tendencia, **mejor exportar sin audio y añadirla dentro de la app** (la plataforma solo da el empuje de "audio en tendencia" si se elige allí y evita bloqueos por derechos).
4. Revisa fotogramas (hook, frase clave, final) antes de entregar. Ninguna palabra sola en un renglón: si pasa, baja `size`.

## Export (máxima calidad para redes)
1080×1920 · 30 fps · H.264 High 4.2 · CRF 16 · máx. 20 Mbps · BT.709 · AAC 320 kbps 48 kHz · faststart.

## Subir sin perder calidad
- **Instagram:** Perfil → ☰ → Configuración → *Calidad de los medios* (o *Uso de datos*) → activar **"Subir con la máxima calidad"**. Subir con wifi, desde el teléfono y sin pasar el archivo por WhatsApp (lo comprime).
- **Facebook:** Configuración → *Contenido multimedia* → Calidad de video → **"Optimizada" / HD**; desactivar "Ahorro de datos".
- **YouTube Shorts:** subir el archivo original. Si queda en 1080p, se ve bien; YouTube tarda unos minutos en procesar la versión HD.
- Pasar el archivo al celular por cable, Google Drive (descargar el original) o AirDrop, nunca por WhatsApp/Telegram como foto/video.

## Historial de aprendizajes
- 2026-11-26 · Reel "Dios no llama a los capacitados": Syne es muy ancha; para frases de 6+ palabras usar size 80-88, para 2-3 palabras 110-120. Render de 20 s tarda ~2,5 min en 4 núcleos.
