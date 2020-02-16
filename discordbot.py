from discord.ext import commands
import os
import traceback
import discord
import asyncio
import random
import urllib.request
import json

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
d = 0
a = 0
async def ping(ctx):
      if client.user != message.author:
        while a != 1:
           a = random.randint(1, 4096)
           d = d + 1
           
        i = message.author.name +"さんは色違いのポケモンに"+str(d)+"回目で遭遇しました。"
        await message.channel.send(i)


bot.run(token)
