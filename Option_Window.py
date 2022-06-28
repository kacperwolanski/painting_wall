import pygame
import Colors
import Config
import Screen
import main

Screen = Screen.Screen
WIN = main.WIN


class Window:
    def __init__(self, x, y, length, height, text):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.text = text
        self.buttoms = []

    def pop_window(self):
        # window surface
        pygame.draw.rect(WIN, Colors.LIGHT_GRAY, pygame.Rect(self.x, self.y, self.length, self.height))
        # poping 3d experience frame
        pygame.draw.rect(WIN, Colors.BLACK, pygame.Rect(self.x + 2, self.y + 2, self.length, self.height),
                         Config.PIXEL_HEIGHT)
        # text_render
        Screen.text_rendering(self.text, Colors.BLACK, Colors.LIGHT_GRAY,
                              (self.x + self.length / 2, self.y + self.height / 2))

    def add_buttoms(self):
        pass
