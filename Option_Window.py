import pygame

import Buttom
import Colors
import Config
import Screen
import main


WIN = main.WIN


class Window:
    def __init__(self, x, y, length, height, text, buttoms_amount):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.text = text
        self.buttoms_amount = buttoms_amount
        self.buttom_length =10* Config.PIXEL_LENGTH
        self.buttom_height= 5* Config.PIXEL_LENGTH
        self.buttoms = []
        self.is_active = False


    def add_closing_buttom(self):
        closing_buttom_size =
        closing_buttom = Buttom.Buttom(WIN,)

    def pop_window(self):

        # window surface
        pygame.draw.rect(WIN, Colors.LIGHT_GRAY, pygame.Rect(self.x, self.y, self.length, self.height))
        # poping 3d experience frame
        pygame.draw.rect(WIN, Colors.BLACK, pygame.Rect(self.x + 2, self.y + 2, self.length, self.height),
                         Config.PIXEL_HEIGHT)
        # text_render
        Screen.text_rendering(self.text, Colors.BLACK, Colors.LIGHT_GRAY,
                              (self.x + self.length / 2, self.y + self.height / 4))


        for buttom in self.buttoms:
            buttom.draw_the_buttom()
            if buttom.active_buttom:



    def generate_buttoms(self,y,text, text_front_color, text_backing_color, activate_color):
        buttom = Buttom.Buttom(WIN,self.length//self.buttoms_amount,y+self.height//2,self.buttom_length,self.buttom_height,text,text_front_color,text_backing_color,activate_color)
        self.buttoms.append(buttom)



    def close_the_window(self):
        pass