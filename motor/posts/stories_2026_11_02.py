"""Stories da semana de 02/11/2026. 3 por dia (21). Queen IA em 1 story por dia (o das 15:50), poses sem repetir.
Rodar: python3 posts/stories_2026_11_02.py"""
import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import render_stories, lista, nota, imagem, queen_img, balao

def quiz(nome, pergunta, opcoes, olho='Teste rápido'):
    return dict(nome=nome, olho=olho, titulo=pergunta, t=80,
                visual=lista([(o, '') for o in opcoes], 'num'), texto='A resposta sai no próximo story.')
def resp(nome, titulo, texto, extra=''):
    return dict(nome=nome, olho='Resposta', titulo=titulo, t=88, texto=texto, visual=nota(extra) if extra else '')
_POSES = iter(['18', '47', '25', '33', '44', '39', '27'])  # uma por dia, nenhuma usada na semana de 26/10
def dica(nome, frase):
    return dict(nome=nome, olho='Dica da Queen IA', visual=balao(frase) + queen_img(820, next(_POSES)), coluna=True)
def enquete(nome, olho, titulo, opcoes):
    return dict(nome=nome, olho=olho, titulo=titulo, t=92, texto='Responde no direct com o número.',
                visual=lista([(o, '') for o in opcoes], 'num'))
def novo(nome, olho, titulo, img):
    return dict(nome=nome, olho=olho, titulo=titulo, t=84, visual=imagem(img, h=900))

S = [
 # segunda 02/11
 quiz('01-seg-1350', 'VCM de 72 fL. Que tipo de anemia é essa?', ['Microcítica', 'Normocítica', 'Macrocítica']),
 dica('02-seg-1550', 'Gasometria: <b>começa sempre pelo pH.</b> Depois vê quem explica o pH: pCO₂ ou HCO₃⁻.'),
 novo('03-seg-2120', 'Post novo', 'Travou na gasometria? Pergunta pra Queen IA.', 'saida/u05-gasometria-queen/01.png'),
 # terça 03/11
 resp('04-ter-1150', 'Microcítica.', 'VCM abaixo de 80 fL. A causa mais comum é a deficiência de ferro.', 'Hoje às 18:50: <b>anemias pelo VCM</b>, completo.'),
 dica('05-ter-1550', 'Anemia na questão? <b>Olha o VCM antes de qualquer outra coisa.</b> Ele já corta metade das hipóteses.'),
 novo('06-ter-2120', 'Post novo', 'Anemia na prova: começa pelo VCM.', 'saida/c04-anemias-vcm/01.png'),
 # quarta 04/11
 quiz('07-qua-1150', 'Exoftalmia aponta pra qual causa de hipertireoidismo?', ['Doença de Graves', 'Bócio multinodular tóxico', 'Tireoidite subaguda']),
 dica('08-qua-1550', 'Fez o Enamed? Enquanto o resultado não sai, <b>refaz as questões que você errou.</b>'),
 novo('09-qua-2120', 'Notícia', 'Enamed 2026: o resultado sai em 4 de dezembro.', 'saida/u06-enamed-resultado/01.png'),
 # quinta 05/11
 resp('10-qui-1150', 'Doença de Graves.', 'A oftalmopatia é própria da doença de Graves, que é autoimune.', 'Hoje às 18:50: <b>hipo x hiper lado a lado.</b>'),
 dica('11-qui-1550', 'Tireoide na prova: <b>pede o TSH primeiro.</b> Na doença primária, ele muda antes do T4 livre.'),
 novo('12-qui-2120', 'Post novo', 'Hipo x hipertireoidismo: lado a lado.', 'saida/c05-hipo-x-hipertireoidismo/01.png'),
 # sexta 06/11
 enquete('13-sex-1150', 'Sexta de estudo', 'Quantas questões você fez essa semana?', ['Menos de 50', 'De 50 a 200', 'Mais de 200']),
 dica('14-sex-1550', 'Prova do professor chegando? <b>Treina com questões da aula dele.</b> É o conteúdo que ele deu em sala.'),
 novo('15-sex-2120', 'Post novo', 'A aula do professor vira simulado.', 'saida/u07-aula-vira-simulado/01.png'),
 # sábado 07/11
 quiz('16-sab-1150', 'Aminoglicosídeos agem em qual subunidade do ribossomo?', ['30S', '50S', '60S']),
 dica('17-sab-1550', 'Antibiótico: <b>decora pelo alvo, não pela lista de nomes.</b> Parede, ribossomo, DNA e folato.'),
 novo('18-sab-2120', 'Resposta: 30S', 'Antibiótico: onde cada classe ataca.', 'saida/c06-antibioticos-mecanismo/01.png'),
 # domingo 08/11
 enquete('19-dom-1150', 'Domingo', 'Qual matéria mais te derrubou essa semana?', ['Hemato', 'Endócrino', 'Farmaco']),
 dica('20-dom-1550', 'Domingo: <b>escolhe 1 tema e faz 10 questões.</b> Pouco, mas toda semana.'),
 novo('21-dom-2120', 'Post novo', 'Estude. Evolua. Salve vidas.', 'saida/u08-estude-evolua-salve-vidas/01.png'),
]
render_stories(S, f'{RAIZ}/saida/stories-2026-11-02')
