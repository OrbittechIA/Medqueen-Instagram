import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import tablet, pronto, lista, numeros, nota, queen_img, balao
# Qua 28/10 18:50, post único. "Tá na hora de... com IA". Isca: comenta IA.
SLUG = 'u02-flashcard-com-ia'
CARDS = [dict(tipo='capa', olho='Flashcards com IA', t=96,
    titulo='Tá na hora de fazer <em>flashcard com IA</em>.',
    texto='Seus erros de questões viram cards com o gabarito confirmado. Sem digitar card por card.',
    visual=tablet('desk-flashcards.png', w=900, crop=(350, 90, 1180, 470), h=440, dest=[(365, 404, 1112, 136), (1385, 444, 252, 54)]),
    pe_final='comenta IA · te mando o guia')]
