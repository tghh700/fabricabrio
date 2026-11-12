# BRIO_25 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = 'Como saber se você está evoluindo (sem espelho nem balança)'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
MODEL = 'eleven_v4'
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Comenta SUBIU se a sua carga subiu esse mês, e confere no gráfico do Bríu.'
GATILHO_TIPO = 2

NARRATION = {'file': 'audio/brio25_v4_tight.mp3', 'starts': [0.0, 4.144, 8.287, 13.074, 19.104, 23.418, 28.368, 34.292, 39.694, 44.372, 50.498]}  # Eleven v4 + apertar.py

BEATS = [
    dict(vis='hook', k='', t1='ESTÁ', t2='EVOLUINDO?',
         text='Como saber se você está evoluindo, sem depender do espelho nem da balança?'),
    dict(vis='mirror', k='', t1='O ESPELHO', t2='ENGANA.',
         text='O espelho engana. Você se vê todo dia, e não percebe as mudanças pequenas.'),
    dict(vis='scale', k='', t1='A BALANÇA', t2='TAMBÉM.',
         text='E a balança mistura tudo: água, comida, músculo e gordura no mesmo número.'),
    dict(vis='sign1', k='', t1='SINAL 1', t2='A CARGA SOBE.',
         text='Primeiro sinal: a carga sobe. Mesmo exercício, mesmas repetições, mais peso que no mês passado.'),
    dict(vis='sign2', k='', t1='SINAL 2', t2='MAIS REPETIÇÕES.',
         text='Segundo sinal: mais repetições com o mesmo peso. Isso também é evolução.'),
    dict(vis='sign3', k='', t1='SINAL 3', t2='A FITA MÉTRICA.',
         text='Terceiro sinal: a fita métrica. Braço, coxa e cintura medidos uma vez por mês.'),
    dict(vis='sign4', k='', t1='SINAL 4', t2='FOTO DO MÊS.',
         text='Quarto sinal: uma foto por mês, mesma luz e mesma posição. Lado a lado, a diferença aparece.'),
    dict(vis='secret', k='', t1='O SEGREDO', t2='COMPARAR.',
         text='O segredo de tudo isso é um só: comparar. E pra comparar, você precisa ter anotado antes.'),
    dict(vis='stuck', k='', t1='SE NADA MUDOU', t2='AJUSTA.',
         text='Se em um mês nada mudou, não desiste. Ajusta uma coisa no treino e mede de novo.'),
    dict(vis='sign5', k='', t1='SINAL 5', t2='A ROUPA.',
         text='E o quinto sinal é o mais gostoso: a roupa. A camiseta apertando no braço e a calça folgando na cintura.'),
    dict(vis='cta', k='', t1='COMENTA', t2='SUBIU.',
         text='Comenta SUBIU se a sua carga subiu esse mês, e confere no gráfico do Bríu. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 2.667, 'fixa': 4.208, 'link': 6.84}),
]
