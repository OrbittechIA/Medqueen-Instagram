"""Formatos de Reel em vídeo da MedQueen IA (sem rosto). Cada função devolve uma ou mais Cena para reel_video.Reel.

Pedido do Matheus (24/10/2026): os Reels NÃO seguem todos o mesmo molde (dor -> produto -> chamada).
Varie o formato. Catálogo e regras de rodízio no LEIA-ME, seção "Reel em vídeo".

Formatos aqui:
  quiz(...)          pergunta de prova + 4 alternativas + contagem 3, 2, 1 + resposta + explicação curta
  mito_verdade(...)  afirmação + carimbo MITO/VERDADE + porquê (use 3 seguidas)
  chat(...)          conversa com a Queen IA, mensagem a mensagem, com "digitando"
  antes_depois(...)  duas colunas: como era x como fica
  lista(...)         "3 sinais de que..." itens numerados entrando um a um
  palavras(...)      frase grande que entra palavra por palavra (gancho, POV, frase de impacto)
  episodio(...)      abertura de série numerada ("Pegadinha de prova #3")
A demonstração de produto em telas (Cena com aparelho=...) continua existindo em reel_video.py.
"""
import os
from reel_video import Cena, MARCA

QUEEN = f'file://{MARCA}/queen-ia-bust-master-384.png'

def palavras(frase, dur=None, fundo='escuro', passo=0.28, tag=None, g=112, sons=None, extra=''):
    """frase: texto com <em>...</em> opcional. Cada palavra entra no seu tempo."""
    toks = []; dentro = False
    for w in frase.split(' '):
        abre = w.startswith('<em>'); fecha = w.endswith('</em>')
        limpo = w.replace('<em>', '').replace('</em>', '')
        toks.append((limpo, dentro or abre)); dentro = (dentro or abre) and not fecha
    def html(n):
        partes = []
        for k, (w, em) in enumerate(toks):
            cls = '' if k < n else ' class="oculto"'
            partes.append(f'<em{cls}>{w}</em>' if em else f'<span{cls}>{w}</span>')
        topo = f'<div class="tag">{tag}</div>' if tag else ''
        return f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center">{topo}<div class="big" style="--g:{g}px">{" ".join(partes)}</div>{extra}</div>'
    est = [(0.15 + k * passo, html(k + 1)) for k in range(len(toks))]
    d = dur or (0.15 + len(toks) * passo + 1.4)
    return Cena(d, '', fundo=fundo, estados=est, sons=sons or [(0.1, 'woosh_1', -12)])

def quiz(pergunta, alternativas, certa, explicacao, tag='Acerta essa?', fundo='claro', t_cont=2.2, pausa=1.0):
    letras = 'ABCD'
    def alts(estado):
        h = []
        for k, a in enumerate(alternativas):
            cls = 'alt' + (' certa' if estado == 'rev' and k == certa else ' apagada' if estado == 'rev' else '')
            h.append(f'<div class="{cls}"><b>{letras[k]}</b><span>{a}</span></div>')
        return ''.join(h)
    base = f'<div class="tag">{tag}</div><div class="q">{pergunta}</div>'
    est = [(0.1, base), (1.0, base + alts(''))]
    for n, k in enumerate((3, 2, 1)):
        est.append((t_cont + n * pausa, base + alts('') + f'<div class="cont">{k}</div>'))
    t_rev = t_cont + 3 * pausa
    est.append((t_rev, base + alts('rev')))
    est.append((t_rev + 1.3, base + alts('rev') + f'<div class="expl">{explicacao}</div>'))
    sons = [(0.1, 'woosh_1', -10), (1.0, 'notification', -14)]
    sons += [(t_cont + n * pausa, 'mouse_click', -6) for n in range(3)]
    sons += [(t_rev, 'hit', -10), (t_rev + 1.3, 'toggle', -8)]
    return Cena(t_rev + 5.2, '', fundo=fundo, estados=est, sons=sons)

