"""Stories da semana de 26/10/2026 (3 por dia). Rodar: python3 posts/stories_2026_10_26.py"""
import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import render_stories, tablet, pronto, lista, nota, imagem, queen_img, balao

def quiz(nome, pergunta, opcoes):
    return dict(nome=nome, olho='Teste rápido', titulo=pergunta, t=84,
                visual=lista([(o, '') for o in opcoes], 'num'), texto='A resposta sai no próximo story.')
def resp(nome, titulo, texto, extra=''):
    return dict(nome=nome, olho='Resposta', titulo=titulo, t=88, texto=texto, visual=nota(extra) if extra else '')
def dica(nome, frase):
    return dict(nome=nome, olho='Dica da Queen IA', visual=balao(frase) + queen_img(820), coluna=True)
def frase(nome, titulo, texto=''):
    return dict(nome=nome, olho='MedQueen IA', titulo=titulo, t=104, texto=texto)
def novo(nome, olho, titulo, img):
    return dict(nome=nome, olho=olho, titulo=titulo, t=84, visual=imagem(img, h=900))

S = [
 # segunda 26/10
 dict(nome='01-seg-1150', olho='Tela Hoje', titulo='Abriu o app, a próxima tarefa já está ali.', t=80,
      visual=tablet('desk-hoje.png', w=860, crop=(330, 140, 1180, 480), h=600, dest=[(360, 180, 600, 300)])),
 quiz('02-seg-1550', 'Qual é o principal ponto de controle do ciclo de Krebs?', ['Citrato sintase', 'Isocitrato desidrogenase', 'Fumarase']),
 novo('03-seg-2120', 'Post novo', 'Ciclo de Krebs em 8 cards. Salva pra prova.', 'saida/s01-krebs/01.png'),
 # terça 27/10
 resp('04-ter-1150', 'Isocitrato desidrogenase.', 'É o principal ponto de controle do ciclo.', '<b>Ativam:</b> ADP e Ca²⁺. <b>Inibem:</b> ATP e NADH.'),
 dica('05-ter-1550', 'Reler dá a sensação de que você aprendeu. <b>Testar mostra o que ficou de verdade.</b>'),
 dict(nome='06-ter-2120', olho='Flashcards', titulo='Seus erros de questões viram cards.', t=84,
      visual=tablet('desk-flashcards.png', w=860, crop=(350, 200, 1150, 520), h=520, dest=[(365, 404, 1112, 136)])),
 # quarta 28/10
 frase('07-qua-1150', 'Semana de prova não começa na véspera.', 'Começa no primeiro erro que você revisa.'),
 quiz('08-qua-1550', 'Por molécula de glicose, quantas voltas o ciclo de Krebs dá?', ['Uma', 'Duas', 'Quatro']),
 novo('09-qua-2120', 'Post novo', 'Errou a questão? Ela volta como treino.', 'saida/p01-erro-vira-treino/01.png'),
 # quinta 29/10
 resp('10-qui-1150', 'Duas voltas.', 'A glicose vira 2 piruvatos, e cada um vira 1 acetil‑CoA.', 'Por isso, por glicose: <b>6 NADH, 2 FADH₂, 2 GTP e 4 CO₂</b>.'),
 dict(nome='11-qui-1550', olho='Caderno de erros', titulo='Onde você está perdendo ponto.', t=88,
      visual=pronto('cel-caderno-erros.png', h=980, lupa=(298, 702, 220, 520, 470, 1.45))),
 dica('12-qui-2120', 'Errou? Antes de ir pra próxima, <b>entende por que a alternativa errada pareceu certa.</b>'),
 # sexta 30/10
 dict(nome='13-sex-1150', olho='Simulados', titulo='Simulado por tema ou pelo seu material.', t=84,
      visual=tablet('desk-simulados.png', w=860, crop=(370, 60, 1110, 640), dest=[(870, 138, 215, 64)])),
 quiz('14-sex-1550', 'Onde fica a succinato desidrogenase?', ['Matriz mitocondrial', 'Membrana mitocondrial interna', 'Citoplasma']),
 novo('15-sex-2120', 'Reel novo', 'A Queen IA explicando Krebs. Assiste até o fim.', 'saida/r01-krebs-queen/quadro-12.png'),
 # sábado 31/10
 resp('16-sab-1150', 'Na membrana mitocondrial interna.', 'É a única enzima do ciclo que não fica na matriz.', 'Ela também é o <b>complexo II</b> da cadeia respiratória.'),
 dica('17-sab-1550', 'Fim de semana: <b>revisa só o que você errou essa semana.</b> Rende mais do que começar matéria nova.'),
 dict(nome='18-sab-2120', olho='Queen IA', titulo='A resposta vira resumo, flashcards, mapa ou questões.', t=80,
      visual=tablet('desk-criar-material-b.png', w=860, h=470, crop=(40, 600, 560, 302), dest=[(54, 700, 516, 140)])),
 # domingo 01/11
 frase('19-dom-1150', 'Domingo é dia de planejar. Não de recomeçar.', 'Separa o que você errou na semana e começa por aí.'),
 quiz('20-dom-1550', 'Qual etapa do ciclo de Krebs gera GTP direto?', ['Citrato → isocitrato', 'Succinil‑CoA → succinato', 'Malato → oxaloacetato']),
 resp('21-dom-2120', 'Succinil‑CoA → succinato.', 'É a única etapa com produção direta de GTP.', 'Quer revisar o ciclo inteiro? <b>O carrossel de segunda está no perfil.</b>'),
]
render_stories(S, f'{RAIZ}/saida/stories-2026-10-26')
