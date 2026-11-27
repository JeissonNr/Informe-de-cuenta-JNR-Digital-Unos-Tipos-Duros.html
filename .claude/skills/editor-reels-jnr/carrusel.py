#!/usr/bin/env python3
"""Carruseles JNR — láminas 1080x1350 con la marca de Jeisson NR.

Uso:
  python3 -I carrusel.py --guion carruseles/toleras.json --out carpeta_salida [--fotos carpeta_fotos]

Las láminas con "foto": "nombre.jpg" usan esa imagen de --fotos. Si falta, dibujan un
marcador "TU FOTO AQUÍ" para ver el diseño y reemplazarla después.
"""
import argparse, json, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

W, H = 1080, 1350
NAVY = (10, 34, 64); NAVY2 = (6, 20, 40)
LIME = (184, 233, 46); WHITE = (255, 255, 255); MUTED = (150, 172, 204)
FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
M = 96  # margen lateral


def F(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)


def wrap(text, fnt, maxw):
    out = []
    for para in text.split("\n"):
        cur = ""
        for w in para.split():
            t = (cur + " " + w).strip()
            if cur and fnt.getlength(t) > maxw:
                out.append(cur); cur = w
            else:
                cur = t
        out.append(cur)
    return out


def rich(d, xy, text, fnt, lime_words, maxw, lh, align="left"):
    """Texto con palabras en lime (marcadas en lime_words)."""
    keys = {k.lower().strip(".,…¿?¡!:") for k in lime_words}
    x0, y = xy
    for line in wrap(text, fnt, maxw):
        lw = fnt.getlength(line)
        x = x0 + ((maxw - lw) / 2 if align == "center" else 0)
        for w in line.split():
            col = LIME if w.lower().strip(".,…¿?¡!:") in keys else WHITE
            d.text((x, y), w, font=fnt, fill=col)
            x += fnt.getlength(w + " ")
        y += lh
    return y


def background():
    bg = Image.new("RGB", (W, H), NAVY2)
    g = Image.new("RGB", (W, H), NAVY)
    mask = Image.linear_gradient("L").resize((W, H)).transpose(Image.FLIP_TOP_BOTTOM)
    bg = Image.composite(g, bg, mask)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((W - 520, -360, W + 260, 380), fill=(*LIME, 46))
    glow = glow.filter(ImageFilter.GaussianBlur(170))
    bg = Image.alpha_composite(bg.convert("RGBA"), glow)
    # grano fino
    noise = Image.effect_noise((W, H), 18).convert("L")
    bg = Image.blend(bg, Image.merge("RGBA", (noise, noise, noise, Image.new("L", (W, H), 255))), 0.035)
    return bg


def photo_layer(path):
    if path and os.path.exists(path):
        im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
        im = ImageOps.fit(im, (W, H), Image.LANCZOS, centering=(0.5, 0.35))
        # filtro JNR: leve desaturado, sombras frías
        im = Image.blend(im, ImageOps.grayscale(im).convert("RGB"), 0.12)
        im = Image.blend(im, Image.new("RGB", (W, H), NAVY), 0.10)
        return im.convert("RGBA")
    ph = Image.new("RGBA", (W, H), (22, 44, 76, 255))
    d = ImageDraw.Draw(ph)
    for i in range(0, W + H, 6):  # textura diagonal suave
        d.line((i, 0, i - H, H), fill=(26, 50, 84, 255), width=2)
    f = F("DMSans-Medium.ttf", 40)
    t = "TU FOTO AQUÍ"
    d.rounded_rectangle((W / 2 - 230, 330, W / 2 + 230, 420), 18, outline=(*MUTED, 255), width=3)
    d.text((W / 2 - f.getlength(t) / 2, 352), t, font=f, fill=MUTED)
    return ph


def chrome(img, i, n, handle, swipe):
    d = ImageDraw.Draw(img)
    f = F("DMSans-Medium.ttf", 30)
    d.text((M, 70), handle, font=f, fill=(*WHITE, 230))
    num = f"{i:02d}/{n:02d}"
    d.text((W - M - f.getlength(num), 70), num, font=f, fill=(*MUTED, 255))
    # barra de progreso
    d.rounded_rectangle((M, H - 70, W - M, H - 64), 3, fill=(255, 255, 255, 40))
    d.rounded_rectangle((M, H - 70, M + (W - 2 * M) * i / n, H - 64), 3, fill=(*LIME, 255))
    if swipe:
        fs = F("DMSans-Medium.ttf", 32)
        t = "Desliza  →"
        d.text((W - M - fs.getlength(t), H - 128), t, font=fs, fill=(*LIME, 255))


