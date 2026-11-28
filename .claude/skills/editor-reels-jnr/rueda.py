#!/usr/bin/env python3
"""Rueda de la Vida JNR — genera los PNG transparentes para superponer en video.
Uso: python3 -I rueda.py --out carpeta   → rueda_base.png, rueda_01..10.png (área encendida), rueda_dinero_sel.png
"""
import argparse, math, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
AREAS = ["Salud y energía", "Mente y emociones", "Dinero y finanzas", "Trabajo y propósito",
         "Familia y relaciones", "Amor y pareja", "Crecimiento personal", "Fe y espiritualidad",
         "Diversión y ocio", "Entorno y hogar"]
NAVY=(10,34,64); LIME=(184,233,46); WHITE=(255,255,255)
FONTS=os.path.join(os.path.dirname(os.path.abspath(__file__)),"fonts")
S=1080; C=S/2; R=470; RI=118; SS=2

def wheel(lit=None, selected=False):
    s=S*SS; c=C*SS; r=R*SS; ri=RI*SS
    im=Image.new("RGBA",(s,s),(0,0,0,0)); d=ImageDraw.Draw(im)
    glow=Image.new("RGBA",(s,s),(0,0,0,0)); dg=ImageDraw.Draw(glow)
    n=len(AREAS); step=360/n
    for i in range(n):
        a0=-90+i*step; a1=a0+step
        on = lit is not None and i==lit
        fill=(*LIME,235) if on else ((*NAVY,200) if i%2==0 else (16,48,88,200))
        d.pieslice((c-r,c-r,c+r,c+r),a0,a1,fill=fill)
        if on:
            dg.pieslice((c-r-30,c-r-30,c+r+30,c+r+30),a0,a1,fill=(*LIME,200))
    glow=glow.filter(ImageFilter.GaussianBlur(40*SS))
    out=Image.alpha_composite(glow,im); d=ImageDraw.Draw(out)
    for i in range(n):  # separadores
        a=math.radians(-90+i*step)
        d.line((c+ri*math.cos(a),c+ri*math.sin(a),c+r*math.cos(a),c+r*math.sin(a)),fill=(*WHITE,120),width=3*SS)
    d.ellipse((c-r,c-r,c+r,c+r),outline=(*WHITE,200),width=4*SS)
    d.ellipse((c-ri,c-ri,c+ri,c+ri),fill=(*NAVY,255),outline=(*LIME,255),width=4*SS)
    ft=ImageFont.truetype(os.path.join(FONTS,"Syne-ExtraBold.ttf"),26*SS)
    for k,t in enumerate(["RUEDA","DE LA","VIDA"]):
        w=ft.getlength(t); d.text((c-w/2,c-50*SS+k*33*SS),t,font=ft,fill=LIME if k==2 else WHITE)
    fl=ImageFont.truetype(os.path.join(FONTS,"DMSans-Medium.ttf"),25*SS)
    for i,t in enumerate(AREAS):
        mid=math.radians(-90+(i+0.5)*step); rr=(r+ri)/2+28*SS
        words=t.split(); lines=[" ".join(words[:1])," ".join(words[1:])] if len(words)>1 else [t]
        on = lit is not None and i==lit
        for j,ln in enumerate(lines):
            w=fl.getlength(ln); x=c+rr*math.cos(mid)-w/2; y=c+rr*math.sin(mid)-28*SS+j*30*SS
            d.text((x,y),ln,font=fl,fill=NAVY if on else WHITE)
    if selected and lit is not None:
        fb=ImageFont.truetype(os.path.join(FONTS,"Syne-ExtraBold.ttf"),34*SS)
        t="SELECCIONADO ✓".replace(" ✓","")
        w=fb.getlength(t); d.rounded_rectangle((c-w/2-30*SS,s-70*SS,c+w/2+30*SS,s-14*SS),28*SS,fill=(*LIME,255))
        d.text((c-w/2,s-64*SS),t,font=fb,fill=NAVY)
    return out.resize((S,S),Image.LANCZOS)

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--out",required=True); a=ap.parse_args()
    os.makedirs(a.out,exist_ok=True)
    wheel().save(os.path.join(a.out,"rueda_base.png"))
    for i,t in enumerate(AREAS):
        wheel(i).save(os.path.join(a.out,f"rueda_{i+1:02d}.png"))
    wheel(2,True).save(os.path.join(a.out,"rueda_dinero_seleccionado.png"))
    print("ok")
