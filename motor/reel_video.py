"""Motor de Reel em vídeo da MedQueen IA (1080x1920, 30 fps, com música de fundo baixa e efeitos sonoros).

Conceito (pedido do Matheus em 24/10/2026, inspirado no vídeo da Orbyt para advogados):
roteiro em cenas curtas; título grande que entra em cima; tela real do app dentro de tablet ou celular;
zoom numa parte da tela; destaque rosa no ponto que importa; selos que vão aparecendo; Queen IA como apoio;
cartão final com a chamada. Música só de fundo (baixa) e efeitos sonoros nas trocas e nos cliques.

Uso (num spec em posts/rv*.py):
    from reel_video import Reel, Cena
    r = Reel('saida/rv02-erro-vira-treino', musica='trilha-01.mp3')
    r.cena(Cena(3.2, 'Você errou 7 de 10 no simulado.', olho='Medicina', escuro=True, sons=[(0.1,'hit')]))
    r.cena(Cena(7, 'Na MedQueen IA, o <em>erro vira treino</em>.', aparelho='tablet', img='desk-simulados.png',
                zoom=[(0,(0,0,1568,704)), (3,(560,0,700,315))], destaques=[(3.3,6.8,(610,40,190,30))],
                selos=[(4,'Caderno de erros')], sons=[(0,'woosh_2'),(3.2,'mouse_click')]))
    r.final('Aproveite os 7 dias de teste grátis.', 'Link na bio')
    r.gravar()

Regras: print nunca solto (sempre no aparelho, com destaque). Sem pessoa gerada por IA; a Queen IA oficial pode entrar.
Títulos curtos (até ~9 palavras), sem travessão.
"""
import os, subprocess, math
from PIL import Image, ImageDraw, ImageFilter
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
F = f'file://{BASE}/www/fonts'; MARCA = f'{BASE}/www/marca'; PR = f'{BASE}/prints'
SOM = f'{BASE}/www/som'
W, H, FPS = 1080, 1920, 30

