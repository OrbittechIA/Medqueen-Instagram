# Motor do Instagram da MedQueen IA (@medqueen.ia)

> **12/11/2026: produto liberado no conteúdo.** Tela do app pode aparecer em post, carrossel, story e Reel, sempre gerada pelo HyperFrames e sempre dentro de celular, tablet, computador ou laptop (regra completa na seção 1). Nunca print solto.

Manual da tarefa semanal. Quem roda isto é uma sessão nova do Claude, sem memória da conversa anterior. Siga na ordem.

> **MUDANÇA DE 03/11/2026 (decisão do Matheus): o TryPost saiu. Feed e stories agora são CRIADOS e AGENDADOS no Best Content** (`social.bestcontent.ai`, plano Max, logado no Chrome principal do Matheus, deviceId `0ffabed5-99a7-491f-b5ee-48a5dbdcab04`). O motor deste repositório continua só para os **Reels em vídeo** (`reel_video.py`), que sobem prontos no Best Content. O passo a passo novo está na **seção 7B**; as seções 5 a 7 sobre renderizar card e TryPost ficam como referência de conteúdo e regra, não de ferramenta. A seção 1 (regras) continua valendo inteira.
> **Aprovação:** o Claude cria, agenda tudo com a legenda no nosso padrão e DEPOIS manda o resumo pro Matheus. Se ele não fizer nada, está aprovado. Se ele reprovar algo, diz qual post editar.
> **Se cair a luz, o PC dormir ou o Chrome desconectar:** pare, avise, e quando ele religar continue de onde parou (confira no Calendário do Best Content o que já está agendado antes de criar de novo).

> **SEMANA NOVA DESDE 09/11/2026 (Matheus, vale acima das seções 3 e 5): feed = 2 motions do produto + 5 carrosséis; 1 Reel de questão por semana.**
> - **Seg e sex 18:50: motion do produto** (formato Reel, 30 s a 1 min, HyperFrames em `motor/motion/`), uma funcionalidade ou um discurso de venda. Sobe pronto no Best Content (Calendário > Nova Pauta > Upload). **Vídeo de 60 s com HyperFrames é só pra esses dias; mas tela do produto (gerada no HyperFrames, dentro de aparelho) pode entrar em qualquer post desde 12/11.**
> - **Ter, qua, qui, sáb e dom 18:50: carrossel feito no Best Content** (seção 7B). **Post único acabou.**
> - **Qui 12:30: 1 Reel de questão por semana** (quiz de prova, "questãozinha", com `reel_video.py`/`reel_formatos.py` como antes), sobe no Best Content igual aos outros Reels. Terça 12:30 não tem mais Reel. Os outros formatos de Reel curto (mito ou verdade, conversa, lista) ficam no banco e só entram se o Matheus pedir.
> - **Stories iguais:** 3 por dia no Best Content (11:50, 15:50, 21:20; seg 13:50, 15:50, 21:20).
> - **Total: 7 feed + 1 Reel de questão + 21 stories = 29 horários.**
> - **Música (biblioteca de 100 faixas no Drive, nunca as trilhas antigas):** aprovadas 050, 048 (motion) e 029 (quiz); reprovadas 078, 080 e 022. Linha certa: tech minimalista, eletrônica tranquila. Não repetir faixa na mesma semana; mixar a cerca de -14 LUFS, pico abaixo de -1,5 dBTP, efeitos por cima.
> - **Motion:** referência aprovada `posts/2026-11-09-m01-conheca-medqueen`. Estilo: telas reais do app em celular, tablet ou computador (variar o aparelho), zoom no ponto que importa, edição por cima (legenda de destaque, marca-texto, círculo, chips, whip, tremida). Vocabulário em `medqueen/instagram/direcao-de-edicao-motion.md` no projeto. Motor: `motor/motion/m02/` (index.html com `render(t)` + `render.py prev|full`, Chromium invisível + FFmpeg, efeitos de `www/som/efeitos`). Copie a pasta, troque prints e textos, renderize, confira 15 quadros. **Print do produto liberado (Matheus, 08/11/2026)** em motion e Reel de produto; a regra "sem print" da seção 1 não vale pra eles. Telas do produto: sempre do HyperFrames (regra de 12/11 na seção 1); os PNGs antigos de `motor/prints` (tirados do Chrome) não entram mais em conteúdo novo. O Best Content aceita upload de até 10 MB pelo file_upload: se o mp4 passar disso, recomprimir com ffmpeg (crf maior) mantendo 1080x1920.

