"""Motor de carrossel e story da MedQueen IA (feed 1080x1350, story 1080x1920).
Uso: python3 carrossel.py posts/<spec>.py  -> PNGs em saida/<SLUG>/01.png ...
O spec define SLUG e CARDS (lista de dicts).

Tipos de card: capa, passo (padrão), final.
Campos: olho, titulo (aceita <em>), texto, visual (HTML de um ajudante), centro, t (tamanho do título), s (tamanho do texto).

REGRA DO MATHEUS: print nunca vai solto. Todo print entra dentro de tablet() ou celular()
e, quando fizer sentido, com destaque (caixa e lupa) no ponto que importa.
"""
import sys, os, html, importlib.util
from PIL import Image
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
F = f'file://{BASE}/www/fonts'
MARCA = f'file://{BASE}/www/marca'
PR = f'{BASE}/prints'

CSS = f"""
@font-face{{font-family:J;src:url({F}/PlusJakartaSans.ttf);font-weight:200 800}}
@font-face{{font-family:S;src:url({F}/SourceSans3.ttf);font-weight:200 900}}
:root{{--roxo:#3A1D8F;--indigo:#263A8F;--lilas:#5865D8;--rosa:#F06F8F;--tinta:#111827;--cinza:#475569;--cinza2:#667085;--linha:#E4E2F0;--nevoa:#F6F5FC}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
html.story,body.story{{height:1920px}}
body{{background:var(--nevoa);color:var(--tinta);font-family:S,sans-serif;position:relative}}
.fundo{{position:absolute;inset:0;pointer-events:none;
 background:radial-gradient(620px 520px at 92% 6%,rgba(158,140,240,.30),transparent 70%),
 radial-gradient(560px 480px at 4% 98%,rgba(240,111,143,.20),transparent 70%),
 radial-gradient(900px 700px at 50% 50%,#FFFFFF 0%,rgba(255,255,255,0) 75%)}}
.topo{{position:absolute;left:92px;right:92px;top:74px;display:flex;justify-content:space-between;align-items:center;z-index:3}}
.lg{{--h:62px;display:inline-flex;align-items:flex-start;height:var(--h)}}
.lg img{{height:var(--h);display:block}}
.lg b{{margin-left:calc(var(--h)*-0.005);margin-top:calc(var(--h)*0.368);height:calc(var(--h)*0.292);padding:0 calc(var(--h)*0.075);border-radius:calc(var(--h)*0.07);background:var(--roxo);color:#fff;font-family:J;font-weight:800;font-size:calc(var(--h)*0.19);letter-spacing:.04em;display:inline-flex;align-items:center;line-height:1}}
.cont{{font-family:J;font-weight:700;font-size:22px;color:var(--cinza2);letter-spacing:.04em}}
.pe{{position:absolute;left:92px;right:92px;bottom:78px;display:flex;align-items:center;gap:26px;z-index:3}}
.barra{{flex:1;height:5px;background:#E2DFF2;border-radius:5px;overflow:hidden}}
.barra i{{display:block;height:100%;background:linear-gradient(90deg,var(--roxo),var(--rosa));border-radius:5px}}
.arraste{{font-family:J;font-weight:700;font-size:21px;color:var(--roxo);letter-spacing:.06em;text-transform:uppercase;white-space:nowrap}}
.miolo{{position:absolute;left:92px;right:92px;top:168px;bottom:146px;display:flex;flex-direction:column;z-index:2}}
.story .miolo{{top:300px;bottom:290px}}
.story .topo{{top:190px}}
.olho{{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;font-family:J;font-weight:700;font-size:22px;letter-spacing:.07em;text-transform:uppercase;color:var(--roxo);background:#ECE8FB;border-radius:999px;padding:10px 20px}}
.olho:before{{content:"";width:10px;height:10px;border-radius:50%;background:var(--rosa)}}
h1{{font-family:J;font-weight:800;letter-spacing:-.018em;word-spacing:.04em;line-height:1.04;font-size:var(--t,84px);margin-top:24px;color:var(--tinta)}}
h1 em{{font-style:normal;color:var(--roxo);background:linear-gradient(transparent 68%,rgba(240,111,143,.32) 68%)}}
.sub{{font-size:var(--s,37px);line-height:1.34;color:var(--cinza);margin-top:24px;max-width:880px}}
.sub b{{color:var(--tinta);font-weight:700}}
.visual{{flex:1;display:flex;align-items:center;justify-content:center;gap:36px;margin-top:36px;min-height:0;position:relative}}
.visual.baixo{{align-items:flex-end}}
.visual.coluna{{flex-direction:column;gap:44px;justify-content:center}}
/* tablet */
.tab{{position:relative;border-radius:46px;padding:22px;background:linear-gradient(150deg,#2B2F38,#11141A 45%,#2A2E36);box-shadow:0 50px 80px -46px rgba(58,29,143,.55),0 0 0 2px #3A3F4A inset}}
.tab .tela{{position:relative;overflow:hidden;border-radius:26px;background:#fff}}
.tab .tela img{{position:absolute;display:block;max-width:none}}
.tab .cam{{position:absolute;top:50%;left:9px;width:8px;height:8px;border-radius:50%;background:#3a3f4a;transform:translateY(-50%)}}
/* celular */
.cel{{position:relative;border-radius:64px;padding:13px;background:linear-gradient(150deg,#2B2F38,#11141A 45%,#2A2E36);box-shadow:0 50px 80px -46px rgba(58,29,143,.55)}}
.cel .tela{{position:relative;overflow:hidden;border-radius:52px;background:#fff}}
.cel .tela img{{position:absolute;display:block;max-width:none}}
.cel .ilha{{position:absolute;top:16px;left:50%;transform:translateX(-50%);width:30%;height:30px;border-radius:20px;background:#0B0D12;z-index:3}}
.pronto img{{display:block;filter:drop-shadow(0 40px 50px rgba(58,29,143,.28))}}
/* destaque */
.dest{{position:absolute;border:5px solid var(--rosa);border-radius:18px;box-shadow:0 0 0 9999px rgba(17,24,39,.12),0 0 0 10px rgba(240,111,143,.25);z-index:2}}
.dest.leve{{box-shadow:0 0 0 10px rgba(240,111,143,.25)}}
.rot{{position:absolute;z-index:4;background:var(--roxo);color:#fff;font-family:J;font-weight:700;font-size:26px;padding:14px 22px;border-radius:16px;white-space:nowrap;box-shadow:0 18px 36px -18px rgba(58,29,143,.8)}}
.rot:before{{content:"";position:absolute;width:16px;height:16px;background:var(--roxo);transform:rotate(45deg)}}
.rot.cima:before{{left:34px;bottom:-7px}} .rot.baixo:before{{left:34px;top:-7px}}
.lupa{{position:absolute;z-index:5;border-radius:50%;overflow:hidden;border:8px solid #fff;box-shadow:0 0 0 5px var(--rosa),0 40px 60px -30px rgba(17,24,39,.6);background:#fff}}
.lupa img{{position:absolute;max-width:none}}
/* listas */
ul.lista{{list-style:none;display:grid;gap:22px;width:100%}}
ul.lista li{{display:flex;gap:24px;align-items:flex-start;font-size:36px;line-height:1.28;background:#fff;border-radius:28px;padding:28px 32px;box-shadow:0 0 0 2px var(--linha),0 24px 40px -34px rgba(58,29,143,.45)}}
ul.lista li i{{flex:none;width:54px;height:54px;border-radius:50%;display:grid;place-items:center;font-style:normal;font-family:J;font-weight:800;font-size:26px;background:var(--roxo);color:#fff;margin-top:-4px}}
ul.lista.rosa li i{{background:var(--rosa)}}
ul.lista li small{{display:block;font-size:28px;color:var(--cinza2);margin-top:6px;line-height:1.3}}
ul.lista li b{{font-weight:700}}
/* números */
.nums{{display:grid;grid-template-columns:repeat(var(--n,4),1fr);gap:18px;width:100%}}
.nums div{{background:#fff;border-radius:28px;padding:30px 20px;text-align:center;box-shadow:0 0 0 2px var(--linha)}}
.nums strong{{display:block;font-family:J;font-weight:800;font-size:96px;letter-spacing:-.02em;color:var(--roxo);line-height:1}}
.nums span{{display:block;font-size:27px;color:var(--cinza);margin-top:12px;line-height:1.2}}
/* fluxo */
.fluxo{{display:flex;flex-wrap:wrap;gap:18px 12px;align-items:center;width:100%}}
.fluxo span{{background:#fff;border-radius:20px;padding:20px 24px;font-family:J;font-weight:700;font-size:34px;box-shadow:0 0 0 2px var(--linha)}}
.fluxo span small{{display:block;font-family:S;font-weight:700;color:#D94A73;font-size:26px;margin-top:4px}}
.fluxo b{{color:var(--lilas);font-size:30px}}
/* caixa de destaque */
.nota{{width:100%;background:#fff;border-left:10px solid var(--rosa);border-radius:22px;padding:30px 34px;font-size:35px;line-height:1.32;box-shadow:0 24px 40px -34px rgba(58,29,143,.45)}}
.nota b{{color:var(--roxo)}}
/* queen */
.queen{{position:absolute;right:-30px;bottom:-40px;width:var(--qw,380px);z-index:1}}
.queen img{{width:100%;display:block;-webkit-mask-image:linear-gradient(#000 75%,transparent)}}
.balao{{background:#fff;border-radius:30px 30px 30px 8px;padding:30px 34px;font-size:36px;line-height:1.3;box-shadow:0 0 0 2px var(--linha),0 30px 50px -36px rgba(58,29,143,.5);max-width:620px}}
.balao b{{color:var(--roxo)}}
/* story: tudo maior */
.story ul.lista li{{font-size:46px;padding:34px 38px}} .story ul.lista li i{{width:62px;height:62px;font-size:30px}}
.story .nota{{font-size:44px;padding:36px 40px}} .story .sub{{font-size:44px}}
.story .balao{{font-size:50px;max-width:880px;padding:40px 44px}} .story .olho{{font-size:28px}}
/* final */
.cartao{{margin-top:auto;background:linear-gradient(135deg,var(--roxo),#4B2AB0 60%,#5B3BC4);color:#fff;border-radius:40px;padding:46px 48px;position:relative;overflow:hidden;box-shadow:0 40px 70px -40px rgba(58,29,143,.8)}}
.cartao:after{{content:"";position:absolute;right:-120px;top:-120px;width:360px;height:360px;border-radius:50%;background:radial-gradient(circle,rgba(240,111,143,.55),transparent 70%)}}
.cartao h2{{font-family:J;font-weight:800;font-size:54px;letter-spacing:-.015em;line-height:1.08;position:relative;z-index:1}}
.cartao p{{font-size:34px;line-height:1.32;margin-top:18px;color:#E7E3FA;position:relative;z-index:1}}
.cartao .acao{{display:inline-block;margin-top:30px;background:#fff;color:var(--roxo);font-family:J;font-weight:800;font-size:30px;padding:20px 30px;border-radius:999px;position:relative;z-index:1}}
"""

