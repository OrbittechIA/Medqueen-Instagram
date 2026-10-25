import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import tablet, pronto, lista, nota, queen_img, balao
# Isca "comenta IA": guia em PDF mandado no direct. Gerar PNGs e juntar em PDF (ver LEIA-ME).
SLUG = 'guia-estudar-com-ia'
CARDS = [
 dict(tipo='capa', olho='Guia gratuito', t=96, titulo='Como estudar Medicina com IA <em>sem se enganar</em>.',
      texto='O método em 6 passos, do jeito que usamos na MedQueen IA.', visual=queen_img(580, '01')),
 dict(olho='Antes de tudo', titulo='IA generalista x IA de Medicina.', t=84,
      visual=lista([('<b>Generalista</b> responde qualquer assunto, sem saber o que cai na sua prova.', ''),
                    ('<b>De Medicina</b> organiza a resposta pra prova, usa o seu material e lembra do que você já estudou.', '')], 'num')),
 dict(olho='Passo 1', titulo='Pede a explicação com foco em prova.', t=84,
      texto='Não pergunta só "o que é". Pede o que mais cai, a pegadinha clássica e um mnemônico.',
      visual=pronto('cel-ia-krebs.png', h=640, dest=[(150, 270, 390, 76)])),
 dict(olho='Passo 2', titulo='Transforma a resposta em material.', t=84,
      texto='Resumo pra ler, flashcard pra revisar, mapa pra ligar os pontos, questão pra testar.',
      visual=tablet('desk-criar-material-b.png', w=860, h=430, crop=(30, 600, 600, 300), dest=[(54, 700, 516, 140)])),
 dict(olho='Passo 3', titulo='Testa antes de achar que sabe.', t=84,
      texto='Faz um simulado curto do tema. Reler dá sensação de domínio; testar mostra o que ficou.',
      visual=pronto('cel-novo-simulado.png', h=640, dest=[(96, 770, 400, 100), (96, 890, 400, 100)])),
 dict(olho='Passo 4', titulo='Seu erro é o próximo estudo.', t=84,
      texto='Cada questão errada vira revisão. Começa a semana pelo caderno de erros, não por matéria nova.',
      visual=pronto('cel-caderno-erros.png', h=660, dest=[(75, 616, 447, 174)])),
 dict(olho='Passo 5', titulo='Confere o que é crítico.', t=84,
      visual=lista([('Dose, critério diagnóstico e conduta: sempre na fonte oficial.', ''),
                    ('Pede o raciocínio, não só a resposta.', ''),
                    ('Desconfia de número sem fonte.', '')], 'check', rosa=True)),
 dict(olho='Passo 6', titulo='Uma rotina simples por semana.', t=84,
      visual=lista([('<b>Seg a qui:</b> explicação com foco em prova + flashcards.', ''),
                    ('<b>Sex:</b> simulado do tema da semana.', ''),
                    ('<b>Sáb:</b> revisa só o que errou.', ''),
                    ('<b>Dom:</b> planeja a próxima semana.', '')], 'num')),
 dict(tipo='final', olho='MedQueen IA', t=80, titulo='Tudo isso num lugar só.', visual=queen_img(380, '16'), pe_final='medqueen.com.br',
      cta_titulo='Teste 7 dias grátis.', cta_texto='Explicação com a Queen IA, simulados, flashcards e caderno de erros. Acesse medqueen.com.br.', acao='medqueen.com.br'),
]
