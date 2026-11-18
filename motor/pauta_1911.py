"""Pauta de 19/11/2026 — FIBRA 4 novos (BRIO 19/11 já agendado do estoque em 17/11). DIA UM pausado.
Métricas de 18/11 (midia/*.json, listar-midia 18/11 16:51 UTC): média FIBRA 913, BRIO 1.043.
  FIBRA: enjoo na perna 4.710 (5,2× a média, 112 compartilhamentos), barra/músculos 1.978, queimação 1.562, pump 1.107,
  descanso 1.040. Mal: velocista×maratonista 22, gordura pelo pulmão 15, supino 259, agachamento 159, tremor 210, cãibra 247,
  estalo no joelho 396. Gosto de sangue 171 (com poucas horas no ar — medir).
  → o que performa no FIBRA é "nomear a sensação que a pessoa sente no treino e explicar" (enjoo/queimação/pump).
Evidência de cada tema (regra de 17/11):
  18 coceira   — nosso: formato sensação (enjoo 4.710 = 5,2×; queimação 1.562 = 1,7×); fora: @dr.dan_dpt (TikTok, fisioterapeuta)
                 tem série recorrente sobre "runner's itch" (tiktok.com/@dr.dan_dpt/video/7224250937395662126 e .../7449854651089915167)
                 — pergunta recorrente o bastante para virar série do criador.
  19 cabeça    — nosso: formato sensação (enjoo 5,2×); mesma família "pressão no esforço" (tontura, agendado 18/11).
  20 vermelho  — nosso: formato sensação (enjoo 5,2×); "sensação visível" igual ao pump (braço inchado 1.107 = 1,2×).
  21 pontada   — nosso: formato sensação (enjoo 5,2×); fora: Tibo InShape (@tiboinshape, maior perfil fitness da França)
                 "Side stitch solution" (tiktok.com/@tiboinshape/video/7371467252480232736); falta de ar/dor no cardio na lista do usuário (17/11).
(TikTok bloqueia leitura de views pela busca; números externos não confirmados — a evidência principal é o nosso enjoo 5,2×.)"""
P = {}


def V(id, perfil, tema, palavra, beats, hora, leg, gat, tags, **kw):
    P[id] = dict(perfil=perfil, tema=tema, palavra=palavra, beats=beats, hora=hora, leg=leg, gat=gat, tags=tags, **kw)


