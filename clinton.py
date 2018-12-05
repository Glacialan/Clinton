import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import asyncio
from itertools import cycle
import random
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = ["k!", "K!"])
client.remove_command("help")
# - - - - -
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Hentai Only For The Plot", type=3))
    print("Bot Status: Online")
    print(" ")
    print("Logged in as: " + client.user.name)
    print(" ")
    print("- - - - -")

# - - - - -



client.run(os.getenv('TOKEN'))
