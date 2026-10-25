import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import tablet, pronto, lista, numeros, nota, queen_img, balao
# Sáb 31/10 18:50, carrossel. Linha "IA sem se enganar". Queen IA na capa e no final.
SLUG = 'c03-ia-errou-como-checar'
CARDS = [
 dict(tipo='capa', olho='IA sem se enganar', t=92, titulo='A IA pode errar. <em>Como checar em 4 passos.</em>', visual=queen_img(560, 'pensando')),
 dict(olho='Passo 1', titulo='Pede o raciocínio, não só a resposta.', t=84,
      visual=nota('Se a IA não consegue explicar <b>por que</b> a resposta é aquela, desconfia.')),
 dict(olho='Passo 2', titulo='Dose, critério e conduta: sempre na fonte.', t=84,
      visual=lista([('Livro-texto da disciplina.', ''), ('Diretriz da sociedade médica.', ''), ('Bula ou protocolo oficial.', '')], 'check')),
 dict(olho='Passo 3', titulo='Testa com questão.', t=84, texto='Se você entendeu, acerta. Se errou, a explicação não serviu.',
      visual=pronto('cel-novo-simulado.png', h=640, dest=[(96, 590, 400, 70)])),
 dict(olho='Passo 4', titulo='Desconfia de número sem fonte.', t=84,
      visual=lista([('Porcentagem que ninguém citou.', ''), ('Dose sem referência.', ''), ('Valor de referência "redondo demais".', '')], 'num', rosa=True)),
 dict(tipo='final', olho='MedQueen IA', t=76, titulo='Na MedQueen IA, a explicação vira questão pra você <em>testar na hora</em>.',
      visual=queen_img(340), pe_final='link na bio',
      cta_titulo='Aproveite os 7 dias de teste grátis.', cta_texto='E comenta IA que eu te mando o guia completo.', acao='Link na bio'),
]
