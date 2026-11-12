"""Pauta de 13/11/2026 (dia 1 do sprint): 1 BRIO + 3 FIBRA + 5 DIA UM. Fonte das evidências: tabela de formatos medidos (tryvolume, 10/11)."""
P = {}
P['brio_27_rosca'] = dict(perfil='brio', hora='22:00', tema='rosca direta com balanço do tronco (erro encenado e correção)', palavra='ROSCA', formato='encenar repetição errada e corrigir (20×)',
 beats=[
  ('hook', 'SUA ROSCA', 'TÁ ASSIM?', '[serious] Se a sua rosca tá assim, para.'),
  ('erro', 'O EMBALO', 'FAZ A FORÇA.', 'Joga o tronco pra trás, balança o quadril, e o peso sobe no embalo.'),
  ('carona', 'O BÍCEPS', 'PEGA CARONA.', 'Quem levanta é a lombar e o ombro. O bíceps só pega carona.'),
  ('cotovelo', 'COTOVELO', 'PARADO.', 'Primeiro: cola o cotovelo do lado do corpo, e deixa ele parado.'),
  ('desce', 'DESCE EM', '3 SEGUNDOS.', 'Depois: sobe em um segundo, e desce contando três.'),
  ('menos', 'MENOS PESO,', 'MAIS BÍCEPS.', '[confident] Vai precisar tirar peso. Tudo bem: com menos carga, o bíceps trabalha mais.'),
  ('conc', 'RESUMINDO:', 'SEM EMBALO.', 'Resumindo: se o corpo balança, o peso tá alto demais. Cotovelo parado, descida lenta, e aí sim você sobe a carga.'),
  ('cta', 'COMENTA', 'ROSCA.', 'Comenta ROSCA que eu te mando como registrar a carga da sua rosca no Bríu e ver ela subir sem roubar. Link na bio.'),
 ])
P['fibra_07_gordura'] = dict(perfil='fibra', hora='12:30', tema='para onde vai a gordura: sai pela respiração, não pelo suor', palavra='PULMÃO', formato='crença popular errada na 1ª frase (9×)',
 fonte='Meerman R, Brown AJ. When somebody loses weight, where does the fat go? BMJ 2014;349:g7257 (84% como CO2, 16% como água)',
 beats=[
  ('hook', 'GORDURA SAI', 'PELO PULMÃO.', '[curious] Você perde gordura pela respiração.'),
  ('suor', 'NÃO É', 'O SUOR.', 'Não é pelo suor. O suor é só água, pra esfriar o corpo.'),
  ('quebra', 'A CÉLULA', 'QUEBRA.', 'Pra usar a gordura, a célula quebra ela junto com oxigênio.'),
  ('co2', '84% VIRA', 'GÁS CARBÔNICO.', 'Sobra gás carbônico e água. Oitenta e quatro por cento sai no ar que você solta.'),
  ('agua', '16% VIRA', 'ÁGUA.', 'O resto sai como água: urina, suor e respiração.'),
  ('gasto', 'QUEM MANDA', 'É O GASTO.', '[matter-of-fact] Mas respirar mais rápido não adianta. Quem manda é o gasto: músculo trabalhando, treino após treino.'),
  ('conc', 'RESUMINDO:', 'SUOR NÃO MEDE.', '[warm] Então, camiseta encharcada não mede nada. O que conta é treinar forte toda semana, sem falhar.'),
  ('cta', 'COMENTA', 'PULMÃO.', 'Comenta PULMÃO que eu te mando como registrar suas séries no Bríu e acompanhar sua evolução. Link na bio.'),
 ], conc=['84% SAI PELO AR', 'SUOR É SÓ ÁGUA', 'CONTA O GASTO, NÃO O SUOR'], cta=['REGISTRE SUAS SÉRIES NO BRIO', 'E ACOMPANHE A EVOLUÇÃO'])
