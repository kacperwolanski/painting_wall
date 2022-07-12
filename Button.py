import pygame
import Config
import Colors
import main
import Screen
import start_menu


class Button:
    def __init__(self, x, y, length, height, text, text_front_color, text_backing_color, activate_color):
        self.WIN = main.WIN
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.text = text
        self.text_front_color = text_front_color
        self.text_backing_color = text_backing_color
        self.activate_color = activate_color
        self.active_button = False
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)

    def draw_the_button(self):
        self.active_button = False
        color = self.button_press()

        pygame.draw.rect(self.WIN, color,
                         pygame.Rect(self.x, self.y, self.length, self.height))

        Screen.text_rendering(self.text, self.text_front_color, color,
                              (self.x + self.length / 2, self.y + self.height / 2),Config.BASIC_FONT)

    def button_press(self):

        color = self.text_backing_color
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(self.WIN, Colors.BLACK,
                                 pygame.Rect(self.x + 2, self.y + 2, self.length, self.height), 2)

            else:
                color = self.activate_color
                self.active_button = True

        return color

    def change_color(self, new_color):
        self.text_backing_color = new_color


# generate buttoms function
def generate_buttons(tool_menu_length, tool_menu_height, draw_surface_length, draw_surface_height, shapes,
                     x_amount_of_shapes):
    buttons = []

    # generate draw reseting button

    function_button_height = 5 * Config.PIXEL_LENGTH
    function_button_length = 10 * Config.PIXEL_LENGTH

    reset_button = Button(Config.SCREEN_LENGTH - 10 * Config.PIXEL_LENGTH, tool_menu_height,
                          function_button_length, function_button_height, "Reset", Colors.BLACK,
                          Colors.RED,
                          Colors.AQUA)
    buttons.append([reset_button, "Reset"])

    # generate save draw button

    save_draw_button = Button(Config.SCREEN_LENGTH - 10 * Config.PIXEL_LENGTH,
                              tool_menu_height + function_button_height + Config.PIXEL_LENGTH,
                              function_button_length, function_button_height, "Save", Colors.BLACK,
                              Colors.LIGHT_GRAY,
                              Colors.AQUA)

    buttons.append([save_draw_button, "Save_draw"])

    # generate open draw button

    open_draw_button = Button(Config.SCREEN_LENGTH - 10 * Config.PIXEL_LENGTH,
                              tool_menu_height + 2 * (function_button_height + Config.PIXEL_LENGTH),
                              function_button_length, function_button_height, "Open", Colors.BLACK,
                              Colors.LIGHT_GRAY,
                              Colors.AQUA)

    buttons.append([open_draw_button, "Open_draw"])

    # generate shapes buttons
    for name_of_shape in shapes.keys():
        shape_button = Button(shapes[name_of_shape][0] + Config.PIXEL_LENGTH,
                              shapes[name_of_shape][1] + Config.PIXEL_LENGTH,
                              tool_menu_length // x_amount_of_shapes - Config.PIXEL_LENGTH,
                              tool_menu_height // (2 * x_amount_of_shapes) - Config.PIXEL_LENGTH,
                              name_of_shape, Colors.BLACK,
                              Colors.WHITE,
                              Colors.AQUA)

        buttons.append([shape_button, name_of_shape])

    # generate fill the background button
    fill_the_background_button = Button(draw_surface_length,
                                        draw_surface_height,
                                        2 * function_button_length, function_button_height,
                                        "Fill background", Colors.BLACK,
                                        Colors.LIGHT_GRAY,
                                        Colors.AQUA)

    buttons.append([fill_the_background_button, "Fill background"])

    # generate add color button
    add_color_button = Button(draw_surface_length,
                              draw_surface_height + function_button_height + Config.PIXEL_LENGTH,
                              2 * function_button_length, function_button_height, "Add color",
                              Colors.BLACK,
                              Colors.LIGHT_GRAY,
                              Colors.AQUA)

    buttons.append([add_color_button, "Add color"])

    # generate add image button
    add_image_button = Button(draw_surface_length,
                              draw_surface_height + 2 * (function_button_height + Config.PIXEL_LENGTH),
                              2 * function_button_length, function_button_height, "Add image", Colors.BLACK,
                              Colors.LIGHT_GRAY,
                              Colors.AQUA)

    buttons.append([add_image_button, "Add image"])
    # generate add text button
    add_text_button = Button(draw_surface_length,
                             draw_surface_height + 3 * (function_button_height + Config.PIXEL_LENGTH),
                             2 * function_button_length, function_button_height, "Add text", Colors.BLACK,
                             Colors.LIGHT_GRAY,
                             Colors.AQUA)

    buttons.append([add_text_button, "Add text"])

    # generate rubber button

    rubber_button = Button(draw_surface_length + 2 * Config.PIXEL_LENGTH,
                           tool_menu_height // 10 + 7 * Config.PIXEL_LENGTH,
                           2 * function_button_length, function_button_height, "Rubber", Colors.BLACK,
                           Colors.LIGHT_GRAY,
                           Colors.AQUA)

    buttons.append([rubber_button, "Rubber"])

    # generate more options button
    more_options_button = Button(draw_surface_length,
                                 draw_surface_height + 4 * (
                                         function_button_height + Config.PIXEL_LENGTH),
                                 2 * function_button_length, function_button_height, "More options",
                                 Colors.BLACK,
                                 Colors.LIGHT_GRAY,
                                 Colors.AQUA)

    buttons.append([more_options_button, "More options"])

    return buttons


# reset button
def reset_button(pixels, color):
    for pixel in pixels:
        pixel.color = color
