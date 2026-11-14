"""Pauta BRIO de 14/11/2026 (lote emergencial: a rotina de 13/11 falhou por limite de uso). 6 vídeos, temas inéditos."""
P = {}
def V(id, tema, palavra, gat, beats):
    P[id] = dict(tema=tema, palavra=palavra, gat=gat, beats=beats)

V('brio_32_dor', 'dor no dia seguinte não mede treino bom', 'DOR', 2, [
 ('hook', 'DOR NO DIA SEGUINTE', 'É TREINO BOM?', '[curious] Dor no dia seguinte é treino bom?'),
 ('nova', 'NEM SEMPRE.', 'DOR É NOVIDADE.', 'Nem sempre. Essa dor aparece mais quando o exercício é novo, ou quando você muda o treino.'),
 ('veterano', 'QUEM TREINA HÁ ANOS', 'SENTE MENOS.', 'Quem treina há anos sente menos dor, e continua crescendo.'),
 ('carga', 'O QUE CRESCE', 'É A CARGA.', 'O que faz o músculo crescer é a carga ou as repetições subindo, semana após semana.'),
 ('semdor', 'SEM DOR', 'TAMBÉM VALE.', 'E um treino sem dor nenhuma também pode ter funcionado.'),
 ('forte', 'DOR FORTE', 'É OUTRA COISA.', '[matter-of-fact] Agora, dor forte que trava o movimento ou não passa em poucos dias, é caso pra um profissional.'),
 ('conc', 'RESUMINDO:', 'DOR NÃO MEDE.', 'Resumindo: dor não mede treino. O que mede é se você levantou mais que na semana passada.'),
 ('cta', 'COMENTA', 'DOR.', 'Comenta DOR que eu te mando como registrar suas séries no Bríu e comparar com a semana passada. Link na bio.'),
])
V('brio_33_sono', 'dormir mal derruba o treino', 'SONO', 2, [
 ('hook', 'DORMIU MAL?', 'O TREINO SENTE.', '[serious] Dormiu mal? Seu treino sente.'),
 ('forca', 'POUCO SONO,', 'MENOS FORÇA.', 'Com poucas horas de sono, a força cai e o esforço parece maior, mesmo com o mesmo peso.'),
 ('repara', 'É DORMINDO', 'QUE RECUPERA.', 'E é dormindo que o corpo repara o músculo que você treinou.'),
 ('meta', 'META:', '7 A 9 HORAS.', 'A meta pra maioria dos adultos é de sete a nove horas por noite.'),
 ('horario', 'HORÁRIO FIXO', 'AJUDA MAIS.', 'Deitar e acordar em horários parecidos ajuda mais do que tentar compensar no fim de semana.'),
 ('leve', 'DIA RUIM:', 'TREINO LEVE.', '[matter-of-fact] E se você dormiu mal, não força a carga máxima. Faz um treino mais leve, e mantém o hábito.'),
 ('conc', 'RESUMINDO:', 'SONO É TREINO.', 'Resumindo: sono também é parte do treino. Cuida dele como cuida da série.'),
 ('cta', 'COMENTA', 'SONO.', 'Comenta SONO que eu te mando como registrar seu treino no Bríu e comparar as semanas de sono bom e ruim. Link na bio.'),
])
V('brio_34_ordem', 'ordem dos exercícios no treino', 'ORDEM', 2, [
 ('hook', 'A ORDEM DO TREINO', 'IMPORTA?', '[curious] A ordem do treino importa?'),
 ('primeiro', 'O PRIMEIRO', 'RENDE MAIS.', 'Importa. O primeiro exercício é o que você faz com mais força e mais energia.'),
 ('prior', 'COMECE PELO', 'QUE IMPORTA.', 'Então começa pelo exercício que você mais quer evoluir.'),
 ('composto', 'COMPOSTOS', 'ANTES.', 'Os compostos, como agachamento, supino e remada, vêm antes dos isolados.'),
 ('cansado', 'CANSADO', 'ERRA MAIS.', 'Porque com o corpo cansado, a técnica piora e a carga cai.'),
 ('atrasado', 'MÚSCULO', 'ATRASADO?', '[matter-of-fact] Tem um músculo atrasado? Treina ele primeiro, quando você está inteiro.'),
 ('conc', 'RESUMINDO:', 'O MELHOR 1º.', 'Resumindo: o que vem primeiro recebe o melhor de você. Coloca ali o que mais importa.'),
 ('cta', 'COMENTA', 'ORDEM.', 'Comenta ORDEM que eu te mando como anotar a carga de cada exercício no Bríu, na ordem do seu treino. Link na bio.'),
])
V('brio_35_alonga', 'alongamento parado antes do treino reduz força', 'ALONGA', 2, [
 ('hook', 'ALONGAR ANTES', 'DE TREINAR?', '[curious] Alongar antes de treinar ajuda?'),
 ('forca', 'PARADO, ANTES,', 'TIRA FORÇA.', 'Alongar parado, por muito tempo, antes da série, pode reduzir sua força naquela hora.'),
 ('minuto', 'MAIS DE', '1 MINUTO.', 'Os estudos mostram essa queda quando o alongamento passa de um minuto no mesmo músculo.'),
 ('antes', 'ANTES:', 'MOVIMENTO.', 'Antes, faz o aquecimento dinâmico: os mesmos movimentos, com peso leve.'),
 ('depois', 'DEPOIS:', 'ALONGA.', 'O alongamento parado fica pro fim do treino, se você gosta dele.'),
 ('proibido', 'NÃO É', 'PROIBIDO.', '[matter-of-fact] Ele não é proibido. Só não é o melhor jeito de começar.'),
 ('conc', 'RESUMINDO:', 'MOVE ANTES.', 'Resumindo: antes do treino, movimento leve. Alongamento parado, só depois.'),
 ('cta', 'COMENTA', 'ALONGA.', 'Comenta ALONGA que eu te mando como registrar seu aquecimento e suas séries no Bríu. Link na bio.'),
])
V('brio_36_horario', 'melhor horário para treinar: manhã ou noite', 'HORA', 2, [
 ('hook', 'TREINAR DE MANHÃ', 'OU À NOITE?', '[curious] Melhor treinar de manhã ou à noite?'),
 ('estudos', 'A FORÇA', 'VARIA NO DIA.', 'Alguns estudos mostram pequenas diferenças de força ao longo do dia.'),
 ('tarde', 'FIM DA TARDE:', 'UM POUCO MAIS.', 'Em geral, a força é um pouco maior no fim da tarde.'),
 ('pequena', 'DIFERENÇA', 'PEQUENA.', 'Mas essa diferença é pequena perto do que realmente importa: ir treinar.'),
 ('repetir', 'O MELHOR HORÁRIO', 'É O QUE REPETE.', 'O melhor horário é o que você consegue repetir toda semana.'),
 ('escolhe', 'ESCOLHE UM', 'E MANTÉM.', '[matter-of-fact] Escolhe um horário que caiba na sua rotina, e mantém por quatro semanas.'),
 ('conc', 'RESUMINDO:', 'O QUE MANTÉM.', 'Resumindo: horário perfeito não existe. O que existe é o horário que você mantém.'),
 ('cta', 'COMENTA', 'HORA.', 'Comenta HORA que eu te mando como registrar seu treino no Bríu e ver se o seu horário está rendendo. Link na bio.'),
])
V('brio_37_semana', 'treinar só uma vez por semana funciona', 'SEMANA', 2, [
 ('hook', 'TREINAR 1 VEZ', 'POR SEMANA?', '[curious] Treinar só uma vez por semana funciona?'),
 ('sim', 'FUNCIONA.', 'É MELHOR QUE 0.', 'Funciona, sim. É melhor que zero, e traz ganho, principalmente pra quem está começando.'),
 ('total', 'O QUE CONTA', 'É O TOTAL.', 'O que conta é o total de séries na semana, não só quantos dias você treina.'),
 ('cansa', 'TUDO NUM DIA', 'CANSA.', 'Mas fazer tudo num dia só cansa, e a qualidade das últimas séries cai.'),
 ('dois', 'SE DER,', 'DIVIDE EM 2.', 'Se der, divide em dois dias, mesmo que curtos.'),
 ('corpo', 'SÓ 1 DIA?', 'CORPO TODO.', '[matter-of-fact] E se só der um dia, faz o corpo todo, com poucos exercícios bem feitos.'),
 ('conc', 'RESUMINDO:', '1 DIA > NENHUM.', 'Resumindo: um dia é melhor que nenhum, e dois é melhor ainda. O que não vale é ficar sem treinar.'),
 ('cta', 'COMENTA', 'SEMANA.', 'Comenta SEMANA que eu te mando como registrar suas séries no Bríu e ver o total da sua semana. Link na bio.'),
])
V('brio_38_pernas', 'treinar perna toda semana mesmo com pouco tempo', 'PERNAS', 2, [
 ('hook', 'PULA O TREINO', 'DE PERNA?', '[serious] Você pula o treino de perna?'),
 ('maior', 'MAIORES', 'MÚSCULOS DO CORPO.', 'As pernas têm os maiores músculos do corpo.'),
 ('desp', 'TRONCO FORTE,', 'PERNA ATRASADA.', 'Quem só treina a parte de cima fica desproporcional, com tronco forte e pernas atrasadas.'),
 ('ajuda', 'PERNA FORTE', 'AJUDA EM TUDO.', 'E perna forte ajuda no agachamento, no terra e até em subir escada sem cansar.'),
 ('curto', 'NÃO PRECISA', 'SER LONGO.', 'Não precisa de duas horas. Dois exercícios, três séries cada, já mantêm a perna no jogo.'),
 ('leve', 'COM MEDO', 'DA DOR? COMEÇA LEVE.', '[matter-of-fact] Se você tem medo da dor do dia seguinte, começa com pouca carga e sobe aos poucos.'),
 ('conc', 'RESUMINDO:', 'PERNA ENTRA NA SEMANA.', 'Resumindo: perna entra no treino da semana. Poucos exercícios, bem feitos, toda semana.'),
 ('cta', 'COMENTA', 'PERNAS.', 'Comenta PERNAS que eu te mando como registrar suas séries de perna no Bríu e acompanhar sua evolução. Link na bio.'),
])
