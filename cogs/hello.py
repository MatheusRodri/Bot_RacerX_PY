from index import *

@bot.command(name='hello')
async def hello(ctx):
    frases = [("Hello!"), ("Hi!"), ("Hello there!"), ("Yo mate!"), ("Hey!")]
    resposta = random.choice(frases)
    await ctx.send(resposta)
    