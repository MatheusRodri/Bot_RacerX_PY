import discord
from key import token

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
TOKEN = token.get("TOKEN")


@client.event
async def on_ready():
    print(f"{client.user} está onlines!")

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        print('teste')
        return

    if message.content.startswith('/hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)