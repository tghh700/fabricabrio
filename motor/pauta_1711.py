"""Pauta de 17/11/2026 — 12 BRIO + 2 FIBRA + 2 DIA UM (nada agendado ainda para 17/11 BRT).
Métricas da API seguem indisponíveis (token do BRIO expirou em 14/11; pausa_global=1 desde 14/11). Base: views reais
informadas pelo usuário em 14/11 — performa pergunta sobre resultado/tempo/perda (BRIO 03, 10, 12) e mito popular (BRIO 14).
Hoje 12 de 12 do BRIO nesse padrão (pergunta com número ou crença errada), sem repetir tema de nenhum perfil.
Tendência BR (busca 16/11): mitos de treino e ciclo menstrual (Metrópoles), "treina pesado e não cresce", cardio x massa.
Evidência por vídeo:
 63 proteína/dia — número de resultado antes do conselho (23×) + pergunta (BRIO 03); Morton et al. 2018 (Br J Sports Med)
 64 cerveja      — pergunta de perda (padrão BRIO 12); Parr et al. 2014 (PLoS One)
 65 genética     — número grande antes do conselho (23×); Hubal et al. 2005 (Med Sci Sports Exerc), 585 pessoas
 66 balança sobe — pergunta de resultado (BRIO 03/10)
 67 memória musc.— variação de BRIO 12 (top 5): voltar é mais rápido; Staron 1991, Seaborne 2018 (Sci Rep)
 68 carboidrato  — crença errada na 1ª frase (9×) + BRIO 14 (mito de dieta); Hall & Guo 2017 (Gastroenterology)
 69 pesa mais    — crença errada (9×)
 70 BCAA         — crença errada (9×) + série de suplemento (BRIO 11 creatina); Wolfe 2017 (JISSN)
 71 abdômen      — número de resultado (23×) + pergunta de resultado
 72 falso magro  — frase que o público fala (11×) + resultado
 73 bulking      — crença errada (9×); Iraki et al. 2019 (Sports)
 74 menstruação  — experimento (10%), tendência BR; McNulty et al. 2020 (Sports Med)
 FIBRA 12 fibras rápidas x lentas — pergunta curiosa + diagrama (6×); Costill et al. 1976 (J Appl Physiol)
 FIBRA 13 estalo na articulação  — nomear a sensação exata (23×); Kawchuk et al. 2015 (PLoS One)
 DIA UM 10 ponte de glúteo — fácil/médio/difícil (8×; série prancha/flexão/agachamento)
 DIA UM 11 medo de se machucar — frase que o público fala (11×); Keogh & Winwood 2017 (Sports Med)"""
P = {}


def V(id, perfil, tema, palavra, beats, hora, leg, gat, tags, **kw):
    P[id] = dict(perfil=perfil, tema=tema, palavra=palavra, beats=beats, hora=hora, leg=leg, gat=gat, tags=tags, **kw)


# ============================================================ BRIO
V('brio_63_proteina', 'brio', 'quanta proteína por dia para ganhar músculo', 'PROTEÍNA', [
 ('hook', 'QUANTA PROTEÍNA', 'POR DIA?', '[curious] Quanta proteína você precisa por dia?'),
 ('conta', '1,6 G', 'POR QUILO.', 'Os estudos apontam uns um vírgula seis gramas por quilo do seu peso. Depois disso, o ganho quase para.'),
 ('exemplo', '70 KG', '= 112 G.', 'Pesa setenta quilos? Uns cento e doze gramas por dia.'),
 ('prato', 'NO PRATO,', 'PARECE MUITO.', 'Parece muito, mas um filé de frango já tem uns trinta. Ovo, leite e feijão somam.'),
 ('divide', 'DIVIDE EM', '3 OU 4 REFEIÇÕES.', 'O melhor é dividir em três ou quatro refeições, e não tudo de uma vez.'),
 ('mais', 'MAIS QUE ISSO', 'NÃO CRESCE MAIS.', '[matter-of-fact] Comer o dobro não faz crescer o dobro. O que sobra vira energia.'),
 ('conc', 'RESUMINDO:', '1,6 G POR QUILO.', 'Resumindo: um vírgula seis por quilo, espalhado no dia, e treino com carga subindo.'),
 ('cta', 'COMENTA', 'PROTEÍNA.', 'Comenta PROTEÍNA que eu te mando como registrar suas cargas no Bríu e ver se a comida está virando força. Link na bio.'),
], '07:00', "Quanta proteína você precisa por dia? 👇\nUns 1,6 g por quilo do seu peso. 70 kg = uns 112 g, divididos em 3 ou 4 refeições. Comer o dobro não faz crescer o dobro.",
  "como registrar suas cargas no Brio e ver se a comida está virando força", "#brio #proteina #hipertrofia #musculacao #dieta")

