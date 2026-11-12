# Produção diária — Fábrica Brio (3 perfis)

Roteiro que a tarefa agendada segue todo dia. Trabalhe sozinho; só pare para perguntar ao usuário em último caso.
Leia antes o `AGENTS.md` (regras fixas). **Nunca imprima, grave ou commite chave/token.** Tudo que precisa de segredo roda nos workflows do GitHub.

## 0. Preparar
```bash
cd <repo fabricabrio> && git pull -q && bash motor/instalar.sh
```
O render roda dentro de `motor/` (`python3 build2s.py ...` para BRIO, `python3 build3.py ...` para FIBRA e DIA UM). Saída em `motor/out/`.

## 1. Quanto produzir (para AMANHÃ)
- Sprint de 8 dias a partir de `config.sprint_inicio` (13/11/2026 = dia 1). Dia ímpar: DIA UM 5, FIBRA 3. Dia par: FIBRA 5, DIA UM 3. BRIO sempre 8.
- Desconte o que já está agendado para amanhã (ver estado no passo 2).
- Horários (Brasília; no D1 grave em **UTC = BRT + 3 h**):
  - BRIO: 07:00, 09:30, 12:00, 14:30, 17:00, 18:30, 20:30, 22:00
  - DIA UM (5): 08:00, 11:30, 15:30, 19:30, 21:30 · (3): 08:00, 15:30, 19:30
  - FIBRA (5): 08:30, 12:30, 16:30, 19:00, 21:00 · (3): 12:30, 19:00, 21:00

## 2. Ler o estado (posts, métricas, temas, cliques)
Escreva `jobs/d1.json` = `{"nome": "estado-AAAAMMDD-HHMM", "videos": []}`, commit e push na `main`. O workflow **d1-job** grava `d1/estado_atual.json` no branch `previas` (~1 min):
```bash
git fetch -q origin previas && git show FETCH_HEAD:d1/estado_atual.json > /tmp/estado.json
```
Use `estado.metricas` para decidir a pauta: formatos com views acima da média do perfil viram série; formato abaixo de 1k em 2 tentativas sai da pauta.

## 3. Pauta (só o que tem chance de 10k+)
- Pesquise na web os Reels/TikToks de treino que estão performando nas últimas 3 semanas (BR e EUA). Use `claude/meta-sprint-modelagem-qa.md` do projeto (tabela de formatos medidos) e o histórico em `referencia/`.
- Cada vídeo precisa de **evidência** (formato com 2×+ a média de contas do nicho, ou um dos nossos que performou). Sem evidência, não gaste crédito.
- Mix: 60% variações do que performou em nós, 30% formatos modelados ainda não testados, 10% experimento.
- Território: BRIO = técnica, erros, progressão · FIBRA = o que acontece dentro do corpo · DIA UM = começar, hábito, vergonha, idade.
- `tema_canonico` curto e único: **nunca** repetir um tema que exista em `estado.temas` (qualquer perfil). O d1-job recusa tema repetido de outro perfil.

## 4. Roteiro (30–40 s)
- 480–620 caracteres de narração. 1ª frase com até 8 palavras, gancho nos 2 primeiros segundos.
- 7 a 9 beats (`t1`/`t2` curtos na tela; `text` = fala).
- Final: gatilho específico com **palavra-chave em MAIÚSCULAS** (é ela que dispara a DM com o link) + frase-ponte para uma função real do app + fixa "Registre e acompanhe seus treinos gratuitamente. Link na bio."
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
- Siga `motor/GUIA_ANIMACAO.md`. O que fica na frente é desenhado por último; nada atravessa texto; sem quadradinho/kicker no topo.
- Força/evolução: boneco fazendo rosca com halter (`curl_up`/`curl_down` + `dumbbell`) ou carga subindo. **Não** use pose de braço atrás da cabeça.
- Teste rápido: `python3 build3.py roteiro_x scenes_x --stills` (2 quadros por beat) antes do render completo.

## 7. QA — 7 portões (nada vai ao ar sem passar)
1. Anti-repetição: tema canônico novo; gancho não repete a fórmula do vídeo anterior do mesmo perfil.
2. Roteiro: faixa de caracteres, 1ª frase ≤ 8 palavras, frase fixa exata, só funções reais, "Bríu" na fala.
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
   Legenda: gancho + 👇, linha do gatilho com a palavra-chave ("Comenta X que eu te mando no direct ..."), 4–6 hashtags (a 1ª é a do perfil: #brio, #fibratreino, #diaumtreino). Escreva "Brio", nunca "Bríu".
3. Push → workflow **d1-job** grava e devolve `d1/<nome>/estado.json` com `relatorio.gravados` e `relatorio.recusados`. Corrija os recusados.
4. O Worker publica sozinho no horário (cria o contêiner 20 min antes). Posts com `status='erro'` aparecem no estado: investigue e reagende.

## 9. Fechar
Mande uma notificação push curta e termine com 3–5 linhas: vídeos agendados por perfil, créditos gastos/saldo, vídeos descartados e por quê, e o que as métricas de ontem mudaram na pauta.
