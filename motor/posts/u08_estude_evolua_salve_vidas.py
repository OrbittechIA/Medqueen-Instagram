import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import lista, numeros, fluxo, nota, queen_img, balao
from conceito import cartoes, erro_vira_card, folha_prova, material_vira, trio, continua, plano_semana, resposta_queen
# Dom 08/11 18:50, post único. Marca. Queen IA (pose 35, estetoscópio).
SLUG = 'u08-estude-evolua-salve-vidas'
CARDS = [dict(tipo='capa', olho='MedQueen IA', t=104,
    titulo='Estude. Evolua. <em>Salve vidas.</em>',
    texto='Cada questão que você treina hoje é um paciente que você atende melhor amanhã.',
    visual=queen_img(640, '35'),
    pe_final='7 dias grátis · link na bio')]
