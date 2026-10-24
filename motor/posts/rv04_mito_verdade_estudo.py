import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from reel_video import Reel
from reel_formatos import palavras, mito_verdade
# Formato MITO OU VERDADE. Fontes: efeito de testagem (Roediger e Karpicke, 2006); erro com correção melhora retenção (Metcalfe, 2017); sono e consolidação da memória (Walker, Stickgold).
r = Reel('saida/rv04-mito-verdade', musica='trilha_anuncio_1.mp3')
r.cena(palavras('3 coisas que estudante de Medicina <em>jura que funcionam</em>.', fundo='escuro', tag='Mito ou verdade?'))
r.cena(mito_verdade(1, 'Reler o resumo várias vezes é a melhor forma de revisar.', 'mito', 'Testar a memória fixa mais do que reler. <b>Faça questões.</b>'))
r.cena(mito_verdade(2, 'Errar questão no simulado ajuda a fixar o conteúdo.', 'verdade', 'Errar e ver a correção logo depois <b>ajuda a lembrar na prova.</b>'))
r.cena(mito_verdade(3, 'Virar a noite antes da prova compensa.', 'mito', 'É dormindo que o cérebro <b>consolida o que você estudou.</b>'))
r.final('Aproveite os 7 dias de teste grátis.', 'Link na bio', texto='Questões, caderno de erros e flashcards na MedQueen IA.', dur=3.8, queen=True)
if __name__ == '__main__': r.gravar()
