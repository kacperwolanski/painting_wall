import pygame
import Config


class Pixel:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.length = Config.PIXEL_LENGTH
        self.height = Config.PIXEL_HEIGHT
        self.rect = pygame.Rect(x, y, self.length, self.height)
