import main
import pygame
import Config
import Colors


class Slider:
    actual_x = 0
    scalling = 1

    def __init__(self, WIN, x, y, length, height, frame_color, buttom_color, mousedown):
        self.WIN = WIN
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.frame_color = frame_color
        self.buttom_color = buttom_color
        self.mousedown = mousedown
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)
        self.mouseup = False
        self.actual_x = 0

        self.draw_the_slider()

    def draw_the_slider(self):
        starting_x = self.x
        x = self.x
        if Slider.actual_x != 0:
            x = Slider.actual_x

        # draw the frame
        pygame.draw.rect(self.WIN, self.frame_color,
                         pygame.Rect(self.x, self.y, self.length, self.height), Config.PIXEL_LENGTH)

        self.move_buttom(self.x)

        # draw the buttom
        pygame.draw.rect(self.WIN, self.buttom_color,
                         pygame.Rect(x, self.y, Config.PIXEL_LENGTH * 2, self.height))

    def move_buttom(self, starting_x):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.mousedown:
                if pygame.mouse.get_pos()[0] > self.x:
                    self.x = pygame.mouse.get_pos()[0]
                    if pygame.mouse.get_pos()[0] + 3 * Config.PIXEL_LENGTH > starting_x + self.length:
                        self.x = starting_x + self.length - 3 * Config.PIXEL_LENGTH
                Slider.actual_x = self.x

                if self.x != starting_x:
                    Slider.scalling = int(((self.x - starting_x) / self.length) * 50)

    def return_val(self):
        return Slider.scalling
