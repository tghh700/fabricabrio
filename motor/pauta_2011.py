"""Pauta de 20/11/2026 — BRIO 4 + FIBRA 4 novos (nada agendado para 20/11 BRT; estoque pausado do BRIO é 30–35 s
e de técnica/organização, fora da regra). DIA UM pausado.
Métricas de 19/11 (midia/*.json, listar-midia 19/11 16:50 UTC): média BRIO 1.029, FIBRA 791 (mediana 262).
  BRIO: mulher pesado 1.377 (17 compart.), 1×/semana 1.185, balança 1.387, parou/perdeu 1.240, pesa mais 1.233;
        mal: emagrecer rápido 324, musculação deixa baixo 170, músculo não vira gordura 254, confunde (horas no ar) 175.
  FIBRA: enjoo na perna 4.967 (6,3×, 112 compart.), barra 1.980, queimação 1.563, pump 1.108, descanso 1.042;
        sensações novas medianas/baixas: coração 570, sangue 319, tontura 262, coceira 184 (horas no ar).
Evidência de cada tema (regra de 17/11):
 BRIO 75 peito não cresce — nosso: "ombro não cresce" 1.507 (1,5×), "treina pesado e não cresce" 1.696 (1,6×);
        fora: ATHLEAN-X "The REAL Reason Your Pecs Won't Grow" (YouTube, r5qUK8c5Y9g), RP Strength "why your chest isn't growing".
 BRIO 76 seis meses     — nosso: "30 dias de academia" 3.513 (3,4× → vira série), "quanto tempo pra ver resultado" 4.124 (4×).
 BRIO 77 perna→braço    — nosso: mito popular em pergunta (jejum 2.307 = 2,2×, mulher pesado 1.377 = 1,3×).
 BRIO 78 flexibilidade  — nosso: mito popular (jejum 2,2×) e família alongamento ("alongar antes" 1.437 = 1,4×).
 FIBRA 22 euforia       — nosso: sensação + mito derrubado (queimação "não é ácido lático" 1.563 = 2×; enjoo 6,3×).
 FIBRA 23 primeiros min — nosso: sensação (enjoo 6,3×); fora: ditado de corredor "the first mile is a liar" (thejolt.substack.com).
 FIBRA 24 cansaço perna — nosso: enjoo NO TREINO DE PERNA 4.967 (6,3×) — mesmo contexto (perna) com outra sensação.
 FIBRA 25 mãos inchadas — nosso: sensação visível como o pump (1.108 = 1,4×); fora: Mayo Clinic Q&A "hand swelling during exercise".
(Views externas não confirmáveis pela busca — TikTok/YouTube bloqueiam a leitura; a evidência principal é a nossa.)"""
P = {}


def V(id, perfil, tema, palavra, beats, hora, leg, gat, tags, **kw):
    P[id] = dict(perfil=perfil, tema=tema, palavra=palavra, beats=beats, hora=hora, leg=leg, gat=gat, tags=tags, **kw)


# ============================================================ BRIO (v2: cenas_v2)
V('brio_75_peito', 'brio', 'peito não cresce: poucas séries por semana e carga parada', 'PEITO', [
 ('hook', 'SEU PEITO', 'NÃO CRESCE?', '[curious] Seu peito não cresce?'),
 ('pouca', 'POUCA SÉRIE', 'NA SEMANA.', 'Quase sempre é pouca série. Três séries de supino por semana não bastam.'),
 ('dez', '10 SÉRIES', 'POR SEMANA.', 'Os estudos mostram: dez ou mais séries por semana fazem crescer bem mais que menos de cinco.'),
 ('carga', 'CARGA PARADA,', 'PEITO PARADO.', 'E a carga tem que subir. Mesmo peso há meses? O músculo não tem motivo pra crescer.'),
 ('conc', 'RESUMINDO:', '10 SÉRIES + CARGA.', 'Resumindo: dez séries por semana, em dois treinos, e carga subindo.'),
 ('cta', 'COMENTA', 'PEITO.', 'Comenta PEITO que eu te mando como registrar suas séries no Bríu. Link na bio.'),
], '18:00', "Seu peito não cresce? 👇\nQuase sempre é pouca série: 10 ou mais séries por semana crescem bem mais que menos de 5. E a carga tem que subir.",
  "como registrar suas séries no Brio", "#brio #peito #hipertrofia #musculacao #academia",
  evid='nosso: ombro não cresce 1.507 (1,5×), treina pesado e não cresce 1.696 (1,6×); fora: ATHLEAN-X "The REAL Reason Your Pecs Won\'t Grow"',
  fonte='Schoenfeld BJ, Ogborn D, Krieger JW. J Sports Sci 2017;35(11):1073-82 (dose-resposta: ≥10 séries/semana > <5)')

