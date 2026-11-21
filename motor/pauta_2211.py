"""Pauta de 22/11/2026 — BRIO 3 novos (11:30, 14:00, 21:00; 18:00 já tem brio-81-gelo) + FIBRA 4 novos. DIA UM pausado.
Estoque pausado do BRIO: 30–35 s, formato antigo e/ou temas que foram mal (suplemento, técnica) — não reagendado.
Métricas (midia/*.json, listar-midia 21/11 16:52 UTC): média BRIO 1.019 (mediana 1.235), FIBRA 690 (mediana 264).
  BRIO: seis meses 1.534, secar e crescer 1.624 (13 compart.), perna→braço 1.301; mal: peito não cresce 142, flexibilidade 133,
        água gelada 139 (horas). Watch time bom ~12–13 s, ruim ~5 s.
  FIBRA: "por que o treino de perna cansa tanto?" 2.182 (3,2×) — de novo treino de perna/academia; enjoo 5.039, barra 1.982,
        queimação 1.563; sensações de corrida/rara ficaram < 450 (começo da corrida 38, sensação boa 71, veias 201, mãos 203).
        → FIBRA sai de "sensação rara" e vai para: academia/perna, barra, mito do corpo derrubado.
BRIO segue a fórmula "erro → consequência → volta" (usuário, 20/11), 30–40 s, kit cenas_v2 com rewind_in e legenda palavra a palavra.
Evidência de cada tema (regra de 17/11):
 BRIO 83 força  — nosso: supino +10 kg quanto tempo 1.678 (1,6×), falha em toda série 1.546 (1,5×), deload 1.4k (1,4×), treino fraco não é regressão 1.218.
 BRIO 84 3x     — nosso: mesmo músculo todo dia 1.703 (1,7×), 1×/semana funciona 1.198 (1,2×), treina pesado e não cresce 1.705.
 BRIO 85 perna  — nosso: "X não cresce" ombro 1.520 (1,5×, 17 compart.), treina pesado e não cresce 1.705 (1,7×), perna faz braço crescer? 1.301;
                  perna é o tema que mais performa no FIBRA (enjoo 5.039, cansaço 2.182).
 FIBRA 30 barra — nosso: músculos da barra fixa 1.982 (2,9×, 25 compart., 24 salvos).
 FIBRA 31 along — nosso: mito do corpo derrubado — queimação "não é ácido lático" 1.563 (2,3×); BRIO "alongar antes" 1.4k.
 FIBRA 32 legpr — nosso: treino de perna — enjoo 5.039 (7,3×), cansaço da perna 2.182 (3,2×).
 FIBRA 33 desc  — nosso: "por que" sobre o músculo na série — queimação 1.563 (2,3×), pump 1.108 (1,6×), descanso 1.043 (1,5×).
(Views de outros perfis não confirmáveis por busca — Instagram/TikTok bloqueiam a leitura; a evidência é a nossa.)"""
P = {}


def V(id, perfil, tema, palavra, beats, hora, leg, gat, tags, **kw):
    P[id] = dict(perfil=perfil, tema=tema, palavra=palavra, beats=beats, hora=hora, leg=leg, gat=gat, tags=tags, **kw)


# ============================================================ BRIO — cadeia erro → consequência → volta
# beat: (vis, palavra-destaque, texto). vis começando com 'f' = "Então..." (entra com ◀◀)
V('brio_83_forca', 'brio', 'por que a força para de subir: carga leve, descanso curto e troca de exercício', 'FORÇA', [
 ('e1', 'LEVE', '[serious] Se você só treina leve, a força trava. Quinze repetições fáceis, todo treino.'),
 ('f1', 'PESADO', 'Então você pega pesado, de cinco a oito repetições.'),
 ('e2', 'TRINTA', 'Mas se descansar só trinta segundos, a próxima série despenca.'),
 ('f2', 'MINUTOS', 'Então você descansa de dois a três minutos.'),
 ('e3', 'TROCAR', 'Mas se trocar de exercício todo mês, nunca pega o jeito.'),
 ('f3', 'MESMOS', 'Então você repete os mesmos por dois meses, e anota a carga.'),
 ('conc', 'SOBE', '[confident] Aí sim: peso, descanso e repetição. A força volta a subir.'),
 ('cta', 'FORÇA', 'Comenta FORÇA que eu te mando como registrar suas séries no Bríu. Link na bio.'),
], '11:30', "Sua força parou de subir? 👇\nSó carga leve, descanso de 30 segundos e exercício novo todo mês. Pesado de 5 a 8 repetições, 2 a 3 minutos de descanso e os mesmos exercícios por 2 meses: aí a força volta a subir.",
  "como registrar suas séries no Brio", "#brio #forca #musculacao #treino #academia",
  titulo=('SUA FORÇA', 'PAROU?'),
  evid='nosso: supino +10 kg 1.678 (1,6×), falha em toda série 1.546 (1,5×), deload 1.4k (1,4×)',
  fonte='Schoenfeld BJ et al. JSCR 2017;31(12):3508-23 (carga alta > leve para força, hipertrofia parecida); Schoenfeld BJ et al. JSCR 2016;30(7):1805-12 (descanso 3 min > 1 min para força); Grgic J et al. 2018 (intervalos de descanso)',
  cons={'e1': 'stuck', 'e2': 'drop', 'e3': 'confuse'})

