"""Pauta de 21/11/2026 — BRIO 4 + FIBRA 4 novos (nada agendado para 21/11 BRT; estoque pausado do BRIO é 30–35 s
e fora da regra). DIA UM pausado.
Métricas (midia/*.json, listar-midia 20/11): média BRIO 1.029, FIBRA 791 (mediana 262).
  BRIO: mulher pesado 1.377 (17 compart.), 1×/semana 1.185; mal: confusão muscular 175 (gancho afirmativo/negando),
        musculação deixa baixo 170, emagrecer rápido 324. Lote 20/11 (peito, 6 meses, perna→braço, flexível) ainda sem medida.
  FIBRA: enjoo na perna 4.967 (6,3×), barra 1.980, queimação 1.563, pump 1.108, descanso 1.042; coceira 184, coração 570.
Evidência de cada tema (regra de 17/11):
 BRIO 79 glúteo  — nosso: mito popular em pergunta (jejum 2.307 = 2,2×; mulher pesado 1.377 = 1,3×, 17 compart.)
        e "não cresce" (ombro 1.507 = 1,5×); fora: estudo viral Plotkin 2023 ("hip thrust vs squat") muito repostado em EN/ES.
 BRIO 80 água    — nosso: mito popular em pergunta (jejum 2.307 = 2,2×; cerveja 1.398 = 1,4×).
 BRIO 81 gelo    — nosso: mito/pergunta de resultado (jejum 2,2×; "treina pesado e não cresce" 1.696 = 1,6×); fora: ice bath trend (EN).
 BRIO 82 noite   — nosso: mito popular (jejum 2,2×) e família sono ("treina pesado e não cresce — SONO" 1.696 = 1,6×).
 FIBRA 26 sentar — nosso: sensação NO TREINO DE PERNA (enjoo 4.967 = 6,3×, 112 compart.); dor muscular "#dormuscular" 1.344 no BRIO.
 FIBRA 27 veias  — nosso: sensação visível do treino como o pump (1.108 = 1,4×) e a barra (1.980).
 FIBRA 28 formiga— nosso: nomear a sensação + derrubar a crença (queimação "não é ácido lático" 1.563 = 2×); fora: "why does pre-workout make you itch" (tema recorrente EN).
 FIBRA 29 escada — nosso: nomear a sensação comum de quem treina (enjoo 6,3×, queimação 2×).
(Views externas não confirmáveis pela busca — Instagram/TikTok bloqueiam a leitura; a evidência principal é a nossa.)"""
P = {}


def V(id, perfil, tema, palavra, beats, hora, leg, gat, tags, **kw):
    P[id] = dict(perfil=perfil, tema=tema, palavra=palavra, beats=beats, hora=hora, leg=leg, gat=gat, tags=tags, **kw)


# ============================================================ BRIO (v2: cenas_v2)
V('brio_79_gluteo', 'brio', 'elevação pélvica x agachamento: glúteo cresce igual', 'GLÚTEO', [
 ('hook', 'ELEVAÇÃO PÉLVICA', 'É A MELHOR?', '[curious] Elevação pélvica é o melhor pro glúteo?'),
 ('estudo', 'AGACHAMENTO', 'OU ELEVAÇÃO?', 'Num estudo de nove semanas, um grupo só agachou e o outro só fez elevação.'),
 ('igual', 'O GLÚTEO', 'CRESCEU IGUAL.', 'O glúteo cresceu parecido nos dois. E o agachamento ainda trabalhou a coxa.'),
 ('carga', 'O QUE MANDA:', 'CARGA SUBINDO.', 'O que faz crescer é série puxada e carga subindo, mais do que o exercício.'),
 ('conc', 'RESUMINDO:', 'OS DOIS FUNCIONAM.', 'Resumindo: os dois funcionam. Escolhe o que você gosta e sobe a carga.'),
 ('cta', 'COMENTA', 'GLÚTEO.', 'Comenta GLÚTEO que eu te mando como registrar suas séries no Bríu. Link na bio.'),
], '14:00', "Elevação pélvica é o melhor pro glúteo? 👇\nNum estudo de 9 semanas, agachamento e elevação pélvica fizeram o glúteo crescer parecido. O que manda é série puxada e carga subindo.",
  "como registrar suas séries no Brio", "#brio #gluteo #agachamento #musculacao #academia",
  evid='nosso: mito popular em pergunta — jejum 2.307 (2,2×), mulher pesado 1.377 (1,3×, 17 compart.); "não cresce": ombro 1.507 (1,5×)',
  fonte='Plotkin DL et al. Front Physiol 2023;14:1279170 ("Hip thrust and back squat training elicit similar gluteus muscle hypertrophy", 9 semanas)')

