import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import tablet, pronto, lista, queen_img
SLUG = 'p01-erro-vira-treino'
CARDS = [
    dict(tipo='capa', olho='Estudante de Medicina', t=90,
         titulo='Errou a questão? <em>Ela volta como treino.</em>',
         visual=pronto('cel-caderno-erros.png', h=730, dest=[(75, 455, 447, 140)])),
    dict(olho='Passo 1', titulo='O simulado mostra onde você erra.',
         texto='Por tema ou pelo seu material. O resultado fica salvo e leva direto ao caderno de erros.',
         visual=tablet('desk-simulados.png', w=860, crop=(370, 60, 1110, 640), dest=[(1010, 85, 175, 36), (1095, 228, 368, 172)])),
    dict(olho='Passo 2', titulo='Cada erro vira um card com o gabarito.',
         texto='Com o gabarito confirmado do banco de questões ou do próprio simulado.',
         visual=tablet('desk-flashcards.png', w=860, crop=(350, 200, 1150, 520), h=390, dest=[(365, 404, 1112, 136)])),
    dict(olho='Passo 3', titulo='O caderno de erros mostra a área fraca.',
         visual=pronto('cel-caderno-erros.png', h=740, lupa=(298, 702, 200, 470, 380, 1.45))),
    dict(olho='Na prática', titulo='Você revisa o que errou. Não o que já sabe.',
         visual=lista([('Faz o simulado do tema da semana.', ''),
                       ('O erro vai para o caderno, separado por área.', ''),
                       ('Vira card e volta na revisão.', 'Até o ponto fraco virar acerto.')])),
    dict(tipo='final', olho='MedQueen IA', t=80,
         titulo='Seu erro de hoje vira o treino de amanhã.',
         visual=queen_img(470), pe_final='link na bio',
         cta_titulo='Teste grátis.',
         cta_texto='Simulados, caderno de erros e flashcards no mesmo lugar, com a Queen IA.',
         acao='Link na bio'),
]