def _dim(img):
    with Image.open(f'{PR}/{img}') as im:
        return im.size

def _tela(img, w, h, crop=None, dest=(), rotulos=(), lupa=None):
    """Monta a tela (w x h) mostrando o recorte crop=(x,y,cw,ch) da imagem. Destaques e rótulos em coordenadas da imagem."""
    iw, ih = _dim(img)
    if crop is None:
        # recorte padrão: largura toda, a partir do topo, na proporção da tela
        cw = iw; ch = cw * h / w
        if ch > ih: ch = ih; cw = ch * w / h
        crop = (0, 0, cw, ch)
    x, y, cw, ch = crop
    s = w / cw
    out = f'<img src="file://{PR}/{img}" style="left:{-x*s:.1f}px;top:{-y*s:.1f}px;width:{iw*s:.1f}px">'
    for d in dest:
        dx, dy, dw, dh = d[:4]; leve = ' leve' if (len(d) > 4 and d[4] == 'leve') else ''
        out += f'<div class="dest{leve}" style="left:{(dx-x)*s-10:.0f}px;top:{(dy-y)*s-10:.0f}px;width:{dw*s+20:.0f}px;height:{dh*s+20:.0f}px"></div>'
    extra = ''
    for (rx, ry, txt, lado) in rotulos:
        px, py = (rx - x) * s, (ry - y) * s
        extra += (f'<div class="rot {lado}" style="left:{px:.0f}px;top:{py:.0f}px;transform:translateY({"-100%" if lado=="cima" else "0"})">{txt}</div>')
    if lupa:
        lx, ly, lr, cx, cy, z = lupa  # centro na imagem (lx,ly), raio na tela lr, posição do centro da lupa na tela (cx,cy), aumento z
        zs = s * z
        extra += (f'<div class="lupa" style="width:{2*lr}px;height:{2*lr}px;left:{cx-lr}px;top:{cy-lr}px">'
                  f'<img src="file://{PR}/{img}" style="width:{iw*zs:.0f}px;left:{lr-lx*zs:.0f}px;top:{lr-ly*zs:.0f}px"></div>')
    return out, extra

