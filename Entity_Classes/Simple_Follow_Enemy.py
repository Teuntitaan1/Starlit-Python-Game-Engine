import pygame

import Entity_Classes
from Entity_Classes.EntityBase import EntityBase


class SimpleFollowEnemy(EntityBase):
    def __init__(self, coords: tuple, scale: tuple, sprite: tuple, movementspeed):
        super().__init__(coords, scale, sprite)

        self.MovementSpeed = movementspeed

        self.TargetX = 0
        self.TargetY = 0

    def update(self, gameinfo):

        for Entity in gameinfo.EntityManager.EntityList:
            # finds the player
            if type(Entity) == Entity_Classes.Player:
                self.TargetX = Entity.x
                self.TargetY = Entity.y
                break

        # moves towards the player
        if self.x > self.TargetX:
            self.x -= self.MovementSpeed * gameinfo.DeltaTime
        elif self.x < self.TargetX:
            self.x += self.MovementSpeed * gameinfo.DeltaTime
        else:
            pass

        if self.y > self.TargetY:
            self.y -= self.MovementSpeed * gameinfo.DeltaTime
        elif self.y < self.TargetY:
            self.y += self.MovementSpeed * gameinfo.DeltaTime
        else:
            pass

        # look in the EntityBase class for what this function does
        super().update(gameinfo)
