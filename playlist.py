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

    def next(self, song):
        if self.loop:
            self.queue.appendleft(self.history[-1])

        if len(self.queue) == 0:
            return None

        if song != "Dummy":
            if len(self.history) > config.MAX_HISTORY:
                self.history.popleft()

        return self.queue



