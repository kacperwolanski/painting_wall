import pygame

import Button
import Colors
import Config

import Screen
import Slider
import file_operations
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
        self.sliders = []
        self.is_active = False
        self.refuse = False
        self.allow = False

        self.button_x_offset = 0
        # color staff
        self.value = ""
        self.color_adding = False

        self.done = False
        self.clear = False
        # text staff
        self.actual_font = "freesansbold.ttf"
        self.typing_text = False
        self.choosing_font_size = False
        self.choosing_font_type = False

        self.choosing_text_color = False
        self.choosing_font_color = False
        self.choosing_text_background_color = False
        self.chosen_point = ()

        # images staff
        self.adding_images = False
        self.image_to_add = ""


        self.add_closing_buttom()

    def add_closing_buttom(self):
        closing_button_size = 5 * Config.PIXEL_LENGTH
        closing_button = Button.Button(self.x + self.length - closing_button_size, self.y, closing_button_size,
                                       closing_button_size, "X",
                                       Colors.WHITE, Colors.RED, Colors.AQUA)

        self.buttons.append([closing_button, "X"])

    def pop_window(self, drawing_surface):

        # window surface
        pygame.draw.rect(main.WIN, Colors.LIGHT_GRAY, pygame.Rect(self.x, self.y, self.length, self.height))
        # poping 3d  frame
        pygame.draw.rect(main.WIN, Colors.BLACK, pygame.Rect(self.x, self.y, self.length, self.height),
                         Config.PIXEL_HEIGHT)
        # text_render
        Screen.text_rendering(self.text, Colors.BLACK, Colors.LIGHT_GRAY,
                              (self.x + self.length / 2, self.y + self.height / 4), Config.BASIC_FONT)

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

                elif button[1] == "Ok":
                    self.allow = True

                elif button[1] == "Yes":
                    self.allow = True

                elif button[1] == "Cancel":
                    self.refuse = True

                elif button[1] == "Add":
                    self.allow = True

                elif button[1] == "Clear values":
                    self.clear = True


# text font staff
                elif button[1] == "Choose font size":
                    self.choosing_font_size = True

                elif button[1] == "Choose font type":
                    self.choosing_font_type = True

                elif button[1] == "czc1":
                    self.actual_font = "fonts/FlappyBirdy.ttf"

                elif button[1] == "czc2":
                    self.actual_font = "fonts/GLADWINDEMORegular.ttf"

                elif button[1] == "czc3":
                    self.actual_font = "fonts/Minercraftory.ttf"

                elif button[1] == "czc4":
                    self.actual_font = "fonts/freesansbold.ttf"


                elif button[1] == "Type text" and not self.typing_text:
                    self.typing_text = True



                # choosing text color
                elif button[1] == "Choose text color":
                    self.choosing_text_color = True

                elif button[1] == "Choose font color":
                    self.choosing_font_color = True

                elif button[1] == "Choose text background color":
                    self.choosing_text_background_color = True


