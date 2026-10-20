import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from carrossel import tablet, lista, numeros, fluxo, nota
# Conteúdo conferido em livro-texto de bioquímica (Lehninger, cap. ciclo do ácido cítrico) e na resposta da Queen IA.
SLUG = 's01-krebs'
CARDS = [
    dict(tipo='capa', olho='Bioquímica', t=92,
         titulo='Ciclo de Krebs: <em>o que cai na prova</em> em 8 cards.',
         texto='Salva agora e revisa na semana da prova.',
         visual=tablet('desk-ia-krebs-1.png', w=780, crop=(660, 80, 640, 480), dest=[(695, 138, 405, 42)])),
    dict(olho='Onde acontece', titulo='Matriz mitocondrial. Com uma exceção.',
         visual=lista([('<b>Localização:</b> matriz da mitocôndria.', ''),
                       ('<b>Exceção:</b> a succinato desidrogenase fica na membrana interna.', 'Ela também é o complexo II da cadeia respiratória.'),
                       ('<b>Oxigênio:</b> o ciclo não usa O₂ diretamente.', 'Mas para sem ele, porque NADH e FADH₂ precisam ser reoxidados na cadeia.')])),
    dict(olho='Porta de entrada', titulo='Antes do ciclo: piruvato vira acetil‑CoA.',
         texto='Reação da <b>piruvato desidrogenase</b>, na mitocôndria. Ela liga a glicólise ao ciclo, mas não faz parte dele.',
         visual=nota('Piruvato + CoA + NAD⁺ → <b>acetil‑CoA</b> + CO₂ + NADH')),
    dict(olho='As 8 etapas', titulo='Acetil‑CoA (2C) + oxaloacetato (4C) = citrato (6C).', t=70, coluna=True,
         visual=fluxo(['Citrato', 'Isocitrato', ('α‑cetoglutarato', 'NADH + CO₂'), ('Succinil‑CoA', 'NADH + CO₂'),
                       ('Succinato', 'GTP'), ('Fumarato', 'FADH₂'), 'Malato', ('Oxaloacetato', 'NADH')])
                + nota('Mnemônico: <b>C I A S S F M O</b>. O oxaloacetato volta e recebe o próximo acetil‑CoA.')),
    dict(olho='Saldo', titulo='Por volta do ciclo, sai isto:', coluna=True,
         visual=numeros([('3', 'NADH'), ('1', 'FADH₂'), ('1', 'GTP'), ('2', 'CO₂')])
                + nota('Por glicose são <b>2 voltas</b>: dobra tudo. Cada acetil‑CoA rende cerca de <b>10 ATP</b> depois da cadeia respiratória.')),
    dict(olho='Regulação', titulo='Quem acelera e quem freia.',
         visual=lista([('<b>Isocitrato desidrogenase:</b> principal ponto de controle.', ''),
                       ('<b>Ativam:</b> ADP e Ca²⁺.', 'Sinal de que a célula precisa de energia.'),
                       ('<b>Inibem:</b> ATP e NADH.', 'Energia sobrando, o ciclo desacelera.'),
                       ('<b>Também regulam:</b> citrato sintase e α‑cetoglutarato desidrogenase.', '')])),
    dict(olho='Pegadinhas', titulo='As que mais derrubam na prova.',
         visual=lista([('O ciclo <b>não gera</b> a maior parte do ATP.', 'Ela vem da cadeia respiratória, reoxidando NADH e FADH₂.'),
                       ('Só uma etapa gera GTP direto:', 'succinil‑CoA → succinato.'),
                       ('É uma via <b>anfibólica</b>.', 'Degrada e também fornece intermediários para síntese.')], rosa=True)),
    dict(tipo='final', olho='Revisão ativa', t=72,
         titulo='Não fixou? Vira treino.',
         visual=tablet('desk-criar-material-b.png', w=700, h=330, crop=(40, 640, 560, 264), dest=[(54, 700, 516, 140)]),
         cta_titulo='Aproveite os 7 dias de teste grátis.',
         cta_texto='Na MedQueen IA, a explicação da Queen IA vira flashcards ou questões em um toque.',
         acao='Link na bio', pe_final='link na bio'),
]
