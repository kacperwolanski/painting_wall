import pygame

import Buttom
import Colors
import Config
import Images
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
        self.buttom_length = 10 * Config.PIXEL_LENGTH
        self.buttom_height = 5 * Config.PIXEL_LENGTH
        self.buttoms = []
        self.is_active = False
        self.refuse = False
        self.allow = False

        self.buttom_x_offset = 0
        self.keyboard_input = ""

        self.color_adding = False
        self.add_closing_buttom()

    def add_closing_buttom(self):
        closing_buttom_size = 5 * Config.PIXEL_LENGTH
        closing_buttom = Buttom.Buttom(WIN, self.x + self.length - closing_buttom_size, self.y, closing_buttom_size,
                                       closing_buttom_size, "X",
                                       Colors.WHITE, Colors.RED, Colors.AQUA)

        self.buttoms.append([closing_buttom, "X"])

    def pop_window(self):
        #self.is_active = True
        # window surface
        pygame.draw.rect(WIN, Colors.LIGHT_GRAY, pygame.Rect(self.x, self.y, self.length, self.height))
        # poping 3d experience frame
        pygame.draw.rect(WIN, Colors.BLACK, pygame.Rect(self.x, self.y, self.length, self.height),
                         Config.PIXEL_HEIGHT)
        # text_render
        Screen.text_rendering(self.text, Colors.BLACK, Colors.LIGHT_GRAY,
                              (self.x + self.length / 2, self.y + self.height / 4))

        for buttom in self.buttoms:

            buttom[0].draw_the_buttom()
            # close buttom
            if buttom[0].active_buttom:
                if buttom[1] == "X":
                    self.is_active = False
                    self.color_adding = False

                elif buttom[1] == "Write color":
                    text = buttom[0].text

                    buttom[0].text = "|..."
                    self.color_adding = True

                elif buttom[1] == "Yes":
                    self.allow = True

                elif buttom[1] == "Cancel":
                    self.refuse = True

                elif buttom[1] == "Add":
                    self.allow = True


        self.realize_tolls()


    def realize_tolls(self):
        if self.color_adding:
            pass






    def generate_buttoms(self, y, text, text_front_color, text_backing_color, activate_color, buttom_name):
        if len(text) < 10:
            self.buttom_length = len(text) * 3 * Config.PIXEL_LENGTH
        else:
            self.buttom_length = len(text) * 1.5 * Config.PIXEL_LENGTH
        buttom = Buttom.Buttom(WIN, 10* Config.PIXEL_LENGTH +self.buttom_x_offset, y + self.height // 2,
                               self.buttom_length, self.buttom_height, text, text_front_color, text_backing_color,
                               activate_color)
        self.buttoms.append([buttom, buttom_name])
        self.buttom_x_offset += self.buttom_length + (self.length-20* Config.PIXEL_LENGTH)//(self.buttoms_amount*2)