def checkbox(d, x, y, s):
    d.rounded_rectangle((x, y, x + s, y + s), 12, outline=(*LIME, 255), width=6)


def render(slide, i, n, handle, fotos):
    tipo = slide.get("tipo", "texto")
    img = background()
    if slide.get("foto"):
        img = photo_layer(os.path.join(fotos, slide["foto"]) if fotos else None)
        shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sd = ImageDraw.Draw(shade)
        for y in range(H):  # degradado navy abajo para el texto
            a = int(max(0, (y - H * 0.38) / (H * 0.62)) ** 1.3 * 240)
            sd.line((0, y, W, y), fill=(*NAVY2, a))
        sd.rectangle((0, 0, W, 170), fill=(*NAVY2, 90))
        img = Image.alpha_composite(img, shade)
    d = ImageDraw.Draw(img)
    lime = slide.get("lime", "").split()
    maxw = W - 2 * M
    # en láminas con foto, el bloque de texto se ancla abajo
    if slide.get("foto") and tipo == "texto":
        fs_ = F("Syne-ExtraBold.ttf", slide.get("size", 80)); fb_ = F("DMSans-Light.ttf", 40)
        th = len(wrap(slide["titulo"], fs_, maxw)) * int(fs_.size * 1.12)
        bh = (24 + len(wrap(slide["texto"], fb_, maxw)) * 54) if slide.get("texto") else 0
        slide = dict(slide, _y0=H - 190 - th - bh, kicker_y=H - 190 - th - bh - 84)
    if slide.get("kicker"):
        fk = F("DMSans-Medium.ttf", 30)
        ky = slide.get("kicker_y", 230)
        d.rounded_rectangle((M, ky, M + fk.getlength(slide["kicker"]) + 44, ky + 54), 27, fill=(*LIME, 255))
        d.text((M + 22, ky + 9), slide["kicker"], font=fk, fill=NAVY)
    if tipo == "check":
        fs = F("Syne-ExtraBold.ttf", slide.get("size", 74))
        d.text((M, 330), "Toleras…", font=F("DMSans-Light.ttf", 52), fill=(*MUTED, 255))
        y = rich(d, (M, 430), slide["titulo"], fs, lime, maxw, int(fs.size * 1.12))
        if slide.get("texto"):
            fb = F("DMSans-Light.ttf", 40)
            for line in wrap(slide["texto"], fb, maxw):
                y += 8; d.text((M, y + 20), line, font=fb, fill=(*WHITE, 220)); y += 52
        cy = H - 360
        checkbox(d, M, cy, 84)
        d.text((M + 120, cy + 14), "¿Lo toleras? Márcalo.", font=F("DMSans-Medium.ttf", 42), fill=WHITE)
    elif tipo == "ejercicio":
        fs = F("Syne-ExtraBold.ttf", slide.get("size", 70))
        y = rich(d, (M, 330), slide["titulo"], fs, lime, maxw, int(fs.size * 1.12)) + 40
        fb = F("DMSans-Medium.ttf", 44)
        for k in range(1, 4):
            d.text((M, y), f"{k}.", font=fb, fill=LIME)
            d.line((M + 70, y + 56, W - M, y + 56), fill=(*WHITE, 150), width=3)
            y += 120
        if slide.get("texto"):
            fl = F("DMSans-Light.ttf", 40)
            for line in wrap(slide["texto"], fl, maxw):
                d.text((M, y + 10), line, font=fl, fill=(*WHITE, 225)); y += 54
    else:
        fs = F("Syne-ExtraBold.ttf", slide.get("size", 80))
        lh = int(fs.size * 1.12)
        lines = wrap(slide["titulo"], fs, maxw)
        if slide.get("foto"):
            y0 = slide["_y0"]
        else:
            y0 = slide.get("y", 380)
        y = rich(d, (M, y0), slide["titulo"], fs, lime, maxw, lh, slide.get("align", "left"))
        if slide.get("texto"):
            fb = F("DMSans-Light.ttf", 40)
            y += 24 if slide.get("foto") else 44
            for line in wrap(slide["texto"], fb, maxw):
                d.text((M, y), line, font=fb, fill=(*WHITE, 225)); y += 54
    chrome(img, i, n, handle, i == 1)
    return img.convert("RGB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guion", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--fotos")
    a = ap.parse_args()
    g = json.load(open(a.guion, encoding="utf-8"))
    os.makedirs(a.out, exist_ok=True)
    n = len(g["laminas"])
    for i, s in enumerate(g["laminas"], 1):
        render(s, i, n, g.get("firma", "@jeissonnr"), a.fotos).save(
            os.path.join(a.out, f"{i:02d}.png"), optimize=True)
    print(f"{n} láminas en {a.out}")


if __name__ == "__main__":
    main()
