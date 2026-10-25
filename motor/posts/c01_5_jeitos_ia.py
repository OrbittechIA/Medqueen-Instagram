import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import tablet, pronto, lista, numeros, nota, queen_img, balao
# Ter 27/10 18:50, carrossel. Linha IA para Medicina (como usar).
SLUG = 'c01-5-jeitos-ia'
CARDS = [
 dict(tipo='capa', olho='IA na Medicina', t=86, titulo='5 jeitos de usar IA pra estudar Medicina <em>sem perder tempo</em>.',
      visual=pronto('cel-ia-krebs.png', h=720, dest=[(150, 270, 390, 76)])),
 dict(olho='1. Explicação com foco em prova', titulo='Pede o que mais cai, não um textão.',
      texto='Conceito, pegadinha e mnemônico. A Queen IA já organiza a resposta assim.',
      visual=pronto('cel-ia-krebs.png', h=700, lupa=(300, 520, 170, 300, 520, 1.6))),
 dict(olho='2. Resposta vira material', titulo='Transforma a explicação em resumo, flashcard ou questão.',
      visual=tablet('desk-criar-material-b.png', w=860, h=430, crop=(30, 600, 600, 300), dest=[(54, 700, 516, 140)])),
 dict(olho='3. Flashcards dos erros', titulo='Cada questão errada vira card.',
      texto='Com o gabarito confirmado. Você revisa o que errou, não o que já sabe.',
      visual=tablet('desk-flashcards.png', w=860, crop=(350, 200, 1150, 520), h=420, dest=[(365, 404, 1112, 136)])),
 dict(olho='4. Simulado com IA', titulo='Monta a prova pelo tema ou pelo seu material.',
      visual=pronto('cel-novo-simulado.png', h=720, dest=[(96, 770, 400, 100), (96, 890, 400, 100)])),
 dict(olho='5. Caderno de erros', titulo='Vê em que área você está perdendo ponto.',
      visual=pronto('cel-caderno-erros.png', h=720, lupa=(298, 702, 200, 470, 380, 1.45))),
 dict(tipo='final', olho='MedQueen IA', t=80, titulo='Os 5 no mesmo lugar.', visual=queen_img(380), pe_final='link na bio',
      cta_titulo='Aproveite os 7 dias de teste grátis.', cta_texto='Comenta IA que eu te mando o guia: como estudar Medicina com IA sem se enganar.', acao='Link na bio'),
]