P['fibra_08_barra'] = dict(perfil='fibra', hora='19:00', tema='músculos que trabalham na barra fixa', palavra='BARRA', formato='diagrama do músculo em cada movimento (6×, 21 contas)',
 fonte='Youdas JW et al. J Strength Cond Res 2010;24(12):3404-14 (pegada supinada ativa mais bíceps; pronada, mais trapézio inferior)',
 beats=[
  ('hook', 'BARRA FIXA:', '5 MÚSCULOS.', '[curious] Uma barra fixa. Cinco músculos trabalhando.'),
  ('dorsal', '1. GRANDE', 'DORSAL.', 'O principal é o grande dorsal: puxa o braço pra baixo e alarga as costas.'),
  ('biceps', '2 E 3. BÍCEPS', 'E BRAQUIAL.', 'O bíceps e o braquial dobram o cotovelo. Por isso o braço também cresce.'),
  ('romboide', '4. ROMBOIDES', 'E TRAPÉZIO.', 'Romboides e trapézio, entre as escápulas, puxam o ombro pra trás.'),
  ('antebraco', '5. ANTEBRAÇO', 'NA PEGADA.', 'E o antebraço segura tudo. Sem pegada, a série acaba antes.'),
  ('pegada', 'A PEGADA', 'MUDA O FOCO.', '[matter-of-fact] Palma virada pra você? Mais bíceps. Palma pra frente? Mais costas.'),
  ('conc', 'RESUMINDO:', '1 BARRA, 5 MÚSCULOS.', '[warm] Resumindo: barra é costas, braço e pegada num exercício só. Se só cabe um no treino, coloca esse.'),
  ('cta', 'COMENTA', 'BARRA.', 'Comenta BARRA que eu te mando como registrar suas repetições no Bríu e ver quantas a mais saem a cada semana. Link na bio.'),
 ], conc=['DORSAL + ROMBOIDES', 'BÍCEPS + BRAQUIAL', 'ANTEBRAÇO NA PEGADA'], cta=['REGISTRE SUAS REPETIÇÕES NO BRIO', 'E VEJA O NÚMERO SUBIR'])
P['fibra_09_enjoo'] = dict(perfil='fibra', hora='21:00', tema='enjoo no treino de perna: o sangue sai da digestão', palavra='PERNA', formato='nomear a sensação exata (23×)',
 fonte='Peters HP et al. Gut 2001;48:435-9 e van Wijck K et al. 2012 (fluxo esplâncnico cai até ~80% em exercício intenso)',
 beats=[
  ('hook', 'ENJOO NO', 'TREINO DE PERNA?', '[curious] Aquele enjoo no meio do treino de perna?'),
  ('sangue', 'PERNA PEDE', 'MUITO SANGUE.', 'Perna é o maior grupo muscular. E músculo trabalhando pede muito sangue.'),
  ('desvio', 'O SANGUE', 'SAI DA BARRIGA.', 'Pra isso, o corpo tira sangue do que não é urgente: estômago e intestino.'),
  ('oitenta', 'ATÉ −80%', 'NA DIGESTÃO.', 'Em treino intenso, o fluxo ali cai até oitenta por cento.'),
  ('parada', 'DIGESTÃO', 'PARADA.', 'Com comida pesada parada ali, vem o enjoo.'),
  ('evita', 'COMO', 'EVITAR.', '[matter-of-fact] Pra evitar: come leve uma a duas horas antes, descansa mais entre as séries e bebe água aos goles. Se for frequente, procura um médico.'),
  ('conc', 'RESUMINDO:', 'SANGUE NA PERNA.', '[warm] Então: o enjoo é sangue indo pra perna. Ajusta comida e descanso, e treina sem passar mal.'),
  ('cta', 'COMENTA', 'PERNA.', 'Comenta PERNA que eu te mando como registrar seu treino no Bríu e receber orientação depois. Link na bio.'),
 ], conc=['O SANGUE FOI PRA PERNA', 'COME LEVE 1 A 2 H ANTES', 'MAIS DESCANSO, ÁGUA AOS GOLES'], cta=['REGISTRE SEU TREINO NO BRIO', 'E RECEBA ORIENTAÇÃO DEPOIS'])
