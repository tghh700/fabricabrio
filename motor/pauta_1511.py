"""Pauta BRIO de 15/11/2026 — 12 vídeos inéditos (FIBRA e DIA UM de 15/11 já cobertos pelo estoque).
Evidência por vídeo (formato medido em claude/meta-sprint-modelagem-qa.md ou fonte):
 39 descida  — erro encenado + correção (20x) · 40 máquina — crença declarada errada (9x), Haugen et al. 2023 (BMC Sports Sci Med Rehabil)
 41 drop set — número/tempo carimbado (7x), Coleman et al. 2022 · 42 bi-set — idem, Iversen et al. 2021 (Sports Med)
 43 lado fraco — forma errada x certa (23x) · 44 séries por treino — crença errada (9x) · 45 barra — níveis/progressão (8x)
 46 música — crença (9x), Terry et al. 2020 (Psychol Bull, 139 estudos) · 47 oscilação — nomear a sensação (23x)
 48 cinto — errado x certo (23x) · 49 pegada/strap — erro encenado (20x) · 50 empurrar x puxar — erro comum (20x)
Sem métricas por post no D1 (coleta ainda falha): pauta segue a tabela de formatos medidos + o único sinal real (DM do BRIO 25)."""
P = {}
def V(id, tema, palavra, gat, beats, hora):
    P[id] = dict(tema=tema, palavra=palavra, gat=gat, beats=beats, hora=hora)

