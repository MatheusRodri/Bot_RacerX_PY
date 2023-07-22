import discord
from key import token
from discord.ext import commands
import os
import random

TOKEN = token.get("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

