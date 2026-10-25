# Motor do Instagram da MedQueen IA (@medqueen.ia)

Manual da tarefa semanal. Quem roda isto é uma sessão nova do Claude, sem memória da conversa anterior. Siga na ordem.
O Matheus revisa tudo na **segunda de manhã** (no TryPost ou pela folha de revisão). O primeiro post da semana sai **segunda à tarde**, então ele tem tempo de cortar ou pedir ajuste. Mesmo assim a conferência do passo 6 é obrigatória: o post sai sozinho se ele não mexer.

Estratégia completa: `medqueen/instagram/brain-instagram.md` e `medqueen/instagram/estrategia-alcance-organico.md` no projeto "MedQueen Growth" do claude.ai (se a sessão tiver acesso ao projeto, leia antes). Este manual tem o necessário para rodar sem o projeto.

## 1. Regras que nunca mudam

- Português do Brasil, direto, adulto. Chama o público de "Estudante de Medicina" ou pelo momento (prova, residência, internato).
- **Nunca usar travessão (U+2014) nem meia-risca (U+2013)** em card, legenda, story ou texto alternativo. Hífen só em palavra composta. O passo 6 tem verificador.
- Sem "não é X, é Y", sem emoji como marcador de lista nos cards, sem frase de efeito vazia, sem "Concorda?".
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

| Dia | Feed | Story 1 | Story 2 | Story 3 |
|---|---|---|---|---|
| Seg | 18:50 (21:50Z) **post único** | 13:50 (16:50Z) | 15:50 (18:50Z) | 21:20 (00:20Z do dia seguinte) |
| Ter | 18:50 (21:50Z) **carrossel** | 11:50 (14:50Z) | 15:50 (18:50Z) | 21:20 (00:20Z) |
| Qua | 18:50 **post único** | 11:50 | 15:50 | 21:20 |
| Qui | 18:50 **carrossel** | 11:50 | 15:50 | 21:20 |
| Sex | 18:50 **post único** | 11:50 | 15:50 | 21:20 |
| Sáb | 18:50 **carrossel** | 11:50 | 15:50 | 21:20 |
| Dom | 18:50 **post único** | 11:50 | 15:50 | 21:20 |

| Ter e Qui | **+ Reel em vídeo 12:30 (15:30Z)** | | | |
| Qua e Sex | **+ vídeo do fundador 12:30 (15:30Z)**: o Matheus grava, o Claude escreve o roteiro (salvo no projeto em `medqueen/instagram/roteiros-founder-*.md`) e edita. Só agenda quando o vídeo chegar. | | | |

Total: **7 feed + 2 reels em vídeo + 21 stories = 30** (decisão do Matheus em 23/10/2026: feed todo dia, alternando post único e carrossel; seg, qua, sex e dom = post único; ter, qui e sáb = carrossel). Segunda nada sai antes das 13:50 (o Matheus revisa de manhã). Reel de pessoa gravada pode entrar no futuro, mas só quando o Matheus mandar o vídeo; até lá não planejar reel de pessoa.

Stories: todo dia o story das 21:20 anuncia o post novo do feed (`imagem('saida/<post>/01.png')`). Os outros alternam: teste rápido (pergunta) com a resposta no story seguinte, dica da Queen IA, tela do produto com destaque, frase curta. Story pela API sai sem texto e sem figurinha: o texto vai dentro da imagem.

## 4. Pauta

**ATENÇÃO, RODADA DE 26/10/2026: a semana de 26/10 a 01/11 foi produzida à mão em 25/10 (linha nova de IA para Medicina) e está com o Matheus para aprovar. Nesta rodada NÃO produza nem agende nada: só meça (seção 8), atualize o histórico e avise. Esta nota vale só para a rodada de 26/10.**

**Antes de tudo, veja se a semana já está pronta:** `list-posts-tool` com `channels=["01a03943-aa85-72df-bb05-0dc788a5e9d9"]` e `status=scheduled` (o resultado é grande: salvar em arquivo e ler com `jq`). Se já houver 30 agendados (7 feed + 2 reels em vídeo + 21 stories) entre segunda 00:00 e domingo 23:59 da semana alvo, não produza nada: só meça (seção 8), atualize o histórico e avise. Se tiver alguns, produza só os horários que faltam.

Linhas (proporção inicial, hipótese a ajustar com as métricas): Estudo ~40% · Notícia de medicina ~25% · Novidade de IA ~15% · Produto ~15% · Marca ~5%. Com 7 feeds por semana, a regra prática é: **3 Estudo + 2 Produto + 1 Notícia ou IA + 1 Marca**. Carrossel combina com Estudo e Produto passo a passo; post único combina com gancho forte, comparação lado a lado, notícia, IA e marca.

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

**Post único** (1 imagem 1080x1350): base `posts/u00_modelo_post_unico.py` (é só modelo, não publicar). Spec com um card só; o motor tira o contador e a barra sozinho. Uma ideia só: título grande (até 8 palavras) com `<em>` na palavra-chave, uma linha de apoio e um visual forte (print no tablet/celular com destaque, comparação lado a lado, número grande ou diagrama). `pe_final` curto, ex.: "7 dias grátis · link na bio" ou "salva pra revisar".

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

**Prints do app** (`motor/prints/`): `desk-ia-krebs-1/2/3.png` e `desk-ia-krebs-longo.png` (conversa com a Queen IA), `desk-criar-material-a/b.png` (menu Criar material), `desk-flashcards.png`, `desk-simulados.png`, `desk-hoje.png`, `cel-caderno-erros.png` (celular com moldura). Para print novo: se a sessão tiver o Chrome do Matheus (ferramentas claude-in-chrome), abrir `https://www.medqueen.com.br/app/...` (ele fica logado), aplicar `document.documentElement.style.zoom='2'`, tirar `zoom` com `save_to_disk` na região inteira e copiar para `motor/prints/`. Se não tiver o Chrome, use só o banco. Nunca digitar senha. Não mostrar nome de aluno real nem dado pessoal em print.

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

## 8. Medir a semana que passou

1. `list-posts-tool` (publicados nos últimos 7 dias) e `get-post-metrics-tool` de cada um; `get-channel-insights-tool` da conta (range 7d).
2. Anotar no `historico.md`, na semana certa: alcance, alcance de não seguidores (se vier), salvamentos, compartilhamentos e visitas ao perfil por post. Se a ferramenta não devolver, escrever "sem dado". Nunca estimar.
3. Regra de decisão: a partir de 4 semanas de dado, dobrar a linha ou formato com mais (salvamentos + compartilhamentos) por alcance e cortar a pior. Anotar a decisão no histórico.
4. Sinal ruim: depois de 3 semanas, alcance quase só de seguidores → trocar 1 carrossel por reel.

## 9. Avisar o Matheus

Mensagem curta (ferramenta SendUserMessage), em português, sem travessão, com:
- os 3 temas do feed e o dia de cada um;
- o link da folha de revisão: `https://github.com/OrbittechIA/Medqueen-Instagram/blob/main/revisao/AAAA-MM-DD.jpg`;
- os números da semana anterior em 3 linhas (melhor post, pior post, alcance total) ou "ainda sem número";
- qualquer coisa que travou e o que ele precisa fazer (só se precisar).
Se algo travar antes de agendar (sem TryPost ou sem GitHub), não inventar e não postar pela metade: avisar o que travou e parar.