V('brio_76_meses', 'brio', 'seis meses de academia: o que muda de verdade', 'MESES', [
 ('hook', '6 MESES', 'DE ACADEMIA.', '[curious] Seis meses de academia. O que muda?'),
 ('forca', 'A CARGA', 'QUASE DOBRA.', 'Primeiro a força: em muitos exercícios, a carga pode quase dobrar.'),
 ('roupa', 'A CAMISETA', 'APERTA.', 'O corpo vem junto: a camiseta aperta no ombro e no braço, e a calça na coxa.'),
 ('outros', 'OS OUTROS', 'NOTAM PRIMEIRO.', 'Aí os outros começam a notar. Você vê menos, porque se olha todo dia.'),
 ('conc', 'RESUMINDO:', 'COMPARA A CARGA.', 'Resumindo: constância muda muito. Compara a carga do primeiro mês com a de hoje.'),
 ('cta', 'COMENTA', 'MESES.', 'Comenta MESES que eu te mando como acompanhar sua evolução no Bríu. Link na bio.'),
], '21:00', "Seis meses de academia. O que muda? 👇\nA carga de muitos exercícios pode quase dobrar, a camiseta aperta e os outros notam antes de você. Compara a carga do 1º mês com a de hoje.",
  "como acompanhar sua evolução no Brio", "#brio #resultado #musculacao #academia #evolucao",
  evid='nosso: 30 dias de academia 3.513 (3,4×, série), quanto tempo pra ver resultado 4.124 (4×)',
  fonte='Ratamess NA et al. ACSM Position Stand, Med Sci Sports Exerc 2009;41(3):687-708 (iniciantes: maiores ganhos de força nos primeiros meses); Kraemer WJ et al. MSSE 2002 (ganhos de 1RM de iniciantes em 6 meses)')

V('brio_77_hormonio', 'brio', 'treinar perna não faz o braço crescer (mito do hormônio)', 'PERNA', [
 ('hook', 'PERNA FAZ', 'O BRAÇO CRESCER?', '[curious] Treinar perna faz o braço crescer?'),
 ('mito', 'NÃO.', 'É MITO.', 'Não. O mito diz que o hormônio da perna faz o corpo todo crescer.'),
 ('estudo', '1 BRAÇO SÓ,', '1 BRAÇO + PERNA.', 'Num estudo, a pessoa treinou um braço sozinho e o outro junto com perna, por quinze semanas.'),
 ('igual', 'CRESCERAM', 'IGUAL.', 'Os dois cresceram igual. O pico de hormônio é pequeno e passa rápido.'),
 ('conc', 'RESUMINDO:', 'BRAÇO CRESCE COM BRAÇO.', 'Resumindo: treina perna pela perna. Braço cresce com braço e carga subindo.'),
 ('cta', 'COMENTA', 'PERNA.', 'Comenta PERNA que eu te mando como registrar suas séries no Bríu. Link na bio.'),
], '14:00', "Treinar perna faz o braço crescer? 👇\nNão. Num estudo, um braço treinou sozinho e o outro junto com perna por 15 semanas: cresceram igual. O pico de hormônio é pequeno e passa rápido.",
  "como registrar suas séries no Brio", "#brio #mitos #treinodeperna #musculacao #academia",
  evid='nosso: mito popular em pergunta — jejum 2.307 (2,2×), mulher pesado 1.377 (1,3×)',
  fonte='West DW et al. J Appl Physiol 2010;108(1):60-7 (braço treinado sozinho x com perna, 15 semanas: mesma hipertrofia e força; elevação hormonal transitória)')

