import discord
import os
import secrets  # Seperate python file to not expose private token for bot login

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('pong!')

    if message.content.startswith('$play flexicution'):
        await message.channel.send('no!')


client.run(secrets.token)
