token = "your token here"
spam_text = "Hello"

import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("Started Text Spam")
    i = 0
    while i <= 1:
        print(spam_text)
        channel = client.get_channel(804004562993676313)
        await channel.send(spam_text)
        await asyncio.sleep(1)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

client.run(token)