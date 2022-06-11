import pygame
import Config


class Slider:
    def __init__(self, WIN, x, y, length, height, frame_color, buttom_color):
        self.WIN = WIN
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.frame_color = frame_color
        self.buttom_color = buttom_color
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)
        self.buttom_x = self.x
        self.scalling = 1



    def draw_the_slider(self,mousedown):


        # draw the frame
        pygame.draw.rect(self.WIN, self.frame_color,
                         pygame.Rect(self.x, self.y, self.length, self.height), Config.PIXEL_LENGTH)

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if mousedown:
                if pygame.mouse.get_pos()[0] > self.x:
                    self.buttom_x = pygame.mouse.get_pos()[0]
                    if pygame.mouse.get_pos()[0] + 3 * Config.PIXEL_LENGTH > self.x + self.length:
                        self.buttom_x = self.x + self.length - 3 * Config.PIXEL_LENGTH
                if self.buttom_x != self.x:
                    self.scalling = int(((self.buttom_x - self.x) / self.length) * 50)

        # draw the buttom
        pygame.draw.rect(self.WIN, self.buttom_color,
                         pygame.Rect(self.buttom_x, self.y, Config.PIXEL_LENGTH * 2, self.height))


    def return_val(self):
        return self.scalling
