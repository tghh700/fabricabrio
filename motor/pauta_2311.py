"""Pauta de 23/11/2026 — BRIO 4 (11:30, 14:00, 18:00, 21:00) + FIBRA 4 (12:30, 16:00, 19:00, 22:00). DIA UM pausado.
Nada agendado para 23/11 antes desta rodada. Estoque pausado do BRIO: 30–35 s no formato antigo — não reagendado (fórmula atual ≥ 1 min).

ANALISE_10 (listar-midia 22/11 16:52 UTC; média BRIO 1.033 / mediana 1.244; FIBRA 663 / mediana 265)
 BRIO — últimos 10:
  melhores: seis meses de academia 1.580 (wt 12,8 s, 11 salvos) · jornada "cortou tudo e não cresce" (brio-75, 67 s) 1.406
            (wt 17,2 s = o MAIOR watch time do perfil, 18 salvos, 8 compart.) · força parou 1.364 em ~2 h (wt 12,6 s, 9 salvos).
  piores:   flexibilidade 137 (wt 5,2 s) · peito não cresce 146 (wt 5,1 s) · água gelada 231 (wt 6,2 s).
  o que separa: os bons abrem com uma situação/pergunta de RESULTADO ou TEMPO que a pessoa vive (6 meses, 2 meses sem crescer,
  força parou) e seguram 12–17 s; os ruins são mito pontual ou músculo isolado ("X não cresce") e perdem a pessoa em 5–6 s.
  A jornada de erros de 1 min teve o maior watch time absoluto → segue como padrão (teste 1/2 acima da média).
 FIBRA — últimos 10:
  melhores: treino de perna cansa tanto 2.220 (wt 13,7 s, 9 compart.) · veias 871 · escada 676 (wt 10,5 s).
  piores:   formigamento do pré-treino 14 · começo da corrida 53 · sensação boa 115.
  o que separa: perna/academia e "por que" de algo que todo mundo sente na série; sensação rara/de corrida/suplemento morre.
  Barra fixa (22/11) 188 em ~1 h — medir.

Evidência de cada tema (regra de 17/11):
 BRIO 86 volta   — nosso: "parou 2 semanas: quanto perde?" 1.9k (1,8×), "parou e perdeu tudo?" 1.224, memória muscular; jornada 75 1.406 (wt 17 s).
 BRIO 87 verão   — nosso: "quanto tempo pra ver resultado" 3,9k (3,8×), "30 dias de academia" 3,4k (3,3×), seis meses 1.580 (1,5×).
 BRIO 88 um ano  — nosso: mesma série de marco de tempo: 30 dias 3,4k, seis meses 1.580, quanto tempo 3,9k. [TESTE: antes/depois]
 BRIO 89 férias  — nosso: parou 2 semanas 1,9k (1,8×), "1×/semana funciona" 1.207 (1,2×).
 FIBRA 34 joelho — nosso: mito do corpo derrubado — queimação 1.563 (2,4×); treino de perna 2.220 (3,3×), enjoo 5.074 (7,7×).
 FIBRA 35 1º trei— nosso: treino de perna 2.220 (3,3×); dor/descanso 1.042 (1,6×).
 FIBRA 36 falha  — nosso: "por que" sobre o músculo na série — queimação 1.563 (2,4×), pump 1.108 (1,7×).
 FIBRA 37 série  — nosso: perna 2.220 + queimação 1.563 + pump 1.108. [TESTE: linha do tempo segundo a segundo]
 (externo: Instagram/TikTok não deixam ler views por busca; registrado só o nosso.)"""
P = {}


def V(id, perfil, tema, palavra, beats, hora, leg, gat, tags, **kw):
    P[id] = dict(perfil=perfil, tema=tema, palavra=palavra, beats=beats, hora=hora, leg=leg, gat=gat, tags=tags, **kw)


