import pygame

import Buttom
import Colors
import Config

import Screen
import main


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
        # color staff
        self.color_to_add = ""
        self.color_adding = False

        self.done = False
        self.clear = False

        self.chosen_point = ""
        self.add_closing_buttom()

    def add_closing_buttom(self):
        closing_buttom_size = 5 * Config.PIXEL_LENGTH
        closing_buttom = Buttom.Buttom(self.x + self.length - closing_buttom_size, self.y, closing_buttom_size,
                                       closing_buttom_size, "X",
                                       Colors.WHITE, Colors.RED, Colors.AQUA)

        self.buttoms.append([closing_buttom, "X"])

    def pop_window(self):

        # window surface
        pygame.draw.rect(main.WIN, Colors.LIGHT_GRAY, pygame.Rect(self.x, self.y, self.length, self.height))
        # poping 3d  frame
        pygame.draw.rect(main.WIN, Colors.BLACK, pygame.Rect(self.x, self.y, self.length, self.height),
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
                    buttom[0].text = ""
                    self.done = False
                    self.color_adding = True

                elif buttom[1]=="Ok":
                    self.allow = True

                elif buttom[1] == "Yes":
                    self.allow = True

                elif buttom[1] == "Cancel":
                    self.refuse = True

                elif buttom[1] == "Add":
                    self.allow = True

                elif buttom[1] == "Clear values":
                    self.clear = True

            # changing buttom's text
            if buttom[1] == "Write color":
                if len(self.color_to_add) > 0:
                    buttom[0].text = str(self.color_to_add)

                if self.done or self.clear:
                    buttom[0].text = "Press to add another one"
                    self.text = "Add color by writing RGB values"
                    self.color_adding = True


            if buttom[1] == "Chosen point":


                if pygame.mouse.get_pressed()[0]:
                    print("prr")
                    self.chosen_point = str(pygame.mouse.get_pos())
                    buttom[0].change_color(Colors.BLUE_1)
                    self.text = "Save this point?"
                elif not self.chosen_point:
                    buttom[0].text = str(pygame.mouse.get_pos())
                    buttom[0].change_color(Colors.WHITE)


    def generate_buttoms(self, x, y, text, text_front_color, text_backing_color, activate_color, buttom_name):
        if len(text) < 10:
            self.buttom_length = len(text) * 3 * Config.PIXEL_LENGTH
        else:
            self.buttom_length = len(text) * 1.5 * Config.PIXEL_LENGTH
        buttom = Buttom.Buttom(x + 10 * Config.PIXEL_LENGTH + self.buttom_x_offset, y + self.height // 2,
                               self.buttom_length, self.buttom_height, text, text_front_color, text_backing_color,
                               activate_color)
        self.buttoms.append([buttom, buttom_name])
        self.buttom_x_offset += self.buttom_length + (self.length - 20 * Config.PIXEL_LENGTH) // (
                self.buttoms_amount * 2)


def generate_info_windows(draw_surface_height, tool_menu_height):
    info_windows = {}
    # add color window
    add_color_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 400, 200,
                              "Add color by writing RGB values", 3)
    # add color window buttoms

    add_color_window.generate_buttoms(0, tool_menu_height, "ADD", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                      "Add")
    add_color_window.generate_buttoms(0, tool_menu_height, "CLEAR", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                      "Clear values")

    add_color_window.generate_buttoms(0, tool_menu_height, "Press to add color in RGB", Colors.GRAY, Colors.WHITE,
                                      Colors.AQUA,
                                      "Write color")
    info_windows.update({add_color_window: [False, "Add color"]})

    # fill background window
    fill_background_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 200, 200,
                                    "Fill the background with       ?", 2)

    # fill background window buttoms
    fill_background_window.generate_buttoms(0, tool_menu_height, "Yes", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                            "Yes")
    fill_background_window.generate_buttoms(0, tool_menu_height, "Cancel", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                            "Cancel")

    info_windows.update({fill_background_window: [False, "Fill background"]})

    # add image window
    add_image_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 200, 200,
                              "Add the image", 1)

    # add image window buttoms
    add_image_window.generate_buttoms(0, tool_menu_height, "Browse...", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                      "Browse")

    info_windows.update({add_image_window: [False, "Add image"]})

    # add text window
    add_text_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 600, 200,
                             "Choose font type, font size, text color and then click where you want to add text",
                             3)

    # add text window buttoms
    add_text_window.generate_buttoms(0, tool_menu_height, "Choose font type", Colors.BLACK, Colors.GRAY,
                                     Colors.AQUA,
                                     "Choose font type")

    add_text_window.generate_buttoms(0, tool_menu_height, "Choose font size", Colors.BLACK, Colors.GRAY,
                                     Colors.AQUA,
                                     "Choose font size")

    add_text_window.generate_buttoms(0, tool_menu_height, "Choose text color", Colors.BLACK, Colors.GRAY,
                                     Colors.AQUA,
                                     "Choose text color")



    # choose the text point window

    choose_point_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 300, 200,
                                 "Choose place for text", 3)
    choose_point_window.generate_buttoms(0, tool_menu_height, "OK", Colors.BLACK, Colors.GRAY,
                                         Colors.AQUA, "Ok")

    choose_point_window.generate_buttoms(0, tool_menu_height, "CANCEL", Colors.BLACK, Colors.GRAY,
                                         Colors.AQUA, "Cancel")
    choose_point_window.generate_buttoms(0, tool_menu_height, "Chosen point", Colors.GRAY, Colors.WHITE,
                                         Colors.AQUA, "Chosen point")


    info_windows.update({choose_point_window: [False, "Add text"]})
    info_windows.update({add_text_window: [False, "Add text2"]})

    # more options window
    more_options_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 400, 200,
                                 "More options", 5)

    info_windows.update({more_options_window: [False, "More options"]})

    return info_windows


