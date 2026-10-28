import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import tablet, pronto, lista, numeros, nota, queen_img, balao
from conceito import cartoes, erro_vira_card, folha_prova, material_vira, trio, continua, plano_semana
# Sex 30/10 18:50, post único.
SLUG = 'u03-simulado-com-ia'
CARDS = [dict(tipo='capa', olho='Simulado com IA', t=96,
    titulo='Tá na hora de fazer <em>simulado com IA</em>.',
    texto='Escolhe o tema ou usa o seu material. A IA monta a prova e mostra onde você errou.',
    visual=folha_prova(),
    pe_final='7 dias grátis · link na bio')]
