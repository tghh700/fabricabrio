# Playbook de qualidade — Shorts BRIO

> **Regras fixas do usuário (prevalecem sobre tudo abaixo):** fechamento "Registre e acompanhe seus treinos gratuitamente. Link na bio."; nome do app escrito "Bríu" na narração (opção 3; "Brío" sai "briô"); vídeos de 1 min ou mais; só funções reais do app; sem quadradinho/kicker no topo; **todo vídeo termina com um gatilho de engajamento ESPECÍFICO do tema (comentar uma palavra/número, mandar pro amigo, enquete de 2 lados ou salvar e voltar), integrado ao CTA: o gatilho expõe a dor que o app resolve, uma frase-ponte liga a uma função real do app e a frase fixa fecha** (detalhes e modelos em AUTOMACAO.md, seção 2). Pedido genérico ("comenta aí", "deixa o like", "se inscreve") continua proibido.

**Data da pesquisa:** 09/11/2026 · Fontes em inglês, 2025–2026 (uma de 2023). Legenda: **[dado]** = número com origem declarada; **[relato]** = opinião ou experiência de criador/vendedor, sem metodologia verificável. Quase todos os "números de retenção" que circulam vêm de blogs de ferramentas, sem dataset público. O YouTube não publica benchmarks oficiais (1of10).

**Resumo**
1. A métrica que decide se o Short é distribuído é "Visualizou vs. deslizou". O gancho precisa entregar a promessa no 1º segundo, com imagem, texto e voz juntos, sem nenhuma introdução.
2. Para ~60 s, use uma batida nova (visual ou de história) a cada 2–4 s. A narração deve ficar entre 120 e 170 palavras e terminar no payoff, emendando de volta no início (loop). Nada de "comenta aí" genérico; o gatilho final específico (regra fixa) vem colado ao payoff, curto.
3. O que dá "cara de IA" é estrutura previsível: "não é X, é Y", trios, frases do mesmo tamanho, palavras infladas. Funcionam melhor amostras de voz e objetivos claros do que listas enormes de proibições.
4. No ElevenLabs, controle ritmo e ênfase com pontuação. Use `<break>` com moderação e só em modelos que suportam. Escreva números por extenso e fixe a pronúncia de "BRIO" (alias/dicionário).
5. O risco nº 1 de um canal automatizado é ser lido como "conteúdo repetitivo/produzido em massa". Varie formatos e cenas e mantenha revisão humana.

---

## Resultados reais do @briotreino (Instagram, print do dono em 10/11 14:45)

| Vídeo | Capa no feed | Views |
|---|---|---|
| brio-03 Quanto tempo pra ver resultado? | gancho | **3.002** |
| brio-02 Falha em toda série? | gancho | 1.432 |
| brio-01 Acordou todo dolorido? | gancho | 1.321 |
| brio-04 Você descansa ou some? | gancho | 1.227 |
| brio-06 Elevação lateral errada | gancho | 1.063 |
| brio-07 O ego tá roubando seu músculo | gancho | 1.053 |
| brio-09 Mesmo músculo todo dia? | gancho | 191 (postado há poucas horas) |
| **brio-05 Quando subir a carga (dupla progressão)** | **tela final do CTA** | **144 · YouTube: 6** |

**Por que o brio-05 afundou (3 diferenças contra todos os outros):**
1. **Capa = tela do CTA** ("COMENTA SUAS REPETIÇÕES" + celular do app). Parece anúncio e não tem pergunta. Todos os que passaram de 1.000 têm a pergunta-dor na capa.
2. **CTA ocupando 37% da narração** (12 s de 33 s). Nos outros ficou entre 23% e 28%. A versão v2 alongou o final (gatilho + "Não lembra?" + app + frase fixa) e o vídeo virou meio anúncio.
3. **Tema de método, com termo técnico** ("dupla progressão", "quando subir a carga"). Os vencedores são dores amplas que até iniciante sente: resultado, dor, falha, descanso.

**Regras novas (valem a partir de 10/11):**
- **Final curto:** gatilho + ponte com o app + frase fixa somam **no máximo 20% da narração e 9 s**. O gatilho é 1 frase; a ponte é 1 frase; não há uma terceira.
- **Capa:** o título-gancho já aparece no **frame 0** e o dono escolhe a capa no frame do gancho (nunca a tela final). A fábrica exporta `capas/<id>.jpg` com o frame do gancho.
- **Gancho = dor ampla na forma de pergunta**, de quem nunca ouviu o termo técnico. O método (dupla progressão, RIR, deload) entra como **resposta**, nunca no título. Ex.: "Treina há meses com o mesmo peso?" em vez de "Quando subir a carga?".
- Não repostar o mesmo arquivo de um vídeo que flopou: refazer com gancho, capa e final novos.

## Regras práticas para o próximo roteiro do BRIO

1. Abra com o payoff ou com o erro específico já na 1ª frase, sem "Oi", logo ou contexto. (learnwithhasan; 1of10; George Blackman)
2. Gancho com ≤ 12 palavras e uma ideia só. Precisa fazer sentido para quem nunca treinou. (Social Media Examiner/John Scott)
3. O texto na tela no 0 s não repete a fala: ele soma subtexto ao gancho falado. (Social Media Examiner)
4. Prefira "erro específico" a "dica genérica": "Seu supino trava no meio por causa disso" é melhor que "dicas de supino". (wildandfreetools, síntese de Reddit [relato])
5. Escreva entre 140 e 160 palavras para 60 s, o que dá cerca de 2,5 palavras/s. Roteiro longo força o TTS a acelerar. (learnwithhasan; EasyViral)
6. Use 3 a 5 frases curtas e varie o tamanho delas: uma de 3 palavras, uma de 12. Leia em voz alta. (Will Francis; dev.to De-slop)
7. Encadeie com "mas/então" em vez de "e depois": cada "mas" abre um conflito novo. (Social Media Examiner)
8. Prometa no gancho e pague só no final. O payoff tem que ser a resposta exata do que o gancho prometeu. (Social Media Examiner; EasyViral)
9. Troque de cena ou de pose do boneco a cada 2–4 s e mude o título grande a cada batida. (OpusClip [relato]; creativeworkflowlab)
10. Feche com uma frase que emenda na primeira (loop) e não peça like nem inscrição. (learnwithhasan; Social Media Examiner)
11. O CTA do app vai no máximo em uma frase curta, colada ao payoff e com utilidade: "Anota a carga no BRIO e compara semana que vem." Proibido "link na descrição para saber mais". (Social Media Examiner)
12. Banir: "não é X, é Y", "e o melhor?", trios de adjetivos, "transformar/elevar/potencializar", frases de "significado" no fim ("mostrando a importância de..."). (TechCrunch/Wikipedia; Will Francis)
13. Nada de travessão (—) no texto do TTS. Pausa se faz com ponto, vírgula ou reticências. (Will Francis; docs ElevenLabs)
14. Números e unidades por extenso: "três séries de oito", "vinte quilos". Nada de "3x8" ou "20kg". (docs ElevenLabs, normalização)
15. Ênfase em no máximo 1 palavra em CAIXA ALTA por frase, e só nos modelos v3/v4. (docs ElevenLabs)
16. Cada afirmação técnica precisa caber em "fonte conhecida ou senso comum de academia". Sem número inventado. Se faltar dado, reescreva sem número. (learnwithhasan; De-slop "specificity pass")
17. Cada vídeo precisa variar pelo menos dois de: formato de gancho, cenário, estrutura, cor do título. Isso evita o rótulo de "template repetido". (OutlierKit; PlagiarismToday)

---

## Ganchos

**O que se sabe**
- Criadores e ferramentas afirmam que a decisão de ficar acontece em 1–2 s [relato] (1of10). O dev.to "Hook Engineering" cita ~2,3 s nos Shorts, mas sem fonte nomeada [relato].
- Os 4 requisitos dos primeiros 2 s são movimento imediato, payoff declarado, loop aberto e zero logo ou intro [relato] (1of10).
- Imagem, texto na tela e áudio devem chegar juntos no 1º segundo [relato] (EasyViral).
- Teste mudo: assista aos 3 primeiros segundos sem som e veja se você continuaria (dev.to Hook Engineering).
- Estão em queda os templates "POV:", "assista até o final" e ganchos que anunciam o assunto ("Hoje vou falar de...") [relato] (wildandfreetools).

**12 modelos adaptados (PT-BR)**
1. *Erro específico:* "Se seu supino trava no meio, o problema não é o peito."
2. *Pare de fazer:* "Para de fazer rosca assim. Sério."
3. *Payoff primeiro:* "Três séries bem feitas batem cinco séries mal feitas. Olha por quê."
4. *Teste com prazo:* "Ele anotou cada treino por trinta dias. Olha o que aconteceu com a carga."
5. *Arrependimento:* "Queria ter sabido disso no meu primeiro ano de academia."
6. *Insider:* "O que o cara forte da academia faz e não te conta."
7. *Meio da história:* "Ele já tava na quarta série quando percebeu o erro."
8. *Contraintuitivo:* "Treinar até a falha toda série pode estar te deixando mais fraco."
9. *Número + promessa:* "Dois ajustes no agachamento que mudam tudo no seu glúteo."
10. *Dor relatável:* "Três meses treinando e o espelho não muda?"
11. *Pergunta direta ao "você":* "Você sabe quanto levantou no supino mês passado?"
12. *Confissão:* "Eu treinei errado por dois anos. Esse era o erro."

(Tipos extraídos de Social Media Examiner, wildandfreetools e dev.to Hook Engineering. A adaptação é nossa.)

---

## Estrutura e retenção de 60 s

Esqueleto sugerido, combinando learnwithhasan, EasyViral e Social Media Examiner:

| Tempo | Batida | Nota |
|---|---|---|
| 0–3 s | Gancho (payoff ou erro) | título grande + boneco já em ação |
| 3–10 s | Uma frase de contexto e o "mas" | abre o loop |
| 10–40 s | 2 ou 3 revelações, uma a cada ~8–10 s | troca visual a cada 2–4 s |
| 40–52 s | Virada ou payoff | entrega exata do gancho |
| 52–65 s | Gatilho específico + ponte para o app + frase fixa | sem "se inscreve"; máx. 240 caracteres |

- **Duração:** a OpusClip diz que Shorts de 15–30 s retêm mais e que acima de 45 s há queda [relato, sem dados abertos]. Já um operador com agentes Claude viu que Shorts mais longos (75 s) davam mais tempo assistido e chegaram a 109% de loop [dado do próprio canal] (dev.to wcamon). Vale testar 40 s contra 60 s.
- **Benchmarks de criadores:** "visualizou vs. deslizou" de 70–79% é considerado bom, 80% ou mais é forte. Média assistida de 60–75% em Shorts de 60 s [relato] (1of10).
- **Pedidos de engajamento quebram o ritmo,** e finais do tipo "trailer" fazem o público sair [relato] (Social Media Examiner).
- **CTA e engajamento:** um canal com agentes teve zero respostas aos CTAs de votação [dado do próprio canal] (wcamon).

---

## Escrita com Claude (prompts e anti-padrões)

**O que funciona (relatos)**
- **Separar regras absolutas de dicas flexíveis no prompt.** Exemplo: um bloco "REGRAS ABSOLUTAS" (duração, tom) e outro "orientações" (creativeworkflowlab).
- **Dar 2–3 roteiros-exemplo bons do próprio canal** em vez de uma lista enorme de proibições. Sozinhas, as proibições fazem o modelo se fixar no termo proibido (Will Francis). Uma amostra de 300–500 palavras funciona; abaixo de 200 vira caricatura (De-slop).
- **Dizer o objetivo e o leitor.** Algo como "iniciante de academia, 18–30 anos, rolando o feed" (Will Francis).
- **Fazer o fluxo em duas etapas.** Primeiro o plano (gancho, beats, fatos a checar), depois o roteiro. Na etapa de plano, um erro factual foi pego antes de renderizar (learnwithhasan).
- **Fazer passes de revisão.** O "coffee test" reescreve como se explicasse a um amigo. O "specificity pass" troca afirmações vagas por concretas e usa placeholder quando falta o dado (De-slop).
- **Alimentar o prompt com métricas.** Mande as métricas do vídeo anterior (retenção, % que ficou no gancho) para o próximo roteiro (creativeworkflowlab; Indie Hackers v3 do prompt; wcamon com memória persistente).
- **Controlar a duração.** Pedir "60 s" gerou ~41 s até o prompt ser ajustado (wcamon). Peça uma contagem de palavras, não de segundos.

**Anti-padrões de "texto de IA"** (TechCrunch/Wikipedia; Will Francis)
- Importância inflada e frases finais de "significado" ("...mostrando o quanto a constância importa").
- Contraste repetido "não é X, é Y", trios e frases que começam todas do mesmo jeito.
- Vocabulário de marketing: transformar, elevar, potencializar, jornada, incrível.
- Abertura que limpa a garganta: "No mundo da academia de hoje...". Corte a primeira frase.
- Muletas do Claude citadas por usuários: "genuinamente", "isso não é pouca coisa", "você tem toda razão".
- Detectores de IA "são basicamente inúteis", então não otimize para eles (TechCrunch).

---

## Narração com IA (ElevenLabs)