# adding images
                elif button[1] == "Browse":
                    self.adding_images = True

                elif button[1] in list(file_operations.images_to_draw.keys()):

                    self.image_to_add = file_operations.images_to_draw[button[1]][0]





            # changing button's text
            if button[1] == "Write color":
                if len(self.value) > 0:
                    button[0].text = str(self.value)

                if self.done or self.clear:
                    button[0].text = "Press to add another one"
                    self.text = "Add color by writing RGB values"
                    self.color_adding = True

            if button[1] == "Chosen point":
                if drawing_surface.collidepoint(pygame.mouse.get_pos()):

                    if pygame.mouse.get_pressed()[0] and not self.done:

                        self.chosen_point = pygame.mouse.get_pos()
                        self.done = True
                        button[0].change_color(Colors.BLUE_1)
                        self.text = "Save this point?"
                    elif not self.chosen_point:
                        button[0].text = str(pygame.mouse.get_pos())
                        button[0].change_color(Colors.WHITE)
                        self.done = False

        for slider in self.sliders:
            slider[0].draw_the_slider()

            if slider[1] == "Choose font size":
                self.value = slider[0].return_val()

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

    def generate_sliders(self, x, y, length, height, frame_color, buttom_color, slider_name):
        slider = Slider.Slider(x, y, length, height, frame_color, buttom_color)
        self.sliders.append([slider, slider_name])


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






    # select point for image window
    select_image_point_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 350, 200,
                              "Select a point for the image", 3)

    # select point for image window buttons
    select_image_point_window.generate_buttons(0, tool_menu_height, "OK", Colors.BLACK, Colors.GRAY,
                                         Colors.AQUA, "Ok")

    select_image_point_window.generate_buttons(0, tool_menu_height, "CANCEL", Colors.BLACK, Colors.GRAY,
                                         Colors.AQUA, "Cancel")
    select_image_point_window.generate_buttons(0, tool_menu_height, "Chosen point", Colors.GRAY, Colors.WHITE,
                                         Colors.AQUA, "Chosen point")

    info_windows.update({select_image_point_window: [False, "Select image point"]})

    # add image window

    add_image_window = Window(350, draw_surface_height + Config.PIXEL_HEIGHT, 200, 200,
                              "Add image", 1)

    # add image window buttoms

    add_image_window.generate_buttons(350, tool_menu_height, "Browse...", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                       "Browse")

    info_windows.update({add_image_window: [False, "Add image"]})


    # browse window

    select_image_window = Window(550, draw_surface_height + Config.PIXEL_HEIGHT, 100*len(file_operations.images_to_draw), 200,
                              "Select image you want to display", len(file_operations.images_to_draw))

    for index,image in enumerate(file_operations.images_to_draw.keys()):
        image_name=image[:len(image)-4]
        select_image_window.generate_buttons(550, tool_menu_height, image_name, Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                         str(image))

    info_windows.update({select_image_window: [False, "Select image"]})








    # add text window
    add_text_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 630, 200,
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
                                 "Select a point for text on the screen", 3)

    # choose text point window buttons
    choose_point_window.generate_buttons(0, tool_menu_height, "OK", Colors.BLACK, Colors.GRAY,
                                         Colors.AQUA, "Ok")

    choose_point_window.generate_buttons(0, tool_menu_height, "CANCEL", Colors.BLACK, Colors.GRAY,
                                         Colors.AQUA, "Cancel")
    choose_point_window.generate_buttons(0, tool_menu_height, "Chosen point", Colors.GRAY, Colors.WHITE,
                                         Colors.AQUA, "Chosen point")

    info_windows.update({choose_point_window: [False, "Add text"]})

    # choose font size window
    choose_font_size_window = Window(630, draw_surface_height + Config.PIXEL_HEIGHT, 200, 200,
                                     "Choose font size", 2)

    # choose font size window buttons

    choose_font_size_window.generate_buttons(630, tool_menu_height, "OK", Colors.BLACK, Colors.GRAY,
                                             Colors.AQUA, "Ok")

    choose_font_size_window.generate_buttons(630, tool_menu_height, "CANCEL", Colors.BLACK, Colors.GRAY,
                                             Colors.AQUA, "Cancel")

    # choose font size window slider
    choose_font_size_window.generate_sliders(680, tool_menu_height + 150, 100, 20, Colors.GRAY, Colors.BLACK,
                                             "Choose font size")

    info_windows.update({choose_font_size_window: [False, "Choose font size"]})

    # choose font type window
    choose_font_type_window = Window(630, draw_surface_height + Config.PIXEL_HEIGHT, 420, 200,
                                     "Choose font type", 3)

    # choose font type window buttons

    choose_font_type_window.generate_buttons(630, tool_menu_height, "FlappyBirdy", Colors.BLACK, Colors.GRAY,
                                             Colors.AQUA, "czc1")

    choose_font_type_window.generate_buttons(630, tool_menu_height, "Slim", Colors.BLACK, Colors.GRAY,
                                             Colors.AQUA, "czc2")

    choose_font_type_window.generate_buttons(630, tool_menu_height, "Black belt", Colors.BLACK, Colors.GRAY,
                                             Colors.AQUA, "czc3")

    choose_font_type_window.generate_buttons(290, tool_menu_height + 50, "Basic", Colors.BLACK, Colors.GRAY,
                                             Colors.AQUA, "czc4")

    info_windows.update({choose_font_type_window: [False, "Choose font type"]})

    # choose text color window
    choose_text_color_window = Window(630, draw_surface_height + Config.PIXEL_HEIGHT, 350, 200,
                                      "Choose text color", 1)
    # choose text color window buttons
    choose_text_color_window.generate_buttons(630, tool_menu_height-50, "Select color and click to add new font color",
                                              Colors.BLACK, Colors.GRAY,
                                              Colors.AQUA, "Choose font color")

    choose_text_color_window.generate_buttons(210, tool_menu_height+20,
                                              "Select color and click to add new background color",
                                              Colors.BLACK, Colors.GRAY,
                                              Colors.AQUA, "Choose text background color")

    info_windows.update({choose_text_color_window: [False, "Choose text color"]})

    # more options window
    more_options_window = Window(0, draw_surface_height + Config.PIXEL_HEIGHT, 400, 200,
                                 "More options", 5)

    info_windows.update({more_options_window: [False, "More options"]})

    return info_windows
