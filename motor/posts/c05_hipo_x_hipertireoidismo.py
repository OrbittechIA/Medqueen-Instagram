import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import lista, numeros, fluxo, nota, queen_img, balao
from conceito import cartoes, erro_vira_card, folha_prova, material_vira, trio, continua, plano_semana, resposta_queen
# Qui 05/11 18:50, carrossel. Estudo (Endocrinologia). Queen IA no card final (pose 16).
# Conteúdo conferido: Harrison (Hipotireoidismo; Hipertireoidismo). Hashimoto: causa mais comum de hipo em área com iodo suficiente; Graves: de hiper.
SLUG = 'c05-hipo-x-hipertireoidismo'
CARDS = [
 dict(tipo='capa', olho='Endocrinologia', t=90, titulo='Hipo x hipertireoidismo: <em>lado a lado.</em>',
      texto='O que cai na prova em 6 cards.',
      visual=trio(itens=(('relogio', 'Hipo: tudo devagar'), ('alerta', 'Hiper: tudo acelerado'), ('alvo', 'TSH decide')))),
 dict(olho='Hipotireoidismo', titulo='O corpo <em>desacelera</em>.',
      visual=lista([('Ganho de peso e intolerância ao frio.', ''), ('Bradicardia e constipação.', ''),
                    ('Pele seca, queda de cabelo, lentidão.', ''), ('Causa mais comum: tireoidite de Hashimoto.', 'Em área com iodo suficiente.')])),
 dict(olho='Hipertireoidismo', titulo='O corpo <em>acelera</em>.',
      visual=lista([('Perda de peso e intolerância ao calor.', ''), ('Taquicardia, palpitação, tremor.', ''),
                    ('Sudorese, ansiedade, mais evacuações.', ''), ('Causa mais comum: doença de Graves.', 'Autoimune, com anticorpo que estimula o receptor de TSH.')], rosa=True)),
 dict(olho='Laboratório', titulo='Primário: TSH e T4 livre andam ao contrário.', t=78, coluna=True,
      visual=numeros([('TSH ↑', 'hipo primário'), ('T4L ↓', 'hipo primário'), ('TSH ↓', 'hiper primário'), ('T4L ↑', 'hiper primário')])),
 dict(olho='Pegadinhas', titulo='As que mais derrubam.',
      visual=lista([('Exoftalmia é da doença de Graves.', 'Bócio multinodular tóxico não dá oftalmopatia.'),
                    ('TSH alto com T4 livre normal:', 'hipotireoidismo subclínico.'),
                    ('TSH é o melhor exame de triagem', 'quando o eixo hipófise e tireoide está íntegro.')], rosa=True)),
 dict(tipo='final', olho='MedQueen IA', t=76, titulo='Ficou dúvida? <em>A Queen IA explica</em> e te testa.',
      visual=queen_img(360, '16'), pe_final='link na bio',
      cta_titulo='Aproveite os 7 dias de teste grátis.', cta_texto='A explicação vira resumo, flashcards ou questões no mesmo lugar.', acao='Link na bio'),
]