> **NÍVEL DO CONTEÚDO: SUBIR UM DEGRAU (feedback que o Matheus recebeu em 09/11/2026, vale a partir da semana de 16/11).** Visual, identidade e estilo estão aprovados ("id visual fera"). O problema é o nível: questão de definição, "teste rápido" de decoreba e post informativo raso são conteúdo de nível baixo. A partir de agora:
> - **Pesquisa antes da pauta (obrigatória, toda semana):** vasculhar onde estudante de Medicina discute e pergunta, e anotar os temas e dúvidas com mais busca, votos ou comentários. **Reddit sempre (Matheus, 09/11/2026), pelo Chrome dele:** abrir o Reddit no Chrome principal e ir buscando e lendo lá, começando por https://www.reddit.com/r/MedicinaBrasil/ (ordenar por Top da semana e do mês e ler os comentários) e seguindo pelas outras comunidades de Medicina e residência que aparecerem (busca do Reddit por medicina, residência, internato, Enamed, Revalida; r/medicalschool e r/medicine pra tema global). Anotar o nome de cada comunidade boa no historico.md pra próxima semana. Outras fontes: comentários de questões e de posts de cursinhos de residência (Estratégia MED, Medway, Sanar, QConcursos), comentários de perfis grandes de Medicina no Instagram e TikTok, Google Trends e "as pessoas também perguntam". Reddit só pelo Chrome; o resto WebSearch primeiro e, se bloquear, pelo Chrome. Só ler: nunca postar, comentar, votar nem entrar em comunidade. Anotar no historico.md, na semana nova, a lista do que foi achado com link (de 5 a 10 itens) e qual post saiu de cada um. Não inventar número de votos ou comentários: só o que a página mostra.
> - **O que é "um degrau acima":** caso clínico curto com raciocínio (o que pensar primeiro, o que descarta, a pegadinha), questão no estilo de prova de residência (ENARE, USP, Unifesp, SUS-SP) com o porquê de cada alternativa errada, "o erro que todo mundo comete" em tema que cai, diferencial de quadro parecido, mudança de diretriz recente explicada (o que mudou e por que cai), interpretação (ECG, gasometria, exame de imagem descrito em texto, laboratório) passo a passo. Fugir de: definição solta, tríade decorada sem contexto, "você sabia?" genérico, dica de estudo óbvia.
> - **Quiz e stories de teste:** a pergunta vira mini caso clínico (2 ou 3 linhas de paciente) com alternativas plausíveis; a resposta explica o raciocínio e a pegadinha, não só a letra certa.
> - Continua valendo: dado médico conferido em fonte confiável (diretriz, sociedade, livro-texto, citada na legenda quando for diretriz), conteúdo de estudo e nunca orientação de conduta pra paciente, e todas as regras da seção 1.

Estratégia completa: `medqueen/instagram/brain-instagram.md` e `medqueen/instagram/estrategia-alcance-organico.md` no projeto "MedQueen Growth" do claude.ai (se a sessão tiver acesso ao projeto, leia antes). Este manual tem o necessário para rodar sem o projeto.

## 1. Regras que nunca mudam

- Português do Brasil, direto, adulto. Chama o público de "Estudante de Medicina" ou pelo momento (prova, residência, internato).
- **Nunca usar travessão (U+2014) nem meia-risca (U+2013)** em card, legenda, story ou texto alternativo. Hífen só em palavra composta. O passo 6 tem verificador.
- Sem "não é X, é Y", sem emoji como marcador de lista nos cards, sem frase de efeito vazia, sem "Concorda?".
- **PRODUTO NO CONTEÚDO LIBERADO (regra do Matheus, 12/11/2026; substitui o "sem print" de 28/10).** Post, carrossel, story e Reel podem mostrar partes reais do produto (conversa com a Queen IA, simulado, resultado, flashcards, PDF virando material, caderno de erros). Só duas regras, sem exceção:
  1. **A tela sai do HyperFrames**, nunca de print solto do Chrome nem de tela inventada pelo Best Content. HyperFrames aqui = tela do app montada em código com o visual real do produto (tokens, fontes e componentes do repositório OrbittechIA/av1-medicina-unibh-builder: tela da Queen em `app/app/mentora`, flashcards em `components/chat-flashcards.tsx`, resposta em `components/markdown.tsx`) e renderizada no Chromium invisível. Bases prontas: o motor de motion (`motor/motion/m02/`, `tiktok/motion/motor/` com `render.js` em modo preview) e o banco `tiktok/carrossel/telas/` (aula, cai na prova, flashcards, simulado, resultado, PDF). Tela nova: copiar uma base, trocar o texto (pergunta pra Queen, questão do simulado, nota) e renderizar em PNG. Conteúdo médico da tela conferido como qualquer card; nada de função que o app não tem, número inventado ou nome de aluno real.
  2. **A tela nunca fica solta.** Sempre DENTRO de um aparelho: celular, tablet, tela de computador ou laptop (variar o aparelho na semana). O aparelho é montado em código junto com a tela (atalho pronto: `python3 telas/aparelho.py <tela.png> celular|tablet|laptop <saida.png>`, que recusa tela no formato errado: tela de celular só vai em celular; pra tablet renderize a tela do HyperFrames em 4:3 e pra laptop em 16:10, com o layout de computador do app) (moldura em CSS no mesmo HTML, como o `.tablet` e o `.laptop` do `m02/index.html`) e sai como um PNG só, com fundo transparente. Assim a tela fica sempre de frente, reta e legível; nada de tela nas costas do laptop, de cabeça pra baixo, espelhada ou cortada. No Best Content, esse PNG entra por "Adicionar imagem" > enviar arquivo, com o prompt de uso: "usar esta imagem exatamente como está: não redesenhar, não alterar o texto da tela, não girar; só posicionar e dimensionar no slide". Pode estar na mão da Queen IA (ela segurando o celular ou o tablet) ou apoiado numa mesa de estudo; mão ou pessoa gerada por IA continua proibida.
  **Conferência antes de agendar:** abrir a arte final e checar que a tela está de frente pra câmera, inteira, legível e igual ao PNG do HyperFrames (texto sem letra trocada). Se o Best Content mexeu na tela, pedir no chat "a tela do aparelho deve ser idêntica à imagem anexada" e, se não resolver em 2 tentativas, montar o slide inteiro no nosso motor e subir como imagem pronta. Tela em dúvida não vai pro ar.