V('brio_84_tres', 'brio', 'crescer treinando só 3 vezes por semana: corpo todo, treino curto e dias fixos', 'TREINO', [
 ('e1', 'UMA', '[serious] Se você faz um músculo por treino. Em três dias, cada um trabalha uma vez só.'),
 ('f1', 'CORPO', 'Então você treina o corpo todo, em cada treino.'),
 ('e2', 'DEZ', 'Mas se fizer dez exercícios, o treino passa de duas horas.'),
 ('f2', 'CINCO', 'Então você faz cinco exercícios, em quarenta e cinco minutos.'),
 ('e3', 'FALTAR', 'Mas se faltar um dia, perde um terço da semana.'),
 ('f3', 'FIXOS', 'Então você deixa os três dias fixos, como compromisso.'),
 ('conc', 'CRESCER', '[confident] Aí sim: corpo todo, treino curto e dias fixos. Três vezes dá pra crescer.'),
 ('cta', 'TREINO', 'Comenta TREINO que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '14:00', "Só dá pra treinar 3 vezes por semana? 👇\nUm músculo por dia deixa cada um parado a semana inteira. Corpo todo em cada treino, 5 exercícios em 45 minutos e 3 dias fixos: dá pra crescer.",
  "como registrar seus treinos no Brio", "#brio #treino #hipertrofia #musculacao #academia",
  titulo=('3 VEZES POR', 'SEMANA DÁ?'),
  evid='nosso: mesmo músculo todo dia 1.703 (1,7×), treina pesado e não cresce 1.705 (1,7×), 1×/semana funciona 1.198 (1,2×)',
  fonte='Schoenfeld BJ, Ogborn D, Krieger JW. Sports Med 2016;46(11):1689-97 (treinar o músculo 2×/sem > 1×/sem); Schoenfeld BJ et al. JSCR 2015;29(7):1821-9 (corpo todo 3×/sem x divisão)',
  cons={'e1': 'week1', 'e2': 'clock', 'e3': 'miss'})

V('brio_85_perna', 'brio', 'por que a perna não cresce: carga perto da falha, descida funda e 2×/semana', 'PERNA', [
 ('e1', 'LEVE', '[serious] Se você treina perna leve, ela não cresce. Vinte repetições fáceis não bastam.'),
 ('f1', 'CARGA', 'Então você coloca carga no agachamento, perto da falha.'),
 ('e2', 'METADE', 'Mas se descer só até a metade, o glúteo cresce menos.'),
 ('f2', 'FUNDO', 'Então você desce fundo, até onde controla.'),
 ('e3', 'QUINZE', 'Mas se treinar perna só a cada quinze dias, ela fica pra trás.'),
 ('f3', 'DUAS', 'Então você treina perna duas vezes por semana.'),
 ('conc', 'CRESCE', '[confident] Aí sim: carga, descida funda e duas vezes na semana. A perna cresce.'),
 ('cta', 'PERNA', 'Comenta PERNA que eu te mando como registrar suas séries no Bríu. Link na bio.'),
], '21:00', "Sua perna não cresce? 👇\nCarga leve, meio agachamento e perna a cada 15 dias. Carga perto da falha, descida funda e perna 2 vezes por semana: aí a perna cresce.",
  "como registrar suas séries no Brio", "#brio #treinodeperna #agachamento #musculacao #academia",
  titulo=('SUA PERNA', 'NÃO CRESCE?'),
  evid='nosso: ombro não cresce 1.520 (1,5×, 17 compart.), treina pesado e não cresce 1.705 (1,7×), perna faz braço crescer? 1.301; perna no FIBRA: enjoo 5.039, cansaço 2.182',
  fonte='Kubo K et al. Eur J Appl Physiol 2019;119(9):1933-42 (agachamento completo x meio: glúteo e adutores cresceram mais; quadríceps parecido); Schoenfeld BJ et al. Sports Med 2016 (2×/sem > 1×/sem)',
  cons={'e1': 'stuck', 'e2': 'half', 'e3': 'cal'})

# ============================================================ FIBRA (build3, prancha técnica)
V('fibra_30_barra', 'fibra', 'barra fixa é difícil porque você levanta quase o corpo inteiro', 'BARRA', [
 ('hook', 'POR QUE A BARRA', 'É TÃO DIFÍCIL?', '[curious] Por que a barra fixa é tão difícil?'),
 ('corpo', 'VOCÊ LEVANTA', 'O CORPO INTEIRO.', 'Você puxa quase o corpo inteiro. Quem pesa oitenta quilos sobe uns setenta e cinco.'),
 ('quilo', 'CADA QUILO', 'PESA NA BARRA.', 'E cada quilo a mais no corpo entra na conta. Na barra, vale a força pelo seu peso.'),
 ('braco', 'BRAÇO PEQUENO,', 'CARGA GRANDE.', 'Quem puxa são as costas e o bíceps, bem menores que a perna que te carrega o dia todo.'),
 ('conc', 'RESUMINDO:', 'É O SEU PESO.', '[warm] Então: não é fraqueza. É o peso do corpo numa puxada só.'),
 ('cta', 'COMENTA', 'BARRA.', 'Comenta BARRA que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '12:30', "Por que a barra fixa é tão difícil? 🔬👇\nVocê puxa quase o corpo inteiro: quem pesa 80 kg sobe uns 75. Cada quilo a mais entra na conta, e quem puxa são as costas e o bíceps.",
  "como registrar seus treinos no Brio", "#fibratreino #barrafixa #costas #ciencia #musculacao",
  formato='músculos da barra fixa 1.982 (2,9×, 25 compart.)',
  fonte='Youdas JW et al. JSCR 2010;24(12):3404-14 (pull-up: latíssimo, bíceps, trapézio); massa dos segmentos: Dempster/Winter (mãos e antebraços ~5% do corpo ficam na barra)',
  conc=['QUASE O CORPO TODO', 'FORÇA PELO PESO', 'COSTAS E BÍCEPS'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_31_alonga', 'fibra', 'alongar depois do treino não evita a dor muscular do dia seguinte', 'ALONGA', [
 ('hook', 'ALONGAR', 'EVITA A DOR?', '[curious] Alongar depois do treino evita a dor?'),
 ('estudo', 'DOZE', 'ESTUDOS.', 'Não evita. Uma revisão de doze estudos achou quase nenhuma diferença.'),
 ('fibra', 'A DOR VEM', 'DE DENTRO.', 'A dor vem de pequenas lesões na fibra e do corpo consertando. Esticar não desfaz isso.'),
 ('serve', 'ALONGAR', 'SERVE PRA OUTRA.', 'Alongar continua bom pra ganhar flexibilidade. Só não serve pra dor.'),
 ('conc', 'RESUMINDO:', 'É O TEMPO.', '[warm] Então: alonga se você gosta. Pra dor, quem resolve é o tempo.'),
 ('cta', 'COMENTA', 'ALONGA.', 'Comenta ALONGA que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '16:00', "Alongar depois do treino evita a dor do dia seguinte? 🔬👇\nUma revisão de 12 estudos achou quase nenhuma diferença. A dor vem de pequenas lesões na fibra e do conserto. Alongar é bom pra flexibilidade, não pra dor.",
  "como registrar seus treinos no Brio", "#fibratreino #alongamento #dormuscular #ciencia #musculacao",
  formato='mito do corpo derrubado — queimação "não é ácido lático" 1.563 (2,3×); BRIO alongar antes 1.4k',
  fonte='Herbert RD, de Noronha M, Kamper SJ. Cochrane Database Syst Rev 2011;(7):CD004577 (12 estudos: alongar antes/depois reduz a dor 1–4 pontos numa escala de 100)',
  conc=['12 ESTUDOS', 'QUASE NADA', 'TEMPO RESOLVE'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_32_legpress', 'fibra', 'leg press parece mais leve que o agachamento: trenó inclinado, tronco e equilíbrio', 'PESO', [
 ('hook', 'O LEG PRESS', 'PARECE LEVE?', '[curious] Por que o leg press parece tão leve?'),
 ('rampa', 'O TRENÓ', 'É INCLINADO.', 'Primeiro: o trenó é inclinado. Só parte do peso das anilhas pesa contra a perna.'),
 ('tronco', 'NO AGACHAMENTO,', 'O TRONCO PESA.', 'Segundo: no agachamento, a perna também levanta o seu tronco, que não entra na conta.'),
 ('equil', 'SEM', 'EQUILÍBRIO.', 'E no leg press ninguém se equilibra: costas e abdômen ficam encostados.'),
 ('conc', 'RESUMINDO:', 'NÃO COMPARA.', '[warm] Então: os números não se comparam. Compara o leg press só com ele mesmo.'),
 ('cta', 'COMENTA', 'PESO.', 'Comenta PESO que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '19:00', "Por que o leg press parece tão mais leve que o agachamento? 🔬👇\nO trenó é inclinado, então só parte das anilhas pesa contra a perna. No agachamento, a perna ainda levanta o tronco e o corpo precisa se equilibrar.",
  "como registrar seus treinos no Brio", "#fibratreino #legpress #treinodeperna #ciencia #musculacao",
  formato='treino de perna — enjoo 5.039 (7,3×), cansaço da perna 2.182 (3,2×)',
  fonte='Física do plano inclinado (trenó a 45°: componente do peso ≈ 0,7 × carga); Escamilla RF et al. MSSE 2001;33(9):1552-66 (leg press x agachamento: cinética e ativação); massa acima do joelho ≈ 85% do corpo (Winter)',
  conc=['TRENÓ INCLINADO', 'TRONCO FORA', 'SEM EQUILÍBRIO'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_33_descida', 'fibra', 'o músculo é mais forte na descida (excêntrica): pontes seguram e a titina ajuda', 'DESCIDA', [
 ('hook', 'MAIS FORTE', 'NA DESCIDA?', '[curious] Por que você aguenta mais peso na descida?'),
 ('freia', 'O MÚSCULO', 'FREIA.', 'Na descida, o músculo não levanta. Ele freia o peso.'),
 ('pontes', 'AS PONTES', 'SEGURAM.', 'As pontes dentro da fibra seguram esticadas, e uma mola gigante, a titina, ajuda a segurar.'),
 ('terco', 'UM TERÇO', 'A MAIS.', 'Por isso você controla cerca de um terço a mais na descida do que na subida.'),
 ('conc', 'RESUMINDO:', 'NÃO É IMPRESSÃO.', '[warm] Então: não é impressão. Na descida, o músculo é mais forte mesmo.'),
 ('cta', 'COMENTA', 'DESCIDA.', 'Comenta DESCIDA que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '22:00', "Por que você aguenta mais peso na descida? 🔬👇\nNa descida o músculo freia em vez de levantar: as pontes dentro da fibra seguram esticadas e a titina, uma mola gigante, ajuda. Dá cerca de um terço a mais.",
  "como registrar seus treinos no Brio", "#fibratreino #excentrico #forca #ciencia #musculacao",
  formato='"por que" sobre o músculo na série — queimação 1.563 (2,3×), pump 1.108 (1,6×), descanso 1.043 (1,5×)',
  fonte='Herzog W. J Appl Physiol 2014;116(11):1407-17 (titina e força excêntrica); Roig M et al. Br J Sports Med 2009;43(8):556-68 (excêntrica ~20–60% acima da concêntrica)',
  conc=['O MÚSCULO FREIA', 'TITINA SEGURA', '1/3 A MAIS'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

if __name__ == '__main__':
    import re
    for k, v in P.items():
        txt = " ".join(b[-1] for b in v['beats'])
        clean = re.sub(r"\[[^\]]*\]\s*", "", txt)
        w1 = len(re.split(r"[.?!]", clean)[0].split())
        print(k, len(clean), 'chars', w1, 'palavras 1ª frase', len(v['beats']), 'beats', 'Bríu' in v['leg'] + v['gat'] + v['tags'])
