# TikTok @medqueen.ia no piloto automático (manual da tarefa de domingo)

Tudo do TikTok fica nesta pasta `tiktok/`. Não mexer em `motor/`, `posts/`, `stories/` nem `revisao/` da raiz: são do Instagram (tarefa própria, segunda 00:01). Daqui só se LÊ `motor/www/marca` (logo e poses da Queen) e `motor/www/som/efeitos` (efeitos sonoros).

Regras de texto que valem sempre: português do Brasil, informal e direto; nunca travessão nem meia-risca (U+2014, U+2013) em tela, legenda ou mensagem; nada de número, depoimento ou função inventada. Fundo escuro é proibido nos posts (fundo claro, lavanda pro creme).

## 1. Grade (decisão do Matheus, 09/11/2026)

A tarefa roda **domingo** e monta a semana que começa na **segunda seguinte** (segunda a domingo). Horários de Brasília (Trypost agenda em UTC: Brasília + 3 h).

| O quê | Quantos | Quando | Quem faz |
|---|---|---|---|
| Carrossel de fotos | 7 (1 por dia) | todo dia 11:43 | esta tarefa |
| Motion do produto | 7 (1 por dia) | todo dia 19:43 | esta tarefa |
| Meme da Cláudia | 6 (seg a sáb) | 15:13 | o Matheus produz; a tarefa só deixa a lacuna e avisa |

Domingo não tem meme: só carrossel e motion. Total da semana: 20 posts.

**Memes:** a tarefa NÃO cria meme. No fim, avisa o Matheus: "precisamos de 6 memes pra seg a sáb, 15:13". Ele produz durante a semana e manda; quem estiver na conversa com ele só agenda no Trypost (tiktok_video, is_aigc true, brand_organic_toggle true, PUBLIC_TO_EVERYONE, allow_comments true).

Conta no Trypost: TikTok `01a1ac00-1cb5-730b-951f-b46dd3c8f372`. Antes de produzir, `list-posts-tool` com `channels` = essa conta e `status: scheduled` (resultado grande: salvar e ler com jq). Se um horário da semana alvo já estiver ocupado pelo mesmo tipo de post, não produzir outro pra ele.

## 2. Medir a semana que passou (antes da pauta)

- `list-channel-publications-tool` e `get-analytics-publication-tool` (ou `get-post-metrics-tool`) dos posts publicados nos últimos 7 dias: views, curtidas, comentários, compartilhamentos.
- Separar por tipo (carrossel, meme, motion) e, nos motions, por **formato** e **assunto**; nos carrosséis, por **gancho**.
- Decisão: metade da semana nova repete o que deu mais view (formato, assunto, gancho), a outra metade testa coisa nova. Cada semana é uma semana nova: nada de copiar a semana anterior.
- Anotar os números e a decisão em `historico.md`.

## 3. Motion (7 por semana)

Motor: `motion/motor/` (`base.html` + `engine.js` com `render(t)` determinístico, `render.js`, `mix.py`). Cada vídeo é uma pasta `motion/videos/AAAA-MM-DD-slug/` com um `config.json`.

**Formatos** (variar: 4 formatos diferentes na semana e 3 variações deles, por exemplo assunto novo no mesmo formato):
- `flashcards`: PDF vira flashcards; 3 cartões virando. Campos: `flashcards.total`, `flashcards.cards` (3 pares pergunta e resposta).
- `aula`: aula com quadro; para e dá zoom na tabela (linha `linha_destaque` em amarelo) e depois no quadro "O que cai na prova". Campo `resposta` com blocos `p`, `h2`, `h3`, `table` (`head`, `rows`), `call` (`lines`, a primeira em negrito é o título), `ul`, `ol`. Precisa de uma `table` e de um `call`.
- `prova`: "o que cai na prova"; zoom no quadro amarelo e marca-texto passando linha por linha. `resposta` com `p`, `call` (título + 3 linhas) e `p`.
- `simulado`: PDF vira simulado; questão, marca a certa, resultado com contagem, aba "Revisar questões" com o porquê. Campo `simulado`: `materia`, `area`, `enunciado`, `opcoes` (4), `certa` (0 a 3), `acertos`, `porque`.

Campos comuns: `gancho` (3 linhas, a do meio em degradê: é a matéria; ex. "POV: joguei o PDF de" / "plexo braquial" / "na IA"), `pdf` (nome do arquivo como aluno salva: "Aula 3 · Membro superior.pdf"), `pedido` (o que a aluna digita), `queen` (pose do card final, arquivo de `motor/www/marca/queen-poses`, variar), `legendas` (uma por zoom, HTML com `<span class="grad">`).