V('brio_64_cerveja', 'brio', 'cerveja no fim de semana atrapalha o ganho de músculo', 'CERVEJA', [
 ('hook', 'CERVEJA NO SÁBADO', 'ESTRAGA O TREINO?', '[curious] Cerveja no fim de semana estraga o treino?'),
 ('depende', 'DEPENDE', 'DA DOSE.', 'Depende muito da dose.'),
 ('estudo', 'UM PORRE', 'DEPOIS DO TREINO:', 'Num estudo, quem bebeu muito depois do treino fabricou bem menos músculo, mesmo tomando proteína.'),
 ('numero', 'ATÉ 37%', 'A MENOS.', 'A queda chegou a trinta e sete por cento.'),
 ('sono', 'E AINDA', 'PIORA O SONO.', 'E o álcool ainda piora o sono, que é quando o corpo se recupera.'),
 ('uma', 'UMA OU DUAS?', 'EFEITO PEQUENO.', '[matter-of-fact] Agora, uma ou duas no fim de semana? O efeito é pequeno. O problema é o porre.'),
 ('conc', 'RESUMINDO:', 'O PORRE ATRAPALHA.', 'Resumindo: não precisa virar abstêmio. Mas porre no dia do treino joga parte do esforço fora.'),
 ('cta', 'COMENTA', 'CERVEJA.', 'Comenta CERVEJA que eu te mando como registrar seus treinos no Bríu e ver se a carga cai depois do fim de semana. Link na bio.'),
], '08:30', "Cerveja no fim de semana estraga o treino? 👇\nUma ou duas: efeito pequeno. Porre depois do treino: até 37% menos fabricação de músculo num estudo, mesmo com proteína.",
  "como registrar seus treinos no Brio e ver se a carga cai depois do fim de semana", "#brio #cerveja #hipertrofia #musculacao #academia")

V('brio_65_genetica', 'brio', 'genética: por que uns crescem mais rápido com o mesmo treino', 'GENÉTICA', [
 ('hook', 'MESMO TREINO,', 'RESULTADO DIFERENTE?', '[curious] Seu amigo cresce mais rápido que você?'),
 ('estudo', '585 PESSOAS,', 'MESMO TREINO.', 'Um estudo pôs quinhentas e oitenta e cinco pessoas no mesmo treino de braço.'),
 ('variou', 'DE 0%', 'A 59%.', 'Teve gente que quase não cresceu, e gente que cresceu cinquenta e nove por cento.'),
 ('gen', 'GENÉTICA', 'PESA.', 'Grande parte disso é genética. Cada corpo responde num ritmo.'),
 ('mais', 'RESPONDE POUCO?', 'MAIS SÉRIES.', 'Mas quem responde pouco costuma melhorar com mais séries e mais tempo.'),
 ('compara', 'COMPARA', 'VOCÊ COM VOCÊ.', '[matter-of-fact] Por isso, comparar com o amigo não serve. O que serve é você contra você mesmo.'),
 ('conc', 'RESUMINDO:', 'SEU RITMO.', 'Resumindo: genética muda a velocidade, não o destino. Se a sua carga sobe, você está crescendo.'),
 ('cta', 'COMENTA', 'GENÉTICA.', 'Comenta GENÉTICA que eu te mando como acompanhar sua evolução no Bríu, só você contra você. Link na bio.'),
], '10:00', "Seu amigo cresce mais rápido que você? 👇\nNum estudo com 585 pessoas no mesmo treino, o braço cresceu de 0% a 59%. Genética muda a velocidade, não o destino.",
  "como acompanhar sua evolução no Brio, só você contra você", "#brio #genetica #hipertrofia #musculacao #academia")

