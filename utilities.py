import config

async def send_message(ctx, message):
    await ctx.send("```\n" + message + "\n```")

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

async def connect(guild, dest_channel, ctx, switch=False, default=True):
    for channel in guild.voice_channels:
        if str(channel.name).strip() == str(dest_channel).strip():
            if switch:
                try:
                    await guild.voice_client.disconnect()
                except:
                    await send_message(ctx, config.USER_NOT_IN_VOICE)
                await channel.connect()
                return
    if default:
        try:
            await guild.voice_channels[0].connect()
        except:
            await send_message(ctx, config.DEFAULT_VC_ERROR)