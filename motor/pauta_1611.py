"""Pauta de 16/11/2026 — 12 BRIO + 2 FIBRA + 1 DIA UM (DIA UM 11:30 já tem o diaum-08 no estoque).
Métricas da API seguem bloqueadas ("API access blocked", 15/11). Base: views reais informadas pelo usuário em 14/11
(o que performa = pergunta sobre resultado/tempo/perda e mito popular). 15/11 saiu quase todo de técnica; hoje 10 de 12
do BRIO estão nesse padrão.
Evidência por vídeo:
 51 músculo/mês  — número de resultado grande antes do conselho (23×) + padrão BRIO 03/10 (top 2)
 52 vira gordura — crença popular declarada errada na 1ª frase (9×) + padrão BRIO 14 (mito)
 53 mulher pesado — crença errada (9×) · 54 whey janela — crença errada (9×), Schoenfeld, Aragon & Krieger 2013 (JISSN)
 55 altura       — crença errada (9×), Lloyd et al. 2014 (Br J Sports Med, consenso de treino de força em jovens)
 56 recomposição — pergunta de resultado (padrão BRIO 03/10), Barakat et al. 2020 (Strength Cond J)
 57 musculação emagrece — crença errada (9×) · 58 café — pergunta + estudo, Guest et al. 2021 (ISSN position stand)
 59 confusão muscular — crença errada (9×) + progressão · 60 shape 90 dias — antes e depois nos 1os segundos (16×)
 61 foco no músculo — experimento (10%), Schoenfeld et al. 2018 (Eur J Sport Sci)
 62 emagrecer rápido — pergunta de perda (padrão BRIO 12), Garthe et al. 2011 (IJSNEM)
 FIBRA 10 supino — diagrama do músculo em cada movimento (6×, 21 contas; série que já rodou com agachamento e barra)
 FIBRA 11 descanso — crença errada na 1ª frase (9×) · DIA UM 09 agachamento — fácil/médio/difícil (8×; série prancha/flexão)"""
P = {}


def V(id, perfil, tema, palavra, beats, hora, leg, gat, tags, **kw):
    P[id] = dict(perfil=perfil, tema=tema, palavra=palavra, beats=beats, hora=hora, leg=leg, gat=gat, tags=tags, **kw)


# ============================================================ BRIO
V('brio_51_mes', 'brio', 'quanto músculo dá pra ganhar por mês', 'QUILO', [
 ('hook', 'QUANTO MÚSCULO', 'POR MÊS?', '[curious] Quanto músculo dá pra ganhar por mês?'),
 ('real', 'INICIANTE:', 'ATÉ 1 KG POR MÊS.', 'Pra quem começa do zero e treina direito, algo perto de meio quilo a um quilo por mês.'),
 ('cai', 'DEPOIS,', 'DESACELERA.', 'No segundo ano, isso cai mais ou menos pela metade. E fica mais lento a cada ano.'),
 ('balanca', 'A BALANÇA', 'MISTURA TUDO.', 'Por isso a balança engana. Ela mistura músculo, água, comida e gordura.'),
 ('promessa', '5 KG EM 1 MÊS?', 'NÃO É MÚSCULO.', '[serious] Cinco quilos de músculo em um mês? Isso é água e gordura, não músculo.'),
 ('medida', 'OLHA A', 'CARGA.', 'Um jeito melhor de acompanhar é a carga. Se ela sobe mês a mês, você está no caminho.'),
 ('conc', 'RESUMINDO:', 'LENTO, MAS VEM.', 'Resumindo: músculo vem devagar, mas vem. Um quilo por mês no começo já é ótimo.'),
 ('cta', 'COMENTA', 'QUILO.', 'Comenta QUILO que eu te mando como registrar suas cargas no Bríu e ver o mês a mês. Link na bio.'),
], '07:00', "Quanto músculo dá pra ganhar por mês? 👇\nIniciante: perto de meio quilo a um quilo por mês. Depois, desacelera. Promessa de 5 kg em um mês é água e gordura.",
  "como registrar suas cargas no Brio e ver o mês a mês", "#brio #hipertrofia #musculacao #academia #resultado")

