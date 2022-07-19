from playlist import Playlist
import config

class audioprocessor(object):
    def __init__(self, client, guild):
        self.client = client
        self.playlist = Playlist()
        self.guild = guild
        self.now_playing = None

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

    async def play_song(self, song):