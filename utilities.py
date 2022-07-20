import config

async def is_connected(ctx):
    try:
        voice_channel = ctx.guild.voice_client.channel
        return voice_channel
    except:
        return None

def get_guild(bot, command):
    if command.guild is not None:
        return command.guild
    for guild in bot.guilds:
        for channel in guild.voice_channels:
            if command.author in channel.members:
                return guild
    return None