import discord
from discord.ext import commands
import secrets  # Seperate python file to not expose private token for bot login
import music  # Music playback capabilities

cogs = [music]

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())
intents = discord.Intents.all()
for cog in cogs:
    cog.setup(client)


client.run(secrets.token)
