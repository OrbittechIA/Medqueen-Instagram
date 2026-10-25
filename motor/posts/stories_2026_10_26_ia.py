"""Stories da semana de 26/10/2026, linha nova (IA para Medicina). 3 por dia, seg a sáb (domingo 01/11 já estava agendado).
Queen IA em 1 story por dia (o das 15:50). Rodar: python3 posts/stories_2026_10_26_ia.py"""
import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import render_stories, tablet, pronto, lista, nota, imagem, queen_img, balao

def quiz(nome, pergunta, opcoes):
    return dict(nome=nome, olho='Teste rápido', titulo=pergunta, t=80,
                visual=lista([(o, '') for o in opcoes], 'num'), texto='A resposta sai no próximo story.')
def resp(nome, titulo, texto, extra=''):
    return dict(nome=nome, olho='Resposta', titulo=titulo, t=88, texto=texto, visual=nota(extra) if extra else '')
def dica(nome, frase):
    return dict(nome=nome, olho='Dica da Queen IA', visual=balao(frase) + queen_img(820), coluna=True)
def frase(nome, titulo, texto=''):
    return dict(nome=nome, olho='IA na Medicina', titulo=titulo, t=100, texto=texto)
def novo(nome, olho, titulo, img):
    return dict(nome=nome, olho=olho, titulo=titulo, t=84, visual=imagem(img, h=900))

S = [
 # segunda 26/10
 dict(nome='01-seg-1350', olho='IA na Medicina', titulo='Você usa IA pra estudar Medicina?', t=100, texto='Responde no direct com o número.',
      visual=lista([('Todo dia', ''), ('Às vezes', ''), ('Ainda não', '')], 'num')),
 dica('02-seg-1550', 'IA generalista responde tudo. <b>Pra prova, pede o que mais cai e as pegadinhas.</b>'),
 novo('03-seg-2120', 'Post novo', 'A IA que você usa foi feita pra Medicina?', 'saida/u01-ia-feita-pra-medicina/01.png'),
 # terça 27/10
 quiz('04-ter-1150', 'Qual destes NÃO é um bom uso de IA pra estudar?', ['Pedir a explicação de um tema', 'Copiar a dose de um remédio sem conferir', 'Transformar a aula em flashcards']),
 dica('05-ter-1550', 'Antes de decorar, <b>pede pra IA te testar.</b> Errar no treino é melhor que errar na prova.'),
 novo('06-ter-2120', 'Post novo', '5 jeitos de usar IA pra estudar Medicina.', 'saida/c01-5-jeitos-ia/01.png'),
 # quarta 28/10
 resp('07-qua-1150', 'Copiar dose sem conferir.', 'IA pode errar número. Dose, critério e conduta você confere sempre na fonte oficial.', 'Explicação, resumo e flashcard: <b>pode usar IA à vontade.</b>'),
 dica('08-qua-1550', 'Tem guia novo: <b>como estudar Medicina com IA sem se enganar.</b> Comenta IA no post de hoje que a gente te manda.'),
 novo('09-qua-2120', 'Post novo', 'Tá na hora de fazer flashcard com IA.', 'saida/u02-flashcard-com-ia/01.png'),
 # quinta 29/10
 dict(nome='10-qui-1150', olho='IA na Medicina', titulo='Estudar com IA não é colar da IA.', t=100,
      visual=lista([('<b>Colar:</b> copiar a resposta e seguir.', ''), ('<b>Estudar:</b> pedir questão, errar, entender e acertar sozinho.', '')], 'num')),
 dica('11-qui-1550', 'Flashcard bom é curto: <b>uma pergunta, uma resposta.</b> Se precisa de parágrafo, vira dois cards.'),
 novo('12-qui-2120', 'Post novo', 'IA generalista x IA de Medicina: 4 diferenças.', 'saida/c02-generalista-x-medicina/01.png'),
 # sexta 30/10
 dict(nome='13-sex-1150', olho='Simulado com IA', titulo='Escolhe o tema. A IA monta a prova.', t=84,
      visual=pronto('cel-novo-simulado.png', h=980, dest=[(96, 770, 400, 100), (96, 890, 400, 100)])),
 dica('14-sex-1550', 'Errou no simulado? <b>Ótimo. Agora você sabe exatamente o que revisar.</b>'),
 novo('15-sex-2120', 'Post novo', 'Tá na hora de fazer simulado com IA.', 'saida/u03-simulado-com-ia/01.png'),
 # sábado 31/10
 quiz('16-sab-1150', 'Qual erro de IA é o mais perigoso na Medicina?', ['Resposta longa demais', 'Número ou dose inventada', 'Resposta em inglês']),
 dica('17-sab-1550', 'Sábado: <b>pede um simulado de 10 questões do tema da semana.</b> Em 20 minutos você sabe onde está.'),
 novo('18-sab-2120', 'Resposta: número ou dose inventada', 'Como checar se a IA errou, em 4 passos.', 'saida/c03-ia-errou-como-checar/01.png'),
]
render_stories(S, f'{RAIZ}/saida/stories-2026-10-26-ia')
