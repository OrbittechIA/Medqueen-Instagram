import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import tablet, pronto, lista, numeros, nota, queen_img, balao
# Dom 01/11 18:50, post único. Tela Hoje (tem a Queen no card).
SLUG = 'u04-domingo-organiza'
CARDS = [dict(tipo='capa', olho='Domingo com IA', t=96,
    titulo='Começa a semana <em>sabendo o que revisar</em>.',
    texto='Na tela Hoje, a próxima tarefa já está pronta, com o seu acerto no tema.',
    visual=tablet('desk-hoje.png', w=900, crop=(330, 140, 1180, 480), h=470, dest=[(370, 288, 590, 44)]),
    pe_final='7 dias grátis · link na bio')]