# ============================================================ BRIO — jornada de erros (beat: vis, t1, t2, texto)
V('brio_86_volta', 'brio', 'voltar a treinar depois de meses parado: metade da carga e subir toda semana', 'VOLTA', [
 ('hook', 'PAROU 3 MESES', 'E VOLTOU COM TUDO?', '[serious] Você ficou três meses parado. Aí volta pra academia com tudo, e pega a mesma carga de antes.'),
 ('dor', 'NO DIA SEGUINTE,', 'NEM ANDA.', 'Termina o treino se achando. No dia seguinte, não consegue nem descer a escada.'),
 ('falta', 'CINCO DIAS', 'DE DOR.', 'A dor dura cinco dias. E você falta a semana inteira esperando passar.'),
 ('leve', 'VOLTOU LEVE', 'DEMAIS.', 'Então você volta leve demais, com medo da dor. Duas semanas depois, a carga é a mesma do primeiro dia.'),
 ('todo', 'TODO DIA', 'PRA COMPENSAR.', 'Então você tenta compensar o tempo perdido e treina todo dia. Mas na segunda semana está exausto, e a força cai.'),
 ('metade', 'METADE DA', 'CARGA.', 'Então você faz diferente. Começa com metade da carga de antes, e metade das séries.'),
 ('sobe', 'UM POUCO', 'POR SEMANA.', 'Toda semana, sobe um pouco. A dor vem fraca, passa em dois dias, e você não falta mais.'),
 ('memoria', 'O MÚSCULO', 'LEMBRA.', 'E em poucas semanas, a carga de antes volta. O músculo lembra o caminho, e reconstrói mais rápido do que da primeira vez.'),
 ('conc', 'O QUE TE', 'TROUXE DE VOLTA', '[confident] O que te trouxe de volta foi começar pela metade, e subir um pouco toda semana, sem pressa.'),
 ('cta', 'COMENTA', 'VOLTA.', 'Comenta VOLTA que eu te mando como registrar suas séries no Bríu e ver a carga voltar. Link na bio.'),
], '11:30', "Ficou meses parado e voltou com tudo? 👇\nMesma carga de antes = 5 dias de dor e semana perdida. Leve demais não sobe, todo dia esgota. O que funciona: metade da carga e das séries, subindo um pouco toda semana. Em poucas semanas a força de antes volta.",
  "como registrar suas séries no Brio", "#brio #voltaratreinar #musculacao #treino #academia",
  formato='jornada', evid='nosso: parou 2 semanas 1,9k (1,8×), parou e perdeu tudo 1.224; jornada 75 1.406 (wt 17,2 s)',
  fonte='Nosaka K et al. 2001 (efeito da carga repetida: menos dor nas sessões seguintes); Staron RS et al. J Appl Physiol 1991;70(2):631-40 (retreino recupera mais rápido); Ogasawara R et al. 2013 (pausa e retorno)',
  app='VOLTA', app_lines=[("SEM 1 · 20 KG", None), ("SEM 2 · 25 KG", None), ("SEM 4 · 40 KG", None)], cta_lines=('REGISTRE SUAS SÉRIES', 'NO BRIO'))

