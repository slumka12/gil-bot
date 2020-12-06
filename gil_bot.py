from os import listdir

import discord
from discord.ext import commands

from func import tget

#SETUP

intents = discord.Intents.default()
intents.members = True
intents.typing = False
PREFIX="."
client = commands.Bot(command_prefix=PREFIX,intents=intents)

#Your ID
me = 382987612736192512
#Bot ID
botID = 702143271144783904

for filename in listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(tget())
