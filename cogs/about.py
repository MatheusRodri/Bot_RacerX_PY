from index import *

@bot.command(name='about')
async def about(ctx):
    text = """A ideia do RacerX surgiu quando 2 amigos, resolveram criar um website para
    o simulador Asseto Corsa Competizone, com o intuito ajudar a comunidade mundial a desenvolver
    setups, guias e etc.. Mas tivemos algumas dificuldades, então foi quando surgiu a ideia de criar um bot
    na qual pudesse ajudar a comunidade, com informações além do Asseto Corsa Competizone, 
    como por exemplo (F1 2023, Automobilista 2, iRacing, etc..), e muito mais além criar campeonatos. 
"""
    await ctx.send(text)