# BRIO_24 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = 'Quanto tempo de treino por dia é suficiente?'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Comenta quantos minutos você tem pra treinar por dia.'
GATILHO_TIPO = 1

NARRATION = {'file': 'audio_tight/roteiro_brio_24.mp3', 'starts': [0.0, 3.466, 7.327, 11.832, 16.132, 19.813, 24.109, 28.111, 32.488, 37.461, 42.894]}  # narração enxuta (tighten.py)

BEATS = [
    dict(vis='hook', k='', t1='SÓ TEM', t2='40 MINUTOS?',
         text='Você acha que precisa de duas horas de academia pra ter resultado? Não precisa.'),
    dict(vis='myth', k='', t1='O MITO', t2='QUANTO MAIS, MELHOR.',
         text='O mito é achar que quanto mais tempo na academia, mais músculo você ganha.'),
    dict(vis='truth', k='', t1='A VERDADE', t2='SÉRIES BOAS.',
         text='O que faz crescer são as séries boas, perto do limite. Não o tempo que você passa lá dentro.'),
    dict(vis='enough', k='', t1='QUANTO BASTA', t2='QUARENTA MINUTOS.',
         text='Pra muita gente, uns quarenta minutos bem feitos, três ou quatro vezes na semana, já funcionam.'),
    dict(vis='waste', k='', t1='ONDE SE PERDE', t2='CELULAR E CONVERSA.',
         text='O tempo que sobra se perde no celular, na conversa e esperando aparelho.'),
    dict(vis='secret', k='', t1='O SEGREDO', t2='CHEGAR COM PLANO.',
         text='O segredo é chegar sabendo o que vai fazer, com os exercícios e as cargas já definidos.'),
    dict(vis='rest', k='', t1='O DESCANSO', t2='CRONOMETRADO.',
         text='E descansar com cronômetro. Dois minutos nos grandes, um nos pequenos. Sem sumir.'),
    dict(vis='short', k='', t1='SEM TEMPO?', t2='PRIORIZA.',
         text='Dia corrido? Faz só os exercícios principais. Um treino curto é melhor do que nenhum.'),
    dict(vis='const', k='', t1='O QUE MANDA', t2='CONSTÂNCIA.',
         text='No final, quem tem resultado é quem vai toda semana, e não quem faz um treino gigante de vez em quando.'),
    dict(vis='order', k='', t1='A ORDEM', t2='GRANDES PRIMEIRO.',
         text='E a ordem ajuda: primeiro os exercícios grandes, com você descansado. Os pequenos ficam pro final.'),
    dict(vis='cta', k='', t1='COMENTA', t2='SEUS MINUTOS.',
         text='Comenta quantos minutos você tem pra treinar por dia. O Bríu monta o treino que cabe nesse tempo. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 2.728, 'fixa': 4.763, 'link': 7.298}),
]
