# BRIO_23 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = 'Por que seu braço não cresce (e não é o bíceps)'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Salva pro próximo treino de braço e volta pra comentar quantas séries de tríceps você fez.'
GATILHO_TIPO = 5

NARRATION = {'file': 'audio_tight/roteiro_brio_23.mp3', 'starts': [0.0, 4.306, 7.894, 10.921, 14.555, 20.1, 24.919, 29.175, 33.423, 38.148, 43.655]}  # narração enxuta (tighten.py)

BEATS = [
    dict(vis='hook', k='', t1='BRAÇO', t2='NÃO CRESCE?',
         text='Seu braço não cresce, mesmo fazendo rosca toda semana? Talvez você esteja treinando o músculo errado.'),
    dict(vis='biceps', k='', t1='O FOCO', t2='SÓ BÍCEPS.',
         text='Quase todo mundo foca no bíceps. É o músculo da frente, o que aparece no espelho.'),
    dict(vis='triceps', k='', t1='O SEGREDO', t2='É O TRÍCEPS.',
         text='Só que a maior parte do braço é tríceps, o músculo de trás.'),
    dict(vis='three', k='', t1='TRÊS PARTES', t2='TRÊS CABEÇAS.',
         text='Ele tem três partes, e uma delas trabalha melhor com o braço acima da cabeça.'),
    dict(vis='overhead', k='', t1='O EXERCÍCIO', t2='ACIMA DA CABEÇA.',
         text='Por isso, inclui um tríceps com o braço lá em cima, como o francês ou o tríceps na polia por trás.'),
    dict(vis='push', k='', t1='E MAIS', t2='EMPURRAR.',
         text='E não esquece os exercícios de empurrar, como supino e mergulho. Eles também pegam o tríceps.'),
    dict(vis='volume', k='', t1='QUANTO', t2='SÉRIES NA SEMANA.',
         text='Uma boa base é umas dez séries de tríceps por semana, divididas em dois dias.'),
    dict(vis='elbow', k='', t1='CUIDADO', t2='COTOVELO.',
         text='Sentiu o cotovelo reclamar? Diminui o peso, e troca por uma variação que não doa.'),
    dict(vis='measure', k='', t1='COMO SABER', t2='FITA MÉTRICA.',
         text='E pra saber se está crescendo, mede o braço com fita uma vez por mês, sempre do mesmo jeito.'),
    dict(vis='time', k='', t1='PACIÊNCIA', t2='BRAÇO DEMORA.',
         text='E paciência: braço é um músculo pequeno, e cresce devagar. Meio centímetro em alguns meses já é ótimo.'),
    dict(vis='cta', k='', t1='SALVA', t2='PRO TREINO.',
         text='Salva pro próximo treino de braço e volta pra comentar quantas séries de tríceps você fez. Registra tudo no Bríu. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 4.655, 'fixa': 5.806, 'link': 8.395}),
]