CSS = f"""
@font-face{{font-family:J;src:url({F}/PlusJakartaSans.ttf);font-weight:200 800}}
@font-face{{font-family:S;src:url({F}/SourceSans3.ttf);font-weight:200 900}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{background:transparent}}
.lg{{--h:64px;display:inline-flex;align-items:flex-start;height:var(--h)}}
.lg img{{height:var(--h);display:block}}
.lg b{{margin-top:calc(var(--h)*0.368);height:calc(var(--h)*0.292);padding:0 calc(var(--h)*0.075);border-radius:calc(var(--h)*0.07);background:#3A1D8F;color:#fff;font-family:J;font-weight:800;font-size:calc(var(--h)*0.19);letter-spacing:.04em;display:inline-flex;align-items:center;line-height:1}}
.escuro .lg b{{background:#fff;color:#3A1D8F}}
.olho{{display:inline-flex;align-items:center;gap:12px;font-family:J;font-weight:700;font-size:28px;letter-spacing:.08em;text-transform:uppercase;color:#F06F8F;margin-bottom:22px}}
.olho:before{{content:"";width:12px;height:12px;border-radius:50%;background:#F06F8F}}
h1{{font-family:J;font-weight:800;font-size:var(--t,84px);line-height:1.06;letter-spacing:-.02em;color:#111827}}
.escuro h1{{color:#fff}}
h1 em{{font-style:normal;color:#3A1D8F;background:linear-gradient(transparent 72%,rgba(240,111,143,.55) 72%)}}
.escuro h1 em{{color:#FFB3C6;background:linear-gradient(transparent 72%,rgba(240,111,143,.45) 72%)}}
.sub{{font-family:S;font-size:40px;line-height:1.3;color:#475569;margin-top:22px}}
.escuro .sub{{color:#CFC8F2}}
.selo{{display:inline-flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:20px 28px;font-family:J;font-weight:700;font-size:34px;color:#111827;box-shadow:0 18px 40px -18px rgba(58,29,143,.45);border:2px solid #ECE8FB}}
.selo i{{width:40px;height:40px;border-radius:50%;background:#3A1D8F;display:inline-flex;align-items:center;justify-content:center;color:#fff;font-style:normal;font-size:24px}}
.balao{{max-width:760px;background:#fff;border-radius:28px;padding:24px 30px;font-family:S;font-size:36px;line-height:1.3;color:#111827;box-shadow:0 18px 40px -18px rgba(58,29,143,.45);border:2px solid #ECE8FB}}
.balao b{{display:block;font-family:J;font-size:24px;color:#3A1D8F;letter-spacing:.06em;text-transform:uppercase;margin-bottom:6px}}
.pergunta{{background:#3A1D8F;color:#fff;border-radius:28px 28px 6px 28px;padding:24px 32px;font-family:S;font-size:38px;max-width:820px}}
.fim{{width:900px;background:linear-gradient(135deg,#3A1D8F,#4B2AB0 60%,#5B3BC4);color:#fff;border-radius:48px;padding:60px 58px;position:relative;overflow:hidden}}
.fim:after{{content:"";position:absolute;right:-120px;top:-120px;width:400px;height:400px;border-radius:50%;background:radial-gradient(circle,rgba(240,111,143,.55),transparent 70%)}}
.fim h2{{font-family:J;font-weight:800;font-size:66px;line-height:1.08;position:relative;z-index:1}}
.fim p{{font-size:38px;line-height:1.3;margin-top:22px;color:#E7E3FA;position:relative;z-index:1;font-family:S}}
.tela{{position:absolute;left:0;top:0;width:1080px;height:1920px;padding:330px 80px 220px;display:flex;flex-direction:column}}
.big{{font-family:J;font-weight:800;font-size:var(--g,112px);line-height:1.06;letter-spacing:-.025em;color:#111827}}
.escuro .big,.roxo .big{{color:#fff}}
.big em{{font-style:normal;color:#3A1D8F;background:linear-gradient(transparent 70%,rgba(240,111,143,.55) 70%)}}
.escuro .big em,.roxo .big em{{color:#FFB3C6;background:none}}
.oculto{{visibility:hidden}}
.tag{{align-self:flex-start;font-family:J;font-weight:800;font-size:30px;letter-spacing:.08em;text-transform:uppercase;color:#fff;background:#F06F8F;border-radius:999px;padding:12px 26px;margin-bottom:34px}}
.q{{font-family:J;font-weight:800;font-size:92px;line-height:1.08;letter-spacing:-.02em;color:#111827;margin-bottom:34px}}
.alt{{display:flex;gap:24px;align-items:center;background:#fff;border-radius:30px;padding:34px 34px;font-family:S;font-size:48px;line-height:1.22;color:#111827;margin-top:26px;border:3px solid #E4E2F0;box-shadow:0 14px 30px -20px rgba(58,29,143,.35)}}
.alt b{{flex:none;width:76px;height:76px;border-radius:50%;background:#ECE8FB;color:#3A1D8F;font-family:J;font-size:32px;display:flex;align-items:center;justify-content:center}}
.alt.certa{{border-color:#16A34A;background:#ECFDF3}} .alt.certa b{{background:#16A34A;color:#fff}}
.alt.apagada{{opacity:.32}}
.cont{{position:absolute;right:80px;top:150px;width:150px;height:150px;border-radius:50%;background:#F06F8F;color:#fff;font-family:J;font-weight:800;font-size:92px;display:flex;align-items:center;justify-content:center;box-shadow:0 20px 40px -16px rgba(240,111,143,.8)}}
.expl{{margin-top:34px;background:#3A1D8F;color:#fff;border-radius:30px;padding:34px 36px;font-family:S;font-size:46px;line-height:1.28}}
.expl b{{color:#FFB3C6}}
.chat{{display:flex;flex-direction:column;gap:22px;margin-top:20px}}
.msg{{max-width:820px;border-radius:38px;padding:30px 36px;font-family:S;font-size:46px;line-height:1.3}}
.aluno{{align-self:flex-end;background:#3A1D8F;color:#fff;border-bottom-right-radius:10px}}
.qmsg{{align-self:flex-start;display:flex;gap:18px;align-items:flex-end}}
.qmsg img{{width:84px;height:84px;border-radius:50%;border:3px solid #fff;box-shadow:0 6px 16px -8px rgba(0,0,0,.4)}}
.qmsg .msg{{background:#fff;color:#111827;border:2px solid #ECE8FB;border-bottom-left-radius:10px;max-width:720px}}
.qmsg .msg b{{color:#3A1D8F}}
.dots{{display:flex;gap:12px;padding:34px 36px}} .dots i{{width:18px;height:18px;border-radius:50%;background:#B9B1E6}}
.cab{{display:flex;align-items:center;gap:20px;font-family:J;font-weight:800;font-size:38px;color:#111827;padding-bottom:22px;border-bottom:2px solid #E4E2F0}}
.cab img{{width:96px;height:96px;border-radius:50%}} .cab small{{display:block;font-family:S;font-weight:600;font-size:26px;color:#16A34A}}
.lados{{display:flex;gap:28px;margin-top:40px}}
.col{{flex:1;border-radius:34px;padding:34px 30px}}
.col.ruim{{background:#EDEBF5}} .col.bom{{background:#3A1D8F;color:#fff}}
.col h3{{font-family:J;font-weight:800;font-size:40px;margin-bottom:22px}}
.col p{{font-family:S;font-size:34px;line-height:1.28;margin-top:18px;padding-left:44px;position:relative}}
.col.ruim p:before{{content:"✕";position:absolute;left:0;color:#E11D48;font-weight:800}}
.col.bom p:before{{content:"✓";position:absolute;left:0;color:#FFB3C6;font-weight:800}}
.afirm{{font-family:J;font-weight:800;font-size:100px;line-height:1.06;letter-spacing:-.02em;color:#111827;margin-top:60px}}
.carimbo{{position:absolute;left:50%;top:1230px;transform:translate(-50%,0) rotate(-10deg);font-family:J;font-weight:800;font-size:150px;letter-spacing:.04em;padding:14px 56px;border:14px solid;border-radius:30px;background:rgba(255,255,255,.88)}}
.carimbo.mito{{color:#E11D48;border-color:#E11D48}} .carimbo.verdade{{color:#16A34A;border-color:#16A34A}}
.porque{{position:absolute;left:90px;right:90px;top:1560px;font-family:S;font-size:50px;line-height:1.3;color:#475569;text-align:center}}
.porque b{{color:#111827}}
.ep{{font-family:J;font-weight:800;font-size:280px;line-height:1;color:#3A1D8F;letter-spacing:-.04em}}
.item{{display:flex;gap:26px;align-items:flex-start;margin-top:34px;font-family:J;font-weight:700;font-size:52px;line-height:1.15;color:#111827}}
.item b{{flex:none;width:86px;height:86px;border-radius:24px;background:#F06F8F;color:#fff;font-size:46px;display:flex;align-items:center;justify-content:center}}
.item span small{{display:block;font-family:S;font-weight:400;font-size:34px;color:#475569;margin-top:8px}}
.fim .bt{{display:inline-block;margin-top:38px;background:#fff;color:#3A1D8F;font-family:J;font-weight:800;font-size:38px;padding:24px 40px;border-radius:999px;position:relative;z-index:1}}
"""

