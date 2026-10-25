import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from reel_video import Reel, Cena
# Reel em vídeo 2 (quinta): abre o app -> próxima tarefa já está ali -> Queen IA explica -> a resposta vira material.
FULL = (0, 0, 1568, 704)
r = Reel('saida/rv02-proxima-tarefa', musica='trilha_anuncio_1.mp3')
r.cena(Cena(3.0, 'Abre o app e <em>não sabe o que estudar</em>?', olho='Rotina de estudo',
            sons=[(0.1, 'hit', -10)]))
r.cena(Cena(3.2, 'Na MedQueen IA, a próxima tarefa <em>já está ali</em>.',
            sons=[(0.0, 'deep_woosh', -10)]))
r.cena(Cena(6.5, 'Sua próxima tarefa, com o <em>seu acerto</em> no tema.', aparelho='tablet', img='desk-hoje.png',
            zoom=[(0, FULL), (1.4, (330, 140, 900, 470))],
            destaques=[(2.0, 4.2, (370, 288, 590, 44)), (4.4, 6.3, (366, 404, 214, 64))],
            selos=[(2.6, 'Revisão focada no tema')],
            sons=[(0.0, 'woosh_2'), (2.0, 'notification', -12), (4.5, 'mouse_click', -6)]))
r.cena(Cena(7.0, 'Travou num tema? <em>Pergunta pra Queen IA.</em>', aparelho='pronto', img='cel-ia-krebs.png',
            destaques=[(0.9, 3.0, (150, 270, 390, 76))],
            lupas=[(1.0, 3.0, (150, 270, 390, 76), (830, 900, 150)), (3.2, 6.8, (90, 420, 470, 330), (820, 1200, 210))],
            sons=[(0.2, 'woosh_1'), (0.6, 'keyboard_typing', -10), (2.4, 'digital_loading', -14), (3.3, 'notification', -12)]))
r.cena(Cena(6.0, 'E a resposta vira <em>o material que você quiser</em>.', aparelho='tablet', img='desk-criar-material-b.png',
            zoom=[(0, (0, 0, 827, 918)), (1.4, (20, 560, 600, 400))],
            destaques=[(1.6, 3.4, (150, 600, 170, 60)), (3.6, 5.8, (44, 660, 548, 200))],
            sons=[(0.0, 'woosh_2'), (1.7, 'mouse_click', -6), (3.6, 'toggle', -8)]))
r.cena(Cena(5.0, 'Um toque e vira:',
            selos=[(0.4, 'Resumo'), (0.9, 'Flashcards'), (1.4, 'Fluxograma'), (1.9, 'Mapa mental'), (2.4, 'Questões')],
            sons=[(0.0, 'woosh_1'), (0.4, 'toggle', -6), (0.9, 'toggle', -6), (1.4, 'toggle', -6), (1.9, 'toggle', -6), (2.4, 'toggle', -6)]))
r.final('Aproveite os 7 dias de teste grátis.', 'Link na bio',
        texto='Pergunta, revisa e treina no mesmo lugar, com a Queen IA.')

if __name__ == '__main__':
    r.gravar()