V('brio_52_vira', 'brio', 'músculo não vira gordura quando a pessoa para de treinar', 'VIRA', [
 ('hook', 'MÚSCULO', 'NÃO VIRA GORDURA.', '[serious] Músculo não vira gordura.'),
 ('tecido', 'SÃO TECIDOS', 'DIFERENTES.', 'São tecidos diferentes. Um não se transforma no outro, nunca.'),
 ('duas', 'QUEM PARA:', 'DUAS COISAS.', 'Quando alguém para de treinar, acontecem duas coisas ao mesmo tempo.'),
 ('encolhe', 'O MÚSCULO', 'DIMINUI.', 'Primeiro, sem o estímulo do treino, o músculo vai diminuindo.'),
 ('sobra', 'COME IGUAL,', 'GASTA MENOS.', 'Segundo, a pessoa continua comendo igual, mas gasta menos. A sobra vira gordura.'),
 ('parece', 'PARECE QUE', 'VIROU.', '[matter-of-fact] Como as duas coisas acontecem juntas, parece que um virou o outro.'),
 ('ajusta', 'VAI PARAR?', 'AJUSTA A COMIDA.', 'Se for parar ou diminuir o treino, ajusta a comida junto.'),
 ('conc', 'RESUMINDO:', 'NÃO VIRA.', 'Resumindo: músculo não vira gordura. Você perde um e ganha o outro, por motivos diferentes.'),
 ('cta', 'COMENTA', 'VIRA.', 'Comenta VIRA que eu te mando como acompanhar sua evolução no Bríu, semana a semana. Link na bio.'),
], '08:30', "Músculo não vira gordura. 👇\nSão tecidos diferentes. Quem para perde músculo e, comendo igual, ganha gordura. Parece que virou, mas são duas coisas.",
  "como acompanhar sua evolução no Brio, semana a semana", "#brio #mitos #musculacao #academia #treino")

V('brio_53_pesado', 'brio', 'mulher que treina pesado fica bombada', 'PESADO', [
 ('hook', 'TREINO PESADO', 'DEIXA BOMBADA?', '[curious] Mulher que treina pesado fica bombada?'),
 ('nao', 'NÃO', 'DO NADA.', 'Não. Pelo menos não do jeito que muita gente tem medo.'),
 ('hormonio', 'MENOS', 'TESTOSTERONA.', 'O corpo da mulher tem bem menos testosterona, e o músculo cresce mais devagar.'),
 ('anos', 'MUITO VOLUME', 'LEVA ANOS.', 'Ganhar muito volume leva anos de treino focado nisso, e muita comida pra isso.'),
 ('forma', 'O PESO', 'DÁ FORMA.', 'O que o peso alto traz é força, firmeza e forma.'),
 ('leve', 'PESO LEVE', 'NÃO TONIFICA MAIS.', '[matter-of-fact] E peso leve com mil repetições não tonifica mais. Tonificar é ganhar músculo e perder gordura.'),
 ('conc', 'RESUMINDO:', 'PODE PEGAR PESADO.', 'Resumindo: pode pegar peso sem medo. O resultado é ficar mais forte, não maior do dia pra noite.'),
 ('cta', 'COMENTA', 'PESADO.', 'Comenta PESADO que eu te mando como registrar suas cargas no Bríu e ver sua força subir. Link na bio.'),
], '10:00', "Mulher que treina pesado fica bombada? 👇\nNão do jeito que muita gente tem medo. O peso alto traz força, firmeza e forma. Volume grande leva anos.",
  "como registrar suas cargas no Brio e ver sua força subir", "#brio #mulheresnamusculacao #musculacao #academia #treinofeminino")

V('brio_54_whey', 'brio', 'janela anabólica: whey logo depois do treino', 'WHEY', [
 ('hook', 'WHEY CORRENDO', 'DEPOIS DO TREINO?', '[curious] Precisa correr pro whey depois do treino?'),
 ('janela', 'JANELA DE', '30 MINUTOS?', 'Muita gente acha que tem uma janela de trinta minutos, senão perde o treino.'),
 ('horas', 'A JANELA', 'É DE HORAS.', 'Os estudos mostram que essa janela é bem maior: de várias horas, antes e depois.'),
 ('total', 'O QUE CONTA:', 'O TOTAL DO DIA.', 'O que mais conta é a proteína do dia inteiro, dividida em umas três ou quatro refeições.'),
 ('comida', 'WHEY', 'É COMIDA.', '[matter-of-fact] E whey não é mágico. É proteína do leite, prática. Comida resolve igual.'),
 ('quando', 'GOSTA?', 'TOMA QUANDO DER.', 'Gosta do whey? Toma na hora que for mais prática pra você.'),
 ('conc', 'RESUMINDO:', 'SEM CORRERIA.', 'Resumindo: sem correria. Bate a proteína do dia e foca em treinar bem.'),
 ('cta', 'COMENTA', 'WHEY.', 'Comenta WHEY que eu te mando como registrar seus treinos no Bríu e acompanhar o que importa: a carga subindo. Link na bio.'),
], '11:30', "Precisa correr pro whey depois do treino? 👇\nA tal janela de 30 minutos é de várias horas. O que conta é a proteína do dia inteiro.",
  "como registrar seus treinos no Brio e acompanhar a carga subindo", "#brio #whey #proteina #musculacao #academia")