- **Resposta da Queen IA nunca curta (Matheus, 29/10/2026):** resposta de uma linha faz a IA parecer pobre; textão ninguém lê. Quando a Queen responde num post, story ou Reel, use `resposta_queen()` de `conceito.py`: pergunta do aluno, resposta em 3 ou 4 blocos com rótulo (onde, saldo, pontos de controle, pegadinha), o último cortado com degradê e a faixa "Resposta completa na MedQueen IA" + "7 dias grátis". No chat do Reel, a mesma lógica: 2 ou 3 mensagens com conteúdo de verdade antes do gancho de "resposta completa".
- **Visual conceitual pode ser o post inteiro:** o par de cartões de flashcard (`cartoes()`) e afins funcionam sozinhos como post de feed, não só dentro de story.
- **Fundo escuro é proibido (regra do Matheus, 25/10/2026), em tudo: feed, stories e Reels.** Nunca fundo preto, azul-marinho ou roxo escuro dominando. O roxo só em detalhe, título e cartão final. No `reel_video.py` a `Cena` já força fundo claro.
- **Variar a cor de fundo (pedido do Matheus em 25/10/2026):** todo fundo é um gradiente que sai de um roxo bem claro e termina em creme (atualizado em 25/10/2026: "post claro, mas sem mesmice"; nunca deixar o roxo dominar). O motor sorteia uma variação por card, com ângulo e cor de acento diferentes (`lavanda`, `creme`, `lilas`, `menta`, `rosa`, `ceu`, `pessego`, `branco`), estável por post, e muda de card para card dentro do mesmo carrossel. Para forçar um tema num card: `fundo='menta'`. Confira na folha de revisão se a semana não ficou toda da mesma cor.
- **Print nunca solto (regra do Matheus).** Todo print entra dentro de `tablet()`, `celular()` ou `pronto()` e, sempre que fizer sentido, com destaque (`dest`) ou lupa (`lupa`) no ponto que importa.
- **Sem pessoa gerada por IA.** No lugar de gente, use a **Queen IA**, a personagem oficial e a cara do produto (ilustração, `www/marca/queen_ia_recorte.png` corpo inteiro e `www/marca/queen-ia-bust-master-384.png` busto, com o símbolo da MedQueen no jaleco). Decisão do Matheus em 24/10/2026: pode usar à vontade, em qualquer formato (capa, card do meio, post único, story, fechamento), inclusive como o visual herói onde os carrosséis de referência usavam uma pessoa. Não alterar o desenho dela. **Poses (pedido do Matheus em 25/10/2026: não usar a mesma imagem em tudo):** use o banco de 50 poses em `www/marca/queen-poses/` (catálogo com "quando usar" em `www/marca/queen-poses/LEIA-ME.md`; no motor, `queen_img(altura, '07')` ou pelo nome). Escolha a pose que conversa com o texto do card (apontando para o título, segurando tablet com print, pensando em card de pergunta, comemorando em resultado) e não repita pose em posts seguidos nem dentro da mesma semana. Pose nova só se nenhuma das 50 servir, sempre a partir do retrato oficial. **Dosar (pedido do Matheus em 24/10/2026): ela não pode aparecer em tudo.** No feed, a Queen IA aparece em 3 ou 4 dos 7 posts da semana, de preferência alternando os dias (nunca 3 dias seguidos). Nos stories, exatamente 1 dos 3 de cada dia (7 por semana). O resto vai com print do app no tablet ou celular, diagrama, comparação, número grande ou só tipografia.
- Claims proibidos: "única", "a melhor", "a maior", "10x", "não alucina", "100% preciso", "te aprova", "garante aprovação", promessa de nota, urgência inventada, plano ou benefício que não existe, citar concorrente pelo nome, "a Queen IA sabe seu período/erros" (o produto ainda pede essas infos). OSCE fora como tema de post até o Matheus liberar.
- O que pode liderar: o material vira resumo, flashcards, simulado; o erro vira explicação e próxima revisão; simulado por tema ou pelo material; caderno de erros por área; a resposta da Queen IA vira resumo, flashcards, mapa ou questões; memória visível.
- **CTA, um só por post, sempre o mesmo (decisão do Matheus, 20/10/2026): "Aproveite os 7 dias de teste grátis. Link na bio."** Vale para card final, fim de reel e legenda. Sem CTA de comentário. "Salva pra revisar" pode aparecer só como apoio no texto, nunca como a chamada.
- **Nome e logo:** o produto se chama **MedQueen IA**. O motor já desenha o logo com o selo "IA" (`LOGO_IA` em `carrossel.py`, e em `reel.py`); PNG em `www/marca/medqueen-ia-logo-horizontal.png`. A Queen IA dentro do app ainda tem um broche de coroa; isso pode aparecer nos prints, o Gustavo troca depois.
- **Conteúdo médico correto.** Todo dado de estudo é conferido em fonte confiável (livro-texto, diretriz, sociedade médica) antes de ir para o card. Na dúvida, corta o dado. É conteúdo de estudo, nunca orientação de conduta para paciente.
- Notícia de medicina ou de IA: só com fonte oficial ou veículo confiável e data; fonte no fim da legenda. Nada de notícia sem fonte.
- Reel sem música da biblioteca (o TryPost não põe música nesta conta) e entendível sem som. Trilha só se o Matheus escolher (regra dele: o Claude não escolhe música sozinho).

## 2. Preparar a sessão

