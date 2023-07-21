import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def mensagem(message):
     if message.content.startswith('/matheus'):
         await message.channel.send('Matheus é top')
     