def tablet(img, w=840, h=None, crop=None, dest=(), rotulos=(), lupa=None):
    """Tablet na horizontal (4:3 por padrão) com o print dentro."""
    h = h or int(w * 3 / 4)
    dentro, fora = _tela(img, w, h, crop, dest, rotulos, lupa)
    return (f'<div class="tab" style="width:{w+44}px"><span class="cam"></span>'
            f'<div class="tela" style="width:{w}px;height:{h}px">{dentro}</div>'
            f'<div style="position:absolute;left:22px;top:22px;width:{w}px;height:{h}px">{fora}</div></div>')

def celular(img, h=760, crop=None, dest=(), rotulos=(), lupa=None):
    """Celular com o print dentro (print de tela de celular, sem moldura)."""
    w = int(h * 390 / 844)
    dentro, fora = _tela(img, w, h, crop, dest, rotulos, lupa)
    return (f'<div class="cel" style="width:{w+26}px"><span class="ilha"></span>'
            f'<div class="tela" style="width:{w}px;height:{h}px">{dentro}</div>'
            f'<div style="position:absolute;left:13px;top:13px;width:{w}px;height:{h}px">{fora}</div></div>')

def pronto(img, h=760, dest=(), lupa=None):
    """Print que já vem com moldura de celular (ex.: cel-caderno-erros.png). Destaques em coordenadas da imagem.
    lupa=(x, y, raio_tela, cx_tela, cy_tela, aumento): círculo ampliado do ponto (x,y) da imagem."""
    iw, ih = _dim(img); s = h / ih; w = iw * s
    d = ''.join(f'<div class="dest leve" style="left:{(x)*s-10:.0f}px;top:{(y)*s-10:.0f}px;width:{dw*s+20:.0f}px;height:{dh*s+20:.0f}px"></div>' for x, y, dw, dh in dest)
    if lupa:
        lx, ly, lr, cx, cy, z = lupa; zs = s * z
        d += (f'<div class="lupa" style="width:{2*lr}px;height:{2*lr}px;left:{cx-lr}px;top:{cy-lr}px">'
              f'<img src="file://{PR}/{img}" style="width:{iw*zs:.0f}px;left:{lr-lx*zs:.0f}px;top:{lr-ly*zs:.0f}px"></div>')
    return f'<div class="pronto" style="position:relative;width:{w:.0f}px;height:{h}px"><img src="file://{PR}/{img}" style="height:{h}px">{d}</div>'