V('brio_66_balanca', 'brio', 'a balança sobe nas primeiras semanas de treino', 'BALANÇA', [
 ('hook', 'COMEÇOU A TREINAR', 'E A BALANÇA SUBIU?', '[curious] Começou a treinar e a balança subiu?'),
 ('calma', 'CALMA.', 'É NORMAL.', 'Calma. Isso é normal, e não é gordura.'),
 ('estoque', 'O MÚSCULO', 'GUARDA ENERGIA.', 'O músculo que começa a treinar passa a guardar mais energia, em forma de glicogênio.'),
 ('agua', 'E CADA GRAMA', 'PUXA ÁGUA.', 'E cada grama de glicogênio vem com umas três gramas de água junto.'),
 ('reparo', 'O REPARO', 'TAMBÉM INCHA.', 'O reparo depois do treino também segura líquido no músculo por uns dias.'),
 ('quilos', '1 A 2 KG', 'A MAIS.', '[matter-of-fact] Resultado: um a dois quilos a mais nas primeiras semanas. Depois estabiliza.'),
 ('conc', 'RESUMINDO:', 'NÃO DESISTE.', 'Resumindo: a balança subir no começo é sinal de músculo trabalhando. Não desiste por isso.'),
 ('cta', 'COMENTA', 'BALANÇA.', 'Comenta BALANÇA que eu te mando como acompanhar sua evolução no Bríu pelo que importa: a carga. Link na bio.'),
], '11:30', "Começou a treinar e a balança subiu? 👇\nNormal: o músculo guarda glicogênio e cada grama puxa água. 1 a 2 kg nas primeiras semanas, e depois estabiliza.",
  "como acompanhar sua evolução no Brio pelo que importa: a carga", "#brio #emagrecimento #iniciante #musculacao #academia")

V('brio_67_memoria', 'brio', 'memória muscular: recuperar o que perdeu é mais rápido', 'VOLTA', [
 ('hook', 'PAROU E PERDEU?', 'VOLTA RÁPIDO.', '[serious] Parou de treinar e perdeu tudo? Volta mais rápido do que você pensa.'),
 ('nome', 'TEM NOME:', 'MEMÓRIA MUSCULAR.', 'Isso tem nome: memória muscular.'),
 ('nervo', 'O CÉREBRO', 'LEMBRA O MOVIMENTO.', 'Primeiro, o cérebro não esquece o movimento. A técnica volta rápido.'),
 ('musculo', 'O MÚSCULO', 'GUARDA MARCAS.', 'E o músculo guarda marcas do treino antigo, que ajudam a crescer de novo.'),
 ('estudo', 'NA 2ª VEZ,', 'CRESCE MAIS RÁPIDO.', 'Nos estudos, quem já tinha treinado recuperou o tamanho mais rápido que da primeira vez.'),
 ('volta', 'VOLTA LEVE,', 'SOBE RÁPIDO.', '[matter-of-fact] Só não volta com a carga antiga. Começa mais leve e sobe toda semana.'),
 ('conc', 'RESUMINDO:', 'NADA FOI PERDIDO.', 'Resumindo: o tempo que você treinou não foi perdido. Voltar é sempre mais rápido que começar.'),
 ('cta', 'COMENTA', 'VOLTA.', 'Comenta VOLTA que eu te mando como registrar suas cargas no Bríu e ver a força voltando semana a semana. Link na bio.'),
], '12:30', "Parou de treinar e perdeu tudo? Volta mais rápido do que você pensa. 👇\nO cérebro lembra o movimento e o músculo guarda marcas do treino antigo. Volta mais leve e sobe toda semana.",
  "como registrar suas cargas no Brio e ver a força voltando", "#brio #memoriamuscular #voltaratreinar #musculacao #academia")

V('brio_68_carbo', 'brio', 'cortar carboidrato não seca mais que outra dieta', 'CARBO', [
 ('hook', 'CORTAR CARBOIDRATO', 'NÃO SECA MAIS.', '[serious] Cortar carboidrato não seca mais.'),
 ('rapido', 'MAS OS PRIMEIROS', 'QUILOS SAEM...', 'Mas, então, por que os primeiros quilos saem tão rápido?'),
 ('agua', 'É ÁGUA.', 'NÃO GORDURA.', 'Porque sai o estoque de energia do músculo, e a água que vem junto. É água, não gordura.'),
 ('estudo', 'MESMAS CALORIAS,', 'MESMA GORDURA.', 'Comparando dietas com as mesmas calorias, a perda de gordura fica praticamente igual.'),
 ('treino', 'E O TREINO', 'SENTE.', 'E no treino pesado, o carboidrato é o combustível. Sem ele, a força cai.'),
 ('decide', 'O QUE DECIDE:', 'O TOTAL.', '[matter-of-fact] O que decide é o total do dia, e a dieta que você consegue manter.'),
 ('conc', 'RESUMINDO:', 'NÃO PRECISA CORTAR.', 'Resumindo: não precisa cortar o arroz. Ajusta a quantidade e mantém proteína alta.'),
 ('cta', 'COMENTA', 'CARBO.', 'Comenta CARBO que eu te mando como registrar suas cargas no Bríu e ver se a força segura na dieta. Link na bio.'),
], '14:00', "Cortar carboidrato não seca mais. 👇\nOs primeiros quilos que saem rápido são água. Com as mesmas calorias, a perda de gordura é praticamente igual.",
  "como registrar suas cargas no Brio e ver se a força segura na dieta", "#brio #carboidrato #dieta #emagrecimento #musculacao")

