"""Legendas por rede (YouTube Shorts, TikTok, Instagram Reels) a partir do vídeo do data.json."""
def build(ch_id, v):
    hook = v['hook'].strip(); tags = [t.lower() for t in v['hashtags']]
    topic = [t for t in tags if t not in ('#brio','#fioterra','#academia','#musculacao','#hipertrofia','#dicasdetreino','#iniciantenaacademia',
                                         '#dicasdecasa','#eletrica','#eletricaresidencial','#manutencaoresidencial','#economiadeenergia')]
    if ch_id == 'brio':
        cta_bio = 'Registre e acompanhe seus treinos gratuitamente no BRIO. Link na bio.'
        cta_yt = 'Registre e acompanhe seus treinos gratuitamente no BRIO: link no perfil do canal.'
        ask = 'Salva pro próximo treino e manda pro seu parceiro de academia.'
        tt_extra = ['#gymtok', '#academia', '#treino']
    else:
        cta_bio = cta_yt = None
        ask = 'Salva esse vídeo e manda pra quem precisa.'
        tt_extra = ['#dicasdecasa', '#eletrica']
    if v.get('gatilho'):
        ask = v['gatilho'].strip()   # gatilho de engajamento do fim do vídeo (comentário/compartilhar/salvar)
    brand = tags[0]
    yt_tags = ['#shorts', brand] + (topic[:1] or tags[1:2])
    yt = f"{v['title']} {' '.join(yt_tags)}"[:100]
    yt_desc = '\n'.join(x for x in [hook, ask, cta_yt] if x)
    tt_tags = list(dict.fromkeys([brand] + topic[:2] + tt_extra + tags[1:]))[:6]
    tt = f"{hook} 👇\n{ask}" + (f"\n{cta_bio}" if cta_bio else '') + f"\n\n{' '.join(tt_tags)}"
    ig_tags = list(dict.fromkeys([brand] + topic[:2] + tags[1:]))[:5]   # Instagram: máximo 5 hashtags
    ig = f"{hook}\n\n{ask}" + (f"\n{cta_bio}" if cta_bio else '') + f"\n\n{' '.join(ig_tags)}"
    return {'youtube': {'titulo': yt, 'descricao': yt_desc + '\n\n' + ' '.join(yt_tags)}, 'tiktok': tt, 'instagram': ig}