def queen_img(h=560):
    """Queen IA oficial em linha (dentro do visual)."""
    return f'<img src="{MARCA}/queen_ia_recorte.png" style="height:{h}px;display:block;-webkit-mask-image:linear-gradient(#000 80%,transparent)">'

def lista(itens, tipo='num', rosa=False):
    li = ''
    for k, it in enumerate(itens, 1):
        a, b = (it if isinstance(it, tuple) else (it, ''))
        i = str(k) if tipo == 'num' else '✓'
        li += f'<li><i>{i}</i><div>{a}{f"<small>{b}</small>" if b else ""}</div></li>'
    return f'<ul class="lista{" rosa" if rosa else ""}">{li}</ul>'

def numeros(pares):
    return f'<div class="nums" style="--n:{len(pares)}">' + ''.join(f'<div><strong>{a}</strong><span>{b}</span></div>' for a, b in pares) + '</div>'

def fluxo(itens):
    """itens: lista de strings ou (texto, nota). Liga com setas."""
    p = []
    for it in itens:
        a, b = (it if isinstance(it, tuple) else (it, ''))
        p.append(f'<span>{a}{f"<small>{b}</small>" if b else ""}</span>')
    return '<div class="fluxo">' + '<b>→</b>'.join(p) + '</div>'

def nota(txt):
    return f'<div class="nota">{txt}</div>'

