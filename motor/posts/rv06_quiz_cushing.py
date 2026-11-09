import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from reel_video import Reel
from reel_formatos import quiz
# Formato QUIZ, série "Tríades que caem na prova" #2.
# Fonte: tríade de Cushing (hipertensão arterial, bradicardia, respiração irregular) como sinal tardio de hipertensão intracraniana,
# com risco de herniação: livros de neurologia/emergência (ex.: Harrison, ATLS para TCE).
r = Reel('saida/rv06-quiz-cushing', musica='trilha_anuncio_1.mp3')
r.cena(quiz('Hipertensão, bradicardia e respiração irregular. <span style="color:#3A1D8F">Pensa em quê?</span>',
            ['Tamponamento cardíaco',
             'Hipertensão intracraniana',
             'Colangite aguda',
             'Tromboembolismo pulmonar'],
            1, 'Tríade de <b>Cushing</b> = hipertensão intracraniana. Sinal tardio: risco de herniação.',
            tag="Tríades que caem na prova #2"))
r.final('Errou? Vira treino.', 'Link na bio', texto='Aproveite os 7 dias de teste grátis na MedQueen IA.', dur=3.8, queen=False)
if __name__ == '__main__': r.gravar()