V('brio_69_pesa', 'brio', 'músculo não pesa mais que gordura: ocupa menos espaço', 'ESPAÇO', [
 ('hook', 'MÚSCULO PESA', 'MAIS QUE GORDURA?', '[curious] Músculo pesa mais que gordura?'),
 ('quilo', '1 KG', '= 1 KG.', 'Não. Um quilo de músculo pesa o mesmo que um quilo de gordura. Um quilo é um quilo.'),
 ('espaco', 'A DIFERENÇA:', 'O ESPAÇO.', 'A diferença é o espaço. O músculo é mais denso, então ocupa menos lugar.'),
 ('volume', 'GORDURA OCUPA', 'UNS 18% A MAIS.', 'O mesmo quilo de gordura ocupa uns dezoito por cento a mais de volume.'),
 ('roupa', 'MESMO PESO,', 'ROUPA FOLGADA.', 'Por isso dá pra ter o mesmo peso e a roupa ficar mais folgada.'),
 ('sinal', 'OLHA A CINTURA', 'E A CARGA.', '[matter-of-fact] Então, se o peso não muda, olha a cintura e a carga no treino.'),
 ('conc', 'RESUMINDO:', 'MESMO PESO, MENOS ESPAÇO.', 'Resumindo: músculo não pesa mais. Ocupa menos. Por isso a balança sozinha engana.'),
 ('cta', 'COMENTA', 'ESPAÇO.', 'Comenta ESPAÇO que eu te mando como acompanhar sua evolução no Bríu além da balança. Link na bio.'),
], '15:30', "Músculo pesa mais que gordura? 👇\nNão: 1 kg é 1 kg. A diferença é o espaço: o mesmo quilo de gordura ocupa uns 18% a mais. Por isso a roupa folga e o peso não muda.",
  "como acompanhar sua evolução no Brio além da balança", "#brio #mitos #emagrecimento #musculacao #academia")

V('brio_70_bcaa', 'brio', 'BCAA não faz diferença para quem come proteína suficiente', 'BCAA', [
 ('hook', 'BCAA', 'VALE A PENA?', '[curious] Bê-cê-a-a vale o dinheiro?'),
 ('oque', 'SÃO 3', 'AMINOÁCIDOS.', 'Bê-cê-a-a são só três aminoácidos. O músculo precisa de nove essenciais pra crescer.'),
 ('falta', 'SÓ 3?', 'A OBRA PARA.', 'Com só três, a construção começa e para, porque faltam as outras peças.'),
 ('comida', 'A COMIDA', 'JÁ TEM.', 'E toda proteína da comida já tem bê-cê-a-a. Frango, ovo, leite, whey.'),
 ('quem', 'COME PROTEÍNA?', 'NÃO SOMA NADA.', '[matter-of-fact] Pra quem já come proteína suficiente, os estudos não mostram ganho extra.'),
 ('troca', 'O MESMO DINHEIRO', 'COMPRA COMIDA.', 'O mesmo dinheiro rende mais em comida de verdade.'),
 ('conc', 'RESUMINDO:', 'GASTA NA COMIDA.', 'Resumindo: bate a proteína do dia. Aí o bê-cê-a-a não soma nada.'),
 ('cta', 'COMENTA', 'BCAA.', 'Comenta BCAA que eu te mando como registrar suas séries no Bríu e ver o que de fato faz sua carga subir. Link na bio.'),
], '17:00', "BCAA vale o dinheiro? 👇\nSão só 3 aminoácidos, e toda proteína da comida já tem. Pra quem come proteína suficiente, os estudos não mostram ganho extra.",
  "como registrar suas séries no Brio e ver o que faz sua carga subir", "#brio #bcaa #suplementos #musculacao #academia")

V('brio_71_abdomen', 'brio', 'com quanto de gordura o abdômen aparece', 'TANQUINHO', [
 ('hook', 'QUANDO O ABDÔMEN', 'APARECE?', '[curious] Com quanto de gordura o abdômen aparece?'),
 ('todos', 'TODO MUNDO', 'TEM.', 'Todo mundo tem os gomos do abdômen. Eles só ficam escondidos embaixo da gordura.'),
 ('homem', 'HOMENS:', 'UNS 10 A 12%.', 'Nos homens, eles costumam aparecer perto de dez a doze por cento de gordura.'),
 ('mulher', 'MULHERES:', 'UNS 18 A 20%.', 'Nas mulheres, perto de dezoito a vinte por cento.'),
 ('ultimo', 'A BARRIGA', 'É A ÚLTIMA.', 'E a barriga costuma ser o último lugar a secar.'),
 ('treino', 'TREINAR O ABDÔMEN', 'DEIXA MAIS GROSSO.', '[matter-of-fact] Treinar o abdômen com carga deixa os gomos mais grossos, e eles aparecem um pouco antes.'),
 ('conc', 'RESUMINDO:', 'É PORCENTAGEM.', 'Resumindo: tanquinho é porcentagem de gordura, com paciência. O treino só deixa o desenho mais forte.'),
 ('cta', 'COMENTA', 'TANQUINHO.', 'Comenta TANQUINHO que eu te mando como acompanhar sua evolução no Bríu enquanto você seca. Link na bio.'),
], '18:30', "Com quanto de gordura o abdômen aparece? 👇\nHomens: perto de 10 a 12%. Mulheres: perto de 18 a 20%. A barriga é o último lugar a secar.",
  "como acompanhar sua evolução no Brio enquanto você seca", "#brio #abdomen #tanquinho #musculacao #emagrecimento")

V('brio_72_falsomagro', 'brio', 'falso magro: magro com barriga precisa de músculo', 'MAGRO', [
 ('hook', 'MAGRO,', 'MAS COM BARRIGA?', '[curious] Você é magro, mas tem barriga?'),
 ('nome', 'TEM NOME:', 'FALSO MAGRO.', 'Isso tem nome: falso magro. Peso normal, pouco músculo e gordura sobrando.'),
 ('erro', 'O ERRO:', 'FAZER DIETA.', 'O erro mais comum é fazer dieta pesada. Aí você perde o pouco músculo que tem.'),
 ('certo', 'O CERTO:', 'GANHAR MÚSCULO.', 'O caminho é o contrário: ganhar músculo com treino de força.'),
 ('come', 'COME NORMAL,', 'PROTEÍNA ALTA.', 'Come normal, com proteína em todas as refeições. Sem cortar comida.'),
 ('muda', 'O PESO QUASE', 'NÃO MUDA.', '[matter-of-fact] O peso quase não muda, mas o corpo muda: a gordura cai e o músculo aparece.'),
 ('conc', 'RESUMINDO:', 'FORÇA, NÃO FOME.', 'Resumindo: falso magro não precisa passar fome. Precisa de força, por uns seis meses.'),
 ('cta', 'COMENTA', 'MAGRO.', 'Comenta MAGRO que eu te mando como registrar suas cargas no Bríu e ver o músculo chegando. Link na bio.'),
], '19:30', "Magro, mas com barriga? 👇\nTem nome: falso magro. O erro é fazer dieta pesada. O caminho é treino de força e proteína alta, sem passar fome.",
  "como registrar suas cargas no Brio e ver o músculo chegando", "#brio #falsomagro #hipertrofia #musculacao #academia")

V('brio_73_bulking', 'brio', 'bulking sujo: comer de tudo para ganhar massa', 'BULK', [
 ('hook', 'COMER DE TUDO', 'NÃO TE DEIXA GRANDE.', '[serious] Comer de tudo não te deixa grande.'),
 ('ideia', 'BULKING', 'SUJO.', 'A ideia do bulking sujo é comer tudo o que vê pra ganhar massa.'),
 ('limite', 'O MÚSCULO', 'TEM LIMITE.', 'Mas o músculo cresce devagar. Ele não usa toda a comida que sobra.'),
 ('sobra', 'O RESTO', 'VIRA GORDURA.', 'O resto vira gordura. Depois, vai levar meses pra secar.'),
 ('certo', 'SÓ UM POUCO', 'A MAIS.', 'O certo é comer só um pouco a mais, uns trezentos a quinhentos de calorias por dia.'),
 ('ritmo', 'MEIO QUILO', 'POR MÊS, OU MENOS.', '[matter-of-fact] Ganhar uns meio quilo a um quilo por mês já é ótimo. Mais rápido que isso, é gordura.'),
 ('conc', 'RESUMINDO:', 'SOBRA PEQUENA.', 'Resumindo: pra crescer, sobra pequena de comida e carga subindo. Não precisa comer tudo.'),
 ('cta', 'COMENTA', 'BULK.', 'Comenta BULK que eu te mando como registrar suas cargas no Bríu e ver se o peso novo é força. Link na bio.'),
], '20:30', "Comer de tudo não te deixa grande. 👇\nO músculo cresce devagar e o resto vira gordura. O certo é comer só um pouco a mais: 300 a 500 calorias por dia.",
  "como registrar suas cargas no Brio e ver se o peso novo é força", "#brio #bulking #hipertrofia #dieta #musculacao")

V('brio_74_menstrual', 'brio', 'treinar durante a menstruação e o ciclo menstrual', 'CICLO', [
 ('hook', 'TREINAR MENSTRUADA', 'ATRAPALHA?', '[curious] Treinar menstruada atrapalha o treino?'),
 ('pode', 'PODE', 'TREINAR.', 'Pode treinar, sim. Não faz mal, e pode até aliviar a cólica.'),
 ('forca', 'A FORÇA', 'CAI?', 'E a força cai? Os estudos mostram uma diferença bem pequena entre as fases do ciclo.'),
 ('cada', 'CADA MULHER', 'É DIFERENTE.', 'O que pesa mais é como cada mulher se sente. Umas rendem igual, outras não.'),
 ('ajusta', 'NO DIA RUIM:', 'AJUSTA.', 'No dia ruim, ajusta: menos séries, ou um pouco menos de carga. Mas vai.'),
 ('anota', 'ANOTA', 'O SEU PADRÃO.', '[matter-of-fact] O melhor jeito de saber é anotar seus treinos por uns meses e ver o seu padrão.'),
 ('conc', 'RESUMINDO:', 'TREINA E AJUSTA.', 'Resumindo: menstruação não é motivo pra parar. Treina, ouve o corpo e ajusta a carga.'),
 ('cta', 'COMENTA', 'CICLO.', 'Comenta CICLO que eu te mando como registrar suas séries no Bríu e ver como você rende em cada semana. Link na bio.'),
], '22:00', "Treinar menstruada atrapalha? 👇\nPode treinar. Os estudos mostram diferença bem pequena de força entre as fases. No dia ruim, ajusta a carga, mas vai.",
  "como registrar suas séries no Brio e ver como você rende em cada semana", "#brio #ciclomenstrual #treinofeminino #musculacao #academia")

# ============================================================ FIBRA (build3, estilo próprio)
V('fibra_12_fibras', 'fibra', 'fibras rápidas e lentas: velocista x maratonista', 'FIBRA', [
 ('hook', 'VELOCISTA FORTE,', 'MARATONISTA MAGRO?', '[curious] Velocista musculoso, maratonista magro. Por quê?'),
 ('tipos', 'DOIS TIPOS', 'DE FIBRA.', 'Porque o músculo tem dois tipos principais de fibra.'),
 ('lenta', 'LENTA:', 'NÃO CANSA.', 'A fibra lenta quase não cansa, mas faz pouca força e cresce pouco.'),
 ('rapida', 'RÁPIDA:', 'FORÇA E TAMANHO.', 'A fibra rápida faz muita força e cresce bem mais. Mas cansa em segundos.'),
 ('mistura', 'VELOCISTA:', 'MAIS RÁPIDAS.', 'Nos estudos, velocistas tinham a maioria de fibras rápidas. Maratonistas, quase oitenta por cento de lentas.'),
 ('treino', 'O TREINO', 'ESCOLHE QUEM CRESCE.', '[matter-of-fact] Parte disso é genética. Mas o treino pesado faz as fibras rápidas crescerem.'),
 ('conc', 'RESUMINDO:', 'PESO ACORDA AS RÁPIDAS.', '[warm] Resumindo: pra crescer, as rápidas precisam de esforço alto, perto do limite da série.'),
 ('cta', 'COMENTA', 'FIBRA.', 'Comenta FIBRA que eu te mando como registrar suas séries no Bríu e ver suas cargas subirem. Link na bio.'),
], '12:30', "Velocista musculoso, maratonista magro. Por quê? 🔬👇\nFibra lenta quase não cansa, mas cresce pouco. Fibra rápida faz força e cresce. O treino pesado faz as rápidas crescerem.",
  "como registrar suas séries no Brio e ver suas cargas subirem", "#fibratreino #fibramuscular #ciencia #musculacao #hipertrofia",
  formato='pergunta curiosa + diagrama das fibras (6×)',
  fonte='Costill DL et al. J Appl Physiol 1976;40(2):149-54 (velocistas ~24% fibras tipo I; fundistas ~79%); Schiaffino S, Reggiani C. Physiol Rev 2011;91(4):1447-531 (tipos de fibra e hipertrofia maior nas tipo II)',
  conc=['LENTA: RESISTE', 'RÁPIDA: CRESCE', 'ESFORÇO ALTO'], cta=['REGISTRE SUAS SÉRIES NO BRIO', 'E VEJA A CARGA SUBIR'])

