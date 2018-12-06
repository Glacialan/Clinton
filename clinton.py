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
client = commands.Bot(command_prefix = ["c!", "C!"])
client.remove_command("help")

# - - - - -
mainColor = 0x8ffc64
# - - - - -

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="USSR Propaganda", type=3))
    print("Bot Status: Online")
    print(" ")
    print("Logged in as: " + client.user.name)
    print(" ")
    print("- - - - -")

# - - - - -

@client.command(pass_context = True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)

# - - - - -

@client.command(pass_context=True)
async def  help(ctx):
        author = ctx.message.author

        embed = discord.Embed(
            color = mainColor
        )

        embed.set_author(name='☭ Help Menu ☭')
        embed.set_footer(text='Stil a work in progress!')
        embed.add_field(name='Info Commands:', value='`help`', inline=False)
        await client.delete_message(ctx.message)
        await client.send_message(author, embed=embed)
        
# - - - - -

@client.command(pass_context=True)
async def text(ctx, *args):
       server = ctx.message.server
        name =  ' '.join(args)
          await client.create_channel(server, name, type=discord.ChannelType.text)


# - - - - -
client.run(os.getenv('TOKEN'))