V('brio_87_verao', 'brio', 'atalhos pra chegar no verão com mais músculo: o plano simples vence a pressa', 'VERÃO', [
 ('hook', 'FALTAM 8', 'SEMANAS PRO VERÃO', '[serious] Faltam oito semanas pro verão. E você quer chegar com mais braço e mais ombro.'),
 ('duas', 'TREINO DUAS', 'VEZES POR DIA.', 'Então você treina duas vezes por dia. Na segunda semana, o corpo não recupera, e a força começa a cair.'),
 ('falha', 'FALHA EM', 'TODA SÉRIE.', 'Então você vai até a falha em todas as séries, pra compensar. Mas sai do treino destruído, e a carga não sobe.'),
 ('troca', 'TREINO NOVO', 'TODA SEMANA.', 'Então você copia um treino novo da internet toda semana. Só que nunca repete nada, e não dá pra saber se evoluiu.'),
 ('sono', 'DORME', 'CINCO HORAS.', 'E pra caber tudo, dorme cinco horas por noite. O braço fica igual, e o cansaço só aumenta.'),
 ('base', 'QUATRO TREINOS,', 'MESMO PLANO.', 'Então você faz o simples. Quatro treinos por semana, e o mesmo plano por oito semanas.'),
 ('carga', 'UMA REPETIÇÃO', 'A MAIS.', 'Em cada treino, tenta uma repetição ou um quilo a mais que na semana anterior. E dorme sete horas.'),
 ('result', 'OITO SEMANAS', 'DEPOIS.', 'Oito semanas depois, a carga subiu em quase todos os exercícios, e o braço e o ombro aparecem mais na camiseta.'),
 ('conc', 'NÃO FOI', 'O ATALHO.', '[confident] O que funcionou não foi o atalho. Foi o mesmo plano, carga subindo e descanso.'),
 ('cta', 'COMENTA', 'VERÃO.', 'Comenta VERÃO que eu te mando como registrar suas séries no Bríu e acompanhar sua evolução. Link na bio.'),
], '14:00', "8 semanas pro verão: o que funciona? 👇\nTreino 2×/dia, falha em tudo, treino novo toda semana e 5 h de sono só travam. Quatro treinos por semana, o mesmo plano, uma repetição ou um quilo a mais por semana e 7 h de sono: a carga sobe e o braço aparece.",
  "como registrar suas séries no Brio", "#brio #projetoverao #hipertrofia #musculacao #academia",
  formato='jornada', evid='nosso: quanto tempo pra ver resultado 3,9k (3,8×), 30 dias de academia 3,4k (3,3×), seis meses 1.580 (1,5×)',
  fonte='Schoenfeld BJ et al. 2016/2019 (frequência e volume); Dattilo M et al. Med Hypotheses 2011 (privação de sono e síntese proteica); Plotkin D et al. PeerJ 2022 (progressão por carga ou repetição: resultados parecidos)',
  app='VERÃO', app_lines=[("SEM 1 · 10 REP", None), ("SEM 4 · 12 REP", None), ("SEM 8 · +6 KG", None)], cta_lines=('REGISTRE SUAS SÉRIES', 'NO BRIO'))

V('brio_88_ano', 'brio', 'um ano de academia: o que muda de verdade (força, músculo, espelho, rotina)', 'ANO', [
 ('hook', 'UM ANO DE', 'ACADEMIA.', '[curious] Um ano de academia. O que muda de verdade?'),
 ('forca', 'FORÇA:', 'QUASE O DOBRO.', 'Força. Antes, trinta quilos no supino tremiam. Depois de um ano, dá pra chegar perto do dobro.'),
 ('musculo', 'MÚSCULO:', '+2 A 5 KG.', 'Músculo. Treinando e comendo direito, o primeiro ano dá de dois a cinco quilos. É o ano em que mais se cresce.'),
 ('espelho', 'ESPELHO:', 'A CAMISETA APERTA.', 'Espelho. Antes, a manga da camiseta ficava solta. Depois, ela aperta no braço.'),
 ('rotina', 'ROTINA:', 'VIRA HÁBITO.', 'Rotina. Antes, ir pra academia era esforço. Depois de um ano, estranho é faltar.'),
 ('conc', 'O 1º ANO', 'É O QUE MAIS MUDA.', '[confident] O primeiro ano é o que mais muda. Só não vale parar no meio.'),
 ('cta', 'COMENTA', 'ANO.', 'Comenta ANO que eu te mando como registrar suas séries no Bríu e comparar seu antes e depois. Link na bio.'),
], '18:00', "Um ano de academia: o que muda? 👇\nForça: perto do dobro no supino. Músculo: de 2 a 5 kg no primeiro ano, o ano em que mais se cresce. Espelho: a manga aperta. Rotina: estranho é faltar.",
  "como registrar suas séries no Brio", "#brio #antesedepois #musculacao #treino #academia",
  formato='teste:antes-depois', evid='nosso: série de marco de tempo — 30 dias 3,4k (3,3×), quanto tempo 3,9k (3,8×), seis meses 1.580 (1,5×)',
  fonte='Aragon AA (taxas de ganho: ~1–1,5% do peso/mês no 1º ano); Kraemer WJ & Ratamess NA MSSE 2004 (ganho de força 40–100% em iniciantes)',
  app='UM ANO', app_lines=[("MÊS 1 · 30 KG", None), ("MÊS 6 · 45 KG", None), ("MÊS 12 · 58 KG", None)], cta_lines=('REGISTRE SUAS SÉRIES', 'NO BRIO'))

