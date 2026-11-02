import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import lista, numeros, fluxo, nota, queen_img, balao
from conceito import cartoes, erro_vira_card, folha_prova, material_vira, trio, continua, plano_semana, resposta_queen
# Qua 04/11 18:50, post único. Notícia. Sem Queen IA.
# Fonte: Inep, gabarito preliminar da reaplicação do Enamed 2026 (20/10/2026): gabarito definitivo e resultado previstos para 04/12/2026.
# https://acritica.net/educacao/inep-divulga-gabarito-preliminar-da-reaplicacao-do-enamed-2026/
SLUG = 'u06-enamed-resultado'
CARDS = [dict(tipo='capa', olho='Notícia · Enamed 2026', t=92,
    titulo='Fez o Enamed? O resultado sai em <em>4 de dezembro.</em>',
    texto='Gabarito definitivo e resultado previstos pelo Inep para a mesma data.',
    coluna=True,
    visual=numeros([('13/09', 'prova'), ('18/10', 'reaplicação'), ('04/12', 'resultado')])
           + nota('Até lá: <b>refaz as questões que você errou</b>. É o que sobra de aprendizado da prova.'),
    pe_final='fonte: Inep')]
