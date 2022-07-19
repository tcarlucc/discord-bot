import random
import config
from collections import deque

class Playlist:
    def __init__(self):
        self.queue = deque()
        self.history = deque()
        self.loop = False

    def __len__(self):
        return len(self.queue)

    def add(self, track):
        self.queue.append(track)

    def playnext(self, track):
        self.queue.appendleft(track)

    def shuffle(self):
        random.shuffle(self.queue)

    def clear(self):
        self.queue.clear()
        self.history.clear()