def queen(w=380):
    """Queen IA oficial (com o símbolo no jaleco). Só em card de apoio/explicação."""
    return f'<div class="queen" style="--qw:{w}px"><img src="{MARCA}/queen_ia_recorte.png"></div>'

def balao(txt):
    return f'<div class="balao">{txt}</div>'

LOGO_IA = f'<span class="lg"><img src="{MARCA}/medqueen-logo-horizontal.svg"><b>IA</b></span>'

def pagina(card, i, n, story=False):
    tipo = card.get('tipo', 'passo')
    t = card.get('t'); s = card.get('s')
    estilo = (f'--t:{t}px;' if t else '') + (f'--s:{s}px;' if s else '')
    unico = (n == 1)   # post único: sem contador nem barra de progresso
    topo = f'<div class="topo">{LOGO_IA}' + ('' if story or unico else f'<div class="cont">{i:02d}/{n:02d}</div>') + '</div>'
    if story: pe = ''
    elif unico: pe = f'<div class="pe"><div></div><div class="arraste">{card.get("pe_final", "link na bio")}</div></div>'
    else: pe = (f'<div class="pe"><div class="barra"><i style="width:{i/n*100:.1f}%"></i></div>'
          + ('<div class="arraste">arraste →</div>' if i < n else f'<div class="arraste">{card.get("pe_final", "salva pra revisar")}</div>') + '</div>')
    corpo = f'<div class="olho">{card["olho"]}</div>' if card.get('olho') else ''
    if card.get('titulo'): corpo += f'<h1>{card["titulo"]}</h1>'
    if card.get('texto'): corpo += f'<p class="sub">{card["texto"]}</p>'
    if card.get('visual'):
        corpo += f'<div class="visual{" baixo" if card.get("baixo") else ""}{" coluna" if card.get("coluna") else ""}">{card["visual"]}</div>'
    if tipo == 'final':
        corpo += f'<div class="cartao"><h2>{card["cta_titulo"]}</h2><p>{card["cta_texto"]}</p>' + (f'<div class="acao">{card["acao"]}</div>' if card.get('acao') else '') + '</div>'
    q = card.get('queen', '')
    return f'''<!doctype html><html class="{'story' if story else ''}"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body class="{'story' if story else ''}" style="{estilo}"><div class="fundo"></div>{topo}<div class="miolo">{corpo}</div>{q}{pe}</body></html>'''

def _carregar(spec_path):
    spec = importlib.util.spec_from_file_location('spec', spec_path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def render(spec_path):
    m = _carregar(spec_path)
    out = f'{BASE}/saida/{m.SLUG}'; os.makedirs(out, exist_ok=True)
    n = len(m.CARDS)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': 1350})
        for i, c in enumerate(m.CARDS, 1):
            f = f'{out}/_c{i}.html'; open(f, 'w', encoding='utf-8').write(pagina(c, i, n))
            pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
            pg.screenshot(path=f'{out}/{i:02d}.png')
        b.close()
    print('ok', out, n)
    return out

def render_stories(lista, pasta):
    """lista de dicts de card (mesmos campos) + 'nome'. Saída 1080x1920."""
    os.makedirs(pasta, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        for s in lista:
            f = f'{pasta}/{s["nome"]}.html'; open(f, 'w', encoding='utf-8').write(pagina(s, 1, 1, story=True))
            pg.goto(f'file://{f}'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
            pg.screenshot(path=f'{pasta}/{s["nome"]}.png'); print('ok', s['nome'])
        b.close()

if __name__ == '__main__':
    render(sys.argv[1])

def imagem(caminho, h=900, girar=0):
    """Imagem já gerada (ex.: capa do post do dia em saida/...) como cartão com sombra. Caminho relativo ao motor."""
    return (f'<img src="file://{BASE}/{caminho}" style="height:{h}px;border-radius:36px;display:block;'
            f'box-shadow:0 0 0 2px #E4E2F0,0 60px 90px -50px rgba(58,29,143,.55);transform:rotate({girar}deg)">')
