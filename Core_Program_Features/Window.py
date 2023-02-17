import pygame


class Window:

    def __init__(
            self,
            background: dict,
            windowsize: tuple = (800, 800),
            window_caption: str = "Starlit default window",):

        self.width = windowsize[0]
        self.height = windowsize[1]

        self.background = background
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(window_caption)

    def render(self, sprite: dict):
        if type(sprite["Sprite"]) == pygame.Rect:
            pygame.draw.rect(self.screen, sprite["Color"], sprite["Sprite"])
        elif type(sprite["Sprite"]) == pygame.Surface:
            self.screen.blit(sprite["Sprite"], sprite["Coordinates"])
        else:
            raise Exception("Image type not supported.")

    def update(self):
        pygame.display.update()
        self.render(self.background)
