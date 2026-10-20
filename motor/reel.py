"""Motor de Reel da MedQueen IA (1080x1920, 30 fps, sem som, entendível sem áudio).
Um print alto do app rola dentro de um tablet em pé; destaques acendem nos pontos-chave;
os títulos de cima trocam por trecho; no fim, cartão com a chamada.
Regra: print nunca solto (sempre no tablet, com destaque).

Uso (no spec):
  from reel import Reel
  r = Reel('saida/r01-krebs', img='desk-ia-krebs-longo.png', crop_x=(20, 620))
  r.trecho(0, 3, 'Bioquímica', 'Ciclo de Krebs em 15 segundos.')   # títulos
  r.rolagem([(0, 0), (2.5, 0), (4.5, 640), ...])                     # (t, y na imagem)
  r.destaque(1.0, 3.0, (52, 164, 315, 26))                           # (t0, t1, caixa na imagem)
  r.fim(12, 'Pergunta. A Queen IA explica.', 'E a resposta vira flashcards ou questões.', 'Teste grátis. Link na bio.')
  r.gravar(16)
"""
import os, subprocess
from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
F = f'file://{BASE}/www/fonts'; MARCA = f'file://{BASE}/www/marca'; PR = f'{BASE}/prints'
W, H, FPS = 1080, 1920, 30
TX, TY, TW, TH = 170, 700, 740, 986      # tela do tablet (em pé, 3:4)
BZ = 24

CSS = f"""
@font-face{{font-family:J;src:url({F}/PlusJakartaSans.ttf);font-weight:200 800}}
@font-face{{font-family:S;src:url({F}/SourceSans3.ttf);font-weight:200 900}}
*{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{background:#F6F5FC;font-family:S;color:#111827;position:relative}}
body.camada{{background:transparent}}
.fundo{{position:absolute;inset:0;background:radial-gradient(700px 600px at 95% 4%,rgba(158,140,240,.32),transparent 70%),radial-gradient(700px 600px at 0% 100%,rgba(240,111,143,.22),transparent 70%)}}
.logo{{position:absolute;left:90px;top:170px;--h:66px;display:inline-flex;align-items:flex-start;height:var(--h)}}
.logo img{{height:var(--h);display:block}}
.logo b{{margin-left:calc(var(--h)*-0.005);margin-top:calc(var(--h)*0.368);height:calc(var(--h)*0.292);padding:0 calc(var(--h)*0.075);border-radius:calc(var(--h)*0.07);background:#3A1D8F;color:#fff;font-family:J;font-weight:800;font-size:calc(var(--h)*0.19);letter-spacing:.04em;display:inline-flex;align-items:center;line-height:1}}
.txt{{position:absolute;left:90px;right:90px;top:270px;height:360px;display:flex;flex-direction:column;justify-content:flex-end}}
.olho{{align-self:flex-start;font-family:J;font-weight:700;font-size:26px;letter-spacing:.07em;text-transform:uppercase;color:#3A1D8F;background:#ECE8FB;border-radius:999px;padding:12px 24px;margin-bottom:22px}}
h1{{font-family:J;font-weight:800;font-size:var(--t,78px);line-height:1.04;letter-spacing:-.018em;word-spacing:.04em}}
h1 em{{font-style:normal;color:#3A1D8F;background:linear-gradient(transparent 68%,rgba(240,111,143,.32) 68%)}}
.tab{{position:absolute;left:{TX-BZ}px;top:{TY-BZ}px;width:{TW+2*BZ}px;height:{TH+2*BZ}px;border-radius:56px;background:linear-gradient(150deg,#2B2F38,#11141A 45%,#2A2E36);box-shadow:0 60px 90px -50px rgba(58,29,143,.6)}}
.fim{{position:absolute;left:110px;right:110px;top:1080px;background:linear-gradient(135deg,#3A1D8F,#4B2AB0 60%,#5B3BC4);color:#fff;border-radius:44px;padding:52px 54px;box-shadow:0 50px 90px -40px rgba(58,29,143,.85);overflow:hidden}}
.fim:after{{content:"";position:absolute;right:-120px;top:-120px;width:380px;height:380px;border-radius:50%;background:radial-gradient(circle,rgba(240,111,143,.55),transparent 70%)}}
.fim h2{{font-family:J;font-weight:800;font-size:60px;line-height:1.08;position:relative;z-index:1}}
.fim p{{font-size:38px;line-height:1.3;margin-top:20px;color:#E7E3FA;position:relative;z-index:1}}
.fim b{{display:inline-block;margin-top:34px;background:#fff;color:#3A1D8F;font-family:J;font-weight:800;font-size:34px;padding:22px 34px;border-radius:999px;position:relative;z-index:1}}
"""

def _html(corpo, camada=False, t=78):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{"camada" if camada else ""}" style="--t:{t}px">{corpo}</body></html>'

def suave(x):
    x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)

