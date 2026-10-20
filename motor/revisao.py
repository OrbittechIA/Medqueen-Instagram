"""Folha de revisão da semana para o Matheus (uma imagem com tudo, em ordem de publicação).
Uso: python3 revisao.py AAAA-MM-DD <pasta em saida> [<pasta> ...]   -> ../revisao/AAAA-MM-DD.jpg
Para reel, use a pasta do reel: entram 4 quadros do vídeo."""
import sys, os, glob, subprocess
from PIL import Image, ImageDraw, ImageFont
BASE = os.path.dirname(os.path.abspath(__file__))
data, pastas = sys.argv[1], sys.argv[2:]
FT = ImageFont.truetype(f'{BASE}/www/fonts/PlusJakartaSans.ttf', 34)
linhas = []
for p in pastas:
    d = f'{BASE}/saida/{p}'
    mp4 = glob.glob(f'{d}/*.mp4')
    if mp4:
        ims = []
        dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp4[0]]).decode())
        for k, t in enumerate([dur * f for f in (.1, .35, .6, .9)]):
            o = f'{d}/_rev{k}.jpg'; subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f'{t:.2f}', '-i', mp4[0], '-frames:v', '1', o]); ims.append(o)
    else:
        ims = sorted(f for f in glob.glob(f'{d}/*.png') if not os.path.basename(f).startswith(('_', 'f', 'camada', 'folha', 'quadro')))
    linhas.append((p, [Image.open(f).convert('RGB') for f in ims]))
H = 420; GAP = 14
rows = []
for nome, ims in linhas:
    ims = [i.resize((int(i.width * H / i.height), H)) for i in ims]
    # quebra em linhas de no máximo 2400 px
    atual, larg = [], 0
    blocos = []
    for i in ims:
        if larg + i.width > 2400 and atual: blocos.append(atual); atual, larg = [], 0
        atual.append(i); larg += i.width + GAP
    if atual: blocos.append(atual)
    for k, b in enumerate(blocos): rows.append((nome if k == 0 else '', b))
W = 2400 + 2 * GAP
Ht = sum(H + GAP + (56 if n else 0) for n, _ in rows) + GAP
F = Image.new('RGB', (W, Ht), (236, 234, 246)); dr = ImageDraw.Draw(F); y = GAP
for nome, b in rows:
    if nome: dr.text((GAP, y + 8), nome, fill=(58, 29, 143), font=FT); y += 56
    x = GAP
    for i in b: F.paste(i, (x, y)); x += i.width + GAP
    y += H + GAP
os.makedirs(f'{BASE}/../revisao', exist_ok=True)
out = f'{BASE}/../revisao/{data}.jpg'; F.save(out, quality=82); print(out, F.size)
