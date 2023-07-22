from index import *

@bot.command(name='hello')
async def hello(ctx):
    frases = [("Hello!"), ("Hi!"), ("Hello there!"), ("Yo mate!")]
    resposta = random.choice(frases)
    await ctx.send(resposta)
