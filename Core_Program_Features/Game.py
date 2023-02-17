import Core_Program_Features
import Entity_Classes
import pygame


class Game:

    def __init__(self):
        self.Running = True

        # fluff needed for the program

        # window variables
        screensize = (800, 800)

        background = pygame.transform.scale(pygame.image.load("Images/Cat.jpg"), screensize)

        # Core mechanics used by the program
        self.GameWindow = Core_Program_Features.Window((background,  (0, 0)), screensize, "Cool game")
        self.EntityManager = Core_Program_Features.EntityManager()
        self.GameInfo = Core_Program_Features.GameInfo()

        # Game entities
        self.EntityManager.add_entity(Entity_Classes.Player((400, 400), (50, 50), (pygame.Rect((0, 0), (0, 0)), (255, 255, 255))))
        self.EntityManager.add_entity(Entity_Classes.Player((600, 400), (50, 50), (pygame.image.load("Images/Cat.jpg"), )))

    def update(self):
        if self.Running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Running = False

            # Core mechanics update statements
            self.GameWindow.update()
            self.GameInfo.update()
            self.EntityManager.update(self.GameWindow, self.GameInfo)