**Conteúdo médico:** só matéria de ciclo básico ou clínico que cai em prova, com informação de livro-texto. Antes de renderizar, conferir TODAS as afirmações na própria MedQueen IA (regra do Matheus: a MedQueen é a referência): abrir `https://www.medqueen.com.br/app/ia` no Chrome principal (Claude in Chrome, "Browser 1", deviceId 0ffabed5-99a7-491f-b5ee-48a5dbdcab04, já logado), mandar numa conversa nova "Revisão técnica: diga se cada afirmação está CORRETA ou ERRADA..." com as afirmações numeradas, esperar a resposta inteira (`get_page_text`, ela demora 1 a 3 min) e corrigir o que ela apontar. Se o Chrome não estiver disponível, conferir com WebSearch em fonte confiável e avisar na mensagem final que a conferência foi pela web.

**Gravar:**
```
cd tiktok/motion/motor
node render.js ../videos/<pasta> preview     # 12 quadros em <pasta>/preview: abrir com Read e conferir
node render.js ../videos/<pasta> frames      # todos os quadros (uns 2 min por vídeo)
python3 -I mix.py ../videos/<pasta> <musica.mp3> [segundo do drop | calma]
```
O `mix.py` alinha o drop da música com o momento da revelação (`DROP` no meta.json), põe a música a -6 dB, os efeitos por cima e normaliza (-14 LUFS). Sai `<pasta>/video.mp4`. Conferir uma tira de quadros (`ffmpeg -i video.mp4 -vf fps=1/2,scale=180:-1,tile=10x1`) antes de agendar. Fontes Plus Jakarta vêm em `motion/motor/assets`.

**Música (autonomia dada pelo Matheus em 09/11/2026):** a tarefa escolhe sozinha.
- Fontes: Drive "Biblioteca de áudios - memes" (pasta id `1Ip1QFXShWm3B40xSsUKfJX3iX9EIaMh9`, subpastas por gênero; Eletrônica id `1tv9NCRIx2a8nrrOxhkMtPDZBsz_8ySqe`) e a biblioteca "Biblioteca de músicas MedQueen IA" (id `1nNle5KRuk8KjvVv8C5L5mUbhcuZAIQq5`, com `indice_musicas.csv`).
- **Nunca funk** na MedQueen. Preferir eletrônica e tech minimalista (aprovadas: eletronica_01, 02 e 05 da pasta de memes; 048, 049 e 050 da biblioteca). Reprovadas: 022, 078, 080.
- Não repetir a mesma faixa antes de 5 vídeos; faixa longa pode voltar com outro trecho. Registro em `musicas.md` (data, vídeo, faixa, trecho).
- Baixar: `search_files` com `parentId` da pasta e `download_file_content` (o resultado vai pra arquivo em tool-results: decodificar o base64 com python).
- Faixa com virada: deixe o `mix.py` achar o drop (sem terceiro argumento) ou passe o segundo. Faixa calma sem virada: `calma`.

