import pygame
import Config
import Colors
import main


class Buttom:
    def __init__(self, WIN, x, y, length, height, text, text_front_color, text_backing_color,activate_color):
        self.WIN = WIN
        self.x =x
        self.y = y
        self.length = length
        self.height = height
        self.text = text
        self.text_front_color = text_front_color
        self.text_backing_color = text_backing_color
        self.activate_color =activate_color
        self.rect = pygame.Rect(self.x, self.y, self.length,self.height)


    def draw_the_buttom(self):
        pygame.draw.rect(self.WIN,self.text_backing_color,
                         pygame.Rect(self.x,self.y,self.length,self.height))