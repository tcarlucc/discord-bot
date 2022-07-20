import config
import linkprocessor
import utilities
import youtube_dl

from playlist import Playlist

class audioprocessor(object):
    def __init__(self, client, guild):
        self.client = client
        self.playlist = Playlist()
        self.guild = guild
        self.now_playing = None
        self.timer = utilities.Timer(self.timeout_handler)

    def play_next(self, error):
        next_song = self.playlist.playnext(self.now_playing)
        self.now_playing = None

        if next_song is None:
            return

    def track_history(self):
        history = config.HISTORY_HEADER

        for song in self.playlist.history:
            history += "\n" + self.playlist.history.index(song) + song

        return history

    def youtube_search(self, msg):
        if linkprocessor.get_url(msg) is not None:
            return msg

        YDL_OPTIONS = {
            'format': 'bestaudio/best',
            'default_search': 'auto',
            'noplaylist': True
        }

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            result = ydl.extract_info(msg, download=False)

        if result == None:
            return None

        videocode = result['entries'][0]['id']

        return "https://www.youtube.com/watch?v={}".format(videocode)

    def stop(self):
        if self.guild.voice_client is None or (not self.guild.voice_client.is_paused() and
                                               not self.guild.voice_client.is_playing()):
            return

        self.playlist.loop = False
        self.playlist.next(self.now_playing)
        self.playlist.clear()
        self.guild.voice_client.stop()

    async def disconnect(self):
        await self.stop()
        await self.guild.voice_client.disconnect(force=True)

    async def timeout_handler(self):
        if len(self.guild.voice_client.channel.voice_states == 1):
            await self.disconnect()

    def clear_queue(self):
        self.playlist.queue.clear()
