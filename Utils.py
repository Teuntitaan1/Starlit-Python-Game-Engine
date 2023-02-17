import pygame


def generate_sprite(sprite, extraparams: dict):
    if type(sprite) == pygame.Surface:
        return {
            "Sprite": sprite,
            "Coordinates": extraparams["Coordinates"]
        }
    elif type(sprite) == pygame.Rect:
        return {
            "Sprite": sprite,
            "Color": extraparams["Color"]
        }
    else:
        raise TypeError("Invalid spritetype provided")