V('brio_55_altura', 'brio', 'musculação não atrapalha o crescimento de jovens', 'ALTURA', [
 ('hook', 'MUSCULAÇÃO', 'DEIXA BAIXO?', '[serious] Musculação não deixa ninguém baixo.'),
 ('origem', 'O MEDO:', 'A PLACA DO OSSO.', 'O mito vem do medo de machucar a placa de crescimento, a parte do osso que ainda cresce.'),
 ('estudos', 'ESTUDOS:', 'SEM PREJUÍZO.', 'Mas os estudos com jovens treinando com orientação não mostram prejuízo no crescimento.'),
 ('impacto', 'CORRER E PULAR', 'TÊM MAIS IMPACTO.', 'Correr e pular já colocam mais impacto no osso que uma série bem feita.'),
 ('risco', 'O RISCO REAL:', 'TÉCNICA RUIM.', '[matter-of-fact] O risco de verdade é técnica ruim e peso alto demais, sem ninguém olhando.'),
 ('osso', 'O OSSO', 'FICA MAIS FORTE.', 'E o treino ainda deixa o osso mais forte.'),
 ('conc', 'RESUMINDO:', 'COM ORIENTAÇÃO, PODE.', 'Resumindo: com orientação e boa técnica, jovem pode treinar. Altura vem da genética, não da academia.'),
 ('cta', 'COMENTA', 'ALTURA.', 'Comenta ALTURA que eu te mando como registrar seus treinos no Bríu, com a carga subindo aos poucos. Link na bio.'),
], '12:30', "Musculação deixa baixo? Não. 👇\nOs estudos com jovens treinando com orientação não mostram prejuízo no crescimento. O risco real é técnica ruim.",
  "como registrar seus treinos no Brio, com a carga subindo aos poucos", "#brio #mitos #musculacao #academia #treino")

V('brio_56_junto', 'brio', 'recomposição corporal: perder gordura e ganhar músculo junto', 'JUNTO', [
 ('hook', 'SECAR E CRESCER', 'AO MESMO TEMPO?', '[curious] Dá pra secar e crescer ao mesmo tempo?'),
 ('sim', 'DÁ, SIM.', 'TEM NOME.', 'Dá, sim. Tem até nome: recomposição corporal.'),
 ('quem', 'QUEM CONSEGUE', 'MAIS FÁCIL?', 'Funciona melhor pra quem está começando, voltando de uma pausa, ou tem mais gordura pra perder.'),
 ('receita', 'FORÇA PESADA', '+ PROTEÍNA.', 'A receita: treino de força pesado, proteína alta e só um pouco menos de comida.'),
 ('balanca', 'A BALANÇA', 'QUASE NÃO MEXE.', 'O detalhe: a balança quase não mexe, porque sai gordura e entra músculo.'),
 ('sinal', 'CINTURA CAI,', 'CARGA SOBE.', '[matter-of-fact] O sinal certo é a cintura diminuindo enquanto a carga sobe.'),
 ('conc', 'RESUMINDO:', 'DÁ, NO COMEÇO.', 'Resumindo: dá pra fazer os dois, principalmente no começo. Olha a cintura e a carga, não a balança.'),
 ('cta', 'COMENTA', 'JUNTO.', 'Comenta JUNTO que eu te mando como registrar suas cargas no Bríu e ver a força subir enquanto você seca. Link na bio.'),
], '14:00', "Dá pra secar e crescer ao mesmo tempo? 👇\nDá: recomposição corporal. Força pesada, proteína alta e um pouco menos de comida. Olha a cintura e a carga, não a balança.",
  "como registrar suas cargas no Brio e ver a força subir enquanto você seca", "#brio #recomposicao #hipertrofia #emagrecimento #musculacao")

