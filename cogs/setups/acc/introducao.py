from index import *


def teste():
    print("Executou a função teste")
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            await message.edit(content = "New content")
            return   
        else:
            await message.channel.send(message.content)
            await bot.process_commands(message)
    return