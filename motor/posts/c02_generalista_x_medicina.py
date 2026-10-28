import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import tablet, pronto, lista, numeros, nota, queen_img, balao
from conceito import cartoes, erro_vira_card, folha_prova, material_vira, trio, continua, plano_semana
# Qui 29/10 18:50, carrossel. IA generalista x IA de Medicina. Queen IA na capa.
SLUG = 'c02-generalista-x-medicina'
CARDS = [
 dict(tipo='capa', olho='IA na Medicina', t=82, titulo='IA generalista x <em>IA de Medicina</em>: 4 diferenças que pesam na sua nota.',
      visual=queen_img(580, '07')),
 dict(olho='1. Memória', titulo='Ela retoma de onde você parou.',
      texto='Suas conversas e materiais ficam salvos. Você não explica tudo de novo a cada pergunta.',
      visual=continua()),
 dict(olho='2. Foco em prova', titulo='Explica do jeito que cai na prova.',
      texto='Estrutura, ponto que mais cai e pegadinha. Não um texto genérico.',
      visual=trio()),
 dict(olho='3. Seu material', titulo='Usa a aula do seu professor.',
      texto='Você manda o PDF e ele vira simulado, resumo ou flashcards.',
      visual=material_vira()),
 dict(olho='4. Erro vira treino', titulo='O que você erra volta pra revisão.',
      visual=erro_vira_card()),
 dict(tipo='final', olho='MedQueen IA', t=78, titulo='IA generalista não foi feita pra Medicina. <em>A MedQueen IA foi.</em>',
      visual=queen_img(350, '10'), pe_final='link na bio',
      cta_titulo='Aproveite os 7 dias de teste grátis.', cta_texto='Explicação, simulados, flashcards e caderno de erros com a Queen IA.', acao='Link na bio'),
]
