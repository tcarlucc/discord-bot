import discord
import datetime
import config

class Song():
    def __init__(self, origin, host, base_url=None, channel=None, title=None, duration=None, full_url=None, \
                 thumbnail=None):
        self.host = host
        self.origin = origin
        self.base_url = base_url
        self.info = self.SongInfo(channel, title, duration, full_url, thumbnail)

        class SongInfo():
            def __init__(self, channel, title, duration, full_url, thumbnail):
                self.channel = channel
                self.title = title
                self.duration = duration
                self.full_url = full_url
                self.thumbnail = thumbnail

                def to_string(self, playtype):
                    return "TODO"