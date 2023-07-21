import discord
from key import token
from discord.ext import commands
from commands.cogs.hello_cog import HelloCog
import os

TOKEN = token.get("TOKEN")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/',intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
           await bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)