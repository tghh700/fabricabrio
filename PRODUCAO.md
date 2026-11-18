# Produção diária — Fábrica Brio (3 perfis)

Roteiro que a tarefa agendada segue todo dia. Trabalhe sozinho; só pare para perguntar ao usuário em último caso.
Leia antes o `AGENTS.md` (regras fixas). **Nunca imprima, grave ou commite chave/token.** Tudo que precisa de segredo roda nos workflows do GitHub.

## 0. Preparar
```bash
cd <repo fabricabrio> && git pull -q && bash motor/instalar.sh
```
O render roda dentro de `motor/` (`python3 build2s.py ...` para BRIO, `python3 build3.py ...` para FIBRA e DIA UM). Saída em `motor/out/`.

## 1. Quanto produzir (para AMANHÃ)
- Escala (`config.escala`, desde 17/11): **BRIO 4/dia, FIBRA 4/dia. DIA UM pausado** (não produza nem agende).
- Desconte o que já está agendado para amanhã e reaproveite o estoque com status `pausado` **só se o tema passar na regra do §3**.
- Horários (Brasília; no D1 grave em **UTC = BRT + 3 h**), intercalados:
  - BRIO: 11:30, 14:00, 18:00, 21:00
  - FIBRA: 12:30, 16:00, 19:00, 22:00

## 2. Ler o estado (posts, métricas, temas, cliques)
Escreva `jobs/d1.json` = `{"nome": "estado-AAAAMMDD-HHMM", "videos": []}`, commit e push na `main`. O workflow **d1-job** grava `d1/estado_atual.json` no branch `previas` (~1 min):
```bash
git fetch -q origin previas && git show FETCH_HEAD:d1/estado_atual.json > /tmp/estado.json
```
Use `estado.metricas` para decidir a pauta: formatos com views acima da média do perfil viram série; formato abaixo de 1k em 2 tentativas sai da pauta.

## 3. Pauta (só o que tem chance de 10k+)
### Validação obrigatória (usuário, 17/11)
Cada tema precisa de **evidência de que já funcionou**: (a) um vídeo nosso acima da média do perfil, ou (b) um Reels/TikTok/Short de outro perfil com views bem acima da média dele, em qualquer idioma (pesquise em PT, EN e ES). Registre a evidência (link ou "nosso: <id> <views>") no comentário do roteiro. Sem evidência, não produz.