V('brio_78_flexivel', 'brio', 'musculação não tira a flexibilidade: amplitude melhora igual ao alongamento', 'FLEXÍVEL', [
 ('hook', 'MUSCULAÇÃO', 'TE DEIXA TRAVADO?', '[curious] Musculação tira a sua flexibilidade?'),
 ('contra', 'PELO', 'CONTRÁRIO.', 'Pelo contrário. Ela pode deixar você mais flexível.'),
 ('estudo', 'MUSCULAÇÃO', '= ALONGAMENTO.', 'Uma revisão comparou musculação com alongamento. A amplitude melhorou parecido nos dois.'),
 ('desce', 'DESCE', 'ATÉ O FIM.', 'O segredo é descer o peso até o fim. O músculo trabalha esticado e ganha amplitude.'),
 ('conc', 'RESUMINDO:', 'MOVIMENTO COMPLETO.', 'Resumindo: com movimento completo, você fica mais forte e mais solto.'),
 ('cta', 'COMENTA', 'FLEXÍVEL.', 'Comenta FLEXÍVEL que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '11:30', "Musculação tira a sua flexibilidade? 👇\nPelo contrário: uma revisão de estudos viu a amplitude melhorar parecido com musculação e com alongamento. O segredo é descer até o fim do movimento.",
  "como registrar seus treinos no Brio", "#brio #flexibilidade #mitos #musculacao #academia",
  evid='nosso: mito popular — jejum 2.307 (2,2×); família alongamento: alongar antes 1.437 (1,4×)',
  fonte='Afonso J et al. Healthcare 2021;9(4):427 (meta-análise: treino de força x alongamento para amplitude — sem diferença)')

# ============================================================ FIBRA (build3)
V('fibra_22_euforia', 'fibra', 'sensação boa depois do treino: endocanabinoides, não só endorfina', 'EUFORIA', [
 ('hook', 'A SENSAÇÃO BOA', 'DEPOIS DO TREINO?', '[curious] Aquela sensação boa depois do treino?'),
 ('barreira', 'NÃO É SÓ', 'ENDORFINA.', 'Não é só endorfina. Ela é grande demais pra passar do sangue pro cérebro.'),
 ('endo', 'QUEM CHEGA:', 'ENDOCANABINOIDES.', 'Quem chega lá são os endocanabinoides, que acalmam e dão prazer.'),
 ('estudo', 'BLOQUEARAM', 'A ENDORFINA.', 'Num estudo, bloquearam a endorfina, e a euforia continuou.'),
 ('conc', 'RESUMINDO:', 'É QUÍMICA REAL.', '[warm] Então: é química de verdade, e uns trinta minutos de treino moderado já costumam liberar.'),
 ('cta', 'COMENTA', 'EUFORIA.', 'Comenta EUFORIA que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '22:00', "Aquela sensação boa depois do treino? 🔬👇\nNão é só endorfina: ela quase não passa do sangue pro cérebro. Quem chega lá são os endocanabinoides, que o corpo fabrica. Num estudo, bloquearam a endorfina e a euforia continuou.",
  "como registrar seus treinos no Brio", "#fibratreino #endorfina #bemestar #ciencia #treino",
  formato='nomear a sensação + derrubar o mito (queimação "não é ácido lático" 1.563 = 2×; enjoo 6,3×)',
  fonte='Fuss J et al. PNAS 2015;112(42):13105-8 (endorfinas não atravessam a barreira hematoencefálica; euforia via receptor canabinoide); Siebers M et al. Psychoneuroendocrinology 2021;126:105173 (naltrexona não bloqueou a euforia em humanos; endocanabinoides subiram com 45 min moderados)',
  conc=['NÃO É SÓ ENDORFINA', 'ENDOCANABINOIDES', '30 MIN MODERADO'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_23_folego', 'fibra', 'primeiros minutos de corrida são os piores: déficit de oxigênio', 'FÔLEGO', [
 ('hook', 'O COMEÇO', 'É O PIOR?', '[curious] O começo da corrida é a pior parte?'),
 ('motor', 'O MOTOR DE AR', 'DEMORA A LIGAR.', 'Não é falta de preparo. O motor de oxigênio demora pra ligar.'),
 ('deficit', '2 A 3 MINUTOS', 'NO VERMELHO.', 'Nos primeiros dois, três minutos, o músculo pede mais oxigênio do que chega.'),
 ('reserva', 'GASTA A', 'RESERVA RÁPIDA.', 'Ele cobre a diferença com uma reserva rápida, que cansa e acelera a respiração.'),
 ('conc', 'RESUMINDO:', 'COMEÇA DEVAGAR.', '[warm] Então: começa devagar e acelera aos poucos. Em uns minutos, o fôlego chega.'),
 ('cta', 'COMENTA', 'FÔLEGO.', 'Comenta FÔLEGO que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '16:00', "O começo da corrida é a pior parte? 🔬👇\nNos primeiros 2 a 3 minutos, o músculo gasta mais oxigênio do que o coração e o pulmão entregam, e cobre a diferença com uma reserva rápida. Começa devagar: o fôlego chega.",
  "como registrar seus treinos no Brio", "#fibratreino #corrida #folego #ciencia #cardio",
  formato='nomear a sensação (enjoo 6,3×); fora: ditado "the first mile is a liar"',
  fonte='Poole DC, Jones AM. Compr Physiol 2012;2(2):933-96 (cinética do VO2: estado estável em ~2–3 min no exercício moderado; déficit de O2 coberto por fosfocreatina e glicólise)',
  conc=['MOTOR DEMORA', 'RESERVA RÁPIDA', 'COMEÇA DEVAGAR'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

V('fibra_24_cansaco', 'fibra', 'treino de perna cansa mais: metade dos músculos do corpo', 'CANSAÇO', [
 ('hook', 'POR QUE PERNA', 'CANSA TANTO?', '[curious] Por que o treino de perna cansa tanto?'),
 ('metade', 'MAIS DA METADE', 'DOS MÚSCULOS.', 'Perna e glúteo são mais da metade do músculo do seu corpo.'),
 ('coracao', 'MAIS MÚSCULO,', 'MAIS SANGUE.', 'Mais músculo trabalhando pede mais sangue: o coração bate forte e a respiração dispara.'),
 ('estoque', 'O ESTOQUE', 'DE ENERGIA CAI.', 'E gastam muito da energia guardada no músculo. Quando ela baixa, vem o cansaço.'),
 ('conc', 'RESUMINDO:', 'COME E DORME.', '[warm] Então: é normal. Come carboidrato e proteína depois e dorme bem.'),
 ('cta', 'COMENTA', 'CANSAÇO.', 'Comenta CANSAÇO que eu te mando como acompanhar sua evolução no Bríu. Link na bio.'),
], '19:00', "Por que o treino de perna cansa tanto? 🔬👇\nPerna e glúteo são mais da metade do músculo do corpo: mais sangue, coração forte, respiração disparada e o estoque de energia do músculo caindo. Come e dorme bem.",
  "como acompanhar sua evolução no Brio", "#fibratreino #treinodeperna #cansaco #ciencia #musculacao",
  formato='nomear a sensação no treino de perna (enjoo na perna 4.967 = 6,3×)',
  fonte='Janssen I et al. J Appl Physiol 2000;89(1):81-8 (membros inferiores ≈ 55% da massa muscular esquelética); Ørtenblad N, Westerblad H, Nielsen J. J Physiol 2013;591(18):4405-13 (glicogênio muscular e fadiga)',
  conc=['METADE DOS MÚSCULOS', 'ENERGIA BAIXA', 'COME E DORME'], cta=['ACOMPANHE SUA EVOLUÇÃO', 'NO BRIO'])

V('fibra_25_maos', 'fibra', 'mãos inchadas na caminhada: balanço do braço empurra sangue', 'MÃOS', [
 ('hook', 'AS MÃOS', 'INCHAM?', '[curious] Suas mãos incham quando você caminha?'),
 ('comum', 'É COMUM.', 'É O BALANÇO.', 'É comum e quase sempre inofensivo: é o balanço do braço.'),
 ('balanco', 'O BALANÇO', 'EMPURRA SANGUE.', 'A cada passo, o braço joga sangue pra ponta dos dedos, e ele demora pra voltar.'),
 ('calor', 'NO CALOR,', 'INCHA MAIS.', 'No calor, os vasinhos da mão se abrem e entra ainda mais líquido.'),
 ('conc', 'RESUMINDO:', 'ABRE E FECHA.', '[warm] Então: abre e fecha as mãos enquanto caminha. Se inchar muito ou doer, procura um médico.'),
 ('cta', 'COMENTA', 'MÃOS.', 'Comenta MÃOS que eu te mando como registrar seus treinos no Bríu. Link na bio.'),
], '12:30', "Suas mãos incham quando você caminha? 🔬👇\nA cada passo, o balanço do braço joga sangue pra ponta dos dedos, e ele demora pra voltar. No calor, piora. Abre e fecha as mãos. Se inchar muito ou doer, procura um médico.",
  "como registrar seus treinos no Brio", "#fibratreino #caminhada #maosinchadas #ciencia #cardio",
  formato='sensação visível como o pump (1.108 = 1,4×); fora: Mayo Clinic Q&A "hand swelling during exercise"',
  fonte='Laskowski ER, Mayo Clinic Expert Answers, "Hand swelling during exercise: cause for concern?" (balanço do braço/força centrífuga e resposta dos vasos ao calor; raramente hiponatremia); Johnson JM et al. Compr Physiol 2014 (vasodilatação cutânea no calor)',
  conc=['BALANÇO DO BRAÇO', 'CALOR PIORA', 'ABRE E FECHA'], cta=['REGISTRE SEUS TREINOS', 'NO BRIO'])

if __name__ == '__main__':
    import re
    for k, v in P.items():
        txt = " ".join(b[3] for b in v['beats'])
        n = len(txt); w1 = len(re.sub(r"\[[^\]]*\]\s*", "", v['beats'][0][3]).split("?")[0].split(".")[0].split())
        print(k, n, 'chars', w1, 'palavras', len(v['beats']), 'beats', 'Bríu' in v['leg'] + v['gat'] + v['tags'])
