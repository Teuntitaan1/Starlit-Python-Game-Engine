import pygame
from Entity_Classes.EntityBase import EntityBase


class Player(EntityBase):
    def __init__(self, coords: tuple, scale: tuple, sprite: tuple):
        super().__init__(coords, scale, sprite)

    def update(self, gameinfo):

        # handles input
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.y -= 100 * gameinfo.DeltaTime
        elif key[pygame.K_DOWN]:
            self.y += 100 * gameinfo.DeltaTime
        if key[pygame.K_LEFT]:
            self.x -= 100 * gameinfo.DeltaTime
        elif key[pygame.K_RIGHT]:
            self.x += 100 * gameinfo.DeltaTime
        if key[pygame.K_SPACE]:
            self.sprite = (pygame.transform.scale(pygame.image.load("C:\\Users\\Teunw\\Desktop\\creeren\\Starlit-Python-Game-Engine\\Images\\Cat.jpg"), (self.width, self.height)), (self.x, self.y))

        # look in the EntityBase class for what this function does
        super().update(gameinfo)