V('brio_39_descida', 'controlar a descida do peso (fase excêntrica)', 'DESCIDA', 2, [
 ('hook', 'DEIXA O PESO', 'CAIR?', '[serious] Você deixa o peso cair?'),
 ('metade', 'A DESCIDA É', 'METADE DA REPETIÇÃO.', 'A descida é metade da repetição. E muita gente desperdiça essa metade.'),
 ('cai', 'PESO CAINDO,', 'GRAVIDADE TRABALHA.', 'Quando o peso cai rápido, quem trabalha é a gravidade, não o seu músculo.'),
 ('tranco', 'E O TRANCO', 'VAI PRA ARTICULAÇÃO.', 'E o tranco no final vai pra articulação, não pro músculo.'),
 ('conta', 'SOBE FIRME,', 'DESCE EM 2 SEGUNDOS.', 'O certo: sobe com firmeza e desce contando dois segundos.'),
 ('lento', 'NÃO É CÂMERA LENTA.', 'É CONTROLE.', '[matter-of-fact] Não precisa ser em câmera lenta. Precisa ser controlado, do começo ao fim.'),
 ('peso', 'SEM CONTROLE?', 'PESO ALTO DEMAIS.', 'Não consegue controlar a descida? O peso está alto demais pra hoje.'),
 ('conc', 'RESUMINDO:', 'VOCÊ CONTROLA.', 'Resumindo: quem manda na descida é você, não a gravidade. Dois segundos, sempre controlado.'),
 ('cta', 'COMENTA', 'DESCIDA.', 'Comenta DESCIDA que eu te mando como registrar suas séries no Bríu e ver a carga subir. Link na bio.'),
], '08:30')
V('brio_40_maquina', 'máquina constrói músculo igual a peso livre', 'MÁQUINA', 2, [
 ('hook', 'MÁQUINA', 'DÁ MÚSCULO, SIM.', '[serious] Máquina dá músculo, sim.'),
 ('mito', 'SÓ BARRA E HALTER?', 'É MITO.', 'Muita gente acha que só barra e halter fazem crescer. Isso é mito.'),
 ('estudo', 'REVISÃO DE 2023:', 'GANHO PARECIDO.', 'Uma revisão de dois mil e vinte e três comparou os dois. O ganho de músculo foi parecido.'),
 ('vantagem', 'MÁQUINA: MAIS FÁCIL', 'IR PERTO DO LIMITE.', 'E a máquina é mais fácil de aprender e de levar perto do limite com segurança.'),
 ('livre', 'PESO LIVRE:', 'TREINA O EQUILÍBRIO.', 'O peso livre também é ótimo, e ainda treina equilíbrio e coordenação.'),
 ('ambos', 'USA', 'OS DOIS.', '[matter-of-fact] Então usa os dois. Escolhe o que você faz com boa técnica e consegue progredir.'),
 ('conc', 'RESUMINDO:', 'ESFORÇO E CARGA.', 'Resumindo: o músculo não sabe se é máquina ou barra. Ele sente esforço e carga subindo.'),
 ('cta', 'COMENTA', 'MÁQUINA.', 'Comenta MÁQUINA que eu te mando como registrar a carga de cada aparelho no Bríu e ver ela subir. Link na bio.'),
], '07:00')
V('brio_41_dropset', 'drop set: tirar peso e continuar a série', 'DROP', 2, [
 ('hook', 'DROP SET', 'ECONOMIZA TEMPO.', '[confident] Drop set economiza tempo de treino.'),
 ('como', 'TIRA PESO', 'E CONTINUA.', 'Você vai até quase não aguentar, tira um pouco de peso, e continua sem descansar.'),
 ('exemplo', 'EXEMPLO:', '14 KG, DEPOIS 10.', 'Exemplo: rosca com quatorze quilos até perto da falha. Troca pra dez e faz mais repetições.'),
 ('tempo', 'RESULTADO PARECIDO,', 'MENOS TEMPO.', 'Estudos mostram resultado parecido com séries normais, em menos tempo.'),
 ('ultima', 'SÓ NA', 'ÚLTIMA SÉRIE.', 'Por isso ele funciona melhor na última série do exercício, não em todas.'),
 ('isolado', 'MELHOR EM MÁQUINA', 'E ISOLADOS.', '[matter-of-fact] E prefira máquinas e isolados. No agachamento pesado, a técnica quebra.'),
 ('conc', 'RESUMINDO:', 'ATALHO DE TEMPO.', 'Resumindo: drop set é atalho pra quem tem pouco tempo. Uma vez por exercício, com técnica.'),
 ('cta', 'COMENTA', 'DROP.', 'Comenta DROP que eu te mando como registrar cada etapa do seu drop set no Bríu. Link na bio.'),
], '10:00')
V('brio_42_biset', 'bi-set para treinar o mesmo em menos tempo', 'BISET', 2, [
 ('hook', 'O MESMO TREINO', 'EM MENOS TEMPO.', '[confident] Dá pra treinar o mesmo em menos tempo.'),
 ('oque', 'BI-SET:', '2 EXERCÍCIOS SEGUIDOS.', 'É o bi-set: dois exercícios seguidos, e só depois o descanso.'),
 ('par', 'MÚSCULOS', 'QUE NÃO COMPETEM.', 'O segredo é juntar músculos que não competem, como bíceps e tríceps.'),
 ('descansa', 'UM TRABALHA,', 'O OUTRO DESCANSA.', 'Enquanto um trabalha, o outro descansa. Você não perde força na série seguinte.'),
 ('tempo', 'MESMAS SÉRIES,', 'MENOS MINUTOS.', 'Estudos mostram que dá pra fazer o mesmo número de séries em bem menos tempo.'),
 ('evita', 'EVITE 2 PESADOS', 'DE PERNA JUNTOS.', '[matter-of-fact] Só evita juntar dois exercícios pesados de perna. Aí as duas séries pioram.'),
 ('conc', 'RESUMINDO:', 'CORTA A ESPERA.', 'Resumindo: com pouco tempo, junta pares que não competem e corta a espera, não as séries.'),
 ('cta', 'COMENTA', 'BISET.', 'Comenta BISET que eu te mando como registrar seus pares de exercício no Bríu, série por série. Link na bio.'),
], '20:30')
V('brio_43_lado', 'um lado mais forte que o outro: exercício unilateral', 'LADO', 2, [
 ('hook', 'UM BRAÇO', 'MAIS FORTE?', '[curious] Um braço mais forte que o outro?'),
 ('normal', 'É NORMAL.', 'TODO MUNDO TEM.', 'Calma, isso é normal. Quase todo mundo tem um lado dominante.'),
 ('barra', 'NA BARRA,', 'O FORTE COMPENSA.', 'Na barra, o lado forte ajuda o fraco, e a diferença continua.'),
 ('halter', 'COM HALTER,', 'CADA LADO SOZINHO.', 'Com halter, ou um lado por vez, cada lado tem que levantar sozinho.'),
 ('fraco', 'COMEÇA PELO', 'LADO FRACO.', 'O truque: começa pelo lado fraco, e o forte faz o mesmo número de repetições. Nem uma a mais.'),
 ('tempo', 'A DIFERENÇA', 'DIMINUI.', '[matter-of-fact] Em algumas semanas, a diferença costuma diminuir.'),
 ('conc', 'RESUMINDO:', 'O FRACO DITA O RITMO.', 'Resumindo: inclui exercícios de um lado só, e deixa o lado fraco ditar o ritmo.'),
 ('cta', 'COMENTA', 'LADO.', 'Comenta LADO que eu te mando como registrar as repetições de cada lado no Bríu e acompanhar a diferença. Link na bio.'),
], '11:30')
V('brio_44_menos', 'muitos exercícios para o mesmo músculo no mesmo treino', 'MENOS', 2, [
 ('hook', '5 EXERCÍCIOS', 'DE BÍCEPS?', '[serious] Cinco exercícios de bíceps é exagero.'),
 ('rende', 'CADA SÉRIE EXTRA', 'RENDE MENOS.', 'Depois de algumas séries duras, cada série a mais rende cada vez menos.'),
 ('cansa', 'SÓ SOMA', 'CANSAÇO.', 'O músculo já está cansado. Você acumula cansaço e quase não soma estímulo.'),
 ('faixa', 'REFERÊNCIA:', 'ATÉ 6 A 8 SÉRIES.', 'Uma referência comum: seis a oito séries duras por músculo, no mesmo treino.'),
 ('divide', 'QUER MAIS?', 'OUTRO DIA.', 'Quer mais volume? Coloca em outro dia da semana, em vez de empilhar tudo num treino só.'),
 ('qualidade', 'BEM FEITO', 'VALE MAIS.', '[matter-of-fact] E dois exercícios bem feitos valem mais que cinco no automático.'),
 ('conc', 'RESUMINDO:', 'MAIS NÃO É MELHOR.', 'Resumindo: mais exercício não é mais músculo. Poucas séries duras, e o resto vai pra outro dia.'),
 ('cta', 'COMENTA', 'MENOS.', 'Comenta MENOS que eu te mando como registrar suas séries no Bríu e acompanhar sua evolução. Link na bio.'),
], '12:30')
V('brio_45_barra', 'primeira barra fixa: progressão com negativas', 'BARRA', 2, [
 ('hook', 'NEM UMA', 'BARRA?', '[serious] Não consegue fazer nem uma barra?'),
 ('normal', 'É O SEU', 'CORPO INTEIRO.', 'Normal. A barra levanta o seu corpo inteiro, e quase ninguém consegue de primeira.'),
 ('negativa', 'SOBE NO BANCO,', 'DESCE EM 5 SEGUNDOS.', 'O caminho é a negativa: sobe com um banco, e desce devagar, contando cinco segundos.'),
 ('pendura', 'FICA', 'PENDURADO.', 'Também vale ficar pendurado, com os braços esticados, segurando o máximo que der.'),
 ('semana', '3 A 5 DESCIDAS,', '2 A 3 VEZES NA SEMANA.', 'Faz isso duas ou três vezes por semana, com três a cinco descidas por vez.'),
 ('puxada', 'A PUXADA', 'AJUDA TAMBÉM.', '[matter-of-fact] E a puxada na máquina fortalece as costas enquanto isso.'),
 ('conc', 'RESUMINDO:', 'DESCE, DEPOIS SOBE.', 'Resumindo: primeiro você aprende a descer, depois a subir. A primeira barra vem.'),
 ('cta', 'COMENTA', 'BARRA.', 'Comenta BARRA que eu te mando como registrar suas descidas no Bríu até a primeira barra. Link na bio.'),
], '14:00')
V('brio_46_musica', 'música no treino melhora o desempenho', 'MÚSICA', 2, [
 ('hook', 'FONE NO OUVIDO', 'DÁ MAIS FORÇA?', '[curious] Treinar com fone te deixa mais forte?'),
 ('estudos', 'MAIS DE 100', 'ESTUDOS.', 'Uma revisão com mais de cem estudos achou que a música melhora o desempenho no exercício.'),
 ('esforco', 'O ESFORÇO', 'PARECE MENOR.', 'Com música, o mesmo esforço parece um pouco mais leve.'),
 ('gosta', 'A QUE VOCÊ', 'GOSTA, ANIMADA.', 'E vale mais a música que você gosta, animada, na hora da série pesada.'),
 ('playlist', 'PLAYLIST', 'PRONTA ANTES.', 'Monta a playlist antes, pra não perder tempo escolhendo no meio do treino.'),
 ('pequena', 'AJUDA,', 'MAS NÃO FAZ MILAGRE.', '[matter-of-fact] Só não espera milagre. A diferença é pequena. Quem faz o resultado ainda é a carga.'),
 ('conc', 'RESUMINDO:', 'MÚSICA É TEMPERO.', 'Resumindo: música ajuda, mas é tempero. O prato principal é a carga subindo.'),
 ('cta', 'COMENTA', 'MÚSICA.', 'Comenta MÚSICA que eu te mando como registrar suas séries no Bríu e ver se a carga está subindo. Link na bio.'),
], '17:00')
V('brio_47_oscila', 'força oscila de um treino pro outro: olhar a tendência', 'OSCILA', 2, [
 ('hook', 'TREINO FRACO', 'NÃO É REGRESSÃO.', '[matter-of-fact] Um treino fraco não é regressão.'),
 ('varia', 'A FORÇA', 'VARIA.', 'A força varia de um treino pro outro. Num dia rende, no outro não.'),
 ('causas', 'SONO, COMIDA,', 'ESTRESSE.', 'Sono, comida, estresse, até o horário mudam o seu rendimento naquele dia.'),
 ('isolado', 'UM TREINO RUIM', 'NÃO DIZ NADA.', 'Por isso, um treino ruim isolado não diz nada sobre a sua evolução.'),
 ('tendencia', 'OLHA A', 'TENDÊNCIA.', 'O que importa é a tendência: compara as últimas quatro semanas com as quatro anteriores.'),
 ('alerta', 'CAIU 4 SEMANAS?', 'AÍ É SINAL.', '[serious] Agora, se a carga cai quatro semanas seguidas, aí é hora de rever sono, treino e descanso.'),
 ('conc', 'RESUMINDO:', 'JULGA PELO MÊS.', 'Resumindo: não julga o treino pelo dia. Julga pelo mês.'),
 ('cta', 'COMENTA', 'OSCILA.', 'Comenta OSCILA que eu te mando como acompanhar sua evolução no Bríu, semana a semana, sem se assustar com um dia ruim. Link na bio.'),
], '18:30')
V('brio_48_cinto', 'cinto de musculação: quando usar', 'CINTO', 2, [
 ('hook', 'CINTO:', 'PRECISA?', '[curious] Cinto na academia: precisa?'),
 ('oque', 'O ABDÔMEN', 'EMPURRA O CINTO.', 'O cinto dá uma parede pro abdômen empurrar, e o tronco fica mais firme.'),
 ('quando', 'AGACHAMENTO E TERRA', 'PESADOS.', 'Ele ajuda no agachamento e no levantamento terra com carga alta, perto do seu máximo.'),
 ('nao', 'SÉRIE LEVE?', 'NÃO PRECISA.', 'Na rosca, no supino ou na série leve, ele não muda quase nada.'),
 ('tecnica', 'NÃO SUBSTITUI', 'A TÉCNICA.', '[matter-of-fact] E primeiro aprende a travar o abdômen sem ele. O cinto não substitui a técnica.'),
 ('aperto', 'FIRME,', 'MAS RESPIRA.', 'Aperta firme, mas dá pra respirar. Se não consegue puxar o ar, está apertado demais.'),
 ('conc', 'RESUMINDO:', 'SÓ NO PESADO.', 'Resumindo: cinto é ferramenta pra série pesada, não acessório pro treino inteiro.'),
 ('cta', 'COMENTA', 'CINTO.', 'Comenta CINTO que eu te mando como registrar suas séries pesadas no Bríu. Link na bio.'),
], '19:30')
V('brio_49_pegada', 'a mão cansa antes das costas: pegada e strap', 'PEGADA', 2, [
 ('hook', 'A MÃO CANSA', 'ANTES DAS COSTAS?', '[serious] Sua mão cansa antes das costas?'),
 ('limita', 'A PEGADA', 'FALHA PRIMEIRO.', 'Na remada e no terra pesado, a pegada costuma falhar antes do músculo que você quer treinar.'),
 ('sobra', 'COSTAS', 'COM SOBRA.', 'Aí a série acaba cedo, e as costas ficam com repetições sobrando.'),
 ('strap', 'STRAP:', 'PRENDE NA BARRA.', 'A solução é a fita de pegada, o strap. Ela prende a mão na barra.'),
 ('quando', 'SÓ NAS SÉRIES', 'PESADAS DE PUXAR.', 'Usa só nas séries pesadas de puxar. No aquecimento e nas leves, mão livre.'),
 ('treina', 'TREINA A PEGADA', 'À PARTE.', '[matter-of-fact] E se quiser uma pegada mais forte, treina ela à parte: segura a barra parado, o máximo que aguentar.'),
 ('conc', 'RESUMINDO:', 'AS COSTAS DECIDEM.', 'Resumindo: não deixa a mão decidir quando acaba a série das costas.'),
 ('cta', 'COMENTA', 'PEGADA.', 'Comenta PEGADA que eu te mando como registrar sua remada no Bríu e ver a carga subir. Link na bio.'),
], '22:00')
V('brio_50_puxar', 'equilíbrio entre exercícios de empurrar e de puxar', 'PUXAR', 2, [
 ('hook', 'MUITO SUPINO,', 'POUCA REMADA.', '[serious] Muito supino e pouca remada é erro.'),
 ('espelho', 'SÓ O QUE', 'O ESPELHO MOSTRA.', 'É o erro mais comum: treinar só o que aparece no espelho, peito e ombro da frente.'),
 ('desequilibrio', 'FRENTE FORTE,', 'COSTAS ATRASADAS.', 'O treino fica desequilibrado: frente forte, costas atrasadas.'),
 ('regra', '1 SÉRIE DE EMPURRAR,', '1 SÉRIE DE PUXAR.', 'Uma regra simples: pra cada série de empurrar, faz uma série de puxar.'),
 ('pares', 'SUPINO E REMADA,', 'DESENVOLVIMENTO E PUXADA.', 'Supino com remada. Desenvolvimento com puxada.'),
 ('supino', 'COSTAS FORTES', 'AJUDAM O SUPINO.', '[matter-of-fact] E costas fortes ajudam até no supino: elas deixam a barra mais estável na descida.'),
 ('conc', 'RESUMINDO:', 'EMPURROU, PUXA.', 'Resumindo: empurrou, puxa. Conta as séries dos dois lados e deixa empatado.'),
 ('cta', 'COMENTA', 'PUXAR.', 'Comenta PUXAR que eu te mando como registrar suas séries no Bríu e conferir se empurrar e puxar estão empatados. Link na bio.'),
], '15:30')

if __name__ == "__main__":
    import re
    for k, v in P.items():
        txt = " ".join(b[3] for b in v['beats']); clean = re.sub(r"\[[^\]]*\]\s*", "", txt)
        first = re.split(r"[.?!]", clean)[0]
        print(f"{k:18} {len(clean):4d} chars  1ª={len(first.split())}p  {v['hora']}  {'OK' if 480 <= len(clean) <= 620 else 'FORA'}")