V('brio_80_agua', 'brio', 'água gelada no treino não faz mal (choque térmico é mito)', 'ÁGUA', [
 ('hook', 'ÁGUA GELADA', 'FAZ MAL?', '[curious] Água gelada no treino faz mal?'),
 ('mito', 'NÃO.', 'É MITO.', 'Não. Esse tal choque térmico é mito.'),
 ('estudo', 'NO CALOR:', '+10 MINUTOS.', 'Num estudo no calor, quem bebeu água gelada pedalou cerca de dez minutos a mais.'),
 ('esfria', 'ESFRIA', 'POR DENTRO.', 'Ela esfria o corpo por dentro, e a temperatura demora mais pra subir.'),
 ('conc', 'RESUMINDO:', 'BEBE ÁGUA.', 'Resumindo: gelada ou natural, o que importa é beber água durante o treino.'),
 ('cta', 'COMENTA', 'ÁGUA.', 'Comenta ÁGUA que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '11:30', "Água gelada no treino faz mal? 👇\nNão: o choque térmico é mito. Num estudo no calor, quem bebeu água gelada pedalou cerca de 10 minutos a mais. Gelada ou natural, beba água no treino.",
  "como registrar seus treinos no Brio", "#brio #mitos #agua #treino #academia",
  evid='nosso: mito popular em pergunta — jejum 2.307 (2,2×), cerveja 1.398 (1,4×)',
  fonte='Lee JKW, Shirreffs SM, Maughan RJ. Med Sci Sports Exerc 2008;40(9):1637-44 ("Cold drink ingestion improves exercise endurance capacity in the heat": 63,8 x 52,9 min); Mündel T et al. Exp Physiol 2006;91(5):925-33')

V('brio_81_gelo', 'brio', 'banho de gelo depois da musculação atrapalha o ganho de músculo', 'GELO', [
 ('hook', 'BANHO DE GELO', 'AJUDA?', '[curious] Banho de gelo depois do treino ajuda?'),
 ('sinal', 'PODE', 'ATRAPALHAR.', 'Pode atrapalhar. O frio apaga parte do sinal que faz o músculo crescer.'),
 ('estudo', '12 SEMANAS', 'DE TREINO.', 'Num estudo de doze semanas, quem fez banho de gelo depois do treino ganhou menos músculo e força.'),
 ('quem', 'SERVE PRA', 'QUEM COMPETE.', 'Ele serve pra quem compete e precisa se recuperar rápido.'),
 ('conc', 'RESUMINDO:', 'GELO LONGE.', 'Resumindo: quer crescer? Deixa o gelo longe do treino de força.'),
 ('cta', 'COMENTA', 'GELO.', 'Comenta GELO que eu te mando como acompanhar sua evolução no Bríu. Link na bio.'),
], '18:00', "Banho de gelo depois do treino ajuda? 👇\nPode atrapalhar: num estudo de 12 semanas, quem entrou na água gelada depois da musculação ganhou menos músculo e menos força. Quer crescer? Gelo longe do treino.",
  "como acompanhar sua evolução no Brio", "#brio #mitos #hipertrofia #musculacao #academia",
  evid='nosso: pergunta de resultado/mito — jejum 2.307 (2,2×), treina pesado e não cresce 1.696 (1,6×)',
  fonte='Roberts LA et al. J Physiol 2015;593(18):4285-301 (imersão em água fria após o treino reduziu ganhos de massa e força em 12 semanas); Fuchs CJ et al. J Physiol 2020;598(4):755-72')

V('brio_82_noite', 'brio', 'treinar à noite não atrapalha o sono (só intenso 1 h antes)', 'NOITE', [
 ('hook', 'TREINAR À NOITE', 'TIRA O SONO?', '[curious] Treinar à noite atrapalha o sono?'),
 ('nao', 'NA MAIORIA,', 'NÃO.', 'Na maioria das vezes, não. Uma revisão juntou vinte e três estudos.'),
 ('profundo', 'SONO PROFUNDO:', 'ATÉ UM POUCO MAIS.', 'Quem treinou à noite dormiu tão bem quanto, e teve até um pouco mais de sono profundo.'),
 ('excecao', 'SÓ EVITA:', 'PESADO 1 H ANTES.', 'A exceção é treino muito intenso, menos de uma hora antes de deitar.'),
 ('conc', 'RESUMINDO:', 'PODE TREINAR.', 'Resumindo: se a noite é seu horário, treina. Só termina uma hora antes de dormir.'),
 ('cta', 'COMENTA', 'NOITE.', 'Comenta NOITE que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '21:00', "Treinar à noite atrapalha o sono? 👇\nNa maioria das vezes, não: numa revisão de 23 estudos, quem treinou à noite dormiu tão bem quanto. Só evite treino muito intenso menos de 1 hora antes de deitar.",
  "como registrar seus treinos no Brio", "#brio #sono #treinoanoite #musculacao #academia",
  evid='nosso: mito popular — jejum 2.307 (2,2×); família sono — treina pesado e não cresce (SONO) 1.696 (1,6×)',
  fonte='Stutz J, Eiholzer R, Spengler CM. Sports Med 2019;49(2):269-87 (meta-análise, 23 estudos: exercício à noite não piora o sono; exceção: exercício vigoroso < 1 h antes de deitar)')

# ============================================================ FIBRA (build3)
V('fibra_26_sentar', 'fibra', 'dor muscular tardia: piora no segundo dia depois do treino de perna', 'SENTAR', [
 ('hook', 'DÓI ATÉ', 'PRA SENTAR?', '[curious] Treinou perna e dói até pra sentar?'),
 ('dia2', 'PIORA NO', 'SEGUNDO DIA.', 'E piora no segundo dia: o pico vem entre um e três dias depois.'),
 ('descida', 'CULPA DA', 'DESCIDA.', 'A culpa é da descida: o músculo freia o peso e ganha pequenas lesões.'),
 ('nervo', 'O NERVO FICA', 'SENSÍVEL.', 'Aí o corpo inflama a área pra consertar, e os nervos ficam sensíveis a cada movimento.'),
 ('conc', 'RESUMINDO:', 'PASSA LOGO.', '[warm] Então: passa em poucos dias, e a cada semana treinando, dói menos.'),
 ('cta', 'COMENTA', 'SENTAR.', 'Comenta SENTAR que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '19:00', "Treinou perna e dói até pra sentar? 🔬👇\nA dor chega ao máximo de 1 a 3 dias depois. A descida do agachamento cria pequenas lesões, o corpo inflama pra consertar e os nervos ficam sensíveis. Passa, e dói menos a cada semana.",
  "como registrar seus treinos no Brio", "#fibratreino #dormuscular #treinodeperna #ciencia #musculacao",
  formato='nomear a sensação NO TREINO DE PERNA (enjoo na perna 4.967 = 6,3×)',
  fonte='Cheung K, Hume P, Maxwell L. Sports Med 2003;33(2):145-64 (DOMS: pico 24–72 h, ação excêntrica); Mizumura K, Taguchi T. J Physiol Sci 2016;66(1):43-52 (sensibilização de nociceptores por NGF/GDNF); Nosaka K: efeito da carga repetida',
  conc=['PICO EM 1 A 3 DIAS', 'CULPA DA DESCIDA', 'DÓI MENOS DEPOIS'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_27_veias', 'fibra', 'veias saltando no treino: mais sangue chegando e pouca gordura', 'VEIA', [
 ('hook', 'AS VEIAS', 'SALTAM?', '[curious] Por que as veias saltam no treino?'),
 ('sangue', 'O MÚSCULO', 'PEDE SANGUE.', 'O músculo trabalhando pede muito mais sangue.'),
 ('volta', 'A VEIA', 'ENCHE.', 'A veia é o caminho de volta. Com tanto sangue chegando, ela enche e estufa.'),
 ('gordura', 'MENOS GORDURA,', 'MAIS VEIA.', 'Com menos gordura embaixo da pele, a veia fica perto da superfície e aparece mais.'),
 ('conc', 'RESUMINDO:', 'É NORMAL.', '[warm] Então: é sinal de músculo trabalhando, e minutos depois ela volta ao normal.'),
 ('cta', 'COMENTA', 'VEIA.', 'Comenta VEIA que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '12:30', "Por que as veias saltam no treino? 🔬👇\nO músculo trabalhando pede muito mais sangue, e a veia, que é o caminho de volta, enche e estufa. Com menos gordura embaixo da pele, aparece mais. Minutos depois, volta ao normal.",
  "como registrar seus treinos no Brio", "#fibratreino #veias #pump #ciencia #musculacao",
  formato='sensação visível do treino, como o pump (1.108 = 1,4×) e a barra (1.980)',
  fonte='Joyner MJ, Casey DP. Physiol Rev 2015;95(2):549-601 (hiperemia do exercício: fluxo muscular sobe muitas vezes); Scientific American, "Why do veins pop out when you exercise?"',
  conc=['MAIS SANGUE', 'A VEIA ENCHE', 'VOLTA AO NORMAL'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_28_formiga', 'fibra', 'formigamento do pré-treino: beta-alanina ativa sensores de coceira', 'FORMIGA', [
 ('hook', 'FORMIGAMENTO', 'DO PRÉ-TREINO?', '[curious] Aquele formigamento depois do pré-treino?'),
 ('beta', 'É A', 'BETA-ALANINA.', 'É a beta-alanina, um ingrediente comum no pré-treino.'),
 ('nervo', 'SENSORES', 'DE COCEIRA.', 'Ela liga sensores de nervo na pele, os mesmos da coceira. Por isso pinica no rosto.'),
 ('dose', 'MAIS DOSE,', 'MAIS FORMIGA.', 'Quanto maior a dose de uma vez, mais formiga. Em geral passa em uma hora.'),
 ('conc', 'RESUMINDO:', 'NÃO MEDE EFEITO.', '[warm] Então: é inofensivo, e não quer dizer que o pré-treino tá funcionando.'),
 ('cta', 'COMENTA', 'FORMIGA.', 'Comenta FORMIGA que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '16:00', "Aquele formigamento depois do pré-treino? 🔬👇\nÉ a beta-alanina: ela liga sensores de nervo da pele, os mesmos da coceira. Quanto maior a dose de uma vez, mais formiga, e em geral passa em uma hora. Não quer dizer que o pré-treino tá funcionando.",
  "como registrar seus treinos no Brio", "#fibratreino #pretreino #betaalanina #ciencia #academia",
  formato='nomear a sensação + derrubar a crença (queimação "não é ácido lático" 1.563 = 2×); fora: "why does pre-workout make you itch" (tema recorrente EN)',
  fonte='Liu Q et al. Cell 2012;149(4):800-13 (beta-alanina ativa o receptor MrgprD em neurônios de coceira); Harris RC et al. Amino Acids 2006;30(3):279-89 (parestesia dose-dependente, ~1 h); Trexler ET et al. JISSN 2015 (ISSN position stand)',
  conc=['BETA-ALANINA', 'NERVOS DA PELE', 'INOFENSIVO'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_29_escada', 'fibra', 'forte na musculação e sem fôlego na escada: especificidade do treino', 'ESCADA', [
 ('hook', 'CANSA', 'NA ESCADA?', '[curious] Treina pesado e cansa na escada?'),
 ('especifico', 'O CORPO MELHORA', 'NO QUE TREINA.', 'O corpo melhora no que treina. Musculação treina pouco o fôlego.'),
 ('usinas', 'USINAS', 'DE ENERGIA.', 'Pra subir sem parar, o músculo precisa de mais usinas de energia.'),
 ('cardio', 'QUEM CRIA:', 'O CARDIO.', 'Quem cria isso é o cardio, e o coração passa a bombear mais a cada batida.'),
 ('conc', 'RESUMINDO:', 'JUNTA OS DOIS.', '[warm] Então: junta os dois. Vinte minutos de cardio puxado, três vezes na semana, já ajudam.'),
 ('cta', 'COMENTA', 'ESCADA.', 'Comenta ESCADA que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '22:00', "Treina pesado e cansa na escada? 🔬👇\nO corpo melhora no que você treina. Fôlego pede mais usinas de energia no músculo e um coração que bombeia mais a cada batida. Quem cria isso é o cardio.",
  "como registrar seus treinos no Brio", "#fibratreino #folego #cardio #ciencia #musculacao",
  formato='nomear a sensação comum de quem treina (enjoo 6,3×, queimação 2×)',
  fonte='Garber CE et al. ACSM Position Stand, Med Sci Sports Exerc 2011;43(7):1334-59 (cardio vigoroso 20–60 min, 3 dias/sem); Hughes DC et al. Front Physiol 2018 (adaptações específicas: força x endurance — mitocôndrias e capilares)',
  conc=['ESPECIFICIDADE', 'MITOCÔNDRIAS', 'CARDIO 3×/SEMANA'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

if __name__ == '__main__':
    import re
    for k, v in P.items():
        txt = " ".join(b[3] for b in v['beats'])
        n = len(txt); w1 = len(re.sub(r"\[[^\]]*\]\s*", "", v['beats'][0][3]).split("?")[0].split(".")[0].split())
        print(k, n, 'chars', w1, 'palavras', len(v['beats']), 'beats', 'Bríu' in v['leg'] + v['gat'] + v['tags'])
