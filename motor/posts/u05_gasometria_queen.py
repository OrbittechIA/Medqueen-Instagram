import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import lista, numeros, fluxo, nota, queen_img, balao
from conceito import cartoes, erro_vira_card, folha_prova, material_vira, trio, continua, plano_semana, resposta_queen
# Seg 02/11 18:50, post único. Produto (a resposta da Queen IA). Queen IA (avatar na resposta).
# Conteúdo conferido: Harrison (distúrbios ácido-base), fórmula de Winter (pCO2 esperada = 1,5 x HCO3 + 8 ± 2), ânion gap = Na - (Cl + HCO3).
SLUG = 'u05-gasometria-queen'
CARDS = [dict(tipo='capa', olho='Pergunta pra Queen IA', t=84,
    titulo='Travou na <em>gasometria?</em>',
    visual=resposta_queen(pergunta='Me explica gasometria pra prova?',
        blocos=(('Passo 1 · pH', 'Abaixo de 7,35 é acidemia. Acima de 7,45, alcalemia.'),
                ('Passo 2 · Quem explica o pH', 'pCO₂ fora de 35 a 45 aponta pro respiratório. HCO₃⁻ fora de 22 a 26, pro metabólico.'),
                ('Passo 3 · Compensação', 'Acidose metabólica: pCO₂ esperada = 1,5 × HCO₃⁻ + 8 ± 2 (fórmula de Winter).')),
        resto='Continua: ânion gap, distúrbio misto e questões', visiveis=2, largura=896),
    pe_final='7 dias grátis · link na bio')]
