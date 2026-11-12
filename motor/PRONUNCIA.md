# Pronúncia do nome do app (BRIO) — regra e status

**Regra (confirmada pelo usuário em 09/11/2026, 15h30: "a pronúncia fica Bríu"):** na NARRAÇÃO, o nome do app vai escrito **`Bríu`** no campo `text` do roteiro. Exemplo: "No Bríu você registra cada série." As grafias "Brío"/"Bríô" foram REJEITADAS (o narrador fala "briô"). Escrito "BRIO", a voz do ElevenLabs (Marcio, eleven_multilingual_v2) lê em inglês, como "Braio". **Na TELA** (títulos t1/t2, chips, logo) continua **BRIO** em maiúsculas.

**Como corrigir um vídeo que saiu com "Braio":** gere de novo SÓ a frase que tem o nome (tts.tts com previous_text/next_text, texto com "Bríu"), encaixe no lugar dela no áudio e re-renderize. Nunca regenere a narração inteira.

**Como conferir:** extraia os últimos ~22 s do mp4 (`ffmpeg -ss <duração-22> -i video.mp4 -vn -ac 1 -ar 16000 fim.mp3`) e transcreva com o speech-to-text do ElevenLabs (`model_id=scribe_v1`, `language_code=por`). O trecho deve trazer o nome lido em português ("Brio"/"Brío") e o fechamento "Registre e acompanhe seus treinos gratuitamente. Link na bio." A transcrição confirma a frase, mas não garante 100% a sílaba tônica: na dúvida, ouça o trecho.

## Status dos vídeos do BRIO (atualizado em 09/11/2026, 15h40)
| Vídeo | Situação | Postar em | Pronúncia no áudio | O que falta |
|---|---|---|---|---|
| brio-05-quando-subir-carga | postado 09/11 12:00 | — | **Bríu — ok** | — |
| brio-04-descanso | pronto | 09/11 20:30 | **Bríu — ok** (frase do nome regravada 09/11 15h30, conferida) | nada |
| brio-07-ego-lifting | pronto | 09/11 22:00 | **Bríu — ok** (frase do nome regravada 09/11 15h30, conferida) | nada |
| brio-06-elevacao-lateral | pronto | 10/11 07:00 | **Bríu — ok** (frase do nome regravada 09/11 15h30, conferida) | nada |
| brio-09-mesmo-musculo | pronto | 10/11 12:00 | **Bríu — ok** (frase do nome regravada 09/11 15h30, conferida) | nada |
| brio-08-cardio | pronto | 10/11 18:00 | **Bríu — ok** (frase do nome regravada 09/11 15h30, conferida) | nada |
| brio-02-falha-toda-serie | pronto | 09/11 18:00 | **Bríu — ok** (frase do nome regravada 09/11 15h30, conferida) | nada |
| brio-03-tempo-resultado | postado 09/11 07:00 | — | "Brío" (versão no ar) | — |
| brio-01-dor-no-dia-seguinte | postado 08/11 18:00 | — | versão antiga no ar | — |
| brio-00-treina-1-ano | reserva | — | "Bríô" (errado) | só se for usar |

**Como foi feito o brio-05 (modelo para os outros):** narração original até o início da última cena + só a última cena gerada de novo (texto novo com "Bríu", ~210 créditos) → arquivo `audio/brio_05_narracao_v2.mp3` no painel; o roteiro aponta para ele em `NARRATION = {"file", "starts"}` e o build2.py usa esse áudio sem chamar o ElevenLabs.