P['diaum_06_prancha'] = dict(perfil='diaum', hora='08:00', tema='prancha em 3 níveis para iniciante', palavra='PRANCHA', formato='cada movimento em fácil, médio e difícil (8×)',
 beats=[
  ('hook', 'NEM 10 S', 'DE PRANCHA?', '[warm] Não aguenta nem dez segundos de prancha?'),
  ('niveis', 'É POR', 'NÍVEIS.', 'Normal. Prancha é força de abdômen, e ela se constrói por níveis.'),
  ('n1', 'NÍVEL 1:', 'JOELHOS.', 'Nível um: com os joelhos no chão. Corpo reto do joelho até a cabeça.'),
  ('n2', 'NÍVEL 2:', 'COMPLETA.', 'Nível dois: prancha completa, nos pés. Barriga firme, sem deixar o quadril cair.'),
  ('n3', 'NÍVEL 3:', 'UM PÉ.', 'Nível três: na prancha, tira um pé do chão por alguns segundos, e troca.'),
  ('regra', '3 × 30 S', '= SOBE.', 'A regra pra subir: quando fizer três vezes trinta segundos com o corpo reto, passa pro próximo.'),
  ('conc', 'RESUMINDO:', 'SOBE AOS POUCOS.', '[encouraging] Então: começa no joelho sem vergonha, e sobe quando os trinta segundos ficarem fáceis.'),
  ('cta', 'COMENTA', 'PRANCHA.', 'Comenta PRANCHA que eu te mando como registrar suas séries no Bríu e ver sua evolução. Link na bio.'),
 ], cta=['registre suas séries no Brio', 'e veja sua evolução'])
P['diaum_04_aparelhos'] = dict(perfil='diaum', hora='11:30', tema='não sei usar os aparelhos da academia', palavra='APARELHO', formato='abrir com uma frase que o público fala (11×)',
 beats=[
  ('hook', '"NÃO SEI USAR', 'OS APARELHOS"', '[warm] "Eu não sei usar os aparelhos." Ninguém nasce sabendo.'),
  ('desenho', 'OLHA O', 'DESENHO.', 'Quase todo aparelho tem um desenho do lado, mostrando o movimento e o músculo.'),
  ('banco', 'REGULA', 'O BANCO.', 'Antes de começar, regula o banco: o eixo do aparelho na altura da sua articulação.'),
  ('leve', 'COMEÇA', 'NO LEVE.', 'Começa no peso mais leve e faz umas dez repetições, só pra sentir.'),
  ('professor', 'PERGUNTA', 'SEM MEDO.', 'E pergunta pro professor. É literalmente o trabalho dele.'),
  ('tres', '3 APARELHOS', 'POR VEZ.', 'No começo, escolhe três aparelhos e repete eles a semana toda.'),
  ('conc', 'RESUMINDO:', '4 PASSOS.', '[encouraging] Então: desenho, banco, peso leve e uma pergunta. Em duas semanas, você usa sem pensar.'),
  ('cta', 'COMENTA', 'APARELHO.', 'Comenta APARELHO que eu te mando como anotar o peso de cada aparelho no Bríu, pra não esquecer no próximo treino. Link na bio.'),
 ], cta=['anote o peso de cada', 'aparelho no Brio'])
P['diaum_07_preguica'] = dict(perfil='diaum', hora='15:30', tema='preguiça na hora de sair pro treino', palavra='FUI', formato='nomear a sensação exata (23×)',
 beats=[
  ('hook', 'BATEU A', 'PREGUIÇA?', '[warm] Bateu aquela preguiça na hora de ir?'),
  ('sair', 'O DIFÍCIL', 'É SAIR.', 'Normal. A parte mais difícil do treino é sair de casa, não o treino.'),
  ('mochila', 'MOCHILA', 'NA PORTA.', 'Então deixa a mochila pronta na porta, na noite anterior. Uma decisão a menos.'),
  ('dez', 'SÓ 10', 'MINUTOS.', 'Faz o combinado dos dez minutos: vai, treina dez minutos, e se quiser, volta.'),
  ('ficou', 'CHEGOU,', 'FICOU.', 'Quase sempre, quando chega lá, você fica e termina.'),
  ('agenda', 'HORA', 'MARCADA.', 'E coloca o treino na agenda, como compromisso, com hora certa.'),
  ('conc', 'RESUMINDO:', 'NÃO ESPERA VONTADE.', '[encouraging] Resumindo: não espera a vontade aparecer. Deixa tudo pronto e só começa. Quem começa, termina.'),
  ('cta', 'COMENTA', 'FUI.', 'Comenta FUI quando voltar do treino de hoje, e registra ele no Bríu pra acompanhar sua evolução. Link na bio.'),
 ], cta=['registre seu treino no Brio', 'e acompanhe sua evolução'])