V('fibra_13_estalo', 'fibra', 'estalo na articulação durante o treino', 'ESTALO', [
 ('hook', 'AQUELE ESTALO', 'NO JOELHO?', '[curious] Aquele estalo no joelho quando você agacha?'),
 ('liquido', 'DENTRO:', 'UM LÍQUIDO.', 'Dentro da articulação existe um líquido que lubrifica o movimento.'),
 ('bolha', 'A PRESSÃO CAI,', 'NASCE UMA BOLHA.', 'Quando a articulação se abre, a pressão cai e nasce uma bolha de gás. É o estalo.'),
 ('tendao', 'OU UM TENDÃO', 'DESLIZANDO.', 'Outras vezes, é um tendão deslizando por cima do osso, como um elástico.'),
 ('normal', 'SEM DOR?', 'COSTUMA SER NORMAL.', '[matter-of-fact] Estalo sem dor é muito comum, e na maioria das vezes não indica lesão.'),
 ('alerta', 'COM DOR,', 'INCHAÇO? AVALIA.', 'O alerta é estalo com dor, inchaço, ou o joelho travando. Aí, procura avaliação.'),
 ('conc', 'RESUMINDO:', 'SEM DOR, SEGUE.', '[warm] Resumindo: estalo sem dor é gás ou tendão. O que importa é a dor, não o barulho.'),
 ('cta', 'COMENTA', 'ESTALO.', 'Comenta ESTALO que eu te mando como registrar seus treinos no Bríu e acompanhar sua evolução com segurança. Link na bio.'),
], '19:00', "Aquele estalo no joelho quando você agacha? 🔬👇\nÉ uma bolha de gás no líquido da articulação, ou um tendão deslizando. Sem dor, costuma ser normal. Com dor ou inchaço, avalia.",
  "como registrar seus treinos no Brio e acompanhar sua evolução", "#fibratreino #articulacao #joelho #ciencia #musculacao",
  formato='nomear a sensação exata (23×)',
  fonte='Kawchuk GN et al. PLoS One 2015;10(4):e0119470 (cavitação: formação de bolha no líquido sinovial, RM em tempo real); Song SJ et al. Knee Surg Relat Res 2018;30(3):183-91 (crepitação sem dor é comum e não indica lesão por si)',
  conc=['GÁS OU TENDÃO', 'SEM DOR: NORMAL', 'COM DOR: AVALIA'], cta=['REGISTRE SEUS TREINOS NO BRIO', 'E ACOMPANHE SUA EVOLUÇÃO'])