1. Anexar o repositório com permissão de envio: ferramenta `add_repo` com owner `OrbittechIA`, repo `Medqueen-Instagram`, access `push`. Clonar com o comando que ela devolver.
2. Conferir: `which ffmpeg`, `python3 -c "import playwright, PIL"`. O Chromium já vem instalado (não rodar `playwright install`).
3. Trabalhar dentro de `motor/`. Fontes em `motor/www/fonts` (Plus Jakarta Sans e Source Sans 3), logo e Queen em `motor/www/marca`, prints do app em `motor/prints`.
4. Ler `motor/historico.md` inteiro: o que já saiu (não repetir tema nem gancho) e os números das semanas anteriores.

## 3. A semana (horário de Brasília, UTC-3; o TryPost recebe em UTC)

A tarefa roda **segunda 00:01** e produz a semana que começa **nesse mesmo dia** (segunda a domingo).

| Dia | Feed 18:50 (21:50Z) | Story 1 | Story 2 | Story 3 |
|---|---|---|---|---|
| Seg | **motion do produto** | 13:50 | 15:50 | 21:20 |
| Ter | **carrossel** | 11:50 | 15:50 | 21:20 |
| Qua | **carrossel** | 11:50 | 15:50 | 21:20 |
| Qui | **carrossel** + **Reel de questão 12:30 (15:30Z)** | 11:50 | 15:50 | 21:20 |
| Sex | **motion do produto** | 11:50 | 15:50 | 21:20 |
| Sáb | **carrossel** | 11:50 | 15:50 | 21:20 |
| Dom | **carrossel** | 11:50 | 15:50 | 21:20 |

Total: **7 feed (2 motions + 5 carrosséis) + 1 Reel de questão + 21 stories = 29** (decisão do Matheus em 09/11/2026; antes eram post único seg/qua/sex/dom e 2 Reels ter e qui). Vídeo do fundador (qua e sex 12:30) só quando o Matheus mandar o vídeo gravado. Segunda nada sai antes das 13:50.

Stories: todo dia o story das 21:20 anuncia o post novo do feed (`imagem('saida/<post>/01.png')`). Os outros alternam: teste rápido (pergunta) com a resposta no story seguinte, dica da Queen IA, tela do produto com destaque, frase curta. Story pela API sai sem texto e sem figurinha: o texto vai dentro da imagem.

## 4. Pauta

**Antes de tudo, veja se a semana já está pronta:** desde 03/11/2026, olhar o **Calendário do Best Content** (quantos "Agendado" na semana alvo). Referência antiga: `list-posts-tool` com `channels=["01a03943-aa85-72df-bb05-0dc788a5e9d9"]` e `status=scheduled` (o resultado é grande: salvar em arquivo e ler com `jq`). Se já houver 30 agendados (7 feed + 2 reels em vídeo + 21 stories) entre segunda 00:00 e domingo 23:59 da semana alvo, não produza nada: só meça (seção 8), atualize o histórico e avise. Se tiver alguns, produza só os horários que faltam.

Linhas (proporção inicial, hipótese a ajustar com as métricas): Estudo ~40% · Notícia de medicina ~25% · Novidade de IA ~15% · Produto ~15% · Marca ~5%. Com 7 feeds por semana (desde 09/11), a regra prática é: **2 motions de Produto (seg e sex) + 5 carrosséis: 3 Estudo + 1 Notícia ou IA + 1 Marca**. Notícia e marca também vão em carrossel (post único acabou em 09/11).

Banco de ideias (risque no histórico o que usar, acrescente ideias novas no fim):

Estudo (resumo ou comparativo com gancho de prova, selo da área, "salva pra revisar")
- Glicólise: as 10 etapas e as 3 irreversíveis.
- Cadeia respiratória: complexos I a IV e o que cada inibidor bloqueia.
- Insuficiência cardíaca: fração de ejeção reduzida x preservada.
- Hipotireoidismo x hipertireoidismo: sinais lado a lado.
- Síndrome nefrótica x nefrítica.
- Sopros cardíacos: sistólicos x diastólicos.
- Antibióticos: mecanismo de ação por classe.
- Distúrbios ácido-base: o passo a passo da gasometria.
- Anemias: microcítica, normocítica e macrocítica.
- Marcos do desenvolvimento infantil.

Produto (mecanismo real, sempre com print no tablet/celular e destaque)
- A resposta da Queen IA vira resumo, flashcards, mapa ou questões (print `desk-criar-material-b.png`).
- Simulado pelo seu material: o PDF da aula vira questões.
- Tela Hoje: a próxima tarefa já está ali (print `desk-hoje.png`).
- Flashcards dos seus erros (print `desk-flashcards.png`).
- Memória de estudo visível e controlável.

Notícia de medicina / Novidade de IA: pesquisar na semana (WebSearch) com fonte oficial: ENAMED, residência, MEC, CFM, editais, diretrizes novas; estudos e lançamentos de IA aplicada a medicina e estudo.

Já usado: ver `historico.md`.

## 5. Produzir

Copie um arquivo de `motor/posts/` como base, troque o texto, rode.

