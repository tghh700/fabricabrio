"""Pauta de 18/11/2026 — BRIO 4 + FIBRA 4 (escala de 17/11; DIA UM pausado). Nada agendado para 18/11 BRT antes desta rodada.
Métricas de 17/11 (midia/*.json): média BRIO 1.048 views, FIBRA 826.
  BRIO acima da média: 30 dias (3.402), tempo pra resultado (3.909), jejum (2.303), mesmo músculo todo dia (1.693),
  não cresce/fora da academia (1.690), parou 2 semanas (1.688), supino +10 kg (1.670), evoluindo (1.536), alongar (1.434),
  cerveja (1.376), mês (1.291), musculação emagrece (1.253). Abaixo: proteína (347), whey (322), genética (403), falso magro (43).
  FIBRA: enjoo na perna 2.624 (3,2× a média, 37 compart.), queimação 1.558 (1,9×), descanso 727, pump 1.104; supino 242,
  agachamento 155 (músculos que trabalham = mal).
BRIO (estoque pausado, 0 crédito — tema validado):
  55 altura   — mito popular (jejum 2.303 = 2,2× média; joelho na ponta do pé 1.256); fora: Jeff Nippard "Does Weight Training
                Stunt Your Growth?" e Stylist "most googled questions" (pergunta mais buscada)
  53 pesado   — mito popular (mesmo padrão de jejum 2.303 e mesmo músculo todo dia 1.693)
  62 rápido   — pergunta de perda (parou 2 semanas perdeu? 1.688; musculação emagrece 1.253)
  37 semana   — pergunta de frequência/resultado (mesmo músculo todo dia 1.693; 30 dias 3.402)
  (19/11) 59 confusão muscular — mito de frequência (1.693); 36 horário — mito de timing (jejum 2.303);
          56 recomposição — resultado (emagrece 1.253, 30 dias 3.402); 47 oscila — "como saber se está evoluindo" (1.536)
FIBRA (novos, formato "o que é essa sensação no corpo?" — enjoo 2.624 / queimação 1.558 / pump 1.104):
  14 tontura  — mesma família do enjoo (sangue que muda de lugar); sensação listada pelo usuário em 17/11
  15 sangue   — fora: @lifeofadoctor (TikTok) "why we taste blood when we run", 17,3 mi views / 2,5 mi likes (inkl)
  16 fome     — sensação listada pelo usuário em 17/11 ("fome depois do treino"); formato enjoo (3,2×)
  17 coração  — sensação listada pelo usuário em 17/11 ("coração acelerado"); formato enjoo (3,2×)"""
P = {}


def V(id, perfil, tema, palavra, beats, hora, leg, gat, tags, **kw):
    P[id] = dict(perfil=perfil, tema=tema, palavra=palavra, beats=beats, hora=hora, leg=leg, gat=gat, tags=tags, **kw)


