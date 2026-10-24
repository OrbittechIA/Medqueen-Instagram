import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from reel_video import Reel, Cena
# Reel em vídeo 1 (terça): semana de prova -> simulado -> onde errou -> caderno de erros -> flashcards.
FULL = (0, 0, 1568, 704)
r = Reel('saida/rv01-simulado', musica='trilha_anuncio_1.mp3')
r.cena(Cena(3.0, 'Faltam 5 dias pra prova. <em>Por onde começar?</em>', olho='Semana de prova', escuro=True,
            sons=[(0.1, 'hit', -10)]))
r.cena(Cena(3.0, 'Reler tudo não dá tempo.', sub='E reler não mostra o que você ainda não sabe.', escuro=True,
            sons=[(0.2, 'downer', -12)]))
r.cena(Cena(3.0, 'Faz um simulado. <em>Ele mostra.</em>', escuro=True,
            sons=[(0.0, 'metallic_rise', -14), (2.0, 'hit', -10)]))
r.cena(Cena(6.0, 'Escolhe o tema ou usa o seu material.', aparelho='pronto', img='cel-novo-simulado.png',
            destaques=[(1.2, 3.2, (96, 770, 400, 100)), (3.4, 5.6, (96, 890, 400, 100))],
            sons=[(0.0, 'woosh_2'), (1.3, 'mouse_click', -6), (3.5, 'mouse_click', -6)]))
r.cena(Cena(6.5, 'No fim, você vê <em>onde errou</em>.', aparelho='tablet', img='desk-simulados.png',
            zoom=[(0, FULL), (1.6, (700, 470, 780, 230))],
            destaques=[(2.2, 6.2, (940, 572, 90, 44))],
            selos=[(3.0, 'Resultado por tema')],
            sons=[(0.0, 'woosh_1'), (1.8, 'mouse_click', -6), (2.2, 'glitch_counter', -16)]))
r.cena(Cena(6.5, 'Cada erro entra no <em>caderno de erros</em>.', aparelho='pronto', img='cel-caderno-erros.png',
            destaques=[(1.2, 3.4, (74, 616, 446, 174)), (3.6, 6.3, (74, 810, 446, 280))],
            lupas=[(1.3, 3.4, (74, 616, 446, 174), (850, 1060, 170)), (3.7, 6.3, (74, 810, 446, 280), (850, 1250, 190))],
            sons=[(0.0, 'woosh_2'), (0.6, 'notification', -12), (1.3, 'camera_shutter', -14), (3.7, 'woosh_1', -10)]))
r.cena(Cena(6.0, 'E vira flashcard com o <em>gabarito confirmado</em>.', aparelho='tablet', img='desk-flashcards.png',
            zoom=[(0, FULL), (1.5, (350, 330, 820, 260)), (3.6, (900, 330, 640, 260))],
            destaques=[(1.8, 3.6, (364, 404, 1108, 120)), (3.8, 5.8, (1202, 444, 252, 54))],
            sons=[(0.0, 'woosh_2'), (3.9, 'mouse_click', -6), (4.1, 'notification', -12)]))
r.cena(Cena(5.5, 'Tudo isso <em>no mesmo lugar</em>:',
            selos=[(0.5, 'Simulado por tema ou pelo seu material'), (1.1, 'Resultado por tema'),
                   (1.7, 'Caderno de erros por área'), (2.3, 'Flashcards dos seus erros')],
            sons=[(0.0, 'woosh_1'), (0.5, 'toggle', -6), (1.1, 'toggle', -6), (1.7, 'toggle', -6), (2.3, 'toggle', -6)]))
r.final('Aproveite os 7 dias de teste grátis.', 'Link na bio',
        texto='Simulados, caderno de erros, flashcards e a Queen IA na MedQueen IA.')

if __name__ == '__main__':
    r.gravar()