def _sfx_path(nome):
    for raiz, _, fs in os.walk(SOM):
        for f in fs:
            if os.path.splitext(f)[0] == nome: return os.path.join(raiz, f)
    raise FileNotFoundError(nome)

def suave(x):
    x = max(0.0, min(1.0, x)); return x * x * (3 - 2 * x)

def saida_rapida(x):  # ease-out
    x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3

class Cena:
    """dur: segundos. titulo: HTML curto (aceita <em>). aparelho: None | 'tablet' | 'celular'.
    img: print em motor/prints. zoom: [(t, (x,y,w,h))] janela da imagem mostrada na tela (anima entre chaves).
    destaques: [(t0,t1,(x,y,w,h))] em pixels da imagem. selos: [(t,'texto')] aparecem empilhados embaixo.
    balao: (t, 'html') balão da Queen IA. pergunta: (t, 'texto') bolha de pergunta que é digitada.
    queen: (t, 'busto'|'corpo') imagem da Queen IA. sons: [(t, nome, ganho_db)] efeitos."""
    def __init__(self, dur, titulo, olho=None, sub=None, escuro=False, aparelho=None, img=None, zoom=None,
                 destaques=None, selos=None, balao=None, pergunta=None, queen=None, sons=None, t=None, lupas=None, estados=None, fundo=None):
        # estados: [(t, html)] telas inteiras (1080x1920, classe .tela) que se sucedem; usadas pelos formatos de reel_formatos.py
        # fundo: 'claro' | 'escuro' | 'roxo' (padrão: escuro se escuro=True, senão claro)
        self.estados = estados or []; self.fundo = fundo or ('escuro' if escuro else 'claro')
        if self.fundo in ('escuro', 'roxo'): escuro = True
        # aparelho 'pronto' = print que já vem com moldura de celular (ex.: cel-ia-krebs.png); sem zoom, use lupas.
        # lupas: [(t0, t1, (x,y,w,h) na imagem, (cx, cy, raio) na tela)]
        self.lupas = lupas or []
        self.dur, self.titulo, self.olho, self.sub, self.escuro = dur, titulo, olho, sub, escuro
        self.aparelho, self.img, self.zoom = aparelho, img, zoom
        self.destaques = destaques or []; self.selos = selos or []
        self.balao, self.pergunta, self.queen = balao, pergunta, queen
        self.sons = [(s[0], s[1], s[2] if len(s) > 2 else -8) for s in (sons or [])]
        self.t = t

