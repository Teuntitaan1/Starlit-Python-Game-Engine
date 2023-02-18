from Images import *


class Window:

    def __init__(
            self,
            background: tuple,
            window_size: tuple = (800, 800),
            window_caption: str = "Starlit default window",
            window_icon=CatImage):

        self.width = window_size[0]
        self.height = window_size[1]

        self.background = background
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(window_caption)
        pygame.display.set_icon(window_icon.convert_alpha())

    def render(self, sprite: tuple):
        if type(sprite[0]) == pygame.Rect:
            pygame.draw.rect(self.screen, sprite[1], sprite[0])
        elif type(sprite[0]) == pygame.Surface:
            self.screen.blit(sprite[0], sprite[1])
        else:
            raise Exception("Image type not supported.")

    def update(self):
        pygame.display.update()
        self.render(self.background)
