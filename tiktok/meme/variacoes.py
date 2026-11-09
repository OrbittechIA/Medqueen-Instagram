"""3 variações de TikTok de um meme da Cláudia que o Matheus entrega pronto (1080x1920).

Uso: python3 -I variacoes.py <pasta do meme>
A pasta tem o vídeo do Matheus (original.mp4) e um config.json:
{
 "corte": 4.0,          segundo em que a parte 1 (sofrimento) vira a parte 2 (virada)
 "card": 8.5,           segundo em que entra o card final (a faixa some antes dele)
 "faixa": [190, 540],   y de cima e de baixo da faixa branca em 1080x1920: tem que cobrir a legenda original
 "v2": ["texto parte 1", "texto parte 2"],
 "v3": ["texto parte 1", "texto parte 2"],
 "v3_pula": 0.8         segundos cortados do começo na v3 (corte diferente; padrão 0.8)
}
Saída na mesma pasta: v1.mp4 (original em 1080x1920), v2.mp4 (faixa branca, texto preto) e
v3.mp4 (faixa branca com outro gancho e outro corte). Faixa preta foi aposentada em 09/11/2026.
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

D = os.path.abspath(sys.argv[1])
C = json.load(open(os.path.join(D, "config.json")))
POP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "carrossel", "Poppins-Bold.ttf")
W, H = 1080, 1920
ENC = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-r", "30",
       "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart"]


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr[-2000:])


def wrap(d, text, f, maxw):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: out.append(cur); cur = w
    out.append(cur); return out


def faixa(path, text):
    y0, y1 = C["faixa"]
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    size = 66
    while True:
        f = ImageFont.truetype(POP, size); lines = wrap(d, text, f, 930); lh = int(size * 1.18)
        if lh * len(lines) <= (y1 - y0) - 30 or size <= 44: break
        size -= 4
    d.rectangle((0, y0, W, y1), fill=(255, 255, 255, 255))
    y = y0 + (y1 - y0 - lh * len(lines)) / 2 - 4
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=(0, 0, 0)); y += lh
    img.save(path)


def overlay(base, out, caps, start=0.0):
    ins, chain, last = (["-ss", str(start)] if start else []) + ["-i", base], [], "[0:v]"
    for i, (png, t0, t1) in enumerate(caps, 1):
        ins += ["-loop", "1", "-t", "90", "-i", png]
        chain.append(f"{last}[{i}:v]overlay=0:0:enable='between(t,{t0},{t1})'[v{i}]"); last = f"[v{i}]"
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", base],
                               capture_output=True, text=True).stdout) - start
    run(["ffmpeg", "-y", "-v", "error", *ins, "-filter_complex", ";".join(chain), "-map", last, "-map", "0:a", "-t", f"{dur}", *ENC, out])


base = os.path.join(D, "v1.mp4")
run(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(D, "original.mp4"),
     "-vf", "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:white", *ENC, base])
cut, card = C["corte"], C["card"]
for v in ("v2", "v3"):
    pula = C.get("v3_pula", 0.8) if v == "v3" else 0.0
    p1, p2 = os.path.join(D, f"_{v}_1.png"), os.path.join(D, f"_{v}_2.png")
    faixa(p1, C[v][0]); faixa(p2, C[v][1])
    overlay(base, os.path.join(D, f"{v}.mp4"), [(p1, 0, cut - pula - 0.001), (p2, cut - pula, card - pula - 0.001)], pula)
    os.remove(p1); os.remove(p2)
print("ok", D)
