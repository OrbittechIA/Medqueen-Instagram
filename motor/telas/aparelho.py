"""Põe uma tela do HyperFrames dentro de um aparelho e salva PNG transparente.
Uso: python3 telas/aparelho.py <tela.png> <celular|tablet|laptop> <saida.png>
A tela fica sempre de frente e reta (regra do Matheus, 12/11/2026)."""
import sys, os, asyncio, urllib.parse
from playwright.async_api import async_playwright
tela, aparelho, saida = sys.argv[1], sys.argv[2], sys.argv[3]
from PIL import Image
w, h = Image.open(tela).size
# trava: tela de celular só em celular; tablet e laptop pedem tela renderizada no formato deitado/4:3
ok = {'celular': h / w >= 1.6, 'tablet': 0.6 <= h / w <= 1.5, 'laptop': 0.5 <= h / w <= 0.8}
if aparelho not in ok: sys.exit('aparelho deve ser celular, tablet ou laptop')
if not ok[aparelho]:
    sys.exit(f'tela {w}x{h} não serve pra {aparelho}: renderize a tela do HyperFrames no formato do aparelho '
             '(celular ~ 9:19,5; tablet ~ 4:3; laptop ~ 16:10) em vez de esticar ou cortar')
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': 1400, 'height': 1400}, device_scale_factor=2)
        url = 'file://' + os.path.abspath(os.path.join(os.path.dirname(__file__), 'aparelho.html'))
        url += '?' + urllib.parse.urlencode({'aparelho': aparelho, 'tela': 'file://' + os.path.abspath(tela)})
        await pg.goto(url); await pg.wait_for_timeout(600)
        await pg.locator('#stage').screenshot(path=saida, omit_background=True)
        await b.close()
asyncio.run(main())