**Carrossel** (1080x1350, 6 a 9 cards): base `posts/s01_krebs.py` (estudo) e `posts/p01_erro_vira_treino.py` (produto). Rodar `python3 carrossel.py posts/<arquivo>.py` (sai em `saida/<SLUG>/01.png...`).
- Card `capa`: gancho de até 10 palavras, com o assunto no texto e um visual real. Nunca começar com "MedQueen".
- Cards do meio: um argumento por card, até 40 palavras. Ajudantes: `lista(itens, 'num'|'check', rosa=)`, `numeros([(valor, rótulo)])`, `fluxo([...])`, `nota(texto)`, `balao(texto)`, `queen_img(h)`.
- Prints: `tablet(img, w, h, crop=(x,y,w,h), dest=[(x,y,w,h)], lupa=(x,y,raio,cx,cy,aumento))`, `celular(...)` (para print de tela de celular sem moldura), `pronto(img, h, dest, lupa)` (para print que já vem com moldura, como `cel-caderno-erros.png`). Coordenadas de `crop`, `dest` e `lupa` em pixels da imagem do print.
- Card `final`: `cta_titulo`, `cta_texto`, `acao` (botão) e `pe_final` (texto do rodapé: "salva pra revisar" ou "link na bio").
- `coluna=True` empilha dois visuais (ex.: fluxo + nota). `<em>` no título pinta de roxo com grifo rosa. Use `‑` (hífen que não quebra) em palavras como acetil‑CoA no título.

**Post único** (ACABOU em 09/11/2026; fica só como referência) (1 imagem 1080x1350): base `posts/u00_modelo_post_unico.py` (é só modelo, não publicar). Spec com um card só; o motor tira o contador e a barra sozinho. Uma ideia só: título grande (até 8 palavras) com `<em>` na palavra-chave, uma linha de apoio e um visual forte (print no tablet/celular com destaque, comparação lado a lado, número grande ou diagrama). `pe_final` curto, ex.: "7 dias grátis · link na bio" ou "salva pra revisar".

