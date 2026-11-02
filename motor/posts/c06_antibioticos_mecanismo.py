import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import lista, numeros, fluxo, nota, queen_img, balao
from conceito import cartoes, erro_vira_card, folha_prova, material_vira, trio, continua, plano_semana, resposta_queen
# Sáb 07/11 18:50, carrossel. Estudo (Farmacologia). Sem Queen IA.
# Conteúdo conferido: Goodman & Gilman e Katzung (mecanismos dos antimicrobianos).
SLUG = 'c06-antibioticos-mecanismo'
CARDS = [
 dict(tipo='capa', olho='Farmacologia', t=90, titulo='Antibiótico: <em>onde cada classe ataca.</em>',
      texto='O mapa que mais cai, em 6 cards.',
      visual=trio(itens=(('alvo', 'Parede celular'), ('repetir', 'Ribossomo 30S e 50S'), ('doc', 'DNA e folato')))),
 dict(olho='Parede celular', titulo='Beta-lactâmicos e vancomicina.',
      visual=lista([('<b>Beta-lactâmicos</b> (penicilinas, cefalosporinas, carbapenêmicos):', 'ligam as PBPs e travam a síntese da parede.'),
                    ('<b>Vancomicina:</b> liga o D-Ala-D-Ala.', 'Bloqueia a parede por outro caminho. Não é beta-lactâmico.')])),
 dict(olho='Ribossomo', titulo='30S ou 50S? <em>Decora em dupla.</em>', coluna=True,
      visual=numeros([('30S', 'aminoglicosídeos e tetraciclinas'), ('50S', 'macrolídeos, clindamicina, cloranfenicol, linezolida')])
             + nota('Todos travam a <b>síntese de proteína</b> da bactéria.')),
 dict(olho='DNA e folato', titulo='Quem mexe no material genético.',
      visual=lista([('<b>Quinolonas:</b> inibem DNA girase e topoisomerase IV.', ''),
                    ('<b>Sulfametoxazol e trimetoprima:</b> bloqueiam a síntese de folato.', 'Em duas etapas seguidas, por isso agem juntos.'),
                    ('<b>Rifampicina:</b> inibe a RNA polimerase.', ''),
                    ('<b>Metronidazol:</b> gera radicais que lesam o DNA.', 'Age em anaeróbios.')])),
 dict(olho='Pegadinhas', titulo='As que mais derrubam.',
      visual=lista([('Aminoglicosídeo não age em anaeróbio.', 'A entrada na bactéria depende de oxigênio.'),
                    ('Beta-lactamase não inativa vancomicina.', 'Ela não tem anel beta-lactâmico.'),
                    ('Tetraciclina e criança pequena:', 'mancha os dentes em formação.')], rosa=True)),
 dict(tipo='final', olho='Revisão ativa', t=74, titulo='Errou? <em>Vira flashcard.</em>',
      visual='<div style="zoom:.62">' + cartoes(pergunta='Aminoglicosídeos agem em qual subunidade do ribossomo?', resposta='30S, travando a síntese de proteína', area='Farmaco') + '</div>',
      pe_final='link na bio',
      cta_titulo='Aproveite os 7 dias de teste grátis.', cta_texto='Na MedQueen IA, o que você erra volta como flashcard e treino.', acao='Link na bio'),
]
