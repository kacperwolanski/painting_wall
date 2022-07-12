import pygame

import Button
import Colors
import Config

import Screen
import main


class Window:
    def __init__(self, x, y, length, height, text, buttons_amount):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.text = text
        self.buttons_amount = buttons_amount
        self.button_length = 10 * Config.PIXEL_LENGTH
        self.button_height = 5 * Config.PIXEL_LENGTH
        self.buttons = []
        self.is_active = False
        self.refuse = False
        self.allow = False

        self.button_x_offset = 0
        # color staff
        self.color_to_add = ""
        self.color_adding = False

        self.done = False
        self.clear = False
        # text staff
        self.typing_text = False
        self.choosing_font_size = False
        self.choosing_font_type = False
        self.choosing_text_color = False
        self.chosen_point = ""


        self.add_closing_buttom()

    def add_closing_buttom(self):
        closing_button_size = 5 * Config.PIXEL_LENGTH
        closing_button = Button.Button(self.x + self.length - closing_button_size, self.y, closing_button_size,
                                       closing_button_size, "X",
                                       Colors.WHITE, Colors.RED, Colors.AQUA)

        self.buttons.append([closing_button, "X"])

    def pop_window(self):

        # window surface
        pygame.draw.rect(main.WIN, Colors.LIGHT_GRAY, pygame.Rect(self.x, self.y, self.length, self.height))
        # poping 3d  frame
        pygame.draw.rect(main.WIN, Colors.BLACK, pygame.Rect(self.x, self.y, self.length, self.height),
                         Config.PIXEL_HEIGHT)
        # text_render
        Screen.text_rendering(self.text, Colors.BLACK, Colors.LIGHT_GRAY,
                              (self.x + self.length / 2, self.y + self.height / 4))

        for button in self.buttons:


            button[0].draw_the_button()
            # close button
            if button[0].active_button:
                if button[1] == "X":
                    self.is_active = False
                    self.color_adding = False

                elif button[1] == "Write color":
                    button[0].text = ""
                    self.done = False
                    self.color_adding = True

                elif button[1]=="Ok":
                    self.allow = True

                elif button[1] == "Yes":
                    self.allow = True

                elif button[1] == "Cancel":
                    self.refuse = True

                elif button[1] == "Add":
                    self.allow = True

                elif button[1] == "Clear values":
                    self.clear = True

                elif button[1] == "Choose text color":
                    self.choosing_text_color = True

                elif button[1] =="Choose font size":
                    self.choosing_font_size = True

                elif button[1] == "Choose font type":
                    self.choosing_font_type = True

                elif button[1] =="Type text":
                    self.typing_text = True

            # changing button's text
            if button[1] == "Write color":
                if len(self.color_to_add) > 0:
                    button[0].text = str(self.color_to_add)

                if self.done or self.clear:
                    button[0].text = "Press to add another one"
                    self.text = "Add color by writing RGB values"
                    self.color_adding = True


            if button[1] == "Chosen point":


                if pygame.mouse.get_pressed()[0]:

                    self.chosen_point = str(pygame.mouse.get_pos())
                    button[0].change_color(Colors.BLUE_1)
                    self.text = "Save this point?"
                elif not self.chosen_point:
                    button[0].text = str(pygame.mouse.get_pos())
                    button[0].change_color(Colors.WHITE)


    def generate_buttons(self, x, y, text, text_front_color, text_backing_color, activate_color, buttom_name):
        if len(text) < 10:
            self.button_length = len(text) * 3 * Config.PIXEL_LENGTH
        else:
            self.button_length = len(text) * 1.5 * Config.PIXEL_LENGTH
        button = Button.Button(x + 10 * Config.PIXEL_LENGTH + self.button_x_offset, y + self.height // 2,
                               self.button_length, self.button_height, text, text_front_color, text_backing_color,
                               activate_color)
        self.buttons.append([button, buttom_name])
        self.button_x_offset += self.button_length + (self.length - 20 * Config.PIXEL_LENGTH) // (
                self.buttons_amount * 2)


