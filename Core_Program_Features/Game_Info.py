import time


class GameInfo:
    def __init__(self):
        self.FramesElapsed = 0
        self.OldTime = time.time()
        self.DeltaTime = 0

    def update(self):
        newtime = time.time()
        self.DeltaTime = newtime - self.OldTime
        self.OldTime = newtime

        self.FramesElapsed += 1