def mito_verdade(n, afirmacao, veredito, porque, total=3, fundo='claro'):
    """veredito: 'mito' ou 'verdade'."""
    base = f'<div class="tag">Mito ou verdade? {n}/{total}</div><div class="afirm">{afirmacao}</div>'
    est = [(0.1, base), (2.2, base + f'<div class="carimbo {veredito}">{veredito.upper()}</div>'),
           (3.0, base + f'<div class="carimbo {veredito}">{veredito.upper()}</div><div class="porque">{porque}</div>')]
    sons = [(0.1, 'woosh_1', -10), (2.2, 'hit', -6), (3.0, 'toggle', -10)]
    return Cena(6.2, '', fundo=fundo, estados=est, sons=sons)

def chat(mensagens, titulo_conversa='Queen IA', fundo='claro', ritmo=1.6):
    """mensagens: [('aluno'|'queen', 'texto html')]. Cada mensagem da Queen tem 'digitando' antes."""
    cab = f'<div class="cab"><img src="{QUEEN}"><div>{titulo_conversa}<small>online</small></div></div>'
    vistos = []; est = [(0.1, cab + '<div class="chat"></div>')]; sons = [(0.1, 'woosh_1', -10)]; t = 0.6
    for quem, txt in mensagens:
        if quem == 'queen':
            est.append((t, cab + '<div class="chat">' + ''.join(vistos) + f'<div class="qmsg"><img src="{QUEEN}"><div class="msg dots"><i></i><i></i><i></i></div></div></div>'))
            sons.append((t, 'digital_loading', -18)); t += 0.9
            vistos.append(f'<div class="qmsg"><img src="{QUEEN}"><div class="msg">{txt}</div></div>')
            sons.append((t, 'notification', -14))
        else:
            sons.append((t - 0.5 if t > 0.6 else t, 'keyboard_typing', -14))
            vistos.append(f'<div class="msg aluno">{txt}</div>')
            sons.append((t, 'woosh_1', -16))
        est.append((t, cab + '<div class="chat">' + ''.join(vistos[-5:]) + '</div>'))
        t += ritmo + len(txt) / 60
    return Cena(t + 1.0, '', fundo=fundo, estados=est, sons=sons)

def antes_depois(titulo, esq_titulo, esq, dir_titulo, dir_, fundo='claro', passo=0.7):
    def html(ne, nd):
        e = ''.join(f'<p{"" if k < ne else " class=oculto"}>{x}</p>' for k, x in enumerate(esq))
        d = ''.join(f'<p{"" if k < nd else " class=oculto"}>{x}</p>' for k, x in enumerate(dir_))
        return f'<div class="big" style="--g:76px">{titulo}</div><div class="lados"><div class="col ruim"><h3>{esq_titulo}</h3>{e}</div><div class="col bom"><h3>{dir_titulo}</h3>{d}</div></div>'
    est = [(0.1, html(0, 0))]; sons = [(0.1, 'woosh_2', -10)]; t = 0.8
    for k in range(len(esq)): est.append((t, html(k + 1, 0))); sons.append((t, 'downer', -22)); t += passo
    t += 0.3
    for k in range(len(dir_)): est.append((t, html(len(esq), k + 1))); sons.append((t, 'toggle', -8)); t += passo
    return Cena(t + 2.2, '', fundo=fundo, estados=est, sons=sons)

def lista(titulo, itens, fundo='claro', passo=1.8, tag=None):
    """itens: [('título', 'detalhe' ou '')]."""
    def html(n):
        h = ''.join(f'<div class="item{"" if k < n else " oculto"}"><b>{k+1}</b><span>{a}' + (f'<small>{b}</small>' if b else '') + '</span></div>' for k, (a, b) in enumerate(itens))
        return (f'<div class="tag">{tag}</div>' if tag else '') + f'<div class="big" style="--g:80px">{titulo}</div>{h}'
    est = [(0.1, html(0))]; sons = [(0.1, 'woosh_2', -10)]; t = 1.2
    for k in range(len(itens)): est.append((t, html(k + 1))); sons.append((t, 'hit', -14)); t += passo
    return Cena(t + 1.6, '', fundo=fundo, estados=est, sons=sons)

def episodio(serie, numero, tema, fundo='roxo'):
    html = f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center"><div class="tag">{serie}</div><div class="ep" style="color:#fff">#{numero}</div><div class="big" style="--g:84px;margin-top:20px">{tema}</div></div>'
    return Cena(2.6, '', fundo=fundo, estados=[(0.1, html)], sons=[(0.1, 'deep_woosh', -10), (0.5, 'hit', -12)])
