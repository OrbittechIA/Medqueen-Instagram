"""Visuais conceituais da MedQueen IA (sem print do produto).

REGRA DO MATHEUS (28/10/2026): não usamos mais print do produto em post, story ou Reel.
A gente argumenta EM VOLTA do recurso: quer falar de flashcard, mostra a ideia de flashcard
(cartão de pergunta e resposta, o erro virando card), não a tela do app. Nada de tela desenhada
imitando o app também. Visual = ideia: cartões, folha de prova, fluxo, número grande, Queen IA.

Uso no spec:
    from conceito import cartoes, erro_vira_card, folha_prova, material_vira, trio, continua, plano_semana
"""
import os
BASE = os.path.dirname(os.path.abspath(__file__))
MARCA = f'file://{BASE}/www/marca'

CSS = """<style>
.cx{font-family:S,sans-serif;color:#111827;position:relative}
.cx *{box-sizing:border-box}
.cx-card{background:#fff;border-radius:34px;box-shadow:0 2px 0 #ECE8F7,0 40px 70px -40px rgba(58,29,143,.45)}
.cx-pill{display:inline-flex;align-items:center;gap:10px;border-radius:999px;padding:10px 22px;font:700 26px S,sans-serif}
.cx-rotulo{font:800 22px S,sans-serif;letter-spacing:3px;text-transform:uppercase}
.cx-seta{width:70px;height:6px;background:linear-gradient(90deg,#C9BDF2,#F06F8F);border-radius:6px;position:relative;flex:none}
.cx-seta:after{content:"";position:absolute;right:-4px;top:-9px;border-left:18px solid #F06F8F;border-top:12px solid transparent;border-bottom:12px solid transparent}
.cx-ic{width:88px;height:88px;border-radius:26px;display:flex;align-items:center;justify-content:center;flex:none}
.cx-ic svg{width:56%;height:56%}
</style>"""

def ic(nome, cor='#3A1D8F'):
    p = {
        'x': '<path d="M6 6l12 12M18 6L6 18"/>',
        'check': '<path d="M5 12l4 4 10-10"/>',
        'card': '<rect x="3" y="6" width="14" height="13" rx="2"/><path d="M7 3h12a2 2 0 0 1 2 2v11"/>',
        'repetir': '<path d="M4 12a8 8 0 0 1 14-5.3L20 9M20 4v5h-5M20 12a8 8 0 0 1-14 5.3L4 15M4 20v-5h5"/>',
        'doc': '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
        'alvo': '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="1"/>',
        'alerta': '<path d="M12 3l9 16H3z"/><path d="M12 10v4M12 17v.5"/>',
        'lampada': '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
        'relogio': '<circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/>',
        'chat': '<path d="M4 5h16v11H8l-4 4z"/>',
    }[nome]
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'

def queen_avatar(px=64):
    return (f'<img src="{MARCA}/queen-ia-bust-master-384.png" style="width:{px}px;height:{px}px;border-radius:50%;object-fit:cover;'
            f'object-position:50% 12%;background:#EFEAFD;box-shadow:0 0 0 4px #fff;flex:none">')

def cartoes(pergunta='Tríade de Virchow: quais são os 3 componentes?',
            resposta='Estase, lesão endotelial e hipercoagulabilidade', area='Hemato', selo='veio do seu erro'):
    """Dois cartões de estudo lado a lado (pergunta e resposta), com o selo de onde o card veio."""
    return CSS + f'''<div class="cx" style="width:920px;height:560px">
<div class="cx-card" style="position:absolute;left:0;top:40px;width:500px;height:420px;padding:40px 42px;transform:rotate(-5deg)">
 <span class="cx-pill" style="background:#FDE8EE;color:#C2416A;font-size:22px">{area}</span>
 <div style="font:800 42px/1.18 J,sans-serif;letter-spacing:-.5px;margin-top:26px">{pergunta}</div>
 <div class="cx-rotulo" style="position:absolute;left:42px;bottom:36px;color:#B9B3D3">Pergunta</div></div>
<div class="cx-card" style="position:absolute;left:420px;top:120px;width:480px;height:400px;padding:40px 42px;transform:rotate(4deg);background:linear-gradient(160deg,#F1EBFE,#fff)">
 <div class="cx-rotulo" style="color:#8A80B8">Resposta</div>
 <div style="font:700 36px/1.3 S,sans-serif;color:#3A1D8F;margin-top:22px">{resposta}</div>
 <div class="cx-pill" style="position:absolute;left:42px;bottom:36px;background:#E6F4F1;color:#0F766E;font-size:22px"><span style="width:28px;height:28px">{ic('check', '#0F766E')}</span>gabarito confirmado</div></div>
<div style="position:absolute;left:300px;top:0;transform:rotate(-8deg);background:#F06F8F;color:#fff;border-radius:22px;padding:16px 26px;font:800 26px J,sans-serif;box-shadow:0 20px 40px -20px rgba(240,111,143,.9)">{selo}</div>
</div>'''