# ============================================================ DIA UM (build3, caderno)
V('diaum_10_ponte', 'diaum', 'ponte de glúteo em 3 níveis para iniciante', 'PONTE', [
 ('hook', 'GLÚTEO FORTE', 'DEITADO NO CHÃO?', '[warm] Quer glúteo forte? Começa deitado no chão.'),
 ('ponte', 'O NOME:', 'PONTE.', 'É a ponte de glúteo. Dá pra fazer em casa, e tem três níveis.'),
 ('n1', 'NÍVEL 1:', 'DOIS PÉS.', 'Nível um: deitado, joelhos dobrados, pés no chão. Sobe o quadril e aperta o glúteo lá em cima.'),
 ('n2', 'NÍVEL 2:', 'PAUSA EM CIMA.', 'Nível dois: o mesmo, mas segura três segundos lá em cima.'),
 ('n3', 'NÍVEL 3:', 'UMA PERNA.', 'Nível três: uma perna esticada no ar, e sobe só com a outra.'),
 ('regra', '15 FÁCEIS', '= PRÓXIMO.', 'Quando quinze ficarem fáceis, sobe de nível. Sem dor nas costas: quem trabalha é o glúteo.'),
 ('conc', 'RESUMINDO:', 'UM NÍVEL POR VEZ.', '[encouraging] Então: começa com os dois pés, e sobe de nível quando ficar fácil.'),
 ('cta', 'COMENTA', 'PONTE.', 'Comenta PONTE que eu te mando como registrar suas séries no Bríu e ver sua evolução. Link na bio.'),
], '11:30', "Quer glúteo forte? Começa deitado no chão. 📓👇\nNível 1: ponte com os dois pés. Nível 2: pausa de 3 segundos em cima. Nível 3: uma perna só.",
  "como registrar suas séries no Brio e ver sua evolução", "#diaumtreino #gluteo #iniciante #treinoemcasa #comecar",
  formato='cada movimento em fácil, médio e difícil (8×)',
  conc=["começa com 2 pés", "15 fáceis = sobe", "um nível por vez"], cta=['registre suas séries no Brio', 'e veja sua evolução'])

V('diaum_11_medo', 'diaum', 'medo de se machucar ao começar a musculação', 'SEGURO', [
 ('hook', '"TENHO MEDO', 'DE ME MACHUCAR."', '[warm] Tenho medo de me machucar na academia.'),
 ('normal', 'É UM MEDO', 'MUITO COMUM.', 'Esse medo é muito comum. E a boa notícia: musculação é das atividades mais seguras.'),
 ('raro', 'LESÃO É RARA', 'NA MUSCULAÇÃO.', 'Os estudos mostram menos lesão nela do que em muito esporte com bola.'),
 ('leve', 'REGRA 1:', 'SOBRAM 3.', 'Regra um: escolhe um peso que deixa sobrar umas três repetições no fim.'),
 ('movimento', 'REGRA 2:', 'APRENDE O MOVIMENTO.', 'Regra dois: aprende o movimento antes de pôr peso. Pede ajuda, sem vergonha.'),
 ('dor', 'REGRA 3:', 'PONTADA = PARA.', 'Regra três: cansaço e queimação são normais. Pontada ou dor na articulação, para.'),
 ('conc', 'RESUMINDO:', 'LEVE E AOS POUCOS.', '[encouraging] Então: começa leve, sobe aos poucos, e respeita a dor. O medo vai embora com a prática.'),
 ('cta', 'COMENTA', 'SEGURO.', 'Comenta SEGURO que eu te mando como registrar suas séries no Bríu e subir a carga aos poucos. Link na bio.'),
], '19:30', "\"Tenho medo de me machucar na academia.\" 📓👇\nA musculação tem menos lesão que muito esporte com bola. 3 regras: sobram 3 repetições, aprende o movimento, pontada = para.",
  "como registrar suas séries no Brio e subir a carga aos poucos", "#diaumtreino #iniciante #academia #comecar #musculacao",
  formato='abrir com uma frase que o público fala (11×)',
  conc=["sobram 3 repetições", "aprende o movimento", "pontada = para"], cta=['registre suas séries no Brio', 'e suba a carga aos poucos'])

VOZ = {'brio': ('plASsyS7JE6GCAvx9uIc', dict(stability=.5, similarity_boost=.8, style=.2, speed=1.1)),
       'fibra': ('r3KkFedJ4n8aabIZ0RFQ', dict(stability=.5, similarity_boost=.75, style=0, speed=1.08)),
       'diaum': ('PznTnBc8X6pvixs9UkQm', dict(stability=.45, similarity_boost=.75, style=0, speed=1.05))}

if __name__ == "__main__":
    import re
    for k, v in P.items():
        txt = " ".join(b[3] for b in v['beats']); clean = re.sub(r"\[[^\]]*\]\s*", "", txt)
        first = re.split(r"[.?!]", clean)[0]
        leg = v['leg'] + v['gat']
        print(f"{k:20} {len(clean):4d} chars  1ª={len(first.split())}p  {v['hora']}  {'OK' if 480 <= len(clean) <= 620 else 'FORA'}"
              f"  bríu-leg={'ERRO' if re.search('br[íi]u', leg, re.I) else 'ok'}  tags={len(v['tags'].split())}  cta-fim={'ok' if clean.endswith('Link na bio.') else 'ERRO'}")
