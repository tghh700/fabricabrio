# BRIO_14 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = 'Treinar em jejum queima mais gordura?'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Comenta quantas vezes você treinou essa semana.'
GATILHO_TIPO = 1

NARRATION = {'file': 'audio_tight/roteiro_brio_14.mp3', 'starts': [0.0, 4.445, 8.884, 13.163, 18.426, 23.347, 28.6, 33.495, 39.037, 43.403, 48.695]}  # narração enxuta (tighten.py)

BEATS = [
    dict(vis='hook', k='', t1='TREINO EM JEJUM', t2='SECA MAIS?',
         text='Treinar em jejum queima mais gordura? Muita gente acorda cedo e vai sem comer por causa disso.'),
    dict(vis='idea', k='', t1='A IDEIA', t2='SEM COMIDA, USA GORDURA.',
         text='A ideia é simples: sem comida no corpo, você usaria mais gordura como energia.'),
    dict(vis='partial', k='', t1='O QUE É VERDADE', t2='DURANTE O TREINO.',
         text='E durante o treino, isso até acontece. Você usa um pouco mais de gordura naquela hora.'),
    dict(vis='day', k='', t1='MAS NO DIA', t2='O CORPO COMPENSA.',
         text='Só que no resto do dia o corpo compensa. Quando os estudos comparam o total, o resultado é parecido.'),
    dict(vis='rule', k='', t1='O QUE DECIDE', t2='O TOTAL DO DIA.',
         text='O que decide se você emagrece é o total do dia: o quanto você come e o quanto você gasta.'),
    dict(vis='perf', k='', t1='O RISCO', t2='TREINO MAIS FRACO.',
         text='E tem um risco: sem comer, muita gente rende menos na musculação, e faz menos série boa.'),
    dict(vis='who', k='', t1='PRA QUEM', t2='FUNCIONA.',
         text='Se você se sente bem em jejum e treina forte assim, pode continuar. É questão de preferência.'),
    dict(vis='dizzy', k='', t1='ATENÇÃO', t2='TONTURA NÃO.',
         text='Mas se der tontura, fraqueza ou enjoo, come alguma coisa antes. Ninguém precisa sofrer pra emagrecer.'),
    dict(vis='secret', k='', t1='O SEGREDO', t2='CONSTÂNCIA.',
         text='O segredo que funciona de verdade é treinar várias vezes por semana, todas as semanas.'),
    dict(vis='eat', k='', t1='E DEPOIS', t2='COME BEM.',
         text='E treinando em jejum ou não, depois do treino come direito, com proteína. É aí que o músculo se recupera.'),
    dict(vis='cta', k='', t1='COMENTA', t2='QUANTOS TREINOS.',
         text='Comenta quantas vezes você treinou essa semana. Não sabe? No Bríu fica tudo registrado. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 2.787, 'fixa': 4.278, 'link': 6.884}),
]
