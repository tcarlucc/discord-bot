import discord
from discord.ext import commands
import secrets  # Seperate python file to not expose private token for bot login
import music  # Music playback capabilities

cogs = [music]

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())
intents = discord.Intents.all()
for cog in cogs:
    cog.setup(client)

'''
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('pong!')
'''


client.run(secrets.token)
