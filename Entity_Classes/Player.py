from Entity_Classes.EntityBase import EntityBase
from Images import *


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
            self.sprite = (pygame.transform.scale(CatImage.convert_alpha(), (self.width, self.height)), (self.x, self.y))

        # collision detection
        for Entity in gameinfo.EntityManager.EntityList:
            if Entity != self:
                # if colliding, handle the collision on the colliding entity's
                if self.rect.colliderect(Entity.rect):
                    self.handle_collision(colliding_entity=Entity.rect)
                    Entity.handle_collision(colliding_entity=Entity.rect)
        # look in the EntityBase class for what this function does
        super().update(gameinfo)

    def handle_collision(self, colliding_entity: pygame.Rect):
        pass