**Padrão visual de referência** (dois carrosséis feitos à mão que o Matheus mandou em 23/10/2026: https://www.instagram.com/p/DctLpAtnFyI/ e https://www.instagram.com/p/DcecNXbn7la/). Não copiar, chegar perto do nível:
- Título enorme, ocupando cerca de 1/3 do card, no máximo 2 cores (roxo escuro + rosa, ou palavra-chave em degradê roxo-rosa), com traço/grifo rosa embaixo da palavra-chave. Pouquíssimo texto por card.
- Cada card tem UM visual herói grande: celular ou tablet com a tela real do app, mapa mental, diagrama com ícones em cartões ligados por linhas com bolinhas, comparação "material bruto → o que a MedQueen gera" com seta.
- Fundo lavanda claro com degradê suave, brilhos (estrelinhas de 4 pontas) e traço fino de ícones médicos ao fundo (estetoscópio, cruz, DNA) bem apagados. Cartões brancos com sombra suave e cantos arredondados.
- Logo sempre presente; "passe para o lado →" no canto inferior direito nos cards do meio; o último card com chamada "link na bio" em botão.
- Narrativa: cada card avança uma ideia (problema → virada → mecanismo → resultado → chamada), não lista solta.
- O que NÃO herdar: as pessoas desses carrosséis são geradas por IA. Onde eles usam uma pessoa (segurando tablet, apontando para a tela), use a Queen IA oficial no lugar.

**Reel em vídeo** (decisão do Matheus em 24/10/2026: pelo menos 2 por semana, terça e quinta às 12:30, além do feed das 18:50): motor `reel_video.py`, bases `posts/rv01_simulado_semana_de_prova.py` e `posts/rv02_proxima_tarefa_e_queen.py`. Rodar `python3 posts/rvNN_<tema>.py` (sai em `saida/<pasta>/reel.mp4` e `reel-capa.jpg`, uns 2 a 3 minutos).
- **VARIAR O FORMATO (regra do Matheus, 24/10/2026: "não é pra fazer todo Reels assim, foi só um exemplo").** Os 2 Reels da semana têm que ser de formatos diferentes, e o mesmo formato não repete em semanas seguidas no mesmo dia. A demonstração de produto em telas (abaixo) entra no máximo 1 vez a cada 2 semanas. Catálogo (funções em `reel_formatos.py`, exemplos prontos em `posts/rv03..rv05`), baseado no que mais funciona em Reel sem rosto em 2026 (quiz com pausa antes da resposta, POV de situação que todo mundo vive, mini-aula de uma ideia só, série numerada, antes e depois, mito ou verdade):
  1. **Quiz de prova** (`quiz`, 12 a 18 s): pergunta + 4 alternativas + contagem 3, 2, 1 + resposta verde + explicação de 1 linha. Legenda pede "comenta sua letra antes de ver". Exemplo `rv03_quiz_triades.py`.
  2. **Mito ou verdade** (`palavras` de gancho + 3x `mito_verdade`, 20 a 28 s). Exemplo `rv04_mito_verdade_estudo.py`.
  3. **Conversa com a Queen IA** (`palavras` com POV + `chat`, 20 a 30 s): dúvida real de prova respondida mensagem a mensagem, termina virando flashcard. Exemplo `rv05_chat_nefro.py`.
  4. **POV / situação que todo estudante vive** (`palavras` com "POV: ..." + 2 ou 3 cenas curtas, 8 a 15 s): feito para ser enviado por direct a um colega.
  5. **Lista "3 sinais de que..." / "3 erros que..."** (`lista`, 12 a 18 s).
  6. **Antes x depois** (`antes_depois`): como estudava x como estuda com a MedQueen IA (10 a 15 s).
  7. **Série numerada** (`episodio` + quiz ou mini-aula): "Pegadinha de prova #N", "Tríades que caem #N". Repetir a mesma série toda semana cria hábito; manter a numeração no histórico.
  8. **Mini-aula em 20 segundos** (`palavras` + `lista` ou uma tela do app): um conceito só, com mnemônico.
  9. **Demonstração de produto em telas** (Cena com `aparelho`, como `rv01`/`rv02`).
  Cartão final curto (3 a 4 s) com a chamada dos 7 dias; com ou sem a Queen conforme o rodízio dela. Todo conteúdo médico conferido e com a fonte num comentário no spec.
  **Prontos e agendados:** `rv03` quiz (ter 03/11 12:30) e `rv04` mito ou verdade (qui 05/11 12:30). **Pronto, ainda não agendado:** `posts/banco-rv05-chat-nefro/` (conversa com a Queen sobre nefrótica x nefrítica): usar na semana de 09/11 (ter ou qui) e só produzir 1 Reel novo naquela semana.
- Conceito do formato de demonstração (referência: vídeo da Orbyt para advogados que o Matheus mandou): roteiro de 35 a 45 s em cenas curtas. Abre com 2 ou 3 cenas escuras de dor (`escuro=True`, uma frase grande cada, 3 s), vira para o claro com a solução, mostra o produto funcionando em telas reais e fecha com o cartão "Aproveite os 7 dias de teste grátis." + "Link na bio".
- Cenas de produto: `aparelho='tablet'` (print de computador, com `zoom` para aproximar uma parte), `'celular'` (print de tela de celular sem moldura) ou `'pronto'` (print que já vem com moldura de iPhone, ex.: `cel-ia-krebs.png`, `cel-novo-simulado.png`, `cel-caderno-erros.png`; use `lupas` para ampliar um pedaço). `destaques` = caixa rosa no ponto que importa. `selos` = itens que vão aparecendo embaixo. `balao`/`queen` para a Queen IA.
- Som: música só de fundo, baixa (o motor já põe em -18 dB com fade). Trilhas em `www/som/musica/`; a escolha da trilha é do Matheus (regra de `producao-de-video.md`): use a que ele aprovou por último (em 24/10/2026, `trilha_anuncio_1.mp3` foi a usada nos dois primeiros, aguardando ele confirmar) e nunca trilha com voz. Efeitos em `www/som/efeitos/` (woosh_1, woosh_2, deep_woosh, mouse_click, notification, keyboard_typing, toggle, digital_loading, glitch_counter, camera_shutter, hit, metallic_rise, boom, downer): woosh na troca de cena, clique quando o destaque acende, toggle em cada selo, notification quando algo aparece. Sem exagero: 2 a 4 efeitos por cena, nunca efeito de meme.
- Queen IA não precisa ser animada; entra parada (imagem oficial) no cartão final ou num balão.
- Conferir antes de publicar: 15 quadros em folha (`ffmpeg -ss`) abertos com Read, e `volumedetect` (tem que ter áudio; pico abaixo de -1 dB).
- Publicar: copiar `reel.mp4` e `reel-capa.jpg` para `posts/AAAA-MM-DD-<slug>/` no repositório. TryPost: `content_type: instagram_reel`, `meta: {"share_to_feed": true}`, `media: [{url, meta: {"cover_offset_ms": 1000}}]`, rótulo Produto (ou o da linha).

**Reel animado só com print** (1080x1920, sem som; o antigo): base `posts/r01_krebs_queen.py`. Um print alto do app rola dentro de um tablet; títulos trocam por trecho; destaques acendem; cartão final com a chamada. Leva cerca de 30 s para gravar.

**Stories** (1080x1920): base `posts/stories_2026_10_26.py`. Ajudantes prontos no arquivo: `quiz`, `resp`, `dica`, `frase`, `novo`. Salvar em `saida/stories-AAAA-MM-DD/` (data da segunda).

**Prints do app** (`motor/prints/`): `desk-ia-krebs-1/2/3.png` e `desk-ia-krebs-longo.png` (conversa com a Queen IA), `desk-criar-material-a/b.png` (menu Criar material), `desk-flashcards.png`, `desk-simulados.png`, `desk-hoje.png`, `cel-caderno-erros.png` (celular com moldura). **Desde 12/11/2026 esses prints de Chrome são só referência visual**: tela que vai pro ar sai do HyperFrames, dentro de um aparelho (regra da seção 1). Nunca digitar senha. Não mostrar nome de aluno real nem dado pessoal em print.

**Legenda** (vai no TryPost, não na imagem): 1ª linha = gancho com a palavra de busca + 🩺, nos primeiros ~125 caracteres. 2 a 4 parágrafos curtos. Emojis ao longo (👑 Queen IA, 📚✨ mecanismo, 📌 salvar, 💜 compartilhar/link). Uma chamada só. Sem hashtag. Sem travessão. Notícia: fonte e data no fim. **Texto alternativo** em toda imagem do feed, com a palavra de busca.

## 6. Conferir antes de publicar (obrigatório)

1. `python3 folha.py saida/<pasta> 4` e abrir a folha com a ferramenta Read. Depois abrir **cada** PNG que tiver print: texto cortado, título encostando no visual, destaque fora do lugar, lupa mostrando o ponto errado, card vazio, palavra quebrada no meio. Corrigir e renderizar de novo.
2. Reel: tirar 5 quadros (`ffmpeg -ss <t> -i reel.mp4 -frames:v 1 q.jpg`) e abrir com Read.
3. Verificador de travessão (tem que sair vazio): `python3 checar.py posts/<arquivos novos>.py`. Escreva as legendas num arquivo `posts/legendas_AAAA_MM_DD.py` e inclua nele.
4. Conferir cada dado médico contra a fonte e cada claim contra a seção 1.

## 7. Publicar e agendar

1. `python3 publicar.py <pasta em saida> posts/AAAA-MM-DD-<slug>` para cada post (data = dia em que sai) e `python3 publicar.py stories-AAAA-MM-DD stories/AAAA-MM-DD` para os stories. Ele converte PNG em JPG e imprime as URLs públicas.
2. Montar a **folha de revisão** da semana (todos os feeds e stories numa imagem) e salvar em `revisao/AAAA-MM-DD.jpg` no repositório. É o que o Matheus abre na segunda de manhã.
3. `git add -A && git commit` (mensagem: "Semana AAAA-MM-DD: 7 posts e 21 stories") e `git push`. Esperar 1 minuto (o link raw demora a ficar disponível). O ambiente não abre raw.githubusercontent.com; quem baixa é o TryPost.
4. TryPost, ferramenta `create-post-tool` (um por vez; o lote pode ser bloqueado e precisar repetir só o que faltou), conta `01a03943-aa85-72df-bb05-0dc788a5e9d9`, `status: scheduled`, `scheduled_at` em UTC (tabela da seção 3).
   - Carrossel: `content_type: instagram_feed`, `media: [{url, meta:{alt_text}}...]` (máximo 10), `content` = legenda.
   - Reel: `content_type: instagram_reel`, `meta: {"share_to_feed": true}`, `media: [{url, meta: {"cover_offset_ms": 1500}}]`.
   - Story: `content_type: instagram_story`, `content: ""`, uma imagem por post.
   - URL base: `https://raw.githubusercontent.com/OrbittechIA/Medqueen-Instagram/main/` (atenção às maiúsculas: o TryPost não segue redirecionamento).
   - Rótulos (`label_ids`): Estudo `01a15a6a-f1d8-704f-adb5-e6b0d92088de` · Notícia `01a15a6a-fa14-73bc-8116-bc9bcef6b7b2` · IA `01a15a6b-0290-7369-86cf-6cbb80097998` · Produto `01a15a6b-0b33-736a-835d-fef36c8141a1` · Marca `01a15a6b-1439-711b-9f6f-9c076509f0f2` · Story `01a15a6b-1cba-7083-a26d-c3f595e41c8f`.
   - Agendar cada um no horário exato. Não usar a fila automática (ela não separa feed de story).
   - Se o TryPost devolver erro de mídia, esperar 2 minutos e tentar de novo uma vez.
   - Post único: `content_type: instagram_feed` com uma imagem só.
5. No fim, `list-posts-tool` da semana: tem que ter 30 agendados (7 feed às 18:50, 2 reels em vídeo ter e qui às 12:30, e 21 stories), sem horário repetido.

## 7B. Criar e agendar no Best Content (fluxo em vigor desde 03/11/2026)

Tudo pelo Chrome principal (ferramentas claude-in-chrome). Nunca digitar senha. Se aparecer "Conexão Instagram expirada", parar e avisar o Matheus (reconectar exige login dele).

**Já configurado (não refazer):** Estilo principal da marca (Editar estilo > Edição avançada > Descrição do estilo) com as regras fixas: fundo claro em gradiente lilás claro (#DDD2FA) para creme (#FFF6EA), igual em todos os slides; sem pessoa gerada por IA (só a Queen IA, com a imagem dela anexada); tela do produto só a que a gente anexar (PNG do HyperFrames já dentro do aparelho), nunca tela inventada por ele; texto curto. (Ajustado em 12/11/2026: antes dizia "sem print de app".) Os prompts que o Best Content gera já trazem o fundo.

**TELA NOVA DO CRIAR (vista em 09/11/2026, vale acima do passo a passo antigo logo abaixo):**
- Story: abrir `https://social.bestcontent.ai/criar/post?formato=story`. Carrossel: `...?formato=carrossel`, e na barra embaixo da caixa escolher "Até N slides" (o número exato) e trocar "Rápido" por **"Mais refinado"** (volta pra Rápido a cada post).
- Escrever a ideia com o texto exato de cada slide e sempre: "sem barra de comentário, sem campo de resposta, sem botão, sem chamada inventada" (sem isso ele desenha uma barra "Deixe seu comentário"). Quando tiver a Queen IA, anexar a imagem da biblioteca e descrever exatamente: "Queen IA oficial (Queen IA 2.0 Frontal.png): cabelo longo castanho ondulado com franja lateral, olhos castanhos, SEM óculos, jaleco branco sobre roupa preta com o símbolo da MedQueen no peito, sem coroa, mesmo rosto e mesmo traço de ilustração da referência". (Correção de 11/11/2026: a descrição antiga "cabelo roxo, óculos roxo" estava ERRADA e gerou uma personagem que não era a Queen.)
- Continuar > perguntas: objetivo "Engajar" (story) ou "Pode decidir por mim" (carrossel); nas outras, "Pode decidir por mim" ou "Deixar de fora". Tela "Confira o texto": conferir e preencher título vazio > "Criar a arte"/"Criar as artes" (story uns 40 s, carrossel uns 3 min).
- Concluir post > na tela "Seu post está pronto", apagar a legenda dele e colar a nossa > "Publicar ou agendar" > **conferir as redes: ele às vezes marca o TikTok junto; deixar só Instagram** > "Escolher dia e hora" > Dia e Hora (campos nativos: clicar no começo do campo e digitar DDMMAAAA e HHMM) > conferir o rodapé "Instagram / dia, às HHhMM" > "Agendar em 1 rede".
- Popups "O que achou do post?" e de conquista: fechar no X (nunca clicar no "Continuar" do popup de conquista achando que é o do formulário).

**Post de imagem (feed ou story):** Criar > Posts de Imagens > **Imagem Estática** > formato (Post Portrait, Carrossel Portrait ou Stories Único) > Continuar > **Engajar** (carrossel: abordagem **Educativo**) > **Criar do Zero** (nunca Inspirações: gasta crédito) > escrever a ideia com o texto exato de cada slide > Continuar > Continuar.
- **Número de slides do carrossel (regra do Matheus, 03/11/2026): pelo tema, não fixo.** Capa + 1 slide por parte do conteúdo + fechamento. Dica em 3 passos = 5; em 2 passos = 4; tema com 4 partes = 6. Escrever "exatamente N slides" na ideia e marcar o limite N.
- Não reescrever os prompts que ele gera por slide (estraga a máquina de criação). Só conferir conteúdo médico e acrescentar o que faltar de padrão.
- **Logo:** ligada no primeiro e no último slide, desligada no meio (o padrão dele já vem assim; conferir). Story: ligada.
- **CHECAGEM OBRIGATÓRIA DA QUEEN (Matheus, 11/11/2026: saiu story com personagem que não era ela).** Antes de agendar qualquer post ou story com a Queen, comparar lado a lado com `www/marca/queen_ia_recorte.png`: cabelo castanho ondulado longo, sem óculos, jaleco branco, roupa preta por baixo, rosto igual. Qualquer diferença (cabelo de outra cor, óculos, outro rosto, outro traço, coroa): corrigir no chat do editor pedindo "a personagem deve ser idêntica à imagem de referência anexada". Se em 2 tentativas não ficar idêntica, refazer esse post SEM a Queen (diagrama ou tipografia). Nunca agendar Queen duvidosa. No resumo de segunda, dizer quais posts têm a Queen e que foram conferidos.
- **Queen IA:** "Adicionar imagem" no slide > Biblioteca > "Queen IA 2.0 Frontal.png" > Usar imagem > prompt de uso (identidade travada, sem coroa, papel e posição no slide) > Adicionar > "Entendi, adicionar" > em carrossel, "Manter como está" (só no slide escolhido). Mesma dosagem da seção 1 (feed 3 ou 4 por semana; story 1 por dia, o das 15:50).
- Carrossel: "Gerar com IA" > **Mais refinado** > Gerar carrossel (uns 5 minutos). Story/post único: uns 40 segundos.
- **Conferir cada slide** (dado médico, CTA). Ele costuma INVENTAR chamada ("Comente X pra receber...", "Arraste pra cima..."): corrigir no chat do editor ("Peça alterações no design"), pedindo pra trocar pelo CTA padrão ou remover e "não mudar mais nada". São 12 edições grátis por post.
- Finalizar > apagar a legenda que ele gerou e colar a NOSSA (padrão da seção 5) > Publicar > Instagram > Continuar > **Agendar** > dia (clicar o número do dia no calendário; conferir a linha "Publicar em DD de mês às HH:MM") > horário > Confirmar. Story não tem legenda no Instagram, pode deixar a dele.
- Popup "O que achou do post?" e "Level up": fechar no X, nunca clicar nas estrelas.

**Reel em vídeo pronto (nosso motor):** Calendário > **Nova Pauta** > **Upload** > título, vídeo (file_upload do mp4 copiado para o scratchpad), legenda, data, horário > Criar Pauta. Ela entra como "Ideia": abrir o card no calendário > **Agendar Publicação** > **Confirmar Agendamento**. Não adicionar áudio (a trilha é escolha do Matheus).

**Créditos:** 10 por imagem. Plano Max = 1.900 por mês.

**No fim:** Calendário do Best Content tem que mostrar todos os horários da tabela da seção 3 como "Agendado". Mandar o resumo pro Matheus (seção 9) já com tudo agendado; silêncio = aprovado.

## 8. Medir a semana que passou

0. **Desde 03/11/2026 os números vêm do Analytics do Best Content** (menu Resultados > Analytics, pelo Chrome). O TryPost foi descontinuado; os passos abaixo valem só para semanas antigas que ainda estiverem lá.
1. `list-posts-tool` (publicados nos últimos 7 dias) e `get-post-metrics-tool` de cada um; `get-channel-insights-tool` da conta (range 7d).
2. Anotar no `historico.md`, na semana certa: alcance, alcance de não seguidores (se vier), salvamentos, compartilhamentos e visitas ao perfil por post. Se a ferramenta não devolver, escrever "sem dado". Nunca estimar.
3. Regra de decisão: a partir de 4 semanas de dado, dobrar a linha ou formato com mais (salvamentos + compartilhamentos) por alcance e cortar a pior. Anotar a decisão no histórico.
4. Sinal ruim: depois de 3 semanas, alcance quase só de seguidores → trocar 1 carrossel por reel.

## 9. Avisar o Matheus

Mensagem curta (ferramenta SendUserMessage), em português, sem travessão, com:
- os 7 temas do feed (2 motions + 5 carrosséis) e o Reel de questão, com dia;
- o link da folha de revisão: `https://github.com/OrbittechIA/Medqueen-Instagram/blob/main/revisao/AAAA-MM-DD.jpg`;
- os números da semana anterior em 3 linhas (melhor post, pior post, alcance total) ou "ainda sem número";
- qualquer coisa que travou e o que ele precisa fazer (só se precisar).
Se algo travar antes de agendar (sem TryPost ou sem GitHub), não inventar e não postar pela metade: avisar o que travou e parar.
