import pygame


class EntityBase:
    def __init__(self, coords: tuple = (0, 0), scale: tuple = (50, 50), sprite: dict = None):

        self.x = coords[0]
        self.y = coords[1]

        self.width = scale[0]
        self.height = scale[1]

        self.rect = pygame.Rect((self.width, self.height), (self.x, self.y))

        # default sprite
        if sprite is None:
            self.sprite = {
                "Sprite": self.rect,
                "Color": (0, 255, 255)}

        else:

            if type(sprite["Sprite"]) == pygame.Rect:
                self.sprite = {
                    "Sprite": self.rect,
                    "Color": sprite["Color"]}
            elif type(sprite["Sprite"]) == pygame.Surface:
                self.sprite = {
                    "Sprite": pygame.transform.scale(sprite["Sprite"], (self.width, self.height)),
                    "Coordinates": sprite["Coordinates"]
                }

    def update(self, gameinfo):
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

        # updates the renderable sprite
        if type(self.sprite["Sprite"]) == pygame.Rect:
            self.sprite = {
                "Sprite": self.rect,
                "Color": self.sprite["Color"]}

        elif type(self.sprite["Sprite"]) == pygame.Surface:
            self.sprite = {
               "Sprite": self.sprite["Sprite"],
               "Coordinates": (self.x, self.y)}

    def return_render_data(self):
        return self.sprite
