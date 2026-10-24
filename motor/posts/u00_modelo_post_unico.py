import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import tablet
# MODELO de post único (1 imagem 1080x1350). Não publicar este arquivo: copiar, trocar SLUG, texto e visual.
# Regra: 1 ideia só. Título grande (até 8 palavras) com <em> na palavra-chave, 1 linha de apoio, 1 visual forte (print no tablet/celular com destaque, comparação lado a lado, número grande ou diagrama).
SLUG = 'u00-modelo'
CARDS = [
    dict(tipo='capa', olho='Revisão ativa', t=96,
         titulo='Seu erro vira o <em>próximo treino</em>.',
         texto='Questão errada no simulado volta como flashcard com o gabarito confirmado.',
         visual=tablet('desk-criar-material-b.png', w=820, h=440, crop=(40, 560, 560, 300), dest=[(54, 700, 516, 140)]),
         pe_final='7 dias grátis · link na bio'),
]