# geometria dos aparelhos (área da tela)
TAB = dict(x=60, y=760, w=960, h=620, borda=26, raio=30)       # tablet deitado (prints de computador)
TAB_PE = dict(x=170, y=700, w=740, h=980, borda=24, raio=34)   # tablet em pé (print alto)
CEL = dict(x=290, y=640, w=500, h=1020, borda=16, raio=58)     # celular

class Reel:
    def __init__(self, pasta, musica=None, musica_db=-18):
        self.pasta = os.path.join(BASE, pasta); os.makedirs(self.pasta, exist_ok=True)
        self.cenas = []; self.musica = musica; self.musica_db = musica_db; self._fim = None

    def cena(self, c): self.cenas.append(c); return c

    def final(self, titulo, botao, texto=None, dur=4.5, queen=True, sons=None):
        self._fim = dict(titulo=titulo, botao=botao, texto=texto, dur=dur, queen=queen,
                         sons=[(s[0], s[1], s[2] if len(s) > 2 else -8) for s in (sons or [(0, 'woosh_2'), (0.35, 'notification', -10)])])

    # ---------- camadas estáticas via navegador ----------
    def _html_png(self, pg, corpo, nome, largura=W, classe=''):
        f = f'{self.pasta}/{nome}.html'
        open(f, 'w', encoding='utf-8').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{classe}"><div id="x" style="display:inline-block;max-width:{largura}px">{corpo}</div></body></html>')
        pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(120)
        pg.locator('#x').screenshot(path=f'{self.pasta}/{nome}.png', omit_background=True)
        return Image.open(f'{self.pasta}/{nome}.png').convert('RGBA')

    def _preparar(self):
        self.camadas = []
        with sync_playwright() as p:
            br = p.chromium.launch(); pg = br.new_page(viewport={'width': W, 'height': H})
            logo = f'<span class="lg"><img src="file://{MARCA}/medqueen-logo-horizontal.svg"><b>IA</b></span>'
            self.logo_claro = self._html_png(pg, logo, 'logo-claro')
            self.logo_escuro = self._html_png(pg, logo, 'logo-escuro', classe='escuro')
            for i, c in enumerate(self.cenas):
                tt = c.t or (96 if not c.aparelho else 76)
                corpo = (f'<div class="olho">{c.olho}</div>' if c.olho else '') + f'<h1 style="--t:{tt}px">{c.titulo}</h1>' + (f'<p class="sub">{c.sub}</p>' if c.sub else '')
                cam = dict(titulo=self._html_png(pg, corpo, f'c{i}-titulo', largura=920, classe='escuro' if c.escuro else '') if c.titulo else Image.new('RGBA', (1, 1), (0, 0, 0, 0)))
                cam['selos'] = [(t, self._html_png(pg, f'<div class="selo"><i>✓</i>{txt}</div>', f'c{i}-selo{k}')) for k, (t, txt) in enumerate(c.selos)]
                if c.balao: cam['balao'] = (c.balao[0], self._html_png(pg, f'<div class="balao"><b>Queen IA</b>{c.balao[1]}</div>', f'c{i}-balao', largura=800))
                if c.pergunta:
                    txt = c.pergunta[1]; passos = []
                    for n in range(0, len(txt) + 1, max(1, len(txt) // 14)):
                        passos.append(self._html_png(pg, f'<div class="pergunta">{txt[:n] or "&nbsp;"}</div>', f'c{i}-perg{n}', largura=860))
                    passos.append(self._html_png(pg, f'<div class="pergunta">{txt}</div>', f'c{i}-pergfim', largura=860))
                    cam['pergunta'] = (c.pergunta[0], passos)
                cam['estados'] = []
                for k, (te, html) in enumerate(c.estados):
                    f = f'{self.pasta}/c{i}-e{k}.html'
                    open(f, 'w', encoding='utf-8').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{c.fundo}" style="width:{W}px;height:{H}px;position:relative;overflow:hidden"><div class="tela">{html}</div></body></html>')
                    pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(100)
                    pg.screenshot(path=f'{self.pasta}/c{i}-e{k}.png', omit_background=True)
                    cam['estados'].append((te, Image.open(f'{self.pasta}/c{i}-e{k}.png').convert('RGBA')))
                self.camadas.append(cam)
            if self._fim:
                f = self._fim
                corpo = f'<div class="fim"><h2>{f["titulo"]}</h2>' + (f'<p>{f["texto"]}</p>' if f['texto'] else '') + f'<div class="bt">{f["botao"]}</div></div>'
                self.cam_fim = self._html_png(pg, corpo, 'fim-cartao')
            br.close()
        self.queen_corpo = Image.open(f'{MARCA}/queen_ia_recorte.png').convert('RGBA')
        self.queen_busto = Image.open(f'{MARCA}/queen-ia-bust-master-384.png').convert('RGBA')
        self.fundo_claro = self._fundo(False); self.fundo_escuro = self._fundo(True); self.fundo_roxo = self._fundo('roxo')
        self.imgs = {}
        for c in self.cenas:
            if c.img and c.img not in self.imgs: self.imgs[c.img] = Image.open(f'{PR}/{c.img}').convert('RGB')

    def _fundo(self, escuro):
        im = Image.new('RGB', (W, H), '#3A1D8F' if escuro == 'roxo' else '#140B33' if escuro else '#F6F5FC')
        cam = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(cam)
        if escuro:
            d.ellipse((620, -300, 1500, 600), fill=(88, 59, 196, 120)); d.ellipse((-400, 1400, 500, 2300), fill=(240, 111, 143, 70))
        else:
            d.ellipse((560, -320, 1500, 560), fill=(158, 140, 240, 85)); d.ellipse((-420, 1380, 480, 2280), fill=(240, 111, 143, 60))
        cam = cam.filter(ImageFilter.GaussianBlur(160)); im = im.convert('RGBA'); im.alpha_composite(cam)
        d = ImageDraw.Draw(im)  # brilhos de 4 pontas
        for (x, y, r) in [(930, 330, 16), (130, 640, 11), (990, 1700, 13), (70, 1240, 9)]:
            cor = (255, 255, 255, 150) if escuro else (240, 111, 143, 150)
            d.polygon([(x, y - r), (x + r * .28, y - r * .28), (x + r, y), (x + r * .28, y + r * .28), (x, y + r), (x - r * .28, y + r * .28), (x - r, y), (x - r * .28, y - r * .28)], fill=cor)
        return im

    # ---------- desenho de um quadro ----------
    def _janela(self, c, t):
        k = c.zoom or [(0, (0, 0) + self.imgs[c.img].size)]
        if t <= k[0][0]: return k[0][1]
        for (a, ja), (b, jb) in zip(k, k[1:]):
            if a <= t <= b:
                s = suave((t - a) / max(1e-6, b - a)); return tuple(ja[i] + (jb[i] - ja[i]) * s for i in range(4))
        return k[-1][1]

    def _geo(self, c):
        if c.aparelho == 'celular': return CEL
        im = self.imgs[c.img]
        return TAB_PE if im.height > im.width else TAB

    def _pronto(self, quadro, c, t, entrada):
        im = self.imgs[c.img]; hmax, wmax, y0 = 940, 600, 580
        s = min(hmax / im.height, wmax / im.width); w, h = int(im.width * s), int(im.height * s)
        x0 = (W - w) // 2
        cel = Image.open(f'{PR}/{c.img}').convert('RGBA').resize((w, h), Image.LANCZOS)
        d = ImageDraw.Draw(cel, 'RGBA')
        for (t0, t1, (bx, by, bw, bh)) in c.destaques:
            if t0 - 0.3 <= t <= t1 + 0.3:
                a = suave((t - (t0 - 0.3)) / 0.3) if t < t0 else (1 - suave((t - t1) / 0.3)) if t > t1 else 1
                X0, Y0, X1, Y1 = bx * s - 8, by * s - 8, (bx + bw) * s + 8, (by + bh) * s + 8
                d.rounded_rectangle((X0 - 7, Y0 - 7, X1 + 7, Y1 + 7), 18, outline=(240, 111, 143, int(80 * a)), width=10)
                d.rounded_rectangle((X0, Y0, X1, Y1), 14, outline=(240, 111, 143, int(255 * a)), width=6)
        sombra = Image.new('RGBA', (w + 200, h + 200), (0, 0, 0, 0))
        ImageDraw.Draw(sombra).rounded_rectangle((100, 140, 100 + w, 100 + h), 70, fill=(58, 29, 143, 80))
        sombra = sombra.filter(ImageFilter.GaussianBlur(36)); sombra.alpha_composite(cel, (100, 100))
        e = saida_rapida(entrada); esc = 0.9 + 0.1 * e
        mw, mh = int(sombra.width * esc), int(sombra.height * esc); mol = sombra.resize((mw, mh), Image.BILINEAR)
        if e < 1: mol.putalpha(mol.getchannel('A').point(lambda v: int(v * e)))
        cx = x0 - 100 + sombra.width / 2; cy = y0 - 100 + sombra.height / 2 + (1 - e) * 120
        quadro.alpha_composite(mol, (int(cx - mw / 2), int(cy - mh / 2)))
        return dict(x=x0, y=y0, w=w, h=h, borda=0)

    def _lupas(self, quadro, c, t):
        im = self.imgs[c.img]
        for (t0, t1, (x, y, w, h), (cx, cy, r)) in c.lupas:
            if not (t0 <= t <= t1 + 0.3): continue
            a = saida_rapida((t - t0) / 0.35) if t < t0 + 0.35 else (1 - suave((t - t1) / 0.3)) if t > t1 else 1
            rr = max(4, int(r * (0.6 + 0.4 * a)))
            src = im.crop((x, y, x + w, y + h)).resize((2 * rr, 2 * rr), Image.LANCZOS).convert('RGBA')
            m = Image.new('L', (4 * rr, 4 * rr), 0); ImageDraw.Draw(m).ellipse((0, 0, 4 * rr - 1, 4 * rr - 1), fill=255)
            src.putalpha(m.resize((2 * rr, 2 * rr), Image.LANCZOS))
            camada = Image.new('RGBA', (2 * rr + 120, 2 * rr + 120), (0, 0, 0, 0)); dc = ImageDraw.Draw(camada)
            dc.ellipse((60, 80, 60 + 2 * rr, 80 + 2 * rr), fill=(58, 29, 143, 90)); camada = camada.filter(ImageFilter.GaussianBlur(24))
            camada.alpha_composite(src, (60, 60)); dc = ImageDraw.Draw(camada)
            dc.ellipse((60 - 4, 60 - 4, 60 + 2 * rr + 4, 60 + 2 * rr + 4), outline=(255, 255, 255, 255), width=10)
            dc.ellipse((60 - 12, 60 - 12, 60 + 2 * rr + 12, 60 + 2 * rr + 12), outline=(240, 111, 143, 255), width=6)
            if a < 1: camada.putalpha(camada.getchannel('A').point(lambda v: int(v * a)))
            quadro.alpha_composite(camada, (int(cx - rr - 60), int(cy - rr - 60)))

    def _aparelho(self, quadro, c, t, entrada):
        if c.aparelho == 'pronto': return self._pronto(quadro, c, t, entrada)
        g = self._geo(c); im = self.imgs[c.img]
        jx, jy, jw, jh = self._janela(c, t)
        # mantém a proporção da tela: ajusta a janela para caber exatamente
        ar = g['w'] / g['h']
        if jw / jh > ar: nh = jw / ar; jy -= (nh - jh) / 2; jh = nh
        else: nw = jh * ar; jx -= (nw - jw) / 2; jw = nw
        jx = max(0, min(im.width - jw, jx)) if jw <= im.width else (im.width - jw) / 2
        jy = max(0, min(im.height - jh, jy)) if jh <= im.height else (im.height - jh) / 2
        tela = Image.new('RGB', (g['w'], g['h']), 'white')
        rec = im.crop((int(jx), int(jy), int(jx + jw), int(jy + jh))).resize((g['w'], g['h']), Image.LANCZOS)
        tela.paste(rec, (0, 0)); tela = tela.convert('RGBA')
        d = ImageDraw.Draw(tela, 'RGBA'); sx = g['w'] / jw; sy = g['h'] / jh
        for (t0, t1, (bx, by, bw, bh)) in c.destaques:
            if t0 - 0.3 <= t <= t1 + 0.3:
                a = suave((t - (t0 - 0.3)) / 0.3) if t < t0 else (1 - suave((t - t1) / 0.3)) if t > t1 else 1
                x0 = (bx - jx) * sx - 10; y0 = (by - jy) * sy - 10; x1 = (bx + bw - jx) * sx + 10; y1 = (by + bh - jy) * sy + 10
                d.rounded_rectangle((x0 - 9, y0 - 9, x1 + 9, y1 + 9), 22, outline=(240, 111, 143, int(80 * a)), width=12)
                d.rounded_rectangle((x0, y0, x1, y1), 16, outline=(240, 111, 143, int(255 * a)), width=7)
        # moldura
        b = g['borda']; fw, fh = g['w'] + 2 * b, g['h'] + 2 * b
        moldura = Image.new('RGBA', (fw + 120, fh + 160), (0, 0, 0, 0)); dm = ImageDraw.Draw(moldura)
        dm.rounded_rectangle((60, 100, 60 + fw, 100 + fh), g['raio'] + b, fill=(58, 29, 143, 70))
        moldura = moldura.filter(ImageFilter.GaussianBlur(34)); dm = ImageDraw.Draw(moldura)
        dm.rounded_rectangle((60, 60, 60 + fw, 60 + fh), g['raio'] + b, fill=(24, 27, 34, 255))
        dm.rounded_rectangle((62, 62, 58 + fw, 58 + fh), g['raio'] + b - 2, outline=(70, 75, 88, 255), width=2)
        m = Image.new('L', (g['w'] * 2, g['h'] * 2), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, g['w'] * 2 - 1, g['h'] * 2 - 1), g['raio'] * 2, fill=255)
        moldura.paste(tela, (60 + b, 60 + b), m.resize((g['w'], g['h']), Image.LANCZOS))
        if c.aparelho == 'celular':
            ImageDraw.Draw(moldura).rounded_rectangle((60 + fw / 2 - 70, 60 + b + 14, 60 + fw / 2 + 70, 60 + b + 52), 20, fill=(10, 10, 12, 255))
        # entrada: sobe e cresce
        e = saida_rapida(entrada); esc = 0.9 + 0.1 * e
        mw, mh = int(moldura.width * esc), int(moldura.height * esc)
        mol = moldura.resize((mw, mh), Image.BILINEAR)
        if e < 1: mol.putalpha(mol.getchannel('A').point(lambda v: int(v * e)))
        cx = g['x'] - b - 60 + moldura.width / 2; cy = g['y'] - b - 60 + moldura.height / 2 + (1 - e) * 120
        quadro.alpha_composite(mol, (int(cx - mw / 2), int(cy - mh / 2)))
        return g

    def _colar(self, quadro, img, x, y, t, t0, dy=40, dur=0.45):
        if t < t0: return
        a = saida_rapida((t - t0) / dur)
        im = img if a >= 1 else img.copy()
        if a < 1: im.putalpha(im.getchannel('A').point(lambda v: int(v * a)))
        quadro.alpha_composite(im, (int(x), int(y + (1 - a) * dy)))

    def quadro(self, t):
        # descobre a cena
        ini = 0
        for i, c in enumerate(self.cenas):
            if t < ini + c.dur: return self._quadro_cena(i, t - ini)
            ini += c.dur
        return self._quadro_fim(t - ini)

    def _quadro_cena(self, i, t):
        c = self.cenas[i]; cam = self.camadas[i]
        q = {'roxo': self.fundo_roxo, 'escuro': self.fundo_escuro}.get(c.fundo, self.fundo_claro).copy()
        q.alpha_composite(self.logo_escuro if c.fundo in ('escuro', 'roxo') else self.logo_claro, (80, 150))
        tit = cam['titulo']
        if c.titulo: self._colar(q, tit, 80, 300 if c.aparelho else 820 - tit.height // 2, t, 0.05, dy=50, dur=0.5)
        if cam['estados']:
            atual = None; ant = None; t_at = 0
            for (te, im) in cam['estados']:
                if t >= te: ant, atual, t_at = atual, im, te
            if atual is not None:
                a = suave((t - t_at) / 0.2)
                if ant is not None and a < 1:
                    q.alpha_composite(Image.blend(ant, atual, a))
                elif ant is None and a < 1:
                    self._colar(q, atual, 0, 0, t, t_at, dy=30, dur=0.3)
                else:
                    q.alpha_composite(atual)
        if c.aparelho:
            g = self._aparelho(q, c, t, min(1, max(0, (t - 0.2) / 0.6)))
            self._lupas(q, c, t)
            base = g['y'] + g['h'] + g['borda'] + 40
        else:
            base = 1200
        # selos empilhados embaixo (ou centralizados sem aparelho)
        y = base
        for (ts, im) in cam['selos']:
            self._colar(q, im, 80, y, t, ts); y += im.height + 18
        if 'pergunta' in cam:
            t0, passos = cam['pergunta']
            if t >= t0:
                n = min(len(passos) - 1, int((t - t0) / 0.09)); im = passos[n]
                self._colar(q, im, W - 80 - im.width, (TAB['y'] - im.height - 40) if c.aparelho != 'celular' else 520, t, t0, dy=20, dur=0.25)
        if 'balao' in cam:
            t0, im = cam['balao']
            yb = (base + 10) if c.aparelho else 1150
            self._colar(q, im, 220, yb, t, t0)
            if t >= t0:
                bu = self.queen_busto.resize((120, 120), Image.LANCZOS)
                mk = Image.new('L', (120, 120), 0); ImageDraw.Draw(mk).ellipse((0, 0, 119, 119), fill=255); bu.putalpha(mk)
                self._colar(q, bu, 80, yb, t, t0)
        if c.queen:
            t0, tipo = c.queen
            if tipo == 'corpo':
                im = self.queen_corpo.resize((540, int(540 * self.queen_corpo.height / self.queen_corpo.width)), Image.LANCZOS)
                self._colar(q, im, W - 540, H - im.height + 40, t, t0, dy=80, dur=0.6)
        # transição: fade curto na entrada da cena
        if t < 0.18 and i > 0:
            ant = self._quadro_cena_simples(i - 1)
            q = Image.blend(ant, q, suave(t / 0.18))
        return q

    def _quadro_cena_simples(self, i):
        c = self.cenas[i]
        if not hasattr(self, '_cache_fim'): self._cache_fim = {}
        if i not in self._cache_fim: self._cache_fim[i] = self._quadro_cena(i, c.dur - 0.01) if i == 0 or True else None
        return self._cache_fim[i]

    def _quadro_fim(self, t):
        q = self.fundo_claro.copy(); q.alpha_composite(self.logo_claro, (80, 150))
        if self._fim['queen']:
            im = self.queen_corpo.resize((640, int(640 * self.queen_corpo.height / self.queen_corpo.width)), Image.LANCZOS)
            self._colar(q, im, (W - 640) // 2, H - im.height + 60, t, 0.1, dy=90, dur=0.6)
        self._colar(q, self.cam_fim, (W - self.cam_fim.width) // 2, 330 if self._fim['queen'] else (H - self.cam_fim.height) // 2, t, 0.25, dy=60, dur=0.5)
        if t < 0.18:
            q = Image.blend(self._quadro_cena_simples(len(self.cenas) - 1), q, suave(t / 0.18))
        return q

    # ---------- áudio ----------
    def _audio(self, dur, saida):
        eventos = []; ini = 0
        for c in self.cenas:
            for (t, nome, db) in c.sons: eventos.append((ini + t, nome, db))
            ini += c.dur
        if self._fim:
            for (t, nome, db) in self._fim['sons']: eventos.append((ini + t, nome, db))
        ent = []; filt = []; n = 0
        if self.musica:
            ent += ['-stream_loop', '-1', '-i', os.path.join(SOM, 'musica', self.musica)]
            filt.append(f'[{n}:a]atrim=0:{dur},asetpts=N/SR/TB,volume={self.musica_db}dB,afade=t=in:st=0:d=0.8,afade=t=out:st={dur-1.5}:d=1.5,aformat=sample_rates=44100:channel_layouts=stereo[m]')
            n += 1
        rotulos = ['[m]'] if self.musica else []
        for k, (t, nome, db) in enumerate(eventos):
            ent += ['-i', _sfx_path(nome)]
            ms = int(t * 1000)
            filt.append(f'[{n}:a]volume={db}dB,aformat=sample_rates=44100:channel_layouts=stereo,adelay={ms}|{ms}[s{k}]')
            rotulos.append(f'[s{k}]'); n += 1
        if not rotulos: return None
        filt.append(''.join(rotulos) + f'amix=inputs={len(rotulos)}:normalize=0:duration=longest,atrim=0:{dur},alimiter=limit=0.89[a]')
        cmd = ['ffmpeg', '-y', '-loglevel', 'error'] + ent + ['-filter_complex', ';'.join(filt), '-map', '[a]', '-c:a', 'aac', '-b:a', '160k', saida]
        subprocess.run(cmd, check=True); return saida

    def gravar(self, nome='reel.mp4', capa_t=1.0):
        self._preparar()
        dur = sum(c.dur for c in self.cenas) + (self._fim['dur'] if self._fim else 0)
        mudo = f'{self.pasta}/_mudo.mp4'
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
               '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', mudo]
        pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for k in range(int(dur * FPS)):
            pr.stdin.write(self.quadro(k / FPS).convert('RGB').tobytes())
        pr.stdin.close(); pr.wait()
        aud = self._audio(dur, f'{self.pasta}/_audio.m4a')
        saida = f'{self.pasta}/{nome}'
        if aud:
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', mudo, '-i', aud, '-c:v', 'copy', '-c:a', 'copy', '-shortest', '-movflags', '+faststart', saida], check=True)
        else:
            os.replace(mudo, saida)
        self.quadro(capa_t).convert('RGB').save(saida.replace('.mp4', '-capa.jpg'), quality=92)
        print('ok', saida, f'{dur:.1f}s')
        return saida
