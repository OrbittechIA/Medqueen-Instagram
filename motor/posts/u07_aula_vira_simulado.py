import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import lista, numeros, fluxo, nota, queen_img, balao
from conceito import cartoes, erro_vira_card, folha_prova, material_vira, trio, continua, plano_semana, resposta_queen
# Sex 06/11 18:50, post único. Produto (simulado pelo seu material). Sem Queen IA.
SLUG = 'u07-aula-vira-simulado'
CARDS = [dict(tipo='capa', olho='Seu material', t=96,
    titulo='A aula do professor <em>vira simulado.</em>',
    texto='Você manda o PDF e treina com questões do que ele deu em sala.',
    visual=material_vira(origem='Aula de Cardio', detalhe='PDF do professor', saidas=('Simulado', 'Resumo', 'Flashcards')),
    pe_final='7 dias grátis · link na bio')]