### O que foi BEM e o que foi MAL (métricas de 17/11 — releia midia/*.json a cada rodada)
- **BRIO bem (1.400–3.900 views):** quanto tempo pra ver resultado (3,9k), 30 dias de academia (3,4k), jejum queima mais? (2,3k), mesmo músculo todo dia (1,7k), treina pesado e não cresce (1,7k), parou 2 semanas perdeu? (1,7k), supino +10 kg quanto tempo (1,7k), falha em toda série (1,5k), como saber se está evoluindo (1,5k), ombro não cresce (1,5k), semana leve/deload (1,4k), alongar antes (1,4k), ganhar músculo sem peso (1,4k). → **resultado/tempo/perda, mitos populares, "por que não cresce".**
- **BRIO mal (< 600):** correção de técnica "se o seu X tá assim, para" (rosca, desenvolvimento, punho, respiração), aquecimento, supino travado, suplementos (whey, proteína, creatina, BCAA), falso magro, genética/amigo cresce mais, carga no chute, tempo de treino por dia. → **não fazer mais esses formatos/temas.**
- **FIBRA bem:** sensação no corpo explicada — enjoo no treino de perna (2,6k, 37 compartilhamentos), queimação não é ácido lático (1,6k), braço inchado/pump (1,1k), descanso/músculo cresce depois (1,4k).
- **FIBRA mal:** "músculos que trabalham no X" (agachamento 155, supino 242), tremor (208), cãibra (246). → priorize **"o que é essa sensação?"** (dor, ardência, tontura, falta de ar, coração acelerado, suor, arrepio, fome depois do treino…).
- **Atualização 18/11 (midia/*.json):** média FIBRA 913, BRIO 1.043. FIBRA: enjoo na perna subiu para **4.710 (5,2×, 112 compartilhamentos)** — o formato "nomear a sensação" é o carro-chefe; barra/músculos 1.978 (exceção dos "músculos que trabalham"); estalo no joelho 396 e velocista×maratonista 22 foram mal (articulação/tipo de fibra não é sensação). BRIO: "músculo pesa mais que gordura" 1.222, "parou e perdeu tudo" 1.224, "balança subiu" 1.373 (mitos/perda seguem na média); "músculo não vira gordura" 237 e "musculação deixa baixo" 130 (poucas horas no ar — medir). Em produção 19/11 (medir): FIBRA coceira nas pernas, dor de cabeça na série, rosto vermelho, pontada na barriga.
- **Estoque pausado do BRIO:** os vídeos restantes têm 30–35 s (formato antigo, 580–640 caracteres) — fora da regra de 20–25 s; não reagendar sem refazer a narração curta.
- **Atualização 17/11 à tarde (midia/*.json):** média BRIO 1.048, FIBRA 826. Lote nutricional do BRIO foi mal: proteína/dia 347, whey 322, genética 403, falso magro 43 → **nada de dieta/suplemento no BRIO** (cerveja 1.376 e "musculação emagrece" 1.253 foram exceção por serem pergunta de perda/mito). Quanto músculo por mês 1.291 (resultado/tempo segue acima da média). FIBRA: descanso 727, supino 242. Em produção 18/11 (medir): FIBRA tontura, gosto de sangue, fome que volta, coração antes da série; BRIO estoque altura, mulher pesado, emagrecer rápido, 1×/semana.

- Pesquise na web os Reels/TikToks de treino que estão performando nas últimas 3 semanas (BR e EUA). Use `claude/meta-sprint-modelagem-qa.md` do projeto (tabela de formatos medidos) e o histórico em `referencia/`.
- Cada vídeo precisa de **evidência** (formato com 2×+ a média de contas do nicho, ou um dos nossos que performou). Sem evidência, não gaste crédito.
- Mix: 60% variações do que performou em nós, 30% formatos modelados ainda não testados, 10% experimento.
- Território: BRIO = técnica, erros, progressão · FIBRA = o que acontece dentro do corpo · DIA UM = começar, hábito, vergonha, idade.
- **Antes de fechar a pauta, compare com o que já foi ao ar** — inclusive os 27 vídeos antigos do BRIO em `referencia/brio_data_painel_antigo.json` (o BRIO 32 "dor no dia seguinte" foi descartado em 14/11 por repetir o BRIO 01): rode o workflow `listar-midia` (push em `jobs/listar.txt`) e leia `midia/<perfil>.json` no branch `previas` (legendas completas de tudo que está publicado) e os roteiros em `referencia/brio_data_painel_antigo.json`. Não pode repetir vídeo nem a ideia central de um vídeo já postado em qualquer perfil (ex.: "força sobe antes do músculo" já saiu no BRIO 03 e 10).
- `tema_canonico` curto e único: **nunca** repetir um tema que exista em `estado.temas` (qualquer perfil). O d1-job recusa tema repetido de outro perfil.

### Desempenho real do BRIO (informado pelo usuário em 14/11 — use até as métricas da API voltarem)
| vídeo | views |
|---|---|
| Quanto tempo pra ver resultado? (BRIO 03) | 3.645 |
| 30 dias de treino, e agora? (BRIO 10) | 3.238 |
| Treino em jejum queima mais? (BRIO 14) | 2.390 |
| Treina pesado e não cresce? (BRIO 15) | 1.958 |
| Ficou sem treinar? (BRIO 12) | 1.912 |
| demais | ~1.300–1.400, e os mais recentes abaixo de 1.000 |
Padrão: o que performa é **pergunta sobre resultado/tempo/perda** ("quanto tempo", "o que muda", "perdi?") e **mito popular** (jejum). Técnica de exercício e organização de treino ficam na média ou abaixo. Pauta: ≥60% nesse padrão (variações novas, sem repetir tema).

## 4. Roteiro (20–25 s — decisão do usuário em 16/11, pelas métricas)
- Métricas de 16/11 (33 Reels do BRIO): tempo médio assistido de 13–17 s em vídeos de 30–35 s — a pessoa sai antes da conclusão. O único com retenção alta ("30 dias", 27,5 s) entrega a resposta logo. Comentários ≈ 0; o que espalha é compartilhamento e salvamento.
- **330–430 caracteres de narração** (≈20–25 s). 1ª frase com até 8 palavras, gancho nos 2 primeiros segundos.
- **A resposta da pergunta do gancho aparece até os 10 s.** Nada de introdução ("normal", "muita gente acha"): pergunta → resposta → por quê/como → conclusão → CTA.
- 5 a 6 beats (`t1`/`t2` curtos na tela; `text` = fala). Um único dado ou número forte por vídeo.
- CTA em no máximo 1 frase (≈3 s). Pode trocar o pedido de comentário por "manda pra quem precisa ouvir isso" ou "salva pra lembrar" quando combinar mais com o tema — mas mantenha a palavra-chave em maiúsculas para a DM.
- **Conclusão antes do CTA (obrigatória, regra do usuário em 12/11):** o vídeo não pode terminar no meio do raciocínio e pular pro anúncio. Antes do CTA vem um beat de conclusão (1–2 frases: "Resumindo/Então..." amarrando a ideia e dizendo o que a pessoa faz com isso). No FIBRA, a cena `conclusao_factory` (quadro "CONCLUSÃO" com 3 ✓).
- Final: gatilho específico com **palavra-chave em MAIÚSCULAS** (é ela que dispara a DM com o link) + menção ao Brio ligada ao tema, com uma função real do app + "Link na bio." **Não existe frase fixa**: "Registre e acompanhe seus treinos gratuitamente" é só um exemplo; adapte ao vídeo (ex.: "Comenta PUMP que eu te mando como acompanhar sua carga no Bríu. Link na bio."). Na tela, use `cta_flex(palavra, linhas)` com linhas adaptadas.
- Funções reais do app: registrar séries, acompanhar evolução, orientação após o treino. Nada além disso.
- Narração escreve "Bríu"; tela e legenda escrevem "Brio". Sem promessa médica. FIBRA: anote a fonte de cada afirmação científica no comentário do roteiro.

## 5. Narração (ElevenLabs v4, via workflow)
Um único `jobs/eleven.json` com todos os vídeos do dia (`op: "tts"`, `model_id: "eleven_v4"`, `timestamps: true`, `seed: 7`). Vozes:
| perfil | voice_id | settings |
|---|---|---|
| brio (Marcio) | plASsyS7JE6GCAvx9uIc | stability .5, similarity .8, style .2, speed 1.1 |
| fibra (Will) | r3KkFedJ4n8aabIZ0RFQ | stability .5, similarity .75, style 0, speed 1.08 |
| diaum (Dani) | PznTnBc8X6pvixs9UkQm | stability .45, similarity .75, style 0, speed 1.05 |

Marcações de emoção v4 ([curious], [warm], [matter-of-fact], [encouraging]) só no começo de frase. Push → workflow **eleven-job** (~1 min) → no branch `previas`, pasta `<nome>/` (`<id>.mp3`, `<id>.json`, `creditos.json`): `git fetch -q origin previas && git show FETCH_HEAD:<nome>/<id>.mp3 > motor/audio/<id>.mp3`. Confira `creditos.json` (`erros` vazio). Nunca regenere um vídeo inteiro para consertar uma palavra.

Depois, aperte o ritmo e ache o início de cada beat:
```python
from apertar import apertar; import json, re
al = json.load(open(f"audio/{id}.json")); chars = "".join(al["characters"]); st = al["character_start_times_seconds"]
_, mapa = apertar(f"audio/{id}.mp3", f"audio/{id}_tight.mp3")
starts, pos = [], 0
for b in BEATS:
    k = chars.find(re.sub(r"\[[^\]]*\]", "", b["text"]).strip()[:14], pos); k = pos if k < 0 else k
    starts.append(round(mapa(st[k]), 3)); pos = k + 1
# no roteiro: NARRATION = {'file': 'audio/<id>_tight.mp3', 'starts': starts}
```

## 6. Animação
- BRIO: `roteiro_<id>.py` + `scenes_<id>.py` no padrão de `roteiro_brio_25v4.py` / `scenes_brio_25v4.py`, render com `build2s.py` (área segura automática).
- FIBRA / DIA UM: padrão de `roteiro_fibra_p1.py`/`scenes_fibra_p1.py` e `roteiro_diaum_p1.py`/`scenes_diaum_p1.py`, render com `build3.py`.
- **Sem logo e sem barra de progresso no rodapé** (o usuário vetou em 12/11: compete com a legenda do Reels). Os builders já não desenham; não recoloque.
- **Checklist de execução (portão 6):** supino = barra sobre o peito/ombros, nunca sobre o rosto; flexão/prancha alta = braço esticado embaixo do ombro e corpo reto; agachamento numa perna = a outra perna à frente; tríceps francês = braço vertical e halter descendo ATRÁS da cabeça; perna levantada sai do quadril. Confira cada exercício em 3 quadros (início, meio, fim) antes de agendar.
- **Plano certo para cada movimento:** se o movimento não fica claro de perfil (ex.: desenvolvimento, elevação, abdução), desenhe de frente (`front_presser` em `brio_kit2.py`) e mostre o que só aparece de lado num quadro "VISTA LATERAL" (`spine_inset`). Nunca deixe um movimento anatomicamente errado só porque o boneco é de perfil.
- **Texto dentro do celular do CTA:** `app_title` com no máximo ~15 caracteres (ex.: "DESENVOLVIMENTO", "AGACHAMENTO"); o `cta_brio` reduz a fonte se passar, mas confira no quadro do CTA que nada sai da tela do celular.
- Siga `motor/GUIA_ANIMACAO.md`. O que fica na frente é desenhado por último; nada atravessa texto; sem quadradinho/kicker no topo.
- Força/evolução: boneco fazendo rosca com halter (`curl_up`/`curl_down` + `dumbbell`) ou carga subindo. **Não** use pose de braço atrás da cabeça.
- Teste rápido: `python3 build3.py roteiro_x scenes_x --stills` (2 quadros por beat) antes do render completo.

## 6b. Padrão visual mínimo (usuário, 14/11)
- Nada de cena "boneco parado + ícone". Cada beat tem ação: boneco executando (act_curl, act_squat, act_press, act_walk, act_tired em `cenas_v2.py`), painel comparativo (`split`), contador/bateria/semana animados, cenário de academia ao fundo e entrada com transição (`wipe_in`). Modelo: `v2_34_ordem.py` … `v2_38_pernas.py`.
- Uma figura por cena, salvo comparação explícita. Cama = só `sleeper()` (o vídeo 33 v1 tinha um boneco em pé ao lado de outro deitado e foi apagado pelo usuário).
- **Glifos:** Anton/Space Mono não têm ✓ ✦ — saem como quadradinho. Rode antes do render: `grep -n "✓\|✦" scenes_*.py v2_*.py` tem que dar vazio em texto desenhado (use `check_mark`).

## 7. QA — 7 portões (nada vai ao ar sem passar)
1. Anti-repetição: tema canônico novo; gancho não repete a fórmula do vídeo anterior do mesmo perfil.
2. Roteiro e legenda: faixa de caracteres, 1ª frase ≤ 8 palavras, conclusão antes do CTA, CTA menciona o Brio e termina em "Link na bio.", só funções reais, "Bríu" só na fala; legenda, DM e tela com "Brio" (`grep -i "br[íi]u"` na legenda tem que dar vazio).
3. Cenas: tudo entre y 250 e 1570 e com 120 px livres à direita; textos cabem na caixa.
4. Arquivo: `python3 qa_video.py out/<id>.mp4 --starts <starts>` (resolução, codec, 15–60 s, tela preta, congelado > 3 s, buraco de áudio, volume).
5. Áudio: ouça/inspecione o alinhamento — "Bríu" e números certos; nenhuma palavra cortada.
6. Visual: abra `out/<id>_folha.png` e `out/<id>_cortes.png` com a ferramenta Read e procure texto sobreposto/cortado, membro solto, objeto atravessando, cor errada do perfil.
7. Revisão final (você, como Opus): 1 em cada 4 vídeos assistidos quadro a quadro em 5 pontos + todo vídeo que algum portão marcou.
Falhou → conserte e repita. Na 3ª falha do mesmo vídeo, descarte-o, registre o motivo no resumo e siga.

## 8. Publicar e agendar
1. Copie o mp4 aprovado para o branch `midia` como `<perfil>/<id>.mp4` (worktree: `git worktree add ../midia midia`), commit e push.
2. Escreva `jobs/d1.json`:
```json
{"nome": "agenda-AAAAMMDD", "videos": [{"id": "fibra-07-xxx", "perfil": "fibra", "tema_canonico": "...", "gancho": "...", "gatilho_tipo": "2",
  "palavra_chave": "CARGA", "arquivo": "fibra/fibra-07-xxx.mp4", "legenda": "gancho 👇\nCTA com a palavra-chave\n\n#hashtags", "hashtags": "#...",
  "duracao_s": 34.2, "dm_texto": "opcional, com {link}", "agendado_para": "2026-11-13 11:30:00"}],
 "creditos": [{"video_id": "fibra-07-xxx", "quantidade": 590}]}
```
   **Nunca copie a fala do roteiro para a legenda sem trocar "Bríu" por "Brio"** — "Bríu" é só a pronúncia; na escrita (legenda, DM, tela, hashtags) é sempre "Brio". O d1-job e o Worker corrigem se escapar, mas isso conta como falha do portão 2.
   Legenda: gancho + 👇, linha do gatilho com a palavra-chave ("Comenta X que eu te mando no direct ..."), 4–6 hashtags (a 1ª é a do perfil: #brio, #fibratreino, #diaumtreino). Escreva "Brio", nunca "Bríu".
3. Push → workflow **d1-job** grava e devolve `d1/<nome>/estado.json` com `relatorio.gravados` e `relatorio.recusados`. Corrija os recusados.
4. O Worker publica sozinho no horário (cria o contêiner 20 min antes). Posts com `status='erro'` aparecem no estado: investigue e reagende.

## 9. Fechar
Mande uma notificação push curta e termine com 3–5 linhas: vídeos agendados por perfil, créditos gastos/saldo, vídeos descartados e por quê, e o que as métricas de ontem mudaram na pauta.
