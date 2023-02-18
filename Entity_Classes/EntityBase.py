import pygame


class EntityBase:
    def __init__(self, coords: tuple = (0, 0), scale: tuple = (50, 50), sprite: tuple = None):

        self.x = coords[0]
        self.y = coords[1]

        self.width = scale[0]
        self.height = scale[1]

        self.rect = pygame.Rect((self.width, self.height), (self.x, self.y))

        # default sprite
        if sprite is None:
            self.sprite = (self.rect, (255, 255, 0))
        else:

            if type(sprite[0]) == pygame.Rect:
                self.sprite = (self.rect, sprite[1])
            elif type(sprite[0]) == pygame.Surface:
                self.sprite = (pygame.transform.scale(sprite[0], (self.width, self.height)),  (self.x, self.y))

    def update(self, gameinfo):

        # updates the collision rect
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

        # updates the renderable sprite
        if type(self.sprite[0]) == pygame.Rect:
            self.sprite = (self.rect, self.sprite[1])
        elif type(self.sprite[0]) == pygame.Surface:
            self.sprite = (self.sprite[0], (self.x, self.y))

    def handle_collision(self, colliding_entity: pygame.Rect):
        print(f"i am colliding! {self}")

    def return_render_data(self):
        return self.sprite