def erro_vira_card(passos=(('x', 'Errou a questão', '#FDE8EE', '#C2416A'), ('card', 'Vira flashcard', '#EFEAFD', '#3A1D8F'),
                            ('repetir', 'Volta na revisão', '#E6F4F1', '#0F766E')), largura=900):
    """Fluxo conceitual em 3 passos ligados por seta."""
    blocos = []
    for k, (n, t, bg, cor) in enumerate(passos):
        blocos.append(f'<div class="cx-card" style="flex:1;padding:56px 22px;display:flex;flex-direction:column;align-items:center;gap:26px;text-align:center">'
                      f'<div class="cx-ic" style="background:{bg};width:120px;height:120px;border-radius:34px">{ic(n, cor)}</div><div style="font:800 36px/1.15 J,sans-serif">{t}</div></div>')
        if k < len(passos) - 1: blocos.append('<div class="cx-seta"></div>')
    return CSS + f'<div class="cx" style="width:{largura}px;display:flex;align-items:center;gap:18px">{"".join(blocos)}</div>'

def folha_prova(titulo='Simulado · Aula 07', temas=(('Cardio', 80, '#3A1D8F'), ('Nefro', 45, '#C2416A'), ('Hemato', 70, '#5865D8')), largura=900):
    """Folha de prova de papel (gabarito de bolinhas) com o resultado por tema ao lado."""
    letras = 'ABCDE'
    marcadas = [1, 3, 0, 2, 4, 1, 2, 0]
    erradas = {2, 5}
    linhas = ''
    for q, m in enumerate(marcadas):
        bol = ''.join(f'<span style="width:34px;height:34px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font:700 16px S,sans-serif;'
                      f'{"background:#C2416A;color:#fff" if (i == m and q in erradas) else ("background:#3A1D8F;color:#fff" if i == m else "border:2px solid #D6D0EA;color:#9C96B8")}">{l}</span>'
                      for i, l in enumerate(letras))
        linhas += f'<div style="display:flex;align-items:center;gap:10px"><span style="width:34px;font:700 20px S,sans-serif;color:#9C96B8">{q+1:02d}</span>{bol}</div>'
    barras = ''.join(f'<div><div style="display:flex;justify-content:space-between;font:800 26px J,sans-serif"><span>{t}</span><span style="color:{c}">{p}%</span></div>'
                     f'<div style="height:14px;border-radius:10px;background:#EEEAF8;margin-top:10px"><div style="width:{p}%;height:14px;border-radius:10px;background:{c}"></div></div></div>' for t, p, c in temas)
    return CSS + f'''<div class="cx" style="width:{largura}px;height:520px">
<div class="cx-card" style="position:absolute;left:0;top:10px;width:430px;padding:34px 36px;transform:rotate(-3deg);background:#FFFDF8">
 <div style="font:800 26px J,sans-serif">{titulo}</div><div style="height:2px;background:#EEE8DC;margin:18px 0 20px"></div>
 <div style="display:flex;flex-direction:column;gap:12px">{linhas}</div></div>
<div class="cx-card" style="position:absolute;right:0;top:70px;width:440px;padding:38px 40px;display:flex;flex-direction:column;gap:26px">
 <div class="cx-rotulo" style="color:#C2416A">Onde você errou</div>{barras}</div>
</div>'''

