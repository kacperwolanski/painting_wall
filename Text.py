import pygame
import Config
import Colors
import Option_Window
import Screen
import main
import Pixel
import Slider
import Button
import Drawing


class Text:
    def __init__(self, text, text_point, font_type, font_color, text_background_color, size):
        self.text = text
        self.text_point = text_point

        self.font_type = font_type
        self.font_color = font_color
        self.text_background_color = text_background_color
        self.size = size

    def pop_text(self):
        Screen.text_rendering(self.text, self.font_color, self.text_background_color, self.text_point,
                              pygame.font.Font(self.font_type, self.size))

    def remove_text(self):
        pass
