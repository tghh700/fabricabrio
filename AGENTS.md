# Fábrica Brio — regras para agentes (Claude e Codex)

Este repositório é só código. Roteiros, pauta, métricas e tarefas ficam no banco D1 `fabrica-brio` (Cloudflare). Segredos ficam apenas nos Secrets do GitHub e do Worker — nunca em arquivos, logs ou no D1.

## Perfis
| perfil | Instagram | vídeos/dia | território |
|---|---|---|---|
| brio | @briotreino | 4 | resultado, tempo, mitos, progressão |
| fibra | @fibratreino | 4 | o que acontece dentro do corpo |
| diaum | @diaumtreino | 0 — PAUSADO (17/11) | começar, hábito, iniciantes |

Escala (config.escala no D1, decisão do usuário em 17/11): **BRIO 4/dia e FIBRA 4/dia** (divididos igualmente). **DIA UM pausado** — não produzir nem agendar até o usuário liberar.

**Regra de pauta (17/11):** todo tema precisa estar validado por um vídeo que JÁ performou — nosso (ver métricas em midia/<perfil>.json no branch previas) ou de outro perfil, em qualquer idioma (PT, EN, ES…), com link/registro da evidência no roteiro. Nada parecido com o que foi mal (lista em PRODUCAO.md §3).

## Regras fixas
- Nunca imprimir, commitar ou gravar no D1 um token, chave ou segredo.
- Nunca o mesmo vídeo ou tema canônico em dois perfis.
- Narração: "Bríu" na fala; na escrita, "Brio" — legenda, DM, hashtags e texto na tela NUNCA levam "Bríu" (o Worker e o d1-job corrigem, mas é erro).
- Todo vídeo tem conclusão antes do CTA. O CTA cita o Brio e termina em "Link na bio.", mas a frase é livre (não há frase fixa).
- Só citar funções reais do app (registrar séries, acompanhar evolução, orientação após o treino).
- Nada vai ao ar sem passar pelos 7 portões de QA (ver PRODUCAO.md §7).
- Qualidade mínima de animação (usuário, 14/11): cena "boneco parado + ícone" é simples demais. Use `motor/cenas_v2.py` (boneco executando o movimento, painéis errado/certo, contadores, cenário de academia, transição entre cenas). Nunca dois bonecos sem motivo; nunca caracteres que a fonte não tem (✓ ✦ viram quadradinho — desenhe com check_mark).

## Protocolo de tarefas (tabela `tasks` no D1)
- Pegue tarefa só com reserva (`claimed_by`, `lease_until` = agora + 30 min).
- Ao terminar: `status='feita'` e `saida` preenchida. Ao falhar: `tentativas+1`; na 3ª falha, `status='escalada'` e `para='opus'`.
- Pode criar tarefa para outro agente (`para` = opus | sonnet | haiku | codex | qualquer).

## Estrutura
- `worker/` — Worker maestro (webhook de comentários, link de clique, publicador, cron).
- `scripts/` — scripts Python usados pelos workflows.
- `.github/workflows/` — automações (deploy, testes, render, agentes).
