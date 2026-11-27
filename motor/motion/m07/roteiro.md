# Motion m07: "Sobe a aula e sai a questão" (seg 30/11, 18:50)

Formato: Reel vertical 1080x1920, 30 fps, uns 35 s. Fundo claro (gradiente lilás para creme, igual à capa). Nada de fundo escuro.
Material: pasta `no-celular/` (telas do app já dentro do celular, PNG com fundo transparente, na ordem 01 a 05), pasta `telas/` (as mesmas telas soltas, pra zoom com mais nitidez), `capa.png` (1080x1920).
Regra: a tela do app aparece sempre dentro do celular, reta e de frente. Zoom pode, mas a moldura do celular continua visível ou o zoom é curto e volta.
Música: 049_ambiente_tech_calma_79s da biblioteca (Drive > MedQueen IA > Biblioteca de músicas), cortada pra uns 35 s, fade de 1 s no fim, volume baixo e constante. Efeitos: woosh nas trocas de tela, mouse_click no "Enviar", notification quando aparece o resultado.
Texto na tela: fonte Plus Jakarta Sans ExtraBold, roxo #2A1460, palavra de destaque em gradiente roxo #7B3FE4 para rosa #E8488A. Tudo que importa entre y=240 e y=1680 (o grid corta 3:4).

| Tempo | Tela (no-celular) | O que acontece | Texto na tela |
|---|---|---|---|
| 0,0 a 0,5 s | capa.png | Capa parada (o capa_reel.py põe isso no fim; pode começar direto na cena 1) | |
| 0 a 3 s | 01-print_pdf | Celular entra de baixo com leve bounce. Zoom no card "Aula 7, Fisiologia renal.pdf, Pronto pra usar". Barra rosa se enchendo. | "Sobe o PDF da aula" |
| 3 a 4 s | 01-print_pdf | Círculo rosa no botão Enviar, click. | |
| 4 a 10 s | 02-print_aula | Whip pra direita. A tela rola devagar de cima pra baixo (usar `telas/02` dentro da moldura). Marca-texto amarelo em "Túbulo proximal: reabsorve cerca de 65% do sódio". | "A Queen resume a aula" |
| 10 a 16 s | 03-print_cai_na_prova | Zoom no quadro laranja "O que cai na prova". Marca-texto em "Furosemida pode causar hipocalemia". Chip rosa entrando de lado. | "e mostra o que cai na prova" / chip: "Direto do seu material" |
| 16 a 23 s | 04-print_simulado | Celular gira 90 graus rápido e volta (whip). Questão aparece; destaque na alternativa B (ADH) com círculo. | "Vira simulado na hora" |
| 23 a 28 s | 05-print_resultado | Números entram com pop: 8/10, 80%. Tremida curta no 80%. | "E você vê onde errou" |
| 28 a 35 s | final | Logo MedQueen IA no topo, Queen pose 12 (apontando pra baixo, `www/marca/queen-poses/12-apontando-baixo.png`) no meio, botão "Link na bio" pulsando. | "Aproveite os 7 dias de teste grátis." |

Legenda pro post (colar no Instagram):
Sobe a aula e sai a questão 📄➡️✅

Você manda o PDF da aula. A Queen resume, aponta o que cai na prova e monta o simulado ali mesmo. No fim, você vê exatamente onde errou.

Sem copiar e colar, sem perder tempo montando material.

👑 A MedQueen IA transforma a sua aula em questões e revisão.

💜 Aproveite os 7 dias de teste grátis. Link na bio.

Depois de editado: rodar `python3 motor/capa_reel.py video.mp4 motor/motion/m07/capa.png saida.mp4`, conferir o quadro 0 e subir no Best Content por Nova Pauta (Upload, até 10 MB), só Instagram, seg 30/11 18:50.