V('fibra_18_coceira', 'fibra', 'coceira nas pernas ao começar o cardio: vasinhos se abrindo', 'COCEIRA', [
 ('hook', 'COCEIRA', 'NAS PERNAS?', '[curious] Coceira nas pernas quando começa a correr?'),
 ('vasos', 'OS VASINHOS', 'SE ABREM.', 'São os vasinhos se abrindo: o sangue chega rápido na pele.'),
 ('nervo', 'OS NERVOS', 'ESTRANHAM.', 'Os nervos em volta sentem esse esticão e mandam sinal de coceira.'),
 ('parado', 'QUEM FICOU PARADO', 'SENTE MAIS.', 'Por isso quem ficou dias parado sente mais: os vasos desacostumaram.'),
 ('conc', 'RESUMINDO:', 'CONSTÂNCIA RESOLVE.', '[warm] Então: com treino frequente, passa. Se aparecer placa ou inchaço, procura um médico.'),
 ('cta', 'COMENTA', 'COCEIRA.', 'Comenta COCEIRA que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '12:30', "Coceira nas pernas quando começa a correr? 🔬👇\nSão os vasinhos se abrindo: o sangue chega rápido e os nervos em volta mandam sinal de coceira. Quem ficou dias parado sente mais. Com treino frequente, passa.",
  "como registrar seus treinos no Brio", "#fibratreino #coceira #cardio #ciencia #corrida",
  formato='nomear a sensação (enjoo 4.710 = 5,2× a média do FIBRA); fora: @dr.dan_dpt série "runner\'s itch"',
  fonte='Joyner MJ, Casey DP. Physiol Rev 2015;95(2):549-601 (vasodilatação no exercício); Cleveland Clinic, "Runner\'s Itch" (2023: capilares dilatando estimulam terminações nervosas; some com a regularidade); urticária induzida por exercício = procurar médico (Kim CW et al. Allergy Asthma Immunol Res 2014)',
  conc=['VASOS SE ABREM', 'NERVO AVISA', 'CONSTÂNCIA'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_19_cabeca', 'fibra', 'dor de cabeça no esforço pesado: pressão disparando', 'CABEÇA', [
 ('hook', 'DOR DE CABEÇA', 'NA SÉRIE PESADA?', '[curious] Dor de cabeça no meio da série pesada?'),
 ('pressao', 'A PRESSÃO', 'DISPARA.', 'No esforço máximo, a pressão do sangue pode chegar perto do triplo do normal.'),
 ('vasos', 'OS VASOS', 'DA CABEÇA DILATAM.', 'Os vasos da cabeça se dilatam pra aguentar, e isso dói.'),
 ('agua', 'CALOR E POUCA ÁGUA', 'AJUDAM A DOER.', 'Calor e pouca água no corpo deixam tudo pior.'),
 ('conc', 'RESUMINDO:', 'SOLTA O AR.', '[warm] Então: solta o ar na subida e bebe água. Se for súbita e muito forte, procura um médico.'),
 ('cta', 'COMENTA', 'CABEÇA.', 'Comenta CABEÇA que eu te mando como acompanhar sua evolução no Bríu. Link na bio.'),
], '16:00', "Dor de cabeça no meio da série pesada? 🔬👇\nNo esforço máximo, a pressão pode chegar perto do triplo do normal e os vasos da cabeça se dilatam. Calor e pouca água pioram. Solta o ar na subida e bebe água. Se for súbita e muito forte, procura um médico.",
  "como acompanhar sua evolução no Brio", "#fibratreino #dordecabeca #pressao #ciencia #musculacao",
  formato='nomear a sensação (enjoo 5,2×)',
  fonte='MacDougall JD et al. J Appl Physiol 1985;58(3):785-90 (leg press pesado: pressão média 320/250 mmHg, ~2,7× o repouso); ICHD-3 4.2 cefaleia primária do exercício (vasodilatação; súbita e intensa = investigar); Sjaastad O, Bakketeig LS. Cephalalgia 2002',
  conc=['PRESSÃO SOBE', 'SOLTA O AR', 'BEBE ÁGUA'], cta=['ACOMPANHE SUA EVOLUÇÃO', 'NO BRIO'])

V('fibra_20_vermelho', 'fibra', 'rosto vermelho no treino: sangue indo pra pele soltar calor', 'CALOR', [
 ('hook', 'O ROSTO', 'FICA VERMELHO?', '[curious] Seu rosto fica vermelho no treino?'),
 ('motor', 'O MÚSCULO', 'ESQUENTA O CORPO.', 'É o radiador do corpo ligando. O músculo trabalhando gera muito calor.'),
 ('pele', 'OS VASOS DA PELE', 'SE ABREM.', 'Os vasos da pele se abrem e o sangue quente sobe pra soltar esse calor.'),
 ('dez', 'ATÉ 10 VEZES', 'MAIS SANGUE.', 'No calor, o sangue que passa pela pele pode aumentar mais de dez vezes.'),
 ('conc', 'RESUMINDO:', 'É O CORPO ESFRIANDO.', '[warm] Então: não é falta de preparo. Bebe água e treina num lugar ventilado.'),
 ('cta', 'COMENTA', 'CALOR.', 'Comenta CALOR que eu te mando como acompanhar sua evolução no Bríu. Link na bio.'),
], '19:00', "Seu rosto fica vermelho no treino? 🔬👇\nÉ o radiador do corpo: os vasos da pele se abrem e o sangue quente sobe pra soltar calor. No calor, passa até dez vezes mais sangue pela pele. Não é falta de preparo.",
  "como acompanhar sua evolução no Brio", "#fibratreino #calor #suor #ciencia #treino",
  formato='nomear a sensação (enjoo 5,2×); sensação visível como o pump (1.107)',
  fonte='Johnson JM, Minson CT, Kellogg DL. Compr Physiol 2014;4(1):33-89 (vasodilatação cutânea na termorregulação); Rowell LB. Physiol Rev 1974;54(1):75-159 (fluxo na pele de ~0,25 L/min em repouso até 6-8 L/min sob calor)',
  conc=['MÚSCULO ESQUENTA', 'PELE SOLTA CALOR', 'NÃO É FRAQUEZA'], cta=['ACOMPANHE SUA EVOLUÇÃO', 'NO BRIO'])

V('fibra_21_pontada', 'fibra', 'pontada do lado da barriga no cardio: membrana do abdômen irritada', 'PONTADA', [
 ('hook', 'PONTADA', 'DO LADO DA BARRIGA?', '[curious] Aquela pontada do lado da barriga no cardio?'),
 ('membrana', 'É UMA MEMBRANA', 'IRRITADA.', 'A explicação mais aceita: a membrana que forra a barriga por dentro fica irritada.'),
 ('sacode', 'CADA PASSADA', 'SACODE TUDO.', 'Cada passada sacode os órgãos, e ela roça e repuxa.'),
 ('cheia', 'BARRIGA CHEIA', 'PIORA.', 'Comer ou beber muito logo antes piora: o estômago cheio estica tudo.'),
 ('conc', 'RESUMINDO:', 'COME 2 H ANTES.', '[warm] Então: come umas duas horas antes. Na pontada, diminui o ritmo e respira fundo.'),
 ('cta', 'COMENTA', 'PONTADA.', 'Comenta PONTADA que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '22:00', "Aquela pontada do lado da barriga no cardio? 🔬👇\nA explicação mais aceita: a membrana que forra a barriga por dentro fica irritada com o sacolejo. Barriga cheia piora. Come umas duas horas antes e, na pontada, diminui o ritmo.",
  "como registrar seus treinos no Brio", "#fibratreino #pontada #cardio #ciencia #corrida",
  formato='nomear a sensação (enjoo 5,2×); fora: @tiboinshape "Side stitch solution"',
  fonte='Morton DP, Callister R. Sports Med 2015;45(1):23-35 (dor abdominal transitória do exercício: irritação do peritônio parietal; pior com refeição/bebida antes e com movimento repetitivo do tronco)',
  conc=['MEMBRANA IRRITADA', 'BARRIGA CHEIA PIORA', 'RESPIRA FUNDO'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

if __name__ == '__main__':
    import re
    for k, v in P.items():
        txt = " ".join(b[3] for b in v['beats'])
        n = len(txt); w1 = len(re.sub(r"\[[^\]]*\]\s*", "", v['beats'][0][3]).split())
        print(k, n, 'chars', w1, 'palavras no gancho', len(v['beats']), 'beats')
