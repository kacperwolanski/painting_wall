import pygame
import Config
import Colors
import main
import Screen
import start_menu


class Buttom:
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

        color = self.text_backing_color
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(self.WIN, Colors.BLACK,
                                 pygame.Rect(self.x + 2, self.y + 2, self.length, self.height), 2)

            else:
                color = self.activate_color
                self.active_buttom = True

        return color

    def change_color(self,new_color):
        self.text_backing_color = new_color
# generate buttoms function
def generate_buttoms(tool_menu_length, tool_menu_height, draw_surface_length, draw_surface_height, shapes,
                     x_amount_of_shapes):
    buttoms = []

    # generate draw reseting buttom

    function_buttom_height = 5 * Config.PIXEL_LENGTH
    function_buttom_length = 10 * Config.PIXEL_LENGTH

    reset_buttom = Buttom( Config.SCREEN_LENGTH - 10 * Config.PIXEL_LENGTH, tool_menu_height,
                          function_buttom_length, function_buttom_height, "Reset", Colors.BLACK,
                          Colors.RED,
                          Colors.AQUA)
    buttoms.append([reset_buttom, "Reset"])

    # generate save draw buttom

    save_draw_buttom = Buttom( Config.SCREEN_LENGTH - 10 * Config.PIXEL_LENGTH,
                              tool_menu_height + function_buttom_height + Config.PIXEL_LENGTH,
                              function_buttom_length, function_buttom_height, "Save", Colors.BLACK,
                              Colors.LIGHT_GRAY,
                              Colors.AQUA)

    buttoms.append([save_draw_buttom, "Save_draw"])

    # generate open draw buttom

    open_draw_buttom = Buttom( Config.SCREEN_LENGTH - 10 * Config.PIXEL_LENGTH,
                              tool_menu_height + 2 * (function_buttom_height + Config.PIXEL_LENGTH),
                              function_buttom_length, function_buttom_height, "Open", Colors.BLACK,
                              Colors.LIGHT_GRAY,
                              Colors.AQUA)

    buttoms.append([open_draw_buttom, "Open_draw"])

    # generate shapes buttoms
    for name_of_shape in shapes.keys():
        shape_buttom = Buttom( shapes[name_of_shape][0] + Config.PIXEL_LENGTH,
                              shapes[name_of_shape][1] + Config.PIXEL_LENGTH,
                              tool_menu_length // x_amount_of_shapes - Config.PIXEL_LENGTH,
                              tool_menu_height // (2 * x_amount_of_shapes) - Config.PIXEL_LENGTH,
                              name_of_shape, Colors.BLACK,
                              Colors.WHITE,
                              Colors.AQUA)

        buttoms.append([shape_buttom, name_of_shape])

    # generate fill the background buttom
    fill_the_background_buttom = Buttom( draw_surface_length,
                                        draw_surface_height,
                                        2 * function_buttom_length, function_buttom_height,
                                        "Fill background", Colors.BLACK,
                                        Colors.LIGHT_GRAY,
                                        Colors.AQUA)

    buttoms.append([fill_the_background_buttom, "Fill background"])

    # generate add color buttom
    add_color_buttom = Buttom( draw_surface_length,
                              draw_surface_height + function_buttom_height + Config.PIXEL_LENGTH,
                              2 * function_buttom_length, function_buttom_height, "Add color",
                              Colors.BLACK,
                              Colors.LIGHT_GRAY,
                              Colors.AQUA)

    buttoms.append([add_color_buttom, "Add color"])

    # generate add image buttom
    add_image_buttom = Buttom( draw_surface_length,
                              draw_surface_height + 2 * (function_buttom_height + Config.PIXEL_LENGTH),
                              2 * function_buttom_length, function_buttom_height, "Add image", Colors.BLACK,
                              Colors.LIGHT_GRAY,
                              Colors.AQUA)

    buttoms.append([add_image_buttom, "Add image"])
    # generate add text buttom
    add_text_buttom = Buttom( draw_surface_length,
                             draw_surface_height + 3 * (function_buttom_height + Config.PIXEL_LENGTH),
                             2 * function_buttom_length, function_buttom_height, "Add text", Colors.BLACK,
                             Colors.LIGHT_GRAY,
                             Colors.AQUA)

    buttoms.append([add_text_buttom, "Add text"])

    # generate rubber buttom

    rubber_buttom = Buttom( draw_surface_length + 2 * Config.PIXEL_LENGTH,
                           tool_menu_height // 10 + 7 * Config.PIXEL_LENGTH,
                           2 * function_buttom_length, function_buttom_height, "Rubber", Colors.BLACK,
                           Colors.LIGHT_GRAY,
                           Colors.AQUA)

    buttoms.append([rubber_buttom, "Rubber"])

    # generate more options buttom
    more_options_buttom = Buttom( draw_surface_length,
                                 draw_surface_height + 4 * (
                                         function_buttom_height + Config.PIXEL_LENGTH),
                                 2 * function_buttom_length, function_buttom_height, "More options",
                                 Colors.BLACK,
                                 Colors.LIGHT_GRAY,
                                 Colors.AQUA)

    buttoms.append([more_options_buttom, "More options"])



    return buttoms



# reset buttom
def reset_buttom(pixels, color):
    for pixel in pixels:
        pixel.color = color