V('brio_89_ferias', 'brio', 'manter o músculo nas férias de fim de ano: dois treinos curtos por semana', 'FÉRIAS', [
 ('hook', 'DEZEMBRO', 'CHEGOU.', '[serious] Chegou dezembro, e vem a viagem. Você pensa: duas semanas sem treino, depois eu recupero.'),
 ('para', 'DUAS SEMANAS', 'VIRARAM CINCO.', 'Então você para tudo. Mas a viagem vira festa, depois ano novo, e duas semanas viram cinco.'),
 ('hotel', 'DUAS HORAS', 'NO HOTEL.', 'Então você tenta compensar: duas horas na academia do hotel no primeiro dia. No segundo, não aguenta, e desiste.'),
 ('solto', 'FLEXÃO', 'QUANDO LEMBRA.', 'Então faz flexão quando lembra, sem contar nada. Um dia faz, três dias não.'),
 ('minimo', 'DOIS TREINOS', 'DE 30 MINUTOS.', 'Então você faz o mínimo, mas fixo. Dois treinos por semana, de trinta minutos, com o que tiver.'),
 ('como', 'POUCAS SÉRIES,', 'PERTO DO LIMITE.', 'Agachamento, flexão, remada com a mochila cheia. Poucas séries, mas perto do limite.'),
 ('mantem', 'UM TERÇO', 'MANTÉM.', 'E funciona: com um terço do treino de sempre, dá pra manter a força e o músculo por meses.'),
 ('janeiro', 'JANEIRO:', 'SEM VOLTAR DO ZERO.', 'Em janeiro, você volta pra academia sem começar do zero. A carga de antes está lá, te esperando.'),
 ('conc', 'O QUE SALVOU', 'FOI O MÍNIMO.', '[confident] O que salvou as férias não foi treinar muito. Foi o mínimo, toda semana.'),
 ('cta', 'COMENTA', 'FÉRIAS.', 'Comenta FÉRIAS que eu te mando como registrar seus treinos no Bríu e não perder o que ganhou. Link na bio.'),
], '21:00', "Vai viajar nas férias? 👇\nParar tudo vira 5 semanas, 2 horas no hotel cansa no 2º dia e flexão solta não conta. Dois treinos de 30 minutos por semana, poucas séries perto do limite: com um terço do treino dá pra manter força e músculo por meses.",
  "como registrar seus treinos no Brio", "#brio #ferias #treinoemcasa #musculacao #academia",
  formato='jornada', evid='nosso: parou 2 semanas 1,9k (1,8×), 1×/semana funciona 1.207 (1,2×)',
  fonte='Bickel CS, Cross JM, Bamman MM. MSSE 2011;43(7):1177-87 (1/9 a 1/3 do volume mantém músculo e força por 32 semanas); Spiering BA et al. JSCR 2021 (manutenção com volume reduzido)',
  app='FÉRIAS', app_lines=[("SEG · 30 MIN", None), ("QUI · 30 MIN", None), ("2 DE 2 FEITOS", None)], cta_lines=('REGISTRE SEUS TREINOS', 'NO BRIO'))