def material_vira(origem='Aula 07', detalhe='PDF do professor', saidas=('Resumo', 'Flashcards', 'Simulado'), largura=900):
    """Um material entrando e virando várias formas de estudo."""
    pills = ''.join(f'<div class="cx-card" style="padding:26px 34px;font:800 34px J,sans-serif;color:#3A1D8F;display:flex;align-items:center;gap:16px">'
                    f'<span style="width:14px;height:14px;border-radius:50%;background:#F06F8F"></span>{s}</div>' for s in saidas)
    return CSS + f'''<div class="cx" style="width:{largura}px;display:flex;align-items:center;gap:30px">
<div class="cx-card" style="width:300px;height:380px;padding:34px;display:flex;flex-direction:column;justify-content:space-between;transform:rotate(-4deg)">
 <div class="cx-ic" style="background:#FDE8EE">{ic('doc', '#C2416A')}</div>
 <div><div style="font:800 40px J,sans-serif">{origem}</div><div style="font-size:26px;color:#667085;margin-top:6px">{detalhe}</div></div>
 <div style="display:flex;flex-direction:column;gap:10px">{''.join('<div style="height:10px;border-radius:6px;background:#EEEAF8;width:%d%%"></div>' % w for w in (100, 86, 92, 60))}</div></div>
<div class="cx-seta" style="width:90px"></div>
<div style="flex:1;display:flex;flex-direction:column;gap:18px">{pills}</div></div>'''

def trio(itens=(('alvo', 'O que mais cai'), ('alerta', 'A pegadinha'), ('lampada', 'Um jeito de lembrar')), largura=900, cores=('#3A1D8F', '#C2416A', '#0F766E')):
    """Três cartões lado a lado com ícone e rótulo curto."""
    fundos = {'#3A1D8F': '#EFEAFD', '#C2416A': '#FDE8EE', '#0F766E': '#E6F4F1'}
    cards = ''.join(f'<div class="cx-card" style="flex:1;padding:60px 26px;display:flex;flex-direction:column;align-items:center;gap:28px;text-align:center">'
                    f'<div class="cx-ic" style="background:{fundos.get(c, "#EFEAFD")};width:120px;height:120px;border-radius:34px">{ic(n, c)}</div><div style="font:800 36px/1.15 J,sans-serif">{t}</div></div>'
                    for (n, t), c in zip(itens, cores))
    return CSS + f'<div class="cx" style="width:{largura}px;display:flex;gap:24px">{cards}</div>'

def continua(ontem='Ontem: ciclo de Krebs, parte 1', hoje='Bora continuar de onde você parou? Faltou a parte das enzimas.', largura=900):
    """A conversa que continua: ontem e hoje, a Queen retomando o assunto."""
    return CSS + f'''<div class="cx" style="width:{largura}px;display:flex;flex-direction:column;gap:26px">
<div style="display:flex;align-items:center;gap:16px;opacity:.55"><span class="cx-pill" style="background:#fff;color:#667085">{ontem}</span></div>
<div style="display:flex;align-items:flex-end;gap:18px">{queen_avatar(92)}
 <div class="cx-card" style="padding:34px 40px;border-radius:34px 34px 34px 10px;font:700 38px/1.3 S,sans-serif;color:#111827">{hoje}</div></div>
<div style="display:flex;justify-content:flex-end"><div style="background:#3A1D8F;color:#fff;border-radius:30px 30px 10px 30px;padding:24px 34px;font:700 34px S,sans-serif">Bora! Sem explicar tudo de novo.</div></div>
</div>'''

def plano_semana(temas=(('Nefrologia', '#C2416A'), ('Cardiologia', '#3A1D8F'), ('Hematologia', '#5865D8')), dias=('Seg', 'Ter', 'Qua'), largura=900):
    """Domingo: 3 temas escolhidos pelos erros da semana, distribuídos nos próximos dias."""
    cards = ''.join(f'<div class="cx-card" style="flex:1;padding:30px 26px;display:flex;flex-direction:column;gap:16px;border-top:10px solid {c}">'
                    f'<div class="cx-rotulo" style="color:#9C96B8">{d}</div><div style="font:800 32px/1.15 J,sans-serif">{t}</div>'
                    f'<div style="font-size:24px;color:#667085">revisar os erros</div></div>' for (t, c), d in zip(temas, dias))
    return CSS + f'''<div class="cx" style="width:{largura}px;display:flex;flex-direction:column;gap:24px">
<div class="cx-card" style="padding:26px 34px;display:flex;align-items:center;gap:20px"><div class="cx-ic" style="background:#FDE8EE;width:72px;height:72px">{ic('alvo', '#C2416A')}</div>
 <div style="font:800 32px J,sans-serif">Domingo: 3 temas que mais te derrubaram</div></div>
<div style="display:flex;gap:20px">{cards}</div></div>'''

