import Core_Program_Features
import Entity_Classes
import pygame
from Images import *


class Game:

    def __init__(self):
        self.Running = True
        # fluff needed for the program
        # window variables
        screensize = (800, 800)
        background = pygame.transform.scale(CatImage, screensize)

        # Core mechanics used by the program
        self.GameInfo = Core_Program_Features.GameInfo(Core_Program_Features.Window((background,  (0, 0)), screensize, "Cool game"), Core_Program_Features.EntityManager())

        # Game entities
        self.GameInfo.EntityManager.add_entity(Entity_Classes.Player((400, 400), (50, 50), (pygame.Rect((0, 0), (800, 800)), (255, 255, 255))))
        self.GameInfo.EntityManager.add_entity(Entity_Classes.SimpleFollowEnemy((760, 400), (50, 50), (pygame.Rect((0, 0), (0, 0)), (255, 255, 255)), 50))

    def update(self):
        if self.Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Running = False

            # Core mechanics update statements
            self.GameInfo.update()