V('fibra_14_tontura', 'fibra', 'vista escurece ao levantar no treino: queda rápida de pressão', 'TONTURA', [
 ('hook', 'A VISTA ESCURECE', 'QUANDO LEVANTA?', '[curious] A vista escurece quando você levanta do banco?'),
 ('pressao', 'A PRESSÃO CAI', 'POR SEGUNDOS.', 'É a pressão caindo por segundos. O sangue desce pras pernas e falta na cabeça.'),
 ('ar', 'PRENDER O AR', 'PIORA.', 'Prender o ar na série piora: menos sangue volta pro coração.'),
 ('corrige', 'O CORPO', 'CORRIGE SOZINHO.', 'Logo o corpo corrige: o coração acelera e as veias apertam.'),
 ('conc', 'RESUMINDO:', 'LEVANTA DEVAGAR.', '[warm] Então: levanta devagar e solta o ar na subida. Se desmaiar, procura um médico.'),
 ('cta', 'COMENTA', 'TONTURA.', 'Comenta TONTURA que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '19:00', "A vista escurece quando você levanta do banco? 🔬👇\nÉ a pressão caindo por alguns segundos: o sangue desce pras pernas e falta um pouco na cabeça. Prender o ar piora. Levanta devagar e solta o ar na subida.",
  "como registrar seus treinos no Brio", "#fibratreino #tontura #pressao #ciencia #musculacao",
  formato='o que é essa sensação no corpo (enjoo 2.624 = 3,2× a média do FIBRA)',
  fonte='MacDougall JD et al. J Appl Physiol 1985;58(3):785-90 (pressão no levantamento pesado e manobra de Valsalva); Freeman R et al. Clin Auton Res 2011;21:69-72 (hipotensão ortostática: queda ao ficar de pé, corrigida pelo barorreflexo)',
  conc=['PRESSÃO CAI', 'SOLTA O AR', 'LEVANTA DEVAGAR'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_15_sangue', 'fibra', 'gosto de sangue na boca no esforço máximo', 'SANGUE', [
 ('hook', 'GOSTO DE SANGUE', 'NA BOCA?', '[curious] Gosto de sangue na boca no treino?'),
 ('pulmao', 'PODE VIR', 'DO PULMÃO.', 'Pode vir do pulmão. No esforço máximo, a pressão nos vasinhos de lá sobe muito.'),
 ('vaza', 'ESCAPA', 'UM POUQUINHO.', 'Escapam alguns glóbulos vermelhos, que sobem até a boca.'),
 ('seca', 'E A GARGANTA', 'RESSECA.', 'E a garganta seca de tanto respirar pela boca reforça o gosto.'),
 ('conc', 'RESUMINDO:', 'É ESFORÇO ALTO.', '[matter-of-fact] Então: é sinal de esforço alto e passa rápido. Tosse com sangue, procura um médico.'),
 ('cta', 'COMENTA', 'SANGUE.', 'Comenta SANGUE que eu te mando como acompanhar sua evolução no Bríu. Link na bio.'),
], '12:30', "Gosto de sangue na boca no treino? 🔬👇\nNo esforço máximo, a pressão nos vasinhos do pulmão sobe e escapam alguns glóbulos vermelhos. A garganta seca reforça o gosto. Passa rápido.",
  "como acompanhar sua evolução no Brio", "#fibratreino #pulmao #cardio #ciencia #treino",
  formato='nomear a sensação exata; evidência externa @lifeofadoctor 17,3 mi views',
  fonte='Hopkins SR et al. Am J Respir Crit Care Med 1997;155(3):1090-4 (mais hemácias no lavado broncoalveolar de atletas após esforço máximo); West JB. J Appl Physiol 2000 (falha por estresse dos capilares pulmonares)',
  conc=['PRESSÃO NO PULMÃO', 'GARGANTA SECA', 'PASSA RÁPIDO'], cta=['ACOMPANHE SUA EVOLUÇÃO', 'NO BRIO'])

V('fibra_16_fome', 'fibra', 'fome some no treino e volta horas depois', 'FOME', [
 ('hook', 'TREINOU', 'E A FOME SUMIU?', '[curious] Treinou pesado e a fome sumiu?'),
 ('grelina', 'O HORMÔNIO', 'DA FOME CAI.', 'No esforço intenso, cai a grelina, o hormônio da fome. O sangue vai pros músculos.'),
 ('volta', 'HORAS DEPOIS,', 'ELA VOLTA.', 'Uma ou duas horas depois, a fome volta. Às vezes com força.'),
 ('repoe', 'O MÚSCULO', 'PEDE REPOSIÇÃO.', 'É o músculo pedindo energia pra repor o estoque.'),
 ('conc', 'RESUMINDO:', 'PLANEJA A REFEIÇÃO.', '[warm] Então: deixa uma refeição com proteína pronta pra depois do treino.'),
 ('cta', 'COMENTA', 'FOME.', 'Comenta FOME que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '16:00', "Treinou pesado e a fome sumiu? 🔬👇\nNo esforço intenso, o hormônio da fome cai. Uma ou duas horas depois ele volta, às vezes com força: é o músculo pedindo reposição.",
  "como registrar seus treinos no Brio", "#fibratreino #fome #hormonios #ciencia #musculacao",
  formato='o que é essa sensação no corpo (enjoo 3,2×; lista do usuário 17/11)',
  fonte='Broom DR et al. Am J Physiol Regul Integr Comp Physiol 2009;296(1):R29-35 (exercício de força e aeróbio suprimem a grelina acilada e a fome por ~1-2 h); King JA et al. Med Sci Sports Exerc 2011 (fome volta depois)',
  conc=['GRELINA CAI', 'FOME VOLTA', 'REFEIÇÃO PRONTA'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_17_coracao', 'fibra', 'coração acelera antes do esforço: resposta antecipatória', 'CORAÇÃO', [
 ('hook', 'O CORAÇÃO DISPARA', 'ANTES DA SÉRIE?', '[curious] O coração dispara antes de pegar o peso?'),
 ('cerebro', 'O CÉREBRO', 'SE ADIANTA.', 'É o cérebro se adiantando: ele sabe que vem esforço e solta adrenalina.'),
 ('bomba', 'MAIS RÁPIDO', 'E MAIS FORTE.', 'O coração bate mais rápido e mais forte, e o sangue já vai pros músculos.'),
 ('prova', 'IGUAL ANTES', 'DE UMA PROVA.', 'É o mesmo frio na barriga de antes de uma prova ou de uma corrida.'),
 ('conc', 'RESUMINDO:', 'É O CORPO LIGANDO.', '[warm] Então: não é fraqueza. É o corpo ligando o motor antes da largada.'),
 ('cta', 'COMENTA', 'CORAÇÃO.', 'Comenta CORAÇÃO que eu te mando como registrar suas séries no Bríu. Link na bio.'),
], '22:00', "O coração dispara antes de pegar o peso? 🔬👇\nÉ o cérebro se adiantando: ele solta adrenalina antes do esforço e o sangue já começa a ir pros músculos. É o corpo ligando o motor.",
  "como registrar suas séries no Brio", "#fibratreino #coracao #adrenalina #ciencia #treino",
  formato='o que é essa sensação no corpo (enjoo 3,2×; lista do usuário 17/11)',
  fonte='Williamson JW. Exp Physiol 2010;95(11):1043-8 (comando central: o cérebro ajusta frequência cardíaca e pressão antes e no início do exercício); Krogh A, Lindhard J. J Physiol 1913 (aumento antecipatório da frequência cardíaca)',
  conc=['CÉREBRO SE ADIANTA', 'ADRENALINA', 'É PREPARO'], cta=['REGISTRE SUAS SÉRIES', 'NO BRIO'])

if __name__ == '__main__':
    import re
    for k, v in P.items():
        txt = " ".join(b[3] for b in v['beats'])
        n = len(txt); w1 = len(re.sub(r"\[[^\]]*\]\s*", "", v['beats'][0][3]).split())
        print(k, n, 'chars', w1, 'palavras no gancho', len(v['beats']), 'beats')