# ============================================================ FIBRA (build3, prancha técnica) — beat: vis, t1, t2, texto
V('fibra_34_joelho', 'fibra', 'agachar fundo não estraga o joelho: cartilagem gosta de carga e a coxa apoia na panturrilha', 'JOELHO', [
 ('hook', 'AGACHAR FUNDO', 'ESTRAGA O JOELHO?', '[curious] Agachar fundo estraga o joelho?'),
 ('carga', 'CARTILAGEM', 'GOSTA DE CARGA.', 'Não, se a carga é controlada. A cartilagem se alimenta de pressão, como uma esponja.'),
 ('grossa', 'QUEM AGACHA', 'TEM MAIS.', 'Levantadores de peso têm a cartilagem atrás da patela mais grossa, não mais fina.'),
 ('apoio', 'A COXA', 'APOIA.', 'E lá embaixo, a coxa encosta na panturrilha e divide parte da força do joelho.'),
 ('conc', 'RESUMINDO:', 'NÃO É O VILÃO.', '[warm] Então: com carga que você controla, descer fundo não é o vilão.'),
 ('cta', 'COMENTA', 'JOELHO.', 'Comenta JOELHO que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '12:30', "Agachar fundo estraga o joelho? 🔬👇\nCom carga controlada, não: a cartilagem se alimenta de pressão, levantadores têm a cartilagem da patela mais grossa e, lá embaixo, a coxa apoia na panturrilha e divide a força.",
  "como registrar seus treinos no Brio", "#fibratreino #agachamento #joelho #ciencia #musculacao",
  formato='mito do corpo derrubado — queimação 1.563 (2,4×); perna 2.220 (3,3×), enjoo 5.074 (7,7×)',
  fonte='Hartmann H, Wirth K, Klusemann M. Sports Med 2013;43(10):993-1008 (agachamento fundo não aumenta risco às estruturas passivas; contato coxa-panturrilha reduz forças); Gratzke C et al. Am J Sports Med 2007;35(8):1346-53 (cartilagem patelar mais espessa em levantadores)',
  conc=['CARGA CONTROLADA', 'CARTILAGEM ADAPTA', 'COXA APOIA'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_35_primeiro', 'fibra', 'o primeiro treino de perna dói muito mais: efeito da carga repetida protege o músculo', 'PERNA', [
 ('hook', 'O 1º TREINO', 'DÓI MAIS?', '[curious] Por que o primeiro treino de perna dói?'),
 ('novo', 'MOVIMENTO', 'NOVO.', 'No primeiro, a descida do agachamento é novidade, e abre pequenas lesões em muitas fibras.'),
 ('protege', 'O CORPO', 'SE PROTEGE.', 'Mas depois de um treino só, o corpo já se protege. O cérebro espalha o esforço por mais fibras, e elas ganham reforço por dentro.'),
 ('menos', 'DÓI BEM', 'MENOS.', 'O mesmo treino, uma semana depois, dói bem menos. E essa proteção dura semanas.'),
 ('conc', 'RESUMINDO:', 'O CORPO APRENDEU.', '[warm] Então: a dor caiu porque o corpo aprendeu, não porque o treino ficou fraco.'),
 ('cta', 'COMENTA', 'PERNA.', 'Comenta PERNA que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '16:00', "Por que o primeiro treino de perna dói tanto? 🔬👇\nA descida é novidade e abre pequenas lesões em muitas fibras. Depois de um treino só, o corpo se protege: o mesmo treino na semana seguinte dói bem menos. Não é treino fraco, é o corpo que aprendeu.",
  "como registrar seus treinos no Brio", "#fibratreino #treinodeperna #dormuscular #ciencia #musculacao",
  formato='treino de perna — cansaço da perna 2.220 (3,3×), enjoo 5.074 (7,7×); descanso 1.042',
  fonte='McHugh MP. Scand J Med Sci Sports 2003;13(2):88-97 (efeito da carga repetida: adaptações neurais, mecânicas e celulares); Nosaka K et al. 2001 (proteção por semanas)',
  conc=['MOVIMENTO NOVO DÓI', 'CORPO SE PROTEGE', 'DURA SEMANAS'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_36_falha', 'fibra', 'por que a última repetição não sobe: todas as fibras recrutadas e sem energia rápida', 'SÉRIE', [
 ('hook', 'A ÚLTIMA', 'NÃO SOBE?', '[curious] Por que a última repetição não sobe?'),
 ('poucas', 'COMEÇA COM', 'POUCAS FIBRAS.', 'No começo da série, o cérebro usa poucas fibras. Conforme elas cansam, ele chama as outras.'),
 ('todas', 'NO FIM,', 'TODAS JUNTAS.', 'Na última, todas já estão trabalhando, e cada uma rende menos: falta energia rápida, e sobra fosfato dentro dela.'),
 ('lenta', 'A BARRA', 'FICA LENTA.', 'Por isso a barra fica lenta antes de parar. A velocidade cai a cada repetição.'),
 ('conc', 'RESUMINDO:', 'SEM RESERVA.', '[warm] Então: não é falta de vontade. É fibra sem reserva.'),
 ('cta', 'COMENTA', 'SÉRIE.', 'Comenta SÉRIE que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '19:00', "Por que a última repetição não sobe? 🔬👇\nO cérebro começa com poucas fibras e vai chamando as outras. No fim, estão todas trabalhando e cada uma rende menos: falta energia rápida e sobra fosfato. Por isso a barra fica lenta antes de parar.",
  "como registrar seus treinos no Brio", "#fibratreino #falhamuscular #forca #ciencia #musculacao",
  formato='"por que" sobre o músculo na série — queimação 1.563 (2,4×), pump 1.108 (1,7×)',
  fonte='Henneman E 1957 (princípio do tamanho: recrutamento das unidades motoras); Allen DG, Lamb GD, Westerblad H. Physiol Rev 2008;88(1):287-332 (fosfato inorgânico e fadiga); González-Badillo JJ 2010 (velocidade cai a cada repetição)',
  conc=['POUCAS FIBRAS NO INÍCIO', 'TODAS NO FIM', 'SEM ENERGIA RÁPIDA'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_37_segundos', 'fibra', 'o que acontece no corpo numa série de agachamento de 40 segundos, segundo a segundo', 'AGACHA', [
 ('hook', 'UMA SÉRIE,', 'SEGUNDO A SEGUNDO.', '[curious] O que acontece numa série de agachamento?'),
 ('s10', 'SEGUNDO 10:', 'RESERVA PRONTA.', 'Nos primeiros dez segundos, a energia vem de uma reserva pronta no músculo, a creatina fosfato.'),
 ('s20', 'SEGUNDO 20:', 'AÇÚCAR RÁPIDO.', 'Aos vinte, essa reserva já caiu. O músculo queima açúcar rápido, e começa a ardência.'),
 ('s30', 'SEGUNDO 30:', 'CORAÇÃO A MIL.', 'Aos trinta, o coração acelera, e a coxa enche de sangue.'),
 ('s40', 'SEGUNDO 40:', 'A PERNA TREME.', 'Aos quarenta, as fibras cansadas chamam reforço, e a perna começa a tremer.'),
 ('conc', 'RESUMINDO:', 'DOIS COMBUSTÍVEIS.', '[warm] Então: em quarenta segundos, sua perna troca de combustível e chama todas as fibras.'),
 ('cta', 'COMENTA', 'AGACHA.', 'Comenta AGACHA que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '22:00', "O que acontece numa série de agachamento? 🔬👇\n10 s: reserva pronta (creatina fosfato). 20 s: a reserva cai e o músculo queima açúcar rápido, vem a ardência. 30 s: coração acelera e a coxa enche de sangue. 40 s: as fibras cansadas chamam reforço e a perna treme.",
  "como registrar seus treinos no Brio", "#fibratreino #agachamento #treinodeperna #ciencia #musculacao",
  formato='teste:linha-do-tempo — base: perna 2.220 (3,3×), queimação 1.563, pump 1.108',
  fonte='Gastin PB. Sports Med 2001;31(10):725-41 (contribuição dos sistemas de energia ao longo do esforço); Gaitanos GC et al. 1993 (queda da fosfocreatina em ~10 s)',
  conc=['10 S: RESERVA', '20 S: AÇÚCAR', '40 S: TODAS AS FIBRAS'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

if __name__ == '__main__':
    import re
    for k, v in P.items():
        txt = " ".join(b[-1] for b in v['beats'])
        clean = re.sub(r"\[[^\]]*\]\s*", "", txt)
        w1 = len(re.split(r"[.?!:]", clean)[0].split())
        print(k, len(clean), 'chars', w1, 'pal. 1ª frase', len(v['beats']), 'beats', 'Bríu na legenda!' if re.search('br[íi]u', v['leg'] + v['gat'] + v['tags'], re.I) else 'ok')