P['diaum_05_magro'] = dict(perfil='diaum', hora='19:30', tema='magro de 19 anos que quer ganhar massa: por onde começar', palavra='MASSA', formato='idade citada ao lado da meta (13×)',
 beats=[
  ('hook', '"TENHO 19,', 'SOU MAGRO"', '[warm] "Tenho dezenove, sou magro e quero ganhar massa."'),
  ('muda', 'DÁ PRA', 'MUDAR.', 'Dá pra mudar sim. E o plano é mais simples do que parece.'),
  ('tres', '3 VEZES', 'POR SEMANA.', 'Treino de força três vezes por semana, com o básico: agachamento, supino e remada.'),
  ('amais', 'UM POUCO', 'A MAIS.', 'Toda semana, tenta um pouquinho mais de peso, ou uma repetição a mais.'),
  ('prato', 'UM LANCHE', 'A MAIS.', 'Na comida: proteína em todas as refeições, e um lanche a mais por dia.'),
  ('balanca', 'BALANÇA', '1 VEZ POR SEMANA.', 'Sobe na balança uma vez por semana. Se não mexeu em um mês, come mais um pouco.'),
  ('conc', 'RESUMINDO:', 'TREINO + PRATO.', '[encouraging] Resumindo: treino de força, comida a mais e paciência. Mês a mês, o corpo responde.'),
  ('cta', 'COMENTA', 'MASSA.', 'Comenta MASSA que eu te mando como registrar suas séries no Bríu e acompanhar a carga subindo. Link na bio.'),
 ], cta=['registre suas séries no Brio', 'e veja a carga subir'])
P['diaum_08_semana2'] = dict(perfil='diaum', hora='21:30', tema='por que iniciantes desistem na segunda semana', palavra='FICO', formato='crença/afirmação forte na 1ª frase + passo a passo (experimento)',
 beats=[
  ('hook', 'A SEMANA 2', 'DERRUBA.', '[warm] A segunda semana é a que mais derruba.'),
  ('empolga', 'A EMPOLGAÇÃO', 'ACABA.', 'A empolgação acaba, e o resultado ainda não apareceu.'),
  ('grande', 'COMEÇOU', 'GRANDE DEMAIS.', 'O erro é começar grande demais: cinco dias, uma hora, dieta perfeita.'),
  ('pequeno', 'COMEÇA', 'PEQUENO.', 'Começa pequeno: dois ou três dias, quarenta minutos. Dá pra manter até numa semana ruim.'),
  ('meta', 'META:', 'NÃO FALTAR.', 'E troca a meta: em vez de perder dez quilos, a meta é não faltar.'),
  ('seguidos', 'NUNCA 2', 'SEGUIDOS.', 'Faltou um dia? Não zera tudo. Só não falta dois seguidos.'),
  ('conc', 'RESUMINDO:', 'PEQUENO E FREQUENTE.', '[encouraging] Então: pequeno, frequente e sem drama. A semana três chega, e ela é bem mais leve.'),
  ('cta', 'COMENTA', 'FICO.', 'Comenta FICO se dessa vez você passa da segunda semana, e registra cada treino no Bríu pra ver tudo que já fez. Link na bio.'),
 ], cta=['registre cada treino no Brio', 'e veja tudo que já fez'])
