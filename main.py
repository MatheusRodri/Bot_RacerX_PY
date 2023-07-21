import discord
from key import token
from discord.ext import commands
import os

TOKEN = token.get("TOKEN")
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/',intents=intents)

bot.add_cog(commands.Cog(bot))

bot.run(TOKEN)