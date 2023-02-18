import Core_Program_Features
import time

BeginTime = time.time()
Game = Core_Program_Features.Game()

while Game.Running:
    Game.update()

print("\n")
print(f"Program Quit with {Game.GameInfo.FramesElapsed} frames elapsed after {round(time.time() - BeginTime, 0)} seconds.")
print(f"Average fps: {Game.GameInfo.FramesElapsed/(time.time() - BeginTime)}")
