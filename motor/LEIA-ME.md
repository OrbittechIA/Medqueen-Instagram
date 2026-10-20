# Motor do Instagram da MedQueen IA (@medqueen.ia)

Manual da tarefa semanal. Quem roda isto é uma sessão nova do Claude, sem memória da conversa anterior. Siga na ordem.
O Matheus revisa tudo na **segunda de manhã** (no TryPost ou pela folha de revisão). O primeiro post da semana sai **segunda à tarde**, então ele tem tempo de cortar ou pedir ajuste. Mesmo assim a conferência do passo 6 é obrigatória: o post sai sozinho se ele não mexer.

Estratégia completa: `medqueen/instagram/brain-instagram.md` e `medqueen/instagram/estrategia-alcance-organico.md` no projeto "MedQueen Growth" do claude.ai (se a sessão tiver acesso ao projeto, leia antes). Este manual tem o necessário para rodar sem o projeto.

## 1. Regras que nunca mudam

- Português do Brasil, direto, adulto. Chama o público de "Estudante de Medicina" ou pelo momento (prova, residência, internato).
- **Nunca usar travessão (U+2014) nem meia-risca (U+2013)** em card, legenda, story ou texto alternativo. Hífen só em palavra composta. O passo 6 tem verificador.
- Sem "não é X, é Y", sem emoji como marcador de lista nos cards, sem frase de efeito vazia, sem "Concorda?".
- **Feed sempre claro**: fundo branco/lavanda do motor. Nunca fundo preto, azul-marinho ou roxo escuro dominando. O roxo só em detalhe, título e cartão final.
- **Print nunca solto (regra do Matheus).** Todo print entra dentro de `tablet()`, `celular()` ou `pronto()` e, sempre que fizer sentido, com destaque (`dest`) ou lupa (`lupa`) no ponto que importa.
- **Sem pessoa gerada por IA.** A única personagem é a Queen IA oficial (ilustração, `www/marca/queen_ia_recorte.png`, com o símbolo da MedQueen no jaleco). Ela entra em apoio, dica e fechamento; nunca em post de dor nem em manifesto.
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
| Seg | 18:50 (21:50Z) **carrossel** | 13:50 (16:50Z) | 15:50 (18:50Z) | 21:20 (00:20Z do dia seguinte) |
| Ter | sem feed | 11:50 (14:50Z) | 15:50 (18:50Z) | 21:20 (00:20Z) |
| Qua | 18:50 (21:50Z) **carrossel** | 11:50 | 15:50 | 21:20 |
| Qui | sem feed | 11:50 | 15:50 | 21:20 |
| Sex | 18:50 (21:50Z) **carrossel ou reel** | 11:50 | 15:50 | 21:20 |
| Sáb | sem feed | 11:50 | 15:50 | 21:20 |
| Dom | sem feed | 11:50 | 15:50 | 21:20 |

Total: 3 feed + 21 stories = 24. Pelo menos 2 dos 3 feeds são carrossel. Segunda nada sai antes das 13:50 (o Matheus revisa de manhã).

Stories: no dia de feed, o story das 21:20 anuncia o post novo (`imagem('saida/<post>/01.png')`). Os outros alternam: teste rápido (pergunta) com a resposta no story seguinte, dica da Queen IA, tela do produto com destaque, frase curta. Story pela API sai sem texto e sem figurinha: o texto vai dentro da imagem.

## 4. Pauta

**Antes de tudo, veja se a semana já está pronta:** `list-posts-tool` com `channels=["01a03943-aa85-72df-bb05-0dc788a5e9d9"]` e `status=scheduled` (o resultado é grande: salvar em arquivo e ler com `jq`). Se já houver 24 agendados entre segunda 00:00 e domingo 23:59 da semana alvo, não produza nada: só meça (seção 8), atualize o histórico e avise. Se tiver alguns, produza só os horários que faltam.

Linhas (proporção inicial, hipótese a ajustar com as métricas): Estudo ~40% · Notícia de medicina ~25% · Novidade de IA ~15% · Produto ~15% · Marca ~5%. Com 3 feeds por semana, a regra prática é: **1 Estudo + 1 Produto + 1 alternando (Notícia, IA ou Estudo)**.

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

**Reel** (1080x1920, sem som): base `posts/r01_krebs_queen.py`. Um print alto do app rola dentro de um tablet; títulos trocam por trecho; destaques acendem; cartão final com a chamada. Leva cerca de 30 s para gravar.

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
3. `git add -A && git commit` (mensagem: "Semana AAAA-MM-DD: 3 posts e 21 stories") e `git push`. Esperar 1 minuto (o link raw demora a ficar disponível). O ambiente não abre raw.githubusercontent.com; quem baixa é o TryPost.
4. TryPost, ferramenta `create-post-tool` (um por vez; o lote pode ser bloqueado e precisar repetir só o que faltou), conta `01a03943-aa85-72df-bb05-0dc788a5e9d9`, `status: scheduled`, `scheduled_at` em UTC (tabela da seção 3).
   - Carrossel: `content_type: instagram_feed`, `media: [{url, meta:{alt_text}}...]` (máximo 10), `content` = legenda.
   - Reel: `content_type: instagram_reel`, `meta: {"share_to_feed": true}`, `media: [{url, meta: {"cover_offset_ms": 1500}}]`.
   - Story: `content_type: instagram_story`, `content: ""`, uma imagem por post.
   - URL base: `https://raw.githubusercontent.com/OrbittechIA/Medqueen-Instagram/main/` (atenção às maiúsculas: o TryPost não segue redirecionamento).
   - Rótulos (`label_ids`): Estudo `01a15a6a-f1d8-704f-adb5-e6b0d92088de` · Notícia `01a15a6a-fa14-73bc-8116-bc9bcef6b7b2` · IA `01a15a6b-0290-7369-86cf-6cbb80097998` · Produto `01a15a6b-0b33-736a-835d-fef36c8141a1` · Marca `01a15a6b-1439-711b-9f6f-9c076509f0f2` · Story `01a15a6b-1cba-7083-a26d-c3f595e41c8f`.
   - Agendar cada um no horário exato. Não usar a fila automática (ela não separa feed de story).
   - Se o TryPost devolver erro de mídia, esperar 2 minutos e tentar de novo uma vez.
5. No fim, `list-posts-tool` da semana: tem que ter 24 agendados, sem horário repetido.

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
