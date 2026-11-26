#!/usr/bin/env python3
"""Editor de Reels JNR — genera un Reel/Short 9:16 con la marca de Jeisson NR.

Uso:
  python3 render_reel.py --bg "video de fondo.mp4" --guion guion.json --out reel.mp4
  python3 render_reel.py --demo --guion guion.json --out preview.mp4   (fondo sintético para aprobar diseño)

Qué hace:
  1. Fondo: recorte/escala a 1080x1920, filtro de marca JNR (sombras navy, contraste,
     grano fino, viñeta) y respiración de zoom que termina igual que empieza.
  2. Loop infinito: el final del video se funde con su propio inicio, así al repetirse
     no se nota el corte (más retención y más reproducciones contadas).
  3. Degradado navy arriba con los textos del guion, palabra por palabra, palabra clave en lime.
  4. Firma @jeissonnr fija abajo.
  5. Export máxima calidad para redes: H.264 High, CRF 16, 30 fps, BT.709, AAC 320k, faststart.
"""
import argparse, json, math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
NAVY = (10, 34, 64)
LIME = (184, 233, 46)
WHITE = (255, 255, 255)
HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def ease_out(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3


def top_gradient():
    """Degradado navy arriba (opaco) → transparente hacia el centro."""
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    px = g.load()
    stop = int(H * 0.56)
    for y in range(stop):
        a = int(235 * (1 - (y / stop)) ** 1.6)
        for x in range(W):
            px[x, y] = (*NAVY, a)
    # brillo lime muy sutil en la esquina para dar profundidad
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((-300, -380, 700, 420), fill=(*LIME, 38))
    glow = glow.filter(ImageFilter.GaussianBlur(160))
    return Image.alpha_composite(g, glow)


def layout_line(words, fnt, max_w):
    """Parte una frase en renglones que quepan en max_w."""
    lines, cur = [], []
    for w in words:
        test = " ".join(t for t, _ in cur + [w])
        if cur and fnt.getlength(test) > max_w:
            lines.append(cur); cur = [w]
        else:
            cur.append(w)
    if cur: lines.append(cur)
    return lines


def render_block(draw_img, block, t, fnt_main):
    """Dibuja un bloque de texto animado palabra por palabra."""
    t0, t1 = block["start"], block["end"]
    if t < t0 - 0.01 or t > t1 + 0.4:
        return
    size = block.get("size", 96)
    fnt = font("Syne-ExtraBold.ttf", size)
    keys = set(w.lower().strip(".,…¿?¡!") for w in block.get("lime", "").split())
    words = [(w, w.lower().strip(".,…¿?¡!") in keys) for w in block["text"].split()]
    lines = layout_line(words, fnt, W - 160)
    lh = int(size * 1.12)
    y0 = block.get("y", 360) - (len(lines) - 1) * lh // 2
    per = block.get("stagger", 0.11)
    out_a = 1.0 - ease_out((t - t1) / 0.35) if t > t1 else 1.0
    idx = 0
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d, ds, dg = ImageDraw.Draw(layer), ImageDraw.Draw(shadow), ImageDraw.Draw(glow)
    for li, line in enumerate(lines):
        txt = " ".join(w for w, _ in line)
        lw = fnt.getlength(txt)
        x = (W - lw) / 2
        y = y0 + li * lh
        for w, hot in line:
            p = ease_out((t - t0 - idx * per) / 0.45)
            a = int(255 * p * out_a)
            if a > 0:
                dy = (1 - p) * 38 - (1 - out_a) * 30
                col = LIME if hot else WHITE
                ds.text((x + 4, y + dy + 6), w, font=fnt, fill=(0, 0, 0, int(a * 0.55)))
                if hot:
                    dg.text((x, y + dy), w, font=fnt, fill=(*LIME, int(a * 0.8)))
                d.text((x, y + dy), w, font=fnt, fill=(*col, a))
            x += fnt.getlength(w + " ")
            idx += 1
    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    glow = glow.filter(ImageFilter.GaussianBlur(22))
    draw_img.alpha_composite(shadow)
    draw_img.alpha_composite(glow)
    draw_img.alpha_composite(layer)


def overlay_frames(guion, dur):
    grad = top_gradient()
    sig_f = font("DMSans-Medium.ttf", 40)
    sig = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sig)
    handle = guion.get("firma", "@jeissonnr")
    tw = sig_f.getlength(handle)
    sd.text(((W - tw) / 2 + 2, H - 330 + 3), handle, font=sig_f, fill=(0, 0, 0, 120))
    sd.text(((W - tw) / 2, H - 330), handle, font=sig_f, fill=(255, 255, 255, 215))
    sd.rounded_rectangle(((W - 60) / 2, H - 272, (W + 60) / 2, H - 266), 3, fill=(*LIME, 230))
    n = int(round(dur * FPS))
    for i in range(n):
        t = i / FPS
        f = grad.copy()
        for b in guion["bloques"]:
            render_block(f, b, t, None)
        f.alpha_composite(sig)
        yield f.tobytes()


