import time


class GameInfo:
    def __init__(self, gamewindow, entitymanager):
        self.FramesElapsed = 0
        self.OldTime = time.time()
        self.DeltaTime = 0

        # core component systems passed through via self
        self.GameWindow = gamewindow
        self.EntityManager = entitymanager

    def update(self):
        newtime = time.time()
        self.DeltaTime = newtime - self.OldTime
        self.OldTime = newtime

        self.FramesElapsed += 1

        self.GameWindow.update()
        self.EntityManager.update(self.GameWindow, self)