**Legenda do post:** 1 frase com a matéria no começo + 1 pergunta pra puxar comentário + 4 ou 5 hashtags (#medicina #estudantedemedicina #iaparamedicina + 1 ou 2 da matéria). Ex.: "Joguei o PDF de cascata de coagulação na IA e saíram 20 flashcards 🩸 / Qual matéria você jogaria primeiro?".

**Agendar:** `request-media-upload-tool`, `curl -F media=@video.mp4 "<upload_url>"` (o shell alcança app.trypost.it), `create-post-tool` com `content_type: tiktok_video`, `scheduled_at` 22:43 UTC do dia, `meta`: privacy_level PUBLIC_TO_EVERYONE, allow_comments true, allow_duet true, allow_stitch true, is_aigc false, brand_organic_toggle true.

## 4. Carrossel (7 por semana)

Padrão aprovado pelo Matheus em 09/11/2026 (cara de **aluno que postou**, não de dono do produto):
- 5 fotos 9:16 geradas na Kairogen, modelo `nano-banana` (2 créditos cada; passar `expected_credits`, `wait_for_completion: true`, aspect 9:16). Ambientes de estudante de Medicina, sem pessoa: sala vazia, biblioteca, quadro depois da aula, caderno bagunçado com marca-texto, post-it, gabarito, cantina, mesa de estudo de madrugada. Pedir "Photorealistic vertical smartphone photo, candid, natural light, no people, no text, no letters, no logos".
- A Kairogen aceita no máximo 4 gerações ao mesmo tempo: mandar de 4 em 4 e esperar com `get_generation` (wait_for_completion true). A imagem pronta fica salva em tool-results (`mcp-Kairogen-blob-*.png`, o caminho vem no resultado): copiar de lá pra `carrossel/AAAA-MM-DD/raw/cN_I.png`. Se faltar crédito, não comprar nada: avisar o Matheus.
- Imagem ruim (folha em branco, tela ilegível, texto escrito na foto) pode ser refeita.
- Último slide: a tela do app DENTRO da foto (celular, tablet ou notebook, variando aparelho e lugar), gerada em modo edição: `reference_image_urls` com a URL pública de uma tela de `carrossel/telas/` (link raw do GitHub com hash do commit) e prompt "Place this exact app screen on the [phone/tablet/laptop] screen in a candid photo of a medical student's desk...". Nunca print solto nem tela com zoom.
- Telas: `carrossel/telas/` (print_aula, print_cai_na_prova, print_flashcards, print_simulado, print_resultado, print_pdf). Telas novas saem dos motions (rodar `render.js` em modo preview e recortar o celular) e devem variar de assunto de uma semana pra outra.
- Texto: `python3 -I carrossel/montar.py <semana.json> <fotos cruas> <saida>` (Poppins Bold branco com contorno; centro do texto no máximo em y 1350, senão a legenda do TikTok cobre). Exemplo de semana.json: `carrossel/2026-11-09/semana.json`.
- Moldes que funcionam: "3 jeitos de decorar X (o 3º salvou meu semestre)", "coisas que eu queria saber no 1º período", "meu método pra estudar X em 30 min", "X sem sofrimento (salva esse)", "professor mandou PDF de 200 páginas", "checklist da véspera de prova", "minha veterana passou em tudo e eu descobri o segredo dela". A revelação (a IA) vem no último slide.
- Agendar: `create-post-tool` com `content_type: tiktok_photo`, 14:43 UTC, `meta`: privacy_level PUBLIC_TO_EVERYONE, allow_comments true, auto_add_music true, brand_organic_toggle true. Mídia pelo link raw do GitHub com hash do commit (`https://raw.githubusercontent.com/OrbittechIA/medqueen-instagram/<hash>/tiktok/carrossel/AAAA-MM-DD/cN/slideI.jpg`). Legenda curta no tom do aluno, terminando em pergunta, 4 ou 5 hashtags.

## 5. Conferir (obrigatório, nada vai pro ar sem isso)

1. Folha de cada carrossel aberta com Read: texto legível, sem palavra sozinha na última linha, imagem combinando com o texto, tela do app nítida no último slide.
2. Prévia de cada motion (12 quadros) e tira do vídeo final: gancho legível no primeiro quadro, zoom no lugar certo, card final com logo, Queen e "Teste grátis por 7 dias".
3. Conteúdo médico conferido na MedQueen (seção 3).
4. Procurar travessão e meia-risca com python (o `grep -P` daqui não aceita esses códigos): `python3 -c "import pathlib;print([str(p) for p in pathlib.Path('tiktok').rglob('*') if p.suffix in ('.md','.json','.txt') and any(c in p.read_text(errors='ignore') for c in chr(0x2013)+chr(0x2014))])"` e conferir as legendas antes de agendar. Tem que voltar vazio.
5. No fim, `list-posts-tool` da conta: 7 carrosséis às 14:43 UTC e 7 motions às 22:43 UTC na semana alvo, sem horário repetido.

## 6. Publicar no GitHub e fechar

- Commit só de `tiktok/` (fotos e slides do carrossel, configs dos vídeos, `historico.md`, `musicas.md`). Não subir `frames/`, `preview/`, `meta.json` nem `.f32` (estão no .gitignore). O `video.mp4` sobe (uns 2,5 MB cada) pra ficar guardado.
- `git fetch origin main && git rebase origin/main` antes do push.
- Mensagem curta pro Matheus (SendUserMessage): os 7 carrosséis e os 7 motions com dia e assunto, os números da semana anterior em 3 linhas (o que ganhou e o que perdeu), as músicas usadas, e o aviso: "precisamos de 6 memes pra seg a sáb às 15:13". Mandar com SendUserFile as folhas dos carrosséis e 2 ou 3 motions.
