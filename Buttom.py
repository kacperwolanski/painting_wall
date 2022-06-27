import pygame
import Config
import Colors
import main
import Screen


class Buttom:
    def __init__(self, WIN, x, y, length, height, text, text_front_color, text_backing_color, activate_color):
        self.WIN = WIN
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.text = text
        self.text_front_color = text_front_color
        self.text_backing_color = text_backing_color
        self.activate_color = activate_color
        self.active_buttom = False
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)

    def draw_the_buttom(self):
        self.active_buttom = False
        color = self.buttom_press()

        pygame.draw.rect(self.WIN, color,
                         pygame.Rect(self.x, self.y, self.length, self.height))

        Screen.text_rendering(self.text, self.text_front_color, color,
                              (self.x + self.length / 2, self.y + self.height / 2))

    def buttom_press(self):

        color= self.text_backing_color
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                color = self.activate_color
                self.active_buttom = True



        return color