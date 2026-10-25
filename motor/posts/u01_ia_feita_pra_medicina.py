import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import tablet, pronto, lista, numeros, nota, queen_img, balao
# Seg 26/10 18:50, post único. Linha IA para Medicina. Queen IA no visual.
SLUG = 'u01-ia-feita-pra-medicina'
CARDS = [dict(tipo='capa', olho='IA na Medicina', t=90,
    titulo='A IA que você usa <em>foi feita pra Medicina</em>?',
    texto='IA generalista responde qualquer coisa. A Queen IA explica do jeito que cai na prova e retoma de onde você parou.',
    visual=queen_img(640, '13'), pe_final='7 dias grátis · link na bio')]