def resposta_queen(pergunta='Me explica o ciclo de Krebs pra prova?',
                   blocos=(('Onde acontece', 'Na matriz mitocondrial. Exceção: a succinato desidrogenase fica na membrana interna, é o complexo II.'),
                           ('Saldo por volta', '3 NADH, 1 FADH₂, 1 GTP e 2 CO₂.'),
                           ('Pontos de controle', 'Citrato sintase, isocitrato desidrogenase e alfa-cetoglutarato desidrogenase.'),
                           ('Pegadinha de prova', 'O ciclo não usa O₂ direto, mas para sem ele, porque NADH e FADH₂ precisam ser reoxidados na cadeia.')),
                   resto='Continua: como cai na prova, mnemônico da ordem e 3 questões comentadas',
                   largura=920, visiveis=3):
    """Resposta da Queen IA que parece rica sem virar textão (pedido do Matheus, 29/10/2026).
    Mostra a pergunta, a resposta estruturada em blocos com rótulo, corta com degradê no meio de um bloco
    e fecha com a faixa 'resposta completa na MedQueen IA'. visiveis: quantos blocos aparecem inteiros."""
    cores = ('#3A1D8F', '#0F766E', '#5865D8', '#C2416A', '#B45309')
    bl = ''
    for k, (rot, txt) in enumerate(blocos):
        corte = k >= visiveis
        bl += (f'<div style="display:flex;gap:18px;{"opacity:.55" if corte else ""}"><span style="width:8px;border-radius:6px;background:{cores[k % 5]};flex:none"></span>'
               f'<div><div class="cx-rotulo" style="font-size:19px;color:{cores[k % 5]}">{rot}</div>'
               f'<div style="font:600 29px/1.32 S,sans-serif;color:#1F2340;margin-top:6px">{txt}</div></div></div>')
    return CSS + f'''<div class="cx" style="width:{largura}px;display:flex;flex-direction:column;gap:22px">
<div style="align-self:flex-end;background:#3A1D8F;color:#fff;border-radius:30px 30px 10px 30px;padding:20px 30px;font:700 30px S,sans-serif;max-width:720px">{pergunta}</div>
<div style="display:flex;gap:16px;align-items:flex-start">{queen_avatar(76)}
<div class="cx-card" style="flex:1;padding:34px 38px 0;border-radius:10px 34px 34px 34px;position:relative;overflow:hidden">
 <div style="display:flex;justify-content:space-between;align-items:center"><div style="font:800 34px J,sans-serif">Queen IA</div>
 <span class="cx-pill" style="background:#EFEAFD;color:#3A1D8F;font-size:20px;padding:8px 18px">foco em prova</span></div>
 <div style="display:flex;flex-direction:column;gap:22px;margin-top:24px;max-height:{110 * visiveis + 150}px;overflow:hidden">{bl}</div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:230px;background:linear-gradient(rgba(255,255,255,0),#fff 62%)"></div>
 <div style="position:relative;margin:-40px -38px 0;padding:22px 38px;background:linear-gradient(90deg,#3A1D8F,#5B3BC4);color:#fff;display:flex;justify-content:space-between;align-items:center;gap:20px">
  <div><div style="font:800 26px J,sans-serif">Resposta completa na MedQueen IA</div><div style="font-size:21px;color:#E4DCFA;margin-top:4px">{resto}</div></div>
  <span style="flex:none;border-radius:999px;background:#fff;color:#3A1D8F;padding:12px 22px;font:800 20px J,sans-serif">7 dias grátis</span></div>
</div></div></div>'''