def bg_filter(src_label, dur, fade, demo):
    """Filtro de fondo: 9:16, grado JNR, respiración de zoom cíclica y loop por fundido."""
    L, F = dur, fade
    grade = (
        "eq=contrast=1.08:saturation=0.88:brightness=-0.02:gamma=0.97,"
        "colorbalance=rs=-0.04:gs=-0.01:bs=0.06:rm=-0.02:bm=0.03:rh=0.02:gh=0.02:bh=-0.01,"
        "vignette=PI/4.2,noise=alls=5:allf=t"
    )
    fit = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS}"
    zoom = (f"scale={int(W*1.06)}:{int(H*1.06)},"
            f"crop={W}:{H}:x='(iw-ow)/2+18*sin(2*PI*t/{L})':y='(ih-oh)/2+28*sin(2*PI*t/{L})'")
    return (
        f"[{src_label}]{fit},split[a][b];"
        f"[a]trim=start={F}:end={L+F},setpts=PTS-STARTPTS[A];"
        f"[b]trim=start=0:end={F},setpts=PTS-STARTPTS[B];"
        f"[A][B]xfade=transition=fade:duration={F}:offset={L-F},{zoom},{grade},format=yuv420p[bg]"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bg"); ap.add_argument("--demo", action="store_true")
    ap.add_argument("--guion", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--audio", help="pista de música opcional")
    ap.add_argument("--keep-audio", action="store_true", help="conserva el audio del video de fondo")
    a = ap.parse_args()
    guion = json.load(open(a.guion, encoding="utf-8"))
    dur = float(guion.get("duracion", 20)); fade = 0.7
    inputs = []
    if a.demo:
        # fondo sintético hipnótico SOLO para previsualizar el diseño
        src = (f"color=c=0x0A2240:s=540x960:d={dur+fade}:r={FPS},"
               "geq=lum='128+90*sin(hypot(X-270,Y-480)/18-T*2.2+6*atan2(Y-480,X-270))':"
               "cb='150+20*sin(T)':cr='118'")
        inputs += ["-f", "lavfi", "-i", src]
    else:
        if not a.bg: sys.exit("Falta --bg con el video de fondo")
        inputs += ["-stream_loop", "-1", "-i", a.bg]
    inputs += ["-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"]
    fc = bg_filter("0:v", dur, fade, a.demo) + ";[bg][1:v]overlay=0:0:format=auto,format=yuv420p[v]"
    maps = ["-map", "[v]"]
    if a.audio:
        inputs += ["-i", a.audio]
        fc += f";[2:a]atrim=0:{dur},afade=t=in:d=0.4,afade=t=out:st={dur-1.2}:d=1.2,loudnorm=I=-14:TP=-1.0[au]"
        maps += ["-map", "[au]"]
    elif a.keep_audio and not a.demo:
        fc += f";[0:a]atrim=0:{dur},loudnorm=I=-14:TP=-1.0[au]"
        maps += ["-map", "[au]"]
    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *inputs,
           "-filter_complex", fc, *maps, "-t", str(dur),
           "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-profile:v", "high", "-level", "4.2",
           "-maxrate", "20M", "-bufsize", "40M", "-pix_fmt", "yuv420p", "-r", str(FPS), "-g", str(FPS * 2),
           "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
           "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-movflags", "+faststart", a.out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for fr in overlay_frames(guion, dur):
        p.stdin.write(fr)
    p.stdin.close()
    sys.exit(p.wait())


if __name__ == "__main__":
    main()
