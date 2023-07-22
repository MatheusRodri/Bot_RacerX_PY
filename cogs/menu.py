from index import *
from cogs.setups.acc.introducao import *

@bot.command(name='menu')
async def menu(ctx):
    text = "Escolha uma opção iniciar\n1-Setups\n2-Eventos\n3-Campeonatos"
    await ctx.send(text)

@bot.event
async def on_message(message):
    print(message.content)
    if message.content == '1':
        print("Executou a validação")
        teste()
    await bot.process_commands(message)
    return


    