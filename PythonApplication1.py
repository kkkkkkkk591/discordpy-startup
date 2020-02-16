import discord
import asyncio
import random
import urllib.request
import json

client = discord.Client()



@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    d = 0
    a = 0

    if message.content.startswith('K!pc'):
     if client.user != message.author:
        while a != 1:
           a = random.randint(1, 4096)
           d = d + 1
           
        i = message.author.name +"さんは色違いのポケモンに"+str(d)+"回目で遭遇しました。"
        await message.channel.send(i)

    if message.content.startswith('K!help'):
        if client.user != message.author:
         await message.channel.send("K!help・・・このメニュー\r\nK!pc・・・色違いと遭遇するまでの野生のポケモンとの遭遇回数計算")

    if message.content.startswith('K!a'):
        if client.user != message.author:
         resp = urllib.request.urlopen('https://twitter.com/mokouliszt').read()
         resp = json.loads(resp.decode('utf-8'))
         await message.channel.send(resp[apple-mobile-web-app-title])

client.run(TOKEN)
