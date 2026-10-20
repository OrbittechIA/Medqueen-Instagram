"""Folha de conferência: junta os PNGs de uma pasta lado a lado. Uso: python3 folha.py <pasta> [colunas]"""
import sys, glob
from PIL import Image
p = sys.argv[1]; c = int(sys.argv[2]) if len(sys.argv) > 2 else 4
fs = sorted(f for f in glob.glob(f'{p}/*.png') if not f.split('/')[-1].startswith(('_', 'folha')))
ims = [Image.open(f).convert('RGB') for f in fs]
w = 400; ims = [i.resize((w, int(i.height * w / i.width))) for i in ims]
h = max(i.height for i in ims); r = (len(ims) + c - 1) // c
F = Image.new('RGB', (c * (w + 12), r * (h + 12)), (200, 200, 210))
for k, i in enumerate(ims): F.paste(i, ((k % c) * (w + 12), (k // c) * (h + 12)))
F.save(f'{p}/folha.jpg', quality=85); print(f'{p}/folha.jpg')
