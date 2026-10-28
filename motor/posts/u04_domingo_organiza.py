import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import tablet, pronto, lista, numeros, nota, queen_img, balao
from conceito import cartoes, erro_vira_card, folha_prova, material_vira, trio, continua, plano_semana
# Dom 01/11 18:50, post único. Tela Hoje (tem a Queen no card).
SLUG = 'u04-domingo-organiza'
CARDS = [dict(tipo='capa', olho='Domingo com IA', t=96,
    titulo='Começa a semana <em>sabendo o que revisar</em>.',
    texto='Olha onde você mais errou e escolhe 3 temas. A IA monta o treino de cada um.',
    visual=plano_semana(),
    pe_final='7 dias grátis · link na bio')]
