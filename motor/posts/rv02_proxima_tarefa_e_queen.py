import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from reel_video import Reel
from reel_formatos import palavras, lista, chat
# Reel em vídeo 2 (quinta 29/10). Refeito em 28/10/2026 SEM print do produto (regra nova do Matheus):
# dor -> o que a MedQueen IA te diz -> conversa com a Queen IA -> a resposta vira material.
# Conteúdo conferido: o ciclo de Krebs ocorre na matriz mitocondrial; a succinato desidrogenase fica
# na membrana mitocondrial interna (é o complexo II da cadeia respiratória).
r = Reel('saida/rv02-proxima-tarefa', musica='trilha_anuncio_1.mp3')
r.cena(palavras('Abre o app pra estudar e <em>não sabe por onde começar</em>?', fundo='claro', g=100, passo=0.24))
r.cena(lista('A MedQueen IA já te entrega:', [('A sua próxima tarefa', ''), ('O seu acerto no tema', ''), ('Um treino focado', '')],
             tag='Rotina de estudo com IA', passo=1.3))
r.cena(chat([
    ('aluno', 'Travei no ciclo de Krebs. Me explica pra prova?'),
    ('queen', '<b>Onde:</b> matriz mitocondrial. <b>Pegadinha:</b> a succinato desidrogenase fica na membrana interna.'),
    ('aluno', 'Dá pra virar flashcard?'),
    ('queen', 'Um toque e vira <b>resumo, flashcards, mapa mental ou questões</b> 💜'),
], ritmo=1.3))
r.final('Aproveite os 7 dias de teste grátis.', 'Link na bio',
        texto='Pergunta, revisa e treina no mesmo lugar, com a Queen IA.')

if __name__ == '__main__':
    r.gravar()
