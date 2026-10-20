"""Copia o que foi gerado em motor/saida/<pasta> para o repositório e mostra as URLs públicas.
Uso: python3 publicar.py <pasta em saida> <destino no repo>
  ex: python3 publicar.py p10-adv-prazo posts/2026-10-26-p10-adv-prazo
      python3 publicar.py stories-2026-10-26 stories/2026-10-26
PNG vira JPG (qualidade 95). MP4 vai como reel.mp4. Depois: git add, commit e push.
"""
import sys, os, json, glob, shutil
from PIL import Image
MOTOR = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(MOTOR)
RAW = 'https://raw.githubusercontent.com/OrbittechIA/Medqueen-Instagram/main/'
orig, dest = sys.argv[1], sys.argv[2].strip('/')
src = os.path.join(MOTOR, 'saida', orig); out = os.path.join(REPO, dest); os.makedirs(out, exist_ok=True)
urls = []
for f in sorted(glob.glob(f'{src}/*.png')):
    nome = os.path.basename(f)
    if nome.startswith(('f', 'camada')) and glob.glob(f'{src}/*.mp4'):
        continue  # fundos do reel não são publicados
    j = nome[:-4] + '.jpg'
    Image.open(f).convert('RGB').save(f'{out}/{j}', quality=95, optimize=True)
    urls.append(RAW + f'{dest}/{j}')
for f in sorted(glob.glob(f'{src}/*.mp4')):
    shutil.copy(f, f'{out}/reel.mp4'); urls.append(RAW + f'{dest}/reel.mp4')
print(json.dumps(urls, indent=1))
