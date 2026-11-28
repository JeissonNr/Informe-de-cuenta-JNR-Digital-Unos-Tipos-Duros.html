#!/usr/bin/env python3
"""Tarjetas de preguntas, puntaje y miniatura para el video Rueda de la Vida · Dinero y finanzas.
Uso: python3 -I pack_rueda.py --out carpeta [--cara foto.png]"""
import argparse, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
NAVY=(10,34,64); NAVY2=(6,20,40); LIME=(184,233,46); WHITE=(255,255,255); MUTED=(160,182,214)
D=os.path.dirname(os.path.abspath(__file__)); FONTS=os.path.join(D,"fonts")
F=lambda n,s: ImageFont.truetype(os.path.join(FONTS,n),s)
PREGUNTAS=[
 "¿Sé exactamente cuánto gano y cuánto gasto cada mes?",
 "¿Llevo un control escrito de mis finanzas: app, Excel o libreta?",
 "¿Tengo mis deudas bajo control y un plan claro para pagarlas?",
 "¿Tengo identificados y frenados mis gastos hormiga?",
 "¿Ahorro una parte fija de lo que gano antes de gastar?",
 "¿Tengo un fondo de emergencia para al menos 3 meses?",
 "¿Llego a fin de mes sin angustia por el dinero?",
 "¿Hablo de dinero con mi pareja o familia sin peleas ni secretos?",
 "¿Invierto en mí o en algo que me genere ingresos a futuro?",
 "¿Tengo una relación sana y tranquila con el dinero?"]
def wrap(t,f,mw):
    out=[];cur=""
    for w in t.split():
        x=(cur+" "+w).strip()
        if cur and f.getlength(x)>mw: out.append(cur);cur=w
        else: cur=x
    return out+[cur]
def card(top,bottom,h_text_fn):
    W,H=1080,1920; im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle((60,top+16,W-60,bottom+16),44,fill=(0,0,0,140))
    im=Image.alpha_composite(im,sh.filter(ImageFilter.GaussianBlur(24))); d=ImageDraw.Draw(im)
    d.rounded_rectangle((60,top,W-60,bottom),44,fill=(*NAVY,236),outline=(*LIME,255),width=4)
    h_text_fn(d); return im
def pregunta(i,q):
    def fn(d):
        fk=F("DMSans-Medium.ttf",34); t=f"DINERO Y FINANZAS · {i}/10"
        d.rounded_rectangle((110,1130,110+fk.getlength(t)+44,1186),28,fill=LIME); d.text((132,1139),t,font=fk,fill=NAVY)
        fq=F("Syne-ExtraBold.ttf",62); y=1225
        for ln in wrap(q,fq,860): d.text((110,y),ln,font=fq,fill=WHITE); y+=72
        fs=F("DMSans-Medium.ttf",38); d.text((110,1590),"Ponte nota del 1 al 10",font=fs,fill=MUTED)
        x=110
        for n in range(1,11):
            d.rounded_rectangle((x,1650,x+72,1722),14,outline=(*LIME,255) if n==10 else (*WHITE,120),width=3)
            fn_=F("DMSans-Medium.ttf",32); w=fn_.getlength(str(n)); d.text((x+36-w/2,1666),str(n),font=fn_,fill=WHITE); x+=87
    return card(1100,1770,fn)
def puntaje():
    def fn(d):
        fh=F("Syne-ExtraBold.ttf",60); y=1060
        for ln in ["Suma tus 10 notas."]: d.text((110,y),ln,font=fh,fill=WHITE); y+=80
        fb=F("DMSans-Medium.ttf",44)
        d.text((110,y+10),"100 − tu total =",font=fb,fill=MUTED)
        fbig=F("Syne-ExtraBold.ttf",78); d.text((110,y+70),"TU MARGEN",font=fbig,fill=LIME); d.text((110,y+160),"DE MEJORA",font=fbig,fill=LIME)
        fe=F("DMSans-Light.ttf",34); d.text((110,y+290),"Ejemplo: sumaste 62 → tienes 38 puntos para crecer.",font=fe,fill=WHITE)
        d.text((110,y+345),"Luego elige las 3 preguntas con más margen:",font=fe,fill=WHITE)
        d.text((110,y+395),"ahí empieza tu cambio.",font=F("DMSans-Medium.ttf",36),fill=LIME)
    return card(1010,1590,fn)
def miniatura(cara):
    W,H=1280,720; bg=Image.new("RGB",(W,H),NAVY2)
    g=Image.new("RGBA",(W,H),(0,0,0,0)); ImageDraw.Draw(g).ellipse((560,-200,1500,700),fill=(*LIME,70)); bg=Image.alpha_composite(bg.convert("RGBA"),g.filter(ImageFilter.GaussianBlur(160)))
    wheel=Image.open(os.path.join(OUT,"overlays_rueda","rueda_03.png")).resize((640,640),Image.LANCZOS)
    bg.alpha_composite(wheel,(700,40))
    if cara and os.path.exists(cara):
        c=ImageOps.exif_transpose(Image.open(cara)).convert("RGBA"); c=ImageOps.contain(c,(520,700)); bg.alpha_composite(c,(560-c.width//2+300,H-c.height))
    else:
        d=ImageDraw.Draw(bg); d.rounded_rectangle((760,470,1240,560),20,fill=(*NAVY,230),outline=(*WHITE,160),width=3)
        d.text((790,495),"TU CARA AQUÍ (recortada, sin fondo)",font=F("DMSans-Medium.ttf",26),fill=WHITE)
    d=ImageDraw.Draw(bg)
    f1=F("Syne-ExtraBold.ttf",96); f2=F("Syne-ExtraBold.ttf",118)
    for x,y,t,col in [(56,90,"¿CUÁNTO",WHITE),(56,195,"VALE TU",WHITE),(56,300,"DINERO?",LIME)]:
        d.text((x+5,y+7),t,font=f2 if col==LIME else f1,fill=(0,0,0,170)); d.text((x,y),t,font=f2 if col==LIME else f1,fill=col)
    fb=F("DMSans-Medium.ttf",40); t="Test de 10 preguntas"
    d.rounded_rectangle((56,470,56+fb.getlength(t)+48,540),35,fill=LIME); d.text((80,481),t,font=fb,fill=NAVY)
    return bg.convert("RGB")
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--out",required=True); ap.add_argument("--cara"); a=ap.parse_args()
    OUT=a.out; os.makedirs(os.path.join(OUT,"overlays_preguntas"),exist_ok=True)
    for i,q in enumerate(PREGUNTAS,1): pregunta(i,q).save(os.path.join(OUT,"overlays_preguntas",f"pregunta_{i:02d}.png"))
    puntaje().save(os.path.join(OUT,"overlays_preguntas","puntaje_margen.png"))
    miniatura(a.cara).save(os.path.join(OUT,"miniatura_youtube_1280x720.jpg"),quality=95)
    print("ok")