Fonte principal: documentação oficial.
- **Pausas:** `<break time="0.5s"/>` vai até 3 s e **não funciona no v3/v4**. Nesses modelos, use pontuação e reticências. Muitas tags de pausa numa só geração causam instabilidade.
- **Ênfase:** CAIXA ALTA e reticências funcionam no v3/v4. Audio tags (`[sussurrando]`, `[suspira]`) precisam combinar com o perfil da voz e devem ser testadas antes, porque nem sempre são obedecidas.
- **Velocidade:** de 0,7 a 1,2, sendo 1,0 o padrão. Valores extremos pioram a qualidade. Melhor encurtar o texto que acelerar.
- **Pronúncia de "BRIO":** use alias, regravando o texto com grafia fonética, ou um dicionário de pronúncia (.PLS/TXT, sensível a maiúsculas, vale só a 1ª regra que casar). Tag de fonema só funciona em alguns modelos. No v4 é possível usar IPA entre barras.
- **Normalização:** expanda números, unidades e abreviações antes do TTS, ou peça isso ao LLM. Modelos maiores leem números melhor que o Flash.
- **Clones:** o v3 não está otimizado para Professional Voice Clones.

---

## Visual / animação

- **Ritmo:** corte ou mudança a cada 2–4 s. Em conteúdo narrativo, uma batida nova a cada 5–7 s [relato] (OpusClip). Uma batida visual nova a cada 3 s (creativeworkflowlab).
- **Texto na tela como camada principal:** fonte sem serifa, grossa, alto contraste, no meio do quadro [relato] (EasyViral). Sobre legendas embutidas, a OpusClip cita "+15–25% de retenção" sem fonte. O único número com origem é de anúncios no Facebook (+12% de tempo de visualização), ou seja, não é de Shorts.
- **Áreas seguras:** nada importante nos 340 px de baixo nem nos 160 px da direita, num quadro de 1080×1920 (learnwithhasan).
- **Sincronia:** a revelação na tela tem que cair na palavra falada. Confira os frames nos momentos de payoff, não só nas transições (learnwithhasan).
- **Legibilidade:** em fundo escuro, garanta contraste do boneco. Cenas escuras demais escondem a ação (George Blackman). Uma tela só com texto e uma pausa breve prende a atenção num ponto-chave.
- **Variedade:** imagens geradas ficaram repetitivas depois de 52 vídeos (wcamon). Faça rodízio de cenários, poses e paleta de títulos.

---

## Pipelines automatizados (o que deu certo / errado)

- **Deu certo:**
  - Cron + LLM + TTS + montagem em código + upload por API, com log em planilha, por cerca de US$15/mês [relato] (Indie Hackers).
  - Ledger de deduplicação de assets, que impede reuso silencioso de clipes (Indie Hackers).
  - Remotion + ElevenLabs + Claude Code com etapa de plano aprovada antes de renderizar, e skills/playbooks versionados no repositório (learnwithhasan).
  - Memória persistente entre sessões para ajustar a pauta (wcamon).
- **Deu errado:**
  - Token OAuth do YouTube expirando é a causa nº 1 de falhas (Indie Hackers).
  - Duas de três canais ficaram "quietos" (Indie Hackers).
  - O agente não sabe julgar se uma história emociona, e a Analytics API atrasa mais de 72 h, o que dificulta otimizar rápido (wcamon).
  - Cor da marca mudada num arquivo e não no outro (learnwithhasan).

---

## O que NÃO fazer

- Abrir com logo, saudação, "neste vídeo" ou contexto.
- Usar "assista até o final", "POV:" ou pedidos genéricos ("comenta aí", "deixa o like", "se inscreve"). O gatilho final específico do tema é obrigatório (regra fixa).
- Terminar com "veja o vídeo completo" ou "link na descrição para saber mais".
- Deixar o roteiro passar de ~170 palavras e compensar acelerando a voz.
- Usar travessões, "3x8", "kg" ou siglas cruas no texto do TTS.
- Inventar estudos ou números ("pesquisas mostram que 73%...").
- Publicar todo dia o mesmo template só com o título trocado. É exatamente o alvo da política de "conteúdo inautêntico", em vigor desde 15/07/2025 e clarificada em 07/2026 (PlagiarismToday; OutlierKit).
- Fazer o personagem de IA dar orientação de saúde em tom de autoridade médica. Isso é categoria de risco (OutlierKit). Fique em técnica de treino e registro.

---

## Ideias para testar (A/B simples)