def generate_info_windows(draw_surface_height, tool_menu_height):
    info_windows = {}
    # add color window
    add_color_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 400, 200,
                              "Add color by writing RGB values", 3)
    # add color window buttons

    add_color_window.generate_buttons(0, tool_menu_height, "ADD", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                      "Add")
    add_color_window.generate_buttons(0, tool_menu_height, "CLEAR", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                      "Clear values")

    add_color_window.generate_buttons(0, tool_menu_height, "Press to add color in RGB", Colors.GRAY, Colors.WHITE,
                                      Colors.AQUA,
                                      "Write color")
    info_windows.update({add_color_window: [False, "Add color"]})

    # fill background window
    fill_background_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 200, 200,
                                    "Fill the background with       ?", 2)

    # fill background window buttons
    fill_background_window.generate_buttons(0, tool_menu_height, "Yes", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                            "Yes")
    fill_background_window.generate_buttons(0, tool_menu_height, "Cancel", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                            "Cancel")

    info_windows.update({fill_background_window: [False, "Fill background"]})

    # add image window
    add_image_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 200, 200,
                              "Add the image", 1)

    # add image window buttons
    add_image_window.generate_buttons(0, tool_menu_height, "Browse...", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                      "Browse")

    info_windows.update({add_image_window: [False, "Add image"]})

    # add text window
    add_text_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 700, 200,
                             "Choose font type, font size, text color and then click where you want to add text",
                             4)

    # add text window buttons
    add_text_window.generate_buttons(0, tool_menu_height, "Choose font type", Colors.BLACK, Colors.GRAY,
                                     Colors.AQUA,
                                     "Choose font type")

    add_text_window.generate_buttons(0, tool_menu_height, "Choose font size", Colors.BLACK, Colors.GRAY,
                                     Colors.AQUA,
                                     "Choose font size")

    add_text_window.generate_buttons(0, tool_menu_height, "Choose text color", Colors.BLACK, Colors.GRAY,
                                     Colors.AQUA,
                                     "Choose text color")

    add_text_window.generate_buttons(0, tool_menu_height, "Type text...", Colors.GRAY, Colors.WHITE,
                                     Colors.AQUA,
                                     "Type text")

    info_windows.update({add_text_window: [False, "Add text2"]})

    # choose text point window

    choose_point_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 300, 200,
                                 "Choose place for text", 3)

    # choose text point window buttons
    choose_point_window.generate_buttons(0, tool_menu_height, "OK", Colors.BLACK, Colors.GRAY,
                                         Colors.AQUA, "Ok")

    choose_point_window.generate_buttons(0, tool_menu_height, "CANCEL", Colors.BLACK, Colors.GRAY,
                                         Colors.AQUA, "Cancel")
    choose_point_window.generate_buttons(0, tool_menu_height, "Chosen point", Colors.GRAY, Colors.WHITE,
                                         Colors.AQUA, "Chosen point")


    info_windows.update({choose_point_window: [False, "Add text"]})

    # choose font size window
    choose_font_size_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 300, 200,
                                 "Choose font size", 2)

    # choose font size window buttons

    choose_font_size_window.generate_buttons(0, tool_menu_height, "OK", Colors.BLACK, Colors.GRAY,
                                             Colors.AQUA, "Ok")

    choose_font_size_window.generate_buttons(0, tool_menu_height, "CANCEL", Colors.BLACK, Colors.GRAY,
                                             Colors.AQUA, "Cancel")

    info_windows.update({choose_font_size_window: [False,"Choose size"]})


    # choose font type window
    choose_font_type_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 300, 200,
                                     "Choose font type", 3)

    # choose font type window buttons

    choose_font_type_window.generate_buttons(0, tool_menu_height, "text czcionka1", Colors.BLACK, Colors.GRAY,
                                             Colors.AQUA, "czc1")

    choose_font_type_window.generate_buttons(0, tool_menu_height, "text czcionka2", Colors.BLACK, Colors.GRAY,
                                             Colors.AQUA, "czc2")

    choose_font_type_window.generate_buttons(0, tool_menu_height, "text czcionka3", Colors.BLACK, Colors.GRAY,
                                             Colors.AQUA, "czc3")

    info_windows.update({choose_font_type_window: [False, "Choose type"]})

    # choose text color window









    # more options window
    more_options_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 400, 200,
                                 "More options", 5)

    info_windows.update({more_options_window: [False, "More options"]})

    return info_windows