V('brio_57_secar', 'brio', 'musculação também emagrece', 'SECAR', [
 ('hook', 'MUSCULAÇÃO', 'EMAGRECE, SIM.', '[serious] Musculação emagrece, sim.'),
 ('mito', 'SÓ CARDIO', 'EMAGRECE?', 'Muita gente acha que só esteira emagrece, e musculação é só pra crescer.'),
 ('gasto', 'O TREINO', 'GASTA ENERGIA.', 'Uma hora de musculação gasta energia, parecido com uma caminhada rápida.'),
 ('musculo', 'MAIS MÚSCULO,', 'MAIS GASTO.', 'E o músculo que você ganha gasta um pouco de energia o dia todo, até parado.'),
 ('prato', 'QUEM DECIDE:', 'O PRATO.', '[matter-of-fact] Mas quem decide se o peso cai é o quanto você come. Treino nenhum vence prato cheio.'),
 ('junto', 'O MELHOR:', 'FORÇA + DIETA.', 'O melhor resultado vem de comer um pouco menos e treinar força. Caminhada entra de bônus.'),
 ('conc', 'RESUMINDO:', 'AJUDA, E MUITO.', 'Resumindo: musculação ajuda a emagrecer, e muda o formato do corpo que a esteira não muda.'),
 ('cta', 'COMENTA', 'SECAR.', 'Comenta SECAR que eu te mando como registrar seus treinos no Bríu e acompanhar sua evolução. Link na bio.'),
], '15:30', "Musculação emagrece, sim. 👇\nO treino gasta energia e o músculo novo gasta mais o dia todo. Mas quem decide se o peso cai é o prato.",
  "como registrar seus treinos no Brio e acompanhar sua evolução", "#brio #emagrecimento #musculacao #academia #treino")

V('brio_58_cafe', 'brio', 'café antes do treino melhora o desempenho', 'CAFÉ', [
 ('hook', 'CAFÉ ANTES', 'DO TREINO?', '[curious] Café antes do treino funciona?'),
 ('sim', 'FUNCIONA.', 'TEM ESTUDO.', 'Funciona. A cafeína é dos poucos suplementos com muita prova de efeito.'),
 ('rende', 'RENDE MAIS,', 'CANSA DEPOIS.', 'Ela ajuda a render um pouco mais na série e a demorar mais pra cansar.'),
 ('quando', '30 A 60 MIN', 'ANTES.', 'O melhor é tomar uns trinta a sessenta minutos antes de treinar.'),
 ('dose', '2 XÍCARAS', 'JÁ BASTAM.', 'Pra maioria, duas xícaras já chegam perto da dose dos estudos. Exagerar não aumenta o efeito.'),
 ('noite', 'TREINA À NOITE?', 'CUIDADO COM O SONO.', '[matter-of-fact] Mas se você treina à noite, cuidado: café tarde atrapalha o sono, e o sono pesa mais no resultado.'),
 ('conc', 'RESUMINDO:', 'AJUDA, COM HORA.', 'Resumindo: café ajuda, sim. Duas xícaras, meia hora antes, e longe da hora de dormir.'),
 ('cta', 'COMENTA', 'CAFÉ.', 'Comenta CAFÉ que eu te mando como registrar suas séries no Bríu e ver se você rende mais. Link na bio.'),
], '17:00', "Café antes do treino funciona? 👇\nFunciona: duas xícaras, 30 a 60 minutos antes. Treina à noite? Cuidado com o sono.",
  "como registrar suas séries no Brio e ver se você rende mais", "#brio #cafe #preTreino #musculacao #academia")

V('brio_59_confunde', 'brio', 'confusão muscular: trocar o treino toda semana', 'TROCA', [
 ('hook', 'TROCAR TODA SEMANA', 'NÃO CONFUNDE.', '[serious] Trocar o treino toda semana? Não confunde o músculo.'),
 ('mito', 'CONFUSÃO', 'MUSCULAR?', 'A ideia de surpreender o músculo pra ele crescer é um mito antigo.'),
 ('sinal', 'O SINAL É', 'A CARGA SUBINDO.', 'O que faz crescer é a carga e as repetições subindo, semana após semana.'),
 ('perde', 'TROCOU TUDO?', 'PERDEU A CONTA.', 'Se você troca tudo toda semana, não sabe se está progredindo. Sempre começa do zero.'),
 ('quando', 'MANTÉM', '4 A 8 SEMANAS.', 'O melhor: mantém os principais exercícios por quatro a oito semanas.'),
 ('varia', 'VARIAR', 'COM MOTIVO.', '[matter-of-fact] Trocar pode, mas com motivo: travou, dói, ou enjoou de verdade.'),
 ('conc', 'RESUMINDO:', 'REPETE E SOBE.', 'Resumindo: músculo não se confunde. Ele responde a carga subindo no mesmo exercício.'),
 ('cta', 'COMENTA', 'TROCA.', 'Comenta TROCA que eu te mando como registrar cada exercício no Bríu e ver a carga subir semana a semana. Link na bio.'),
], '18:30', "Trocar o treino toda semana não confunde o músculo. 👇\nO que faz crescer é a carga subindo no mesmo exercício. Mantém os principais por 4 a 8 semanas.",
  "como registrar cada exercício no Brio e ver a carga subir semana a semana", "#brio #treino #musculacao #academia #progressao")

V('brio_60_shape', 'brio', 'transformação de 90 dias da internet: os truques da foto', 'REAL', [
 ('hook', 'SHAPE EM 90 DIAS', 'É REAL?', '[curious] Aquele shape em noventa dias é real?'),
 ('parte', 'PARTE', 'É TRUQUE.', 'Parte é treino. Mas parte é truque de foto.'),
 ('luz', 'LUZ DE CIMA', 'CRIA SOMBRA.', 'Luz de cima marca o abdômen. Na foto do antes, luz de frente e barriga solta.'),
 ('pump', 'PUMP', 'ANTES DA FOTO.', 'Uns minutos de flexão antes da foto incham o músculo por meia hora.'),
 ('postura', 'POSTURA', 'E CONTRAÇÃO.', 'Postura reta, abdômen contraído, e a pele mais escura. Tudo no mesmo dia.'),
 ('compara', 'COMPARA', 'COM VOCÊ.', '[matter-of-fact] Então não compara o seu começo com a foto editada de alguém.'),
 ('conc', 'RESUMINDO:', 'COMPARA NÚMEROS.', 'Resumindo: noventa dias mudam muito, mas não tudo. Compara você com você, nos números.'),
 ('cta', 'COMENTA', 'REAL.', 'Comenta REAL que eu te mando como acompanhar sua evolução no Bríu, com números de verdade. Link na bio.'),
], '19:30', "Aquele shape em 90 dias é real? 👇\nParte é treino, parte é luz, pump e postura na foto. Compara você com você, nos números.",
  "como acompanhar sua evolução no Brio, com números de verdade", "#brio #antesedepois #musculacao #academia #shape")

V('brio_61_foco', 'brio', 'foco mental no músculo durante a série', 'FOCO', [
 ('hook', 'PENSAR NO MÚSCULO', 'FAZ CRESCER?', '[curious] Pensar no músculo faz ele crescer mais?'),
 ('estudo', 'UM ESTUDO', 'TESTOU.', 'Um estudo de dois mil e dezoito testou isso na rosca e na cadeira extensora.'),
 ('braco', 'NO BÍCEPS:', 'CRESCEU MAIS.', 'Quem pensava no músculo durante a série ganhou mais bíceps do que quem só pensava em levantar o peso.'),
 ('perna', 'NA PERNA:', 'QUASE IGUAL.', 'Na perna, a diferença foi pequena.'),
 ('como', 'SENTE', 'O MÚSCULO.', 'Como fazer: peso que você controla, mais devagar, e a atenção no músculo apertando.'),
 ('pesado', 'NO PESADO,', 'FOCA NO MOVIMENTO.', '[matter-of-fact] No pesado, perto do máximo, o foco volta pro movimento. Aí é técnica.'),
 ('conc', 'RESUMINDO:', 'ATENÇÃO CONTA.', 'Resumindo: nos exercícios isolados, sentir o músculo ajuda. É de graça e só pede atenção.'),
 ('cta', 'COMENTA', 'FOCO.', 'Comenta FOCO que eu te mando como registrar suas séries no Bríu e ver seu bíceps responder. Link na bio.'),
], '20:30', "Pensar no músculo faz ele crescer mais? 👇\nNum estudo de 2018, quem focava no bíceps durante a rosca ganhou mais braço. No pesado, o foco é a técnica.",
  "como registrar suas séries no Brio e ver seu bíceps responder", "#brio #biceps #hipertrofia #musculacao #academia")

V('brio_62_rapido', 'brio', 'emagrecer rápido demais leva músculo junto', 'DEVAGAR', [
 ('hook', 'EMAGRECER RÁPIDO', 'LEVA MÚSCULO?', '[curious] Emagrecer rápido demais leva músculo junto?'),
 ('sim', 'PODE', 'LEVAR.', 'Pode. Quanto mais rápido o peso cai, mais músculo tende a sair junto.'),
 ('estudo', 'ESTUDO COM', 'ATLETAS.', 'Num estudo com atletas, quem emagreceu mais devagar perdeu gordura e ainda ganhou músculo.'),
 ('ritmo', 'RITMO:', 'MEIO A 1% POR SEMANA.', 'Um ritmo seguro: meio a um por cento do seu peso por semana.'),
 ('treino', 'NÃO TIRA', 'O PESO PESADO.', '[matter-of-fact] E na dieta, não troca a carga por peso leve. É a carga que avisa o corpo pra guardar o músculo.'),
 ('proteina', 'PROTEÍNA', 'ALTA.', 'Junto com proteína alta, em todas as refeições.'),
 ('conc', 'RESUMINDO:', 'DEVAGAR SEGURA.', 'Resumindo: devagar e com carga, o que sai é gordura. Rápido demais, o músculo vai junto.'),
 ('cta', 'COMENTA', 'DEVAGAR.', 'Comenta DEVAGAR que eu te mando como registrar suas cargas no Bríu e ver se elas seguram na dieta. Link na bio.'),
], '22:00', "Emagrecer rápido demais leva músculo junto? 👇\nPode levar. Meio a 1% do peso por semana, carga alta no treino e proteína em todas as refeições.",
  "como registrar suas cargas no Brio e ver se elas seguram na dieta", "#brio #emagrecimento #dieta #musculacao #academia")

# ============================================================ FIBRA (build3, estilo próprio)
V('fibra_10_supino', 'fibra', 'músculos que trabalham no supino', 'SUPINO', [
 ('hook', 'SUPINO:', '3 MÚSCULOS.', '[curious] Um supino. Três músculos empurrando a barra.'),
 ('peitoral', '1. PEITORAL', 'MAIOR.', 'O principal é o peitoral maior: traz o braço pra frente e empurra a barra.'),
 ('ombro', '2. OMBRO', 'DA FRENTE.', 'O deltoide da frente, no ombro, ajuda a subida inteira.'),
 ('triceps', '3. TRÍCEPS,', 'NO FINAL.', 'E o tríceps estica o cotovelo. Ele trabalha mais no final, quando o braço trava.'),
 ('inclina', 'BANCO', 'INCLINADO?', '[matter-of-fact] Banco inclinado? Mais a parte de cima do peito, e mais ombro.'),
 ('escapula', 'AS COSTAS', 'SEGURAM.', 'E as costas seguram as escápulas firmes no banco. Sem isso, a barra balança.'),
 ('conc', 'RESUMINDO:', 'PEITO, OMBRO, TRÍCEPS.', '[warm] Resumindo: supino é peito, ombro e tríceps juntos. Quer mais a parte de cima do peito? Inclina o banco.'),
 ('cta', 'COMENTA', 'SUPINO.', 'Comenta SUPINO que eu te mando como registrar sua carga no Bríu e ver o supino subir semana a semana. Link na bio.'),
], '12:30', "Um supino. Três músculos empurrando a barra. 🔬👇\nPeitoral maior, deltoide da frente e tríceps no final. Banco inclinado puxa mais a parte de cima do peito.",
  "como registrar sua carga no Brio e ver o supino subir", "#fibratreino #supino #peitoral #musculacao #anatomia",
  formato='diagrama do músculo em cada movimento (6×, 21 contas)',
  fonte='Rodríguez-Ridao D et al. Int J Environ Res Public Health 2020;17(19):7339 (inclinação 30° ativa mais o peitoral clavicular e o deltoide anterior); Lehman GJ. J Strength Cond Res 2005 (tríceps na extensão final)',
  conc=['PEITORAL MAIOR', 'DELTOIDE DA FRENTE', 'TRÍCEPS NO FINAL'], cta=['REGISTRE SUA CARGA NO BRIO', 'E VEJA O SUPINO SUBIR'])

