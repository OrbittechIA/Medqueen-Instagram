import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from reel_video import Reel
from reel_formatos import quiz
# Formato QUIZ. Fontes: tríades clássicas (Virchow, Beck, Charcot, Cushing) em livros de clínica/semiologia.
r = Reel('saida/rv03-quiz-triades', musica='trilha_anuncio_1.mp3')
r.cena(quiz('Qual é a tríade de <span style="color:#3A1D8F">Virchow</span>?',
            ['Estase, lesão endotelial e hipercoagulabilidade',
             'Hipotensão, turgência jugular e bulhas abafadas',
             'Febre, icterícia e dor no hipocôndrio direito',
             'Hipertensão, bradicardia e respiração irregular'],
            0, '<b>Virchow</b> = trombose. Beck = tamponamento. Charcot = colangite. Cushing = hipertensão intracraniana.',
            tag="Tríades que caem na prova"))
r.final('Errou? Vira treino.', 'Link na bio', texto='Aproveite os 7 dias de teste grátis na MedQueen IA.', dur=3.8, queen=False)
if __name__ == '__main__': r.gravar()
