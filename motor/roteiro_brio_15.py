# BRIO_15 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = 'Treina pesado e não cresce? O erro está fora da academia'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Comenta SONO se você dorme menos de sete horas, e anota no Bríu como rende o treino depois de uma noite boa.'
GATILHO_TIPO = 2

NARRATION = {'file': 'audio_tight/roteiro_brio_15.mp3', 'starts': [0.0, 3.69, 8.448, 14.19, 18.468, 23.238, 28.305, 33.35, 38.477, 43.014, 48.193]}  # narração enxuta (tighten.py)

BEATS = [
    dict(vis='hook', k='', t1='TREINA PESADO', t2='E NÃO CRESCE?',
         text='Você treina pesado e não cresce? Talvez o problema esteja fora da academia.'),
    dict(vis='gym', k='', t1='UMA HORA', t2='NA ACADEMIA.',
         text='A academia é uma hora do seu dia. O músculo é construído nas outras vinte e três.'),
    dict(vis='sleep', k='', t1='ERRO 1', t2='DORMIR POUCO.',
         text='Erro um: dormir pouco. Com cinco horas de sono, você recupera menos e rende menos no próximo treino.'),
    dict(vis='protein', k='', t1='ERRO 2', t2='POUCA PROTEÍNA.',
         text='Erro dois: pouca proteína. Sem matéria-prima, o músculo não tem com o que crescer.'),
    dict(vis='food', k='', t1='ERRO 3', t2='COMER POUCO.',
         text='Erro três: comer pouco no geral. Quem quer ganhar massa e vive com fome trava rápido.'),
    dict(vis='weekend', k='', t1='ERRO 4', t2='O FIM DE SEMANA.',
         text='Erro quatro: a semana certinha, e o fim de semana que desfaz tudo, com festa e noite virada.'),
    dict(vis='stress', k='', t1='ERRO 5', t2='ESTRESSE ALTO.',
         text='Erro cinco: estresse alto todo dia. Ele piora o sono, a fome e a vontade de treinar.'),
    dict(vis='secret', k='', t1='O SEGREDO', t2='O BÁSICO BEM FEITO.',
         text='O segredo não tem nada de mágico: sono, comida e treino bem feitos, por meses seguidos.'),
    dict(vis='check', k='', t1='O TESTE', t2='COMPARE OS TREINOS.',
         text='Faz o teste: compara o treino depois de uma noite boa com o treino depois de uma noite ruim.'),
    dict(vis='fix', k='', t1='O AJUSTE', t2='UM POR VEZ.',
         text='O ajuste mais fácil é começar pelo sono. Meia hora a mais por noite já muda o seu próximo treino.'),
    dict(vis='cta', k='', t1='COMENTA', t2='SONO.',
         text='Comenta SONO se você dorme menos de sete horas, e anota no Bríu como rende o treino depois de uma noite boa. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 2.611, 'fixa': 5.711, 'link': 8.244}),
]
