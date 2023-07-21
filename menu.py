from discord.ext import commands

@client.event
async def menu(message):
     if message.content.startswith('/menu'):
         await message.channel.send('Matheus é top')
     