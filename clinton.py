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

# - - - - -

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Through Your Webcam", type=3))
    print("Bot Status: Online")
    print(" ")
    print("Logged in as: " + client.user.name)
    print(" ")
    print("- - - - -")

# - - - - -

#Warn
@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, user: discord.Member, *args):
    author = ctx.message.author
    embed = discord.Embed(
        description='*You have been warned!*',
        color = 0xffa499
    )
    reason = ' '.join(args)

    embed.add_field(name='Warned By:', value='*{}*'.format(author), inline=False)
    embed.add_field(name='Reason:', value=reason, inline=False)

    await client.delete_message(ctx.message)
    await client.send_message(user, embed=embed)
    await client.send_message(author, '{} has been warned!!'.format(user))
    await client.send_message(author, 'For: {}'.format(reason))
                              
        
# - - - - -        
        
#Kick
@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    author = ctx.message.author.name
    await client.kick(user)

    embed = discord.Embed(
        description='**Kick Alert**'.format(user.name),
        color = 0xffa499

    )

    embed.add_field(name='User Kicked:', value='*{}*'.format(user.name), inline=True)
    embed.add_field(name='Kicked By:', value='*{}*'.format(author), inline=True)

    await client.delete_message(ctx.message)
    await client.say(embed=embed)
   
# - - - - -

#Say (For Owner Only)
@client.command(pass_context=True)
async def say(ctx, *args):
    if ctx.message.author.id == '171335165476470784':
        mesg = ' '.join(args)
        await client.delete_message(ctx.message)
        return await client.say(mesg)

# - - - - -

@client.command(pass_context=True)
async def help(ctx):
        author = ctx.message.author

        embed = discord.Embed(
            color = mainColor
        )

        embed.set_author(name='☭ Help Menu ☭')
        embed.set_footer(text='Clinton Bot')
        embed.add_field(name='Moderation ⚙️:', value='`help`', inline=False)
        await client.delete_message(ctx.message)
        await client.say(embed=embed)
        
# - - - - -


# - - - - -
client.run(os.getenv('TOKEN'))
