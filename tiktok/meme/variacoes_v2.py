"""Variações de TikTok de um meme da Cláudia, padrão de 09/11/2026 (decisão do Matheus):
v1 = original (legenda original, trilha original)
v2 = faixa branca com texto novo (formato que ganhou na semana 1) + trilha de OUTRO gênero
v3 = formato novo: legenda original borrada + caixas brancas arredondadas por linha (estilo texto nativo do TikTok),
     outro gancho, começo cortado (v3_pula) + trilha de um TERCEIRO gênero
Uso: python3 -I variacoes_v2.py <pasta do meme>
config.json, além dos campos de variacoes.py: "trilha_v2": [arquivo, segundo_do_drop], "trilha_v3": [arquivo, segundo_do_drop]
O drop de cada trilha cai exatamente no corte da virada.
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
D = os.path.abspath(sys.argv[1]); C = json.load(open(os.path.join(D, "config.json")))
POP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "carrossel", "Poppins-Bold.ttf")
W, H = 1080, 1920
def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr[-2000:])
def dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout)
def wrap(d, t, f, mw):
    out, cur = [], ""
    for w in t.split():
        x = (cur+" "+w).strip()
        if d.textlength(x, font=f) <= mw: cur = x
        else: out.append(cur); cur = w
    out.append(cur); return out
def caixas(path, text):
    y0, y1 = C["faixa"]; img = Image.new("RGBA",(W,H),(0,0,0,0)); d = ImageDraw.Draw(img)
    size = 60
    while True:
        f = ImageFont.truetype(POP, size); lines = wrap(d, text, f, 860); lh = int(size*1.45)
        if lh*len(lines) <= (y1-y0) or size <= 42: break
        size -= 4
    y = (y0+y1)/2 - lh*len(lines)/2
    for ln in lines:
        tw = d.textlength(ln, font=f); x = (W-tw)/2
        d.rounded_rectangle((x-26, y, x+tw+26, y+lh-8), radius=22, fill=(255,255,255,255))
        d.text((x, y+(lh-8-size*1.25)/2), ln, font=f, fill=(0,0,0)); y += lh
    img.save(path)
cut, card = C["corte"], C["card"]
v1 = os.path.join(D, "v1.mp4"); total = dur(v1)
ENC = ["-c:v","libx264","-preset","veryfast","-crf","20","-pix_fmt","yuv420p","-r","30","-c:a","aac","-b:a","192k","-movflags","+faststart"]
def audio_args(trilha, pula, length):
    arq, drop = trilha; start = drop - (cut - pula)
    return ["-ss", f"{start:.3f}", "-i", arq], f"atrim=0:{length:.3f},asetpts=PTS-STARTPTS,afade=t=out:st={length-0.8:.3f}:d=0.8,loudnorm=I=-14:TP=-1"
# v2: vídeo da v2 já feita (faixa branca) + trilha nova
v2src = os.path.join(D, "v2.mp4"); tmp = os.path.join(D, "_v2v.mp4"); os.replace(v2src, tmp)
a_in, a_f = audio_args(C["trilha_v2"], 0.0, total)
run(["ffmpeg","-y","-v","error","-i",tmp,*a_in,"-filter_complex",f"[1:a]{a_f}[a]","-map","0:v","-map","[a]","-t",f"{total:.3f}",*ENC,v2src]); os.remove(tmp)
# v3: caixa estilo TikTok sobre a legenda original borrada + trilha nova
pula = C.get("v3_pula", 0.8); L = total - pula
p1, p2 = os.path.join(D,"_c1.png"), os.path.join(D,"_c2.png"); caixas(p1, C["v3"][0]); caixas(p2, C["v3"][1])
y0, y1 = C["faixa"]; a_in, a_f = audio_args(C["trilha_v3"], pula, L)
fc = (f"[0:v]split[m][c];[c]crop={W}:{y1-y0}:0:{y0},boxblur=28:4[b];[m][b]overlay=0:{y0}:enable='lt(t,{card-pula:.3f})'[bv];"
      f"[bv][1:v]overlay=0:0:enable='lt(t,{cut-pula:.3f})'[x1];[x1][2:v]overlay=0:0:enable='between(t,{cut-pula:.3f},{card-pula-0.001:.3f})'[v];"
      f"[3:a]{a_f}[a]")
run(["ffmpeg","-y","-v","error","-ss",str(pula),"-i",v1,"-loop","1","-t","90","-i",p1,"-loop","1","-t","90","-i",p2,*a_in,
     "-filter_complex",fc,"-map","[v]","-map","[a]","-t",f"{L:.3f}",*ENC,os.path.join(D,"v3.mp4")])
os.remove(p1); os.remove(p2); print("ok", D)
