# BRIO_20 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = 'Semana leve: o descanso que faz a carga subir'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Comenta LEVE se você nunca fez uma semana leve, e marca no Bríu a carga antes e depois.'
GATILHO_TIPO = 2

NARRATION = {'file': 'audio_tight/roteiro_brio_20.mp3', 'starts': [0.0, 5.271, 10.645, 16.049, 20.619, 26.361, 30.367, 34.561, 38.752, 43.44, 48.083]}  # narração enxuta (tighten.py)

BEATS = [
    dict(vis='hook', k='', t1='PEGAR LEVE', t2='É FRAQUEZA?',
         text='Pegar leve uma semana inteira na academia parece fraqueza. Mas pode ser o que faz a sua carga voltar a subir.'),
    dict(vis='tired', k='', t1='O CANSAÇO', t2='ACUMULA.',
         text='Semana após semana de treino pesado, o cansaço vai acumulando, mesmo quando você não percebe.'),
    dict(vis='signs', k='', t1='OS SINAIS', t2='PRESTA ATENÇÃO.',
         text='Os sinais: carga parada, articulação reclamando, sono pior e zero vontade de treinar.'),
    dict(vis='what', k='', t1='O QUE É', t2='SEMANA LEVE.',
         text='A semana leve é simples: você treina, mas com menos séries e menos peso que o normal.'),
    dict(vis='how', k='', t1='COMO FAZER', t2='METADE DAS SÉRIES.',
         text='Um jeito comum: corta mais ou menos metade das séries, e tira um pouco do peso. Nada de ir até o limite.'),
    dict(vis='when', k='', t1='QUANDO', t2='A CADA ALGUMAS SEMANAS.',
         text='Muita gente faz a cada quatro a oito semanas, ou quando os sinais aparecem.'),
    dict(vis='after', k='', t1='O SEGREDO', t2='A VOLTA.',
         text='O segredo aparece na volta: o corpo descansado, e a carga voltando a subir.'),
    dict(vis='lose', k='', t1='O MEDO', t2='"VOU PERDER TUDO."',
         text='E não, você não perde músculo em uma semana leve. Você só deixa o corpo se recuperar.'),
    dict(vis='beginner', k='', t1='INICIANTE', t2='PODE ESPERAR.',
         text='Se você começou há pouco, nem precisa ainda. Isso é mais pra quem treina pesado há meses.'),
    dict(vis='feel', k='', t1='NA SEMANA LEVE', t2='VOCÊ SE SENTE BEM.',
         text='Na semana leve é normal sair do treino achando que fez pouco. É exatamente essa a ideia.'),
    dict(vis='cta', k='', t1='COMENTA', t2='LEVE.',
         text='Comenta LEVE se você nunca fez uma semana leve, e marca no Bríu a carga antes e depois. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 2.403, 'fixa': 4.34, 'link': 6.777}),
]
