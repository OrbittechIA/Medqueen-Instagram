"""Carrosséis de foto do TikTok da MedQueen IA: fotos Kairogen 9:16 + texto (Poppins Bold branco com contorno preto).

Uso: python3 -I montar.py <semana.json> <pasta das fotos cruas> <pasta de saída>
semana.json: {"c1": [[texto, y_do_centro, tamanho], ..., [[texto, y, tam], [texto, y, tam]]], "c2": ...}
- Um item por slide, na ordem; o slide pode ter uma lista de textos.
- Foto crua: <pasta das fotos>/<cN>_<i>.png (i de 1 a 5). Saída: <saida>/<cN>/slideI.jpg e <saida>/<cN>_folha.jpg.
- Centro do texto sempre com y <= 1350 (embaixo disso a legenda e os botões do TikTok cobrem).
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

POP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Poppins-Bold.ttf")
W, H = 1080, 1920


def fit(path):
    im = Image.open(path).convert("RGB")
    s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H) // 2
    return im.crop((x, y, x + W, y + H))


def wrap(d, text, f, maxw):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: out.append(cur); cur = w
    out.append(cur); return out


def texto(img, text, yc, size=64, maxw=900):
    assert yc <= 1350, f"texto abaixo de y 1350: {text}"
    d = ImageDraw.Draw(img); f = ImageFont.truetype(POP, size)
    lines = wrap(d, text, f, maxw); lh = int(size * 1.22)
    y = yc - lh * len(lines) / 2
    for ln in lines:
        w = d.textlength(ln, font=f)
        d.text(((W - w) / 2, y), ln, font=f, fill="white", stroke_width=max(4, size // 13), stroke_fill="black")
        y += lh


if __name__ == "__main__":
    C = json.load(open(sys.argv[1])); RAW, OUT = sys.argv[2], sys.argv[3]
    for c, slides in C.items():
        os.makedirs(f"{OUT}/{c}", exist_ok=True)
        for i, s in enumerate(slides, 1):
            img = fit(f"{RAW}/{c}_{i}.png")
            for t, y, sz in (s if isinstance(s[0], list) else [s]):
                texto(img, t, y, sz)
            img.save(f"{OUT}/{c}/slide{i}.jpg", quality=93)
        ims = [Image.open(f"{OUT}/{c}/slide{i}.jpg").resize((270, 480)) for i in range(1, len(slides) + 1)]
        sh = Image.new("RGB", (270 * len(ims) + 40, 520), "white")
        for i, im in enumerate(ims): sh.paste(im, (20 + i * 270, 20))
        sh.save(f"{OUT}/{c}_folha.jpg", quality=88)
    print("ok")
