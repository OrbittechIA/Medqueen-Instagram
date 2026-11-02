import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import lista, numeros, fluxo, nota, queen_img, balao
from conceito import cartoes, erro_vira_card, folha_prova, material_vira, trio, continua, plano_semana, resposta_queen
# Ter 03/11 18:50, carrossel. Estudo (Hematologia). Sem Queen IA.
# Conteúdo conferido: Harrison (Anemia e policitemia; anemias ferropriva e megaloblástica). VCM normal 80 a 100 fL.
SLUG = 'c04-anemias-vcm'
CARDS = [
 dict(tipo='capa', olho='Hematologia', t=92, titulo='Anemia na prova: <em>começa pelo VCM.</em>',
      texto='O tamanho da hemácia já corta metade das hipóteses.',
      visual='<style>.nums strong{white-space:nowrap;font-size:76px}</style>' + numeros([('&lt;80', 'microcítica'), ('80 a 100', 'normocítica'), ('&gt;100', 'macrocítica')])),
 dict(olho='Microcítica · VCM abaixo de 80 fL', titulo='Lembra de <em>TAILS</em>.', coluna=True,
      visual=lista([('<b>T</b>alassemia', ''), ('<b>A</b>nemia de doença crônica', 'Às vezes microcítica, mais vezes normocítica.'),
                    ('<b>I</b>ron: deficiência de ferro', 'A causa mais comum de todas.'), ('<b>L</b>ead: intoxicação por chumbo', ''),
                    ('<b>S</b>ideroblástica', '')])),
 dict(olho='Normocítica · VCM 80 a 100 fL', titulo='Aqui quem decide é o <em>reticulócito</em>.',
      visual=lista([('<b>Reticulócito alto:</b> a medula está respondendo.', 'Hemorragia aguda ou hemólise.'),
                    ('<b>Reticulócito baixo:</b> a medula não está produzindo.', 'Doença crônica, doença renal crônica, aplasia.')])),
 dict(olho='Macrocítica · VCM acima de 100 fL', titulo='Megaloblástica ou não?',
      visual=lista([('<b>Megaloblástica:</b> deficiência de B12 ou de folato.', 'Neutrófilos hipersegmentados no sangue periférico.'),
                    ('<b>Não megaloblástica:</b> álcool, hepatopatia, hipotireoidismo.', 'Reticulocitose também aumenta o VCM.')])),
 dict(olho='Pegadinhas', titulo='As que mais derrubam.',
      visual=lista([('B12 dá sintoma <b>neurológico</b>. Folato, não.', 'Repor só folato na falta de B12 pode piorar o quadro neurológico.'),
                    ('Ferritina baixa confirma ferropenia.', 'Mas ela sobe na inflamação: ferritina normal não exclui na doença crônica.'),
                    ('Talassemia minor: microcitose com ferro normal.', '')], rosa=True)),
 dict(tipo='final', olho='Revisão ativa', t=74, titulo='Errou? <em>Vira flashcard.</em>',
      visual='<div style="zoom:.62">' + cartoes(pergunta='VCM de 72 fL e ferritina baixa: qual anemia?', resposta='Ferropriva: microcítica com estoque de ferro baixo', area='Hemato') + '</div>',
      pe_final='link na bio',
      cta_titulo='Aproveite os 7 dias de teste grátis.', cta_texto='Na MedQueen IA, o que você erra volta como flashcard e treino.', acao='Link na bio'),
]
