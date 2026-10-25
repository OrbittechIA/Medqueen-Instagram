import os as _os; RAIZ = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys; sys.path.insert(0, RAIZ)
from reel_video import Reel
from reel_formatos import palavras, chat
# Formato CONVERSA COM A QUEEN. Conteúdo conferido em nefrologia básica: nefrótica (proteinúria > 3,5 g/dia, hipoalbuminemia, edema, hiperlipidemia); nefrítica (hematúria, hipertensão, oligúria, edema; proteinúria geralmente < 3,5 g/dia).
r = Reel('saida/rv05-chat-nefro', musica='trilha_anuncio_1.mp3')
r.cena(palavras('POV: prova de Nefro amanhã e você ainda confunde <em>nefrótica e nefrítica</em>.', fundo='claro', g=96, passo=0.22))
r.cena(chat([
    ('aluno', 'Me explica rápido nefrótica x nefrítica? Prova amanhã 😭'),
    ('queen', '<b>Nefrótica:</b> proteinúria acima de 3,5 g/dia, hipoalbuminemia, edema e hiperlipidemia.'),
    ('queen', '<b>Nefrítica:</b> hematúria, hipertensão, oligúria e edema. Proteinúria costuma ser menor.'),
    ('queen', 'Dica: nefr<b>Ó</b>tica lembra pr<b>O</b>teína. Nefr<b>Í</b>tica lembra <b>I</b>nflamação e sangue na urina.'),
    ('aluno', 'Salvou. Vira flashcard?'),
    ('queen', 'Vira sim. Um toque e já está no seu baralho 💜'),
], ritmo=1.3))
r.final('Aproveite os 7 dias de teste grátis.', 'Link na bio', texto='Pergunta pra Queen IA e transforma a resposta em flashcards.', dur=3.8, queen=False)
if __name__ == '__main__': r.gravar()