class Reel:
    def __init__(self, pasta, img, crop_x=None):
        self.pasta = os.path.join(BASE, pasta); os.makedirs(self.pasta, exist_ok=True)
        im = Image.open(f'{PR}/{img}').convert('RGB')
        if crop_x: im = im.crop((crop_x[0], 0, crop_x[1], im.height)); self.ox = crop_x[0]
        else: self.ox = 0
        self.s = TW / im.width
        self.im = im.resize((TW, int(im.height * self.s)), Image.LANCZOS)
        self.trechos = []; self.keys = []; self.dest = []; self._fim = None

    def trecho(self, t0, t1, olho, titulo, t=78):
        self.trechos.append((t0, t1, olho, titulo, t))

    def rolagem(self, keys):
        self.keys = keys

    def destaque(self, t0, t1, caixa):
        self.dest.append((t0, t1, caixa))

    def fim(self, t0, titulo, texto, acao):
        self._fim = (t0, titulo, texto, acao)

    def _y(self, t):
        k = self.keys
        if t <= k[0][0]: return k[0][1]
        for (a, ya), (b, yb) in zip(k, k[1:]):
            if a <= t <= b: return ya + (yb - ya) * suave((t - a) / max(1e-6, b - a))
        return k[-1][1]

    def _render(self):
        pares = []
        for i, (t0, t1, olho, titulo, tt) in enumerate(self.trechos):
            corpo = f'<div class="fundo"></div><span class="logo"><img src="{MARCA}/medqueen-logo-horizontal.svg"><b>IA</b></span><div class="txt"><div class="olho">{olho}</div><h1>{titulo}</h1></div><div class="tab"></div>'
            pares.append((f'f{i}', _html(corpo, t=tt), False))
        if self._fim:
            _, a, b, c = self._fim
            pares.append(('camada-fim', _html(f'<div class="fim"><h2>{a}</h2><p>{b}</p><b>{c}</b></div>', camada=True), True))
        with sync_playwright() as p:
            br = p.chromium.launch(); pg = br.new_page(viewport={'width': W, 'height': H})
            for nome, h, tr in pares:
                f = f'{self.pasta}/{nome}.html'; open(f, 'w', encoding='utf-8').write(h)
                pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(250)
                pg.screenshot(path=f'{self.pasta}/{nome}.png', omit_background=tr)
            br.close()
        self.fundos = [Image.open(f'{self.pasta}/f{i}.png').convert('RGB') for i in range(len(self.trechos))]
        self.camada = Image.open(f'{self.pasta}/camada-fim.png').convert('RGBA') if self._fim else None
        m = Image.new('L', (TW * 3, TH * 3), 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, TW * 3 - 1, TH * 3 - 1), radius=34 * 3, fill=255)
        self.masc = m.resize((TW, TH), Image.LANCZOS)

    def _fundo(self, t):
        for i, (t0, t1, *_r) in enumerate(self.trechos):
            if t0 <= t < t1:
                if i > 0 and t < t0 + 0.35:
                    return Image.blend(self.fundos[i - 1], self.fundos[i], suave((t - t0) / 0.35))
                return self.fundos[i]
        return self.fundos[-1]

    def quadro(self, t):
        q = self._fundo(t).copy()
        y = int(self._y(t) * self.s); y = max(0, min(self.im.height - TH, y))
        tela = self.im.crop((0, y, TW, y + TH)).convert('RGBA')
        d = ImageDraw.Draw(tela, 'RGBA')
        for (t0, t1, (bx, by, bw, bh)) in self.dest:
            if t0 - 0.3 <= t <= t1 + 0.3:
                a = suave((t - (t0 - 0.3)) / 0.3) if t < t0 else (1 - suave((t - t1) / 0.3)) if t > t1 else 1
                x0 = (bx - self.ox) * self.s - 12; y0 = by * self.s - y - 12
                x1 = x0 + bw * self.s + 24; y1 = y0 + bh * self.s + 24
                d.rounded_rectangle((x0 - 8, y0 - 8, x1 + 8, y1 + 8), 22, outline=(240, 111, 143, int(70 * a)), width=10)
                d.rounded_rectangle((x0, y0, x1, y1), 16, outline=(240, 111, 143, int(255 * a)), width=6)
        q.paste(tela.convert('RGB'), (TX, TY), self.masc)
        if self._fim and t >= self._fim[0]:
            a = suave((t - self._fim[0]) / 0.4)
            c = self.camada if a >= 1 else self.camada.copy()
            if a < 1: c.putalpha(c.getchannel('A').point(lambda v: int(v * a)))
            qa = q.convert('RGBA'); qa.alpha_composite(c); q = qa.convert('RGB')
        return q

    def gravar(self, dur, nome='reel.mp4', capa_t=1.0):
        self._render()
        saida = f'{self.pasta}/{nome}'
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
               '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', saida]
        pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for k in range(int(dur * FPS)):
            pr.stdin.write(self.quadro(k / FPS).tobytes())
        pr.stdin.close(); pr.wait()
        self.quadro(capa_t).save(saida.replace('.mp4', '-capa.jpg'), quality=92)
        print('ok', saida)
        return saida