1. **Gancho "erro específico" vs. "payoff primeiro"** no mesmo tema, comparando a métrica "visualizou vs. deslizou".
2. **40 s vs. 60 s**, comparando a média assistida e o tempo total assistido.
3. **Tipo de gatilho final** (comenta número vs. palavra-chave + desafio vs. manda pro amigo vs. enquete vs. salva e volta), comparando comentários, compartilhamentos, salvamentos e retenção nos últimos 5 s. O tipo usado fica em `gatilho_tipo` no data.json.
4. **Texto na tela que complementa vs. que repete a fala no 0 s**, comparando "visualizou vs. deslizou".
5. **Cena nova a cada 2 s vs. a cada 4 s**, comparando a média assistida.
6. **Voz em velocidade 1,0 vs. 1,1**, com o mesmo roteiro encurtado, comparando a média assistida.
7. **Prompt com 3 roteiros-exemplo vs. prompt só com regras**, numa avaliação cega pelo humano mais a retenção.
8. **Feedback de métricas no prompt** (últimos 5 vídeos) vs. sem, ao longo de 2 semanas.

---

## Fontes

| # | Título | Link | Data | Plataforma |
|---|---|---|---|---|
| 1 | YouTube Shorts Analytics: The Metrics That Matter (2026) | https://1of10.com/blog/youtube-shorts-analytics/ | 12/09/2026 | Blog (1of10) |
| 2 | The Ideal YouTube Shorts Length & Format for Retention | https://www.opus.pro/blog/ideal-youtube-shorts-length-format-retention | 11/11/2025 | Blog (OpusClip) |
| 3 | YouTube Shorts Hooks and Curiosity Loops (John Scott) | https://www.socialmediaexaminer.com/youtube-shorts-hooks-and-curiosity-loops-that-explode-your-views/ | 21/05/2026 | Social Media Examiner |
| 4 | Best TikTok Hooks in 2026: What Reddit Creators Actually Use | https://wildandfreetools.com/blog/best-tiktok-hooks-reddit-2026/ | 03/2026 | Blog (síntese de Reddit) |
| 5 | Hook Engineering: The Science of the First 3 Seconds | https://dev.to/bulkdl/hook-engineering-the-science-of-the-first-3-seconds-in-short-form-video-2026-2jp9 | 2026 | DEV Community |
| 6 | What Viral Faceless Shorts Have in Common | https://easyviral.ai/blog/we-analyzed-500-viral-faceless-shorts | 11/05/2026 | Blog (EasyViral) |
| 7 | RR#8 – Study this hook edit | https://georgeblackman.substack.com/p/rr8-study-this-hook-edit | 13/01/2023 | Substack |
| 8 | How I'm Prompting Claude AI to Maximize Engagement for Short-Form Videos | https://creativeworkflowlab.substack.com/p/how-im-prompting-claude-ai-to-maximize | s/d | Substack |
| 9 | How to Stop Claude Writing Like an AI | https://willfrancis.com/how-to-stop-claude-writing-like-an-ai/ | 13/03/2026 | Blog |
| 10 | The De-Slop Prompt Stack | https://dev.to/promptway/the-de-slop-prompt-stack-six-prompts-that-stop-claude-and-chatgpt-from-sounding-like-a-robot-36ji | 06/2026 | DEV Community |
| 12 | The best guide to spotting AI writing comes from Wikipedia | https://techcrunch.com/2025/11/20/the-best-guide-to-spotting-ai-writing-comes-from-wikipedia/ | 20/11/2025 | TechCrunch |
| 13 | ElevenLabs – Text to speech best practices | https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices.md | atual | Docs oficiais |
| 14 | ElevenLabs – Prompting Eleven v3 | https://elevenlabs.io/docs/best-practices/prompting/eleven-v3 | atual | Docs oficiais |
| 15 | How to Make Faceless YouTube Shorts With Claude Code | https://learnwithhasan.com/guide/how-to-make-faceless-youtube-shorts-with-claude-code/ | 30/07/2026 | Blog/guia |
| 16 | Show IH: I automated 3 YouTube channels with GitHub Actions | https://www.indiehackers.com/post/show-ih-i-automated-3-youtube-channels-with-github-actions-heres-the-full-stack-c73d2096f9 | 15/05/2026 | Indie Hackers |
| 17 | I let AI agents run my YouTube channel for 6 weeks | https://dev.to/wcamon/i-let-ai-agents-run-my-youtube-channel-for-6-weeks-heres-what-actually-happened-21b1 | 16/02/2026 | DEV Community |
| 18 | YouTube Targets "Inauthentic" Content | https://www.plagiarismtoday.com/2025/07/08/youtube-targets-inauthentic-content/ | 08/07/2025 | Blog (PlagiarismToday) |
| 19 | YouTube AI Slop Crackdown 2026 | https://outlierkit.com/resources/youtube-ai-slop-crackdown-2026/ | 03/03/2026 (atual. 03/10/2026) | Blog (OutlierKit) |

Observação: o site pasqualepillitteri.it bloqueou a leitura (anti-bot), por isso não foi usado. X/Twitter e Hacker News não trouxeram material citável nas buscas.