V('fibra_11_descanso', 'fibra', 'síntese de proteína: o músculo cresce no descanso', 'DESCANSO', [
 ('hook', 'O MÚSCULO NÃO', 'CRESCE NO TREINO.', '[curious] O músculo não cresce durante o treino.'),
 ('treino', 'NO TREINO,', 'A FIBRA É ESTRESSADA.', 'No treino, a fibra é estressada: tensão alta, energia gasta e pequenas lesões.'),
 ('sinal', 'O ESTRESSE', 'É UM AVISO.', 'Esse estresse é um aviso. Ele diz pro corpo que aquilo foi pesado demais.'),
 ('obra', 'DEPOIS:', 'A OBRA.', 'Depois, a fabricação de proteína no músculo sobe, e fica alta por um a dois dias.'),
 ('grossa', 'A FIBRA FICA', 'MAIS GROSSA.', 'É aí que a fibra é reforçada, e fica um pouquinho mais grossa do que antes.'),
 ('precisa', 'A OBRA PRECISA:', 'PROTEÍNA E SONO.', '[matter-of-fact] Pra essa obra acontecer, ela precisa de proteína na comida e de sono.'),
 ('conc', 'RESUMINDO:', 'O DESCANSO CONSTRÓI.', '[warm] Resumindo: o treino faz o pedido, o descanso faz a obra. Um sem o outro não cresce.'),
 ('cta', 'COMENTA', 'DESCANSO.', 'Comenta DESCANSO que eu te mando como registrar seus treinos no Bríu e ver a evolução de cada semana. Link na bio.'),
], '19:00', "O músculo não cresce durante o treino. 🔬👇\nO treino é o aviso. A construção vem depois: a fabricação de proteína fica alta por um a dois dias. Precisa de proteína e sono.",
  "como registrar seus treinos no Brio e ver a evolução de cada semana", "#fibratreino #hipertrofia #ciencia #musculacao #descanso",
  formato='crença popular errada na 1ª frase (9×)',
  fonte='MacDougall JD et al. Can J Appl Physiol 1995;20(4):480-6 (síntese proteica +50% em 4 h, +109% em 24 h, perto do basal em 36 h); Phillips SM et al. Am J Physiol 1997;273(1):E99-107 (elevada até 48 h)',
  conc=['TREINO = AVISO', 'DESCANSO = OBRA', 'PROTEÍNA + SONO'], cta=['REGISTRE SEUS TREINOS NO BRIO', 'E VEJA CADA SEMANA'])

# ============================================================ DIA UM (build3, caderno)
V('diaum_09_agacha', 'diaum', 'agachamento em 3 níveis para iniciante', 'AGACHA', [
 ('hook', 'AGACHAR', 'PARECE DIFÍCIL?', '[warm] Agachar parece difícil? Começa pela cadeira.'),
 ('niveis', 'DÁ PRA IR', 'POR NÍVEIS.', 'O agachamento é um dos exercícios mais úteis da vida, e dá pra aprender por níveis.'),
 ('n1', 'NÍVEL 1:', 'CADEIRA.', 'Nível um: senta e levanta da cadeira, sem usar as mãos. Pés firmes no chão.'),
 ('n2', 'NÍVEL 2:', 'SEM CADEIRA.', 'Nível dois: o mesmo movimento, sem a cadeira. Quadril pra trás e peito aberto.'),
 ('n3', 'NÍVEL 3:', 'PAUSA EMBAIXO.', 'Nível três: desce, segura três segundos lá embaixo, e sobe.'),
 ('regra', '3 × 12', '= PRÓXIMO.', 'Quando fizer três séries de doze, todas bem feitas, passa pro próximo nível.'),
 ('conc', 'RESUMINDO:', 'UM NÍVEL POR VEZ.', '[encouraging] Então: começa na cadeira, e sobe um nível de cada vez. Sem pressa.'),
 ('cta', 'COMENTA', 'AGACHA.', 'Comenta AGACHA que eu te mando como registrar suas séries no Bríu e ver sua evolução. Link na bio.'),
], '19:30', "Agachar parece difícil? Começa pela cadeira. 📓👇\nNível 1: senta e levanta da cadeira. Nível 2: sem a cadeira. Nível 3: pausa de 3 segundos embaixo.",
  "como registrar suas séries no Brio e ver sua evolução", "#diaumtreino #agachamento #iniciante #treinoemcasa #comecar",
  formato='cada movimento em fácil, médio e difícil (8×)',
  conc=["começa na cadeira", "3 × 12 = sobe", "um nível por vez"], cta=['registre suas séries no Brio', 'e veja sua evolução'])

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
