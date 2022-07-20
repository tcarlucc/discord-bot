import discord
import youtube_dl
import utilities
from discord.ext import commands
from youtube_dl import DownloadError


class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await utilities.send_message(ctx, "Please join a voice channel.")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
        await ctx.guild.change_voice_state(channel=voice_channel, self_deaf=True)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        # TODO: Queue functionality
        if ctx.voice_client is None:
            await self.join(ctx)

        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'}
        YDL_OPTIONS = {'format': 'bestaudio'}
        voice_channel = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                stream = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)  # Creates audio stream
                voice_channel.play(stream)  # Plays stream in voice chat
            except DownloadError:
                await utilities.send_message(ctx, "Please use a valid youtube link.")


    @commands.command()
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await utilities.send_message(ctx, "Nothing is playing.")

    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await utilities.send_message(ctx, "Cannot resume music.")

    @commands.command()
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()


def setup(client):
    client.add_cog(music(client))
