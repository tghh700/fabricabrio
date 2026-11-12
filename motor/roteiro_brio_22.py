# BRIO_22 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = '5 erros de quem começou na academia agora'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Manda pra quem começou na academia esse mês.'
GATILHO_TIPO = 3

NARRATION = {'file': 'audio_tight/roteiro_brio_22.mp3', 'starts': [0.0, 4.139, 9.235, 13.631, 18.803, 24.16, 29.422, 34.56, 38.523, 43.325, 48.52]}  # narração enxuta (tighten.py)

BEATS = [
    dict(vis='hook', k='', t1='COMEÇOU', t2='AGORA?',
         text='Começou na academia agora? Esses cinco erros atrasam quase todo iniciante.'),
    dict(vis='e1', k='', t1='ERRO 1', t2='TROCAR TODA SEMANA.',
         text='Erro um: trocar o treino toda semana. Sem repetir, você nunca sabe se está evoluindo.'),
    dict(vis='e2', k='', t1='ERRO 2', t2='COPIAR O MAIS FORTE.',
         text='Erro dois: copiar o treino do mais forte da academia. Ele está em outra fase.'),
    dict(vis='e3', k='', t1='ERRO 3', t2='PESO ANTES DA TÉCNICA.',
         text='Erro três: colocar peso antes de aprender o movimento. Primeiro a técnica, depois a carga.'),
    dict(vis='e4', k='', t1='ERRO 4', t2='PULAR PERNA.',
         text='Erro quatro: pular o treino de perna. É a maior parte do seu corpo, e a que mais gasta energia.'),
    dict(vis='e5', k='', t1='ERRO 5', t2='NÃO ANOTAR.',
         text='Erro cinco: não anotar nada. Na semana seguinte, você não lembra a carga nem as repetições.'),
    dict(vis='secret', k='', t1='O SEGREDO', t2='O BÁSICO.',
         text='O segredo do começo é sem graça: poucos exercícios, bem feitos, repetidos por semanas.'),
    dict(vis='first', k='', t1='O PRIMEIRO MÊS', t2='APRENDER.',
         text='No primeiro mês, o objetivo é aprender os movimentos e criar o hábito de ir.'),
    dict(vis='help', k='', t1='DÚVIDA?', t2='PERGUNTA.',
         text='E se tiver dúvida no movimento, pede ajuda pro professor da academia. Ninguém nasce sabendo.'),
    dict(vis='bonus', k='', t1='BÔNUS', t2='COMPARAR COM OS OUTROS.',
         text='E um erro bônus: se comparar com quem treina há anos. Compara só com você mesmo, do mês passado.'),
    dict(vis='cta', k='', t1='MANDA', t2='PRA QUEM COMEÇOU.',
         text='Manda pra quem começou na academia esse mês. No Bríu, cada série fica anotada. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 2.346, 'fixa': 4.309, 'link': 7.049}),
]
