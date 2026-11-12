# Fábrica Brio — regras para agentes (Claude e Codex)

Este repositório é só código. Roteiros, pauta, métricas e tarefas ficam no banco D1 `fabrica-brio` (Cloudflare). Segredos ficam apenas nos Secrets do GitHub e do Worker — nunca em arquivos, logs ou no D1.

## Perfis
| perfil | Instagram | vídeos/dia | território |
|---|---|---|---|
| brio | @briotreino | 18 | técnica, erros, progressão |
| fibra | @fibratreino | 12 | o que acontece dentro do corpo |
| diaum | @diaumtreino | 10 | começar, hábito, iniciantes |

## Regras fixas
- Nunca imprimir, commitar ou gravar no D1 um token, chave ou segredo.
- Nunca o mesmo vídeo ou tema canônico em dois perfis.
- Narração: "Bríu" na fala; na escrita, "Brio".
- Só citar funções reais do app (registrar séries, acompanhar evolução, orientação após o treino).
- Nada vai ao ar sem passar pelos 7 portões de QA (ver docs do projeto).

## Protocolo de tarefas (tabela `tasks` no D1)
- Pegue tarefa só com reserva (`claimed_by`, `lease_until` = agora + 30 min).
- Ao terminar: `status='feita'` e `saida` preenchida. Ao falhar: `tentativas+1`; na 3ª falha, `status='escalada'` e `para='opus'`.
- Pode criar tarefa para outro agente (`para` = opus | sonnet | haiku | codex | qualquer).

## Estrutura
- `worker/` — Worker maestro (webhook de comentários, link de clique, publicador, cron).
- `scripts/` — scripts Python usados pelos workflows.
- `.github/workflows/` — automações (deploy, testes, render, agentes).
