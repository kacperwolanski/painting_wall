import pygame
import Config
import Colors
import Option_Window
import main
import Pixel
import Slider
import Buttom
import Drawing

WIN = main.WIN
Paint = main.Paint

font = main.font


class Screen:
    def __init__(self):

        self.draw_surface_length = Config.WINDOW_LENGTH * (Config.PIXEL_LENGTH - 1)
        self.draw_surface_height = Config.WINDOW_HEIGHT * (Config.PIXEL_HEIGHT - 1) + 1
        self.tool_menu_length = Config.SCREEN_LENGTH - self.draw_surface_length
        self.tool_menu_height = self.draw_surface_height

        self.keyboard_input = ""
        self.pixels = []

        # color staff
        self.palette_height = 1
        self.actual_color = Colors.BLACK
        self.samples = []
        self.color_choose = -1
        self.actual_drawing_width = 1

        # tool staff
        self.sliders = []
        self.buttoms = []
        self.info_windows = {}
        self.info_windows_names = []
        self.append_tools = True
        self.rubber = False

        # shapes staff
        self.x_amount_of_shapes = 3
        self.shapes = {'Rectangle': [], 'Circle': [], 'Ellipse': [], 'Line': [], 'Square': [], 'Triangle': []}

    def generate_tools(self):
        if self.append_tools:
            self.generate_pixels()
            self.generate_sliders()
            self.generate_buttoms()
            self.generate_info_windows()
            self.append_tools = False

    # drawing staff
    def draw_the_window(self):

        WIN.fill(Colors.WHITE)
        # print(self.info_windows)
        self.make_the_drawing()
        self.samples = Drawing.draw_color_palette(self.tool_menu_length,self.tool_menu_height,self.draw_surface_length,self.color_choose,self.samples,Config.palette_height)
        Drawing.draw_frames(self.draw_surface_length, self.draw_surface_height, self.tool_menu_length,
                            self.tool_menu_height, self.actual_color, self.x_amount_of_shapes, self.shapes)
        self.realize_info_windows()
        self.realize_the_tools()
        self.generate_tools()
        self.blit_text()

        pygame.display.update()

    def generate_pixels(self):

        offset_x = 0
        offset_y = 0

        for x in range(Config.WINDOW_LENGTH):
            for y in range(Config.WINDOW_HEIGHT):
                self.pixels.append(Pixel.Pixel(offset_x, offset_y, Colors.WHITE))
                offset_y += Config.PIXEL_HEIGHT - 1

            offset_x += Config.PIXEL_LENGTH - 1
            offset_y = 0

    def make_the_drawing(self):

        if pygame.mouse.get_pressed()[0]:
            for pixel in range(len(self.pixels)):
                if self.pixels[pixel].rect.collidepoint(pygame.mouse.get_pos()):
                    if self.actual_drawing_width > 1:
                        for w_x in range(self.actual_drawing_width):
                            for w_y in range(self.actual_drawing_width):
                                index = pixel + w_x * Config.WINDOW_HEIGHT + w_y
                                if index < len(self.pixels) and self.pixels[index].y >= pygame.mouse.get_pos()[1]:
                                    self.pixels[index].color = self.actual_color

                    else:
                        self.pixels[pixel].color = self.actual_color

        for i in self.pixels:
            pygame.draw.rect(WIN, i.color, i)



    def realize_the_tools(self):

        # rubber
        if self.rubber:
            # rubber cleaning

            # rubber frame
            pygame.draw.rect(WIN, Colors.BLACK, pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],
                                                            3 * self.actual_drawing_width,
                                                            3 * self.actual_drawing_width), 2)

        # sliders
        for slider in self.sliders:
            slider[0].draw_the_slider()

            if slider[1] == 'actual_drawing_width':
                self.actual_drawing_width = slider[0].return_val()

        # buttoms
        for buttom in self.buttoms:
            buttom[0].draw_the_buttom()
            if buttom[0].active_buttom:
                # Reset buttom
                if buttom[1] == "Reset":
                    Buttom.reset_buttom(self.pixels, Colors.WHITE)
                # save draw buttom

                elif buttom[1] == "Rubber":

                    if self.rubber:
                        self.rubber = False
                    else:
                        self.rubber = True
                        self.actual_color = Colors.WHITE

                elif buttom[1] == "Save_draw":
                    pass


                # open draw buttom
                elif buttom[1] == "Open_draw":
                    pass


                # shapes
                elif buttom[1] in self.shapes:
                    if buttom[1] == 'Rectangle':
                        pass


                elif buttom[1] in self.info_windows_names:
                    if self.check_if_other_windows_work(buttom[1]):
                        self.activate_window(buttom[1])

    # info windows staff
    def activate_window(self, name):
        for window in list(self.info_windows.keys()):
            if self.info_windows[window][1] == name:
                self.info_windows[window][0] = True

    def check_if_other_windows_work(self, name_of_window):
        for window in list(self.info_windows.keys()):
            if self.info_windows[window][0]:
                if self.info_windows[window][1] != name_of_window:
                    return False
        return True

    def realize_info_windows(self):
        for window in self.info_windows.keys():
            if len(self.info_windows_names) < len(self.info_windows):
                self.info_windows_names.append(self.info_windows[window][1])

            if self.info_windows[window][0]:
                window.is_active = True
                window.pop_window()

                # fill background
                if self.info_windows[window][1] == "Fill background":
                    pygame.draw.rect(WIN, self.actual_color,
                                     pygame.Rect(window.x + 50 + window.length / 2, window.y + window.height / 5, 15,
                                                 15))

                    if window.allow:
                        Buttom.reset_buttom(self.pixels, self.actual_color)
                        window.allow = False
                    elif window.refuse:
                        window.is_active = False
                        window.refuse = False

                # add color
                if self.info_windows[window][1] == "Add color":
                    pass

                self.info_windows[window][0] = window.is_active

    def generate_info_windows(self):
        # add color window
        add_color_window = Option_Window.Window(0, self.draw_surface_height + Config.PIXEL_HEIGHT, 400, 200,
                                                "Add color by writing RGB values", 3)
        # add color window buttoms

        add_color_window.generate_buttoms(self.tool_menu_height, "ADD", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                          "Add color")
        add_color_window.generate_buttoms(self.tool_menu_height, "CLEAR", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                          "Clear values")

        add_color_window.generate_buttoms(self.tool_menu_height, "Press to add color in RGB", Colors.GRAY, Colors.WHITE,
                                          Colors.AQUA,
                                          "Write color")
        self.info_windows.update({add_color_window: [False, "Add color"]})

        # fill background window
        fill_background_window = Option_Window.Window(0, self.draw_surface_height + Config.PIXEL_HEIGHT, 200, 200,
                                                      "Fill the background with       ?", 2)

        # fill background window buttoms
        fill_background_window.generate_buttoms(self.tool_menu_height, "Yes", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                                "Yes")
        fill_background_window.generate_buttoms(self.tool_menu_height, "Cancel", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                                "Cancel")

        self.info_windows.update({fill_background_window: [False, "Fill background"]})

        # add image window
        add_image_window = Option_Window.Window(0, self.draw_surface_height + Config.PIXEL_HEIGHT, 200, 200,
                                                "Add the image", 1)

        # add image window buttoms
        add_image_window.generate_buttoms(self.tool_menu_height, "Browse...", Colors.BLACK, Colors.GRAY, Colors.AQUA,
                                          "Browse")

        self.info_windows.update({add_image_window: [False, "Add image"]})

        # add text window
        add_text_window = Option_Window.Window(0, self.draw_surface_height + Config.PIXEL_HEIGHT, 600, 200,
                                               "Choose font type, font size, text color and then click where you want to add text",
                                               3)

        # add text window buttoms
        add_text_window.generate_buttoms(self.tool_menu_height, "Choose font type", Colors.BLACK, Colors.GRAY,
                                         Colors.AQUA,
                                         "Choose font type")

        add_text_window.generate_buttoms(self.tool_menu_height, "Choose font size", Colors.BLACK, Colors.GRAY,
                                         Colors.AQUA,
                                         "Choose font size")

        add_text_window.generate_buttoms(self.tool_menu_height, "Choose text color", Colors.BLACK, Colors.GRAY,
                                         Colors.AQUA,
                                         "Choose text color")

        self.info_windows.update({add_text_window: [False, "Add text"]})

        # more options window
        more_options_window = Option_Window.Window(0, self.draw_surface_height + Config.PIXEL_HEIGHT, 400, 200,
                                                   "More options", 5)

        self.info_windows.update({more_options_window: [False, "More options"]})

    def generate_sliders(self):
        # generate width slider
        width_slider = Slider.Slider(WIN, self.draw_surface_length + self.tool_menu_length // 4,
                                     Config.PIXEL_LENGTH * 2,
                                     self.tool_menu_length // 2, Config.PIXEL_LENGTH * 5,
                                     Colors.LIGHT_GRAY, self.actual_color)

        self.sliders.append([width_slider, 'actual_drawing_width'])

    def generate_buttoms(self):

        # generate draw reseting buttom

        function_buttom_height = 5 * Config.PIXEL_LENGTH
        function_buttom_length = 10 * Config.PIXEL_LENGTH

        reset_buttom = Buttom.Buttom(WIN, Config.SCREEN_LENGTH - 10 * Config.PIXEL_LENGTH, self.tool_menu_height,
                                     function_buttom_length, function_buttom_height, "Reset", Colors.BLACK,
                                     Colors.RED,
                                     Colors.AQUA)
        self.buttoms.append([reset_buttom, "Reset"])

        # generate save draw buttom

        save_draw_buttom = Buttom.Buttom(WIN, Config.SCREEN_LENGTH - 10 * Config.PIXEL_LENGTH,
                                         self.tool_menu_height + function_buttom_height + Config.PIXEL_LENGTH,
                                         function_buttom_length, function_buttom_height, "Save", Colors.BLACK,
                                         Colors.LIGHT_GRAY,
                                         Colors.AQUA)

        self.buttoms.append([save_draw_buttom, "Save_draw"])

        # generate open draw buttom

        open_draw_buttom = Buttom.Buttom(WIN, Config.SCREEN_LENGTH - 10 * Config.PIXEL_LENGTH,
                                         self.tool_menu_height + 2 * (function_buttom_height + Config.PIXEL_LENGTH),
                                         function_buttom_length, function_buttom_height, "Open", Colors.BLACK,
                                         Colors.LIGHT_GRAY,
                                         Colors.AQUA)

        self.buttoms.append([open_draw_buttom, "Open_draw"])

        # generate shapes buttoms
        for name_of_shape in self.shapes.keys():
            shape_buttom = Buttom.Buttom(WIN, self.shapes[name_of_shape][0] + Config.PIXEL_LENGTH,
                                         self.shapes[name_of_shape][1] + Config.PIXEL_LENGTH,
                                         self.tool_menu_length // self.x_amount_of_shapes - Config.PIXEL_LENGTH,
                                         self.tool_menu_height // (2 * self.x_amount_of_shapes) - Config.PIXEL_LENGTH,
                                         name_of_shape, Colors.BLACK,
                                         Colors.WHITE,
                                         Colors.AQUA)

            self.buttoms.append([shape_buttom, name_of_shape])

        # generate fill the background buttom
        fill_the_background_buttom = Buttom.Buttom(WIN, self.draw_surface_length,
                                                   self.draw_surface_height,
                                                   2 * function_buttom_length, function_buttom_height,
                                                   "Fill background", Colors.BLACK,
                                                   Colors.LIGHT_GRAY,
                                                   Colors.AQUA)

        self.buttoms.append([fill_the_background_buttom, "Fill background"])

        # generate add color buttom
        add_color_buttom = Buttom.Buttom(WIN, self.draw_surface_length,
                                         self.draw_surface_height + function_buttom_height + Config.PIXEL_LENGTH,
                                         2 * function_buttom_length, function_buttom_height, "Add color",
                                         Colors.BLACK,
                                         Colors.LIGHT_GRAY,
                                         Colors.AQUA)

        self.buttoms.append([add_color_buttom, "Add color"])

        # generate add image buttom
        add_image_buttom = Buttom.Buttom(WIN, self.draw_surface_length,
                                         self.draw_surface_height + 2 * (function_buttom_height + Config.PIXEL_LENGTH),
                                         2 * function_buttom_length, function_buttom_height, "Add image", Colors.BLACK,
                                         Colors.LIGHT_GRAY,
                                         Colors.AQUA)

        self.buttoms.append([add_image_buttom, "Add image"])
        # generate add text buttom
        add_text_buttom = Buttom.Buttom(WIN, self.draw_surface_length,
                                        self.draw_surface_height + 3 * (function_buttom_height + Config.PIXEL_LENGTH),
                                        2 * function_buttom_length, function_buttom_height, "Add text", Colors.BLACK,
                                        Colors.LIGHT_GRAY,
                                        Colors.AQUA)

        self.buttoms.append([add_text_buttom, "Add text"])

        # generate rubber buttom

        rubber_buttom = Buttom.Buttom(WIN, self.draw_surface_length + 2 * Config.PIXEL_LENGTH,
                                      self.tool_menu_height // 10 + 7 * Config.PIXEL_LENGTH,
                                      2 * function_buttom_length, function_buttom_height, "Rubber", Colors.BLACK,
                                      Colors.LIGHT_GRAY,
                                      Colors.AQUA)

        self.buttoms.append([rubber_buttom, "Rubber"])

        # generate more options buttom
        more_options_buttom = Buttom.Buttom(WIN, self.draw_surface_length,
                                            self.draw_surface_height + 4 * (
                                                    function_buttom_height + Config.PIXEL_LENGTH),
                                            2 * function_buttom_length, function_buttom_height, "More options",
                                            Colors.BLACK,
                                            Colors.LIGHT_GRAY,
                                            Colors.AQUA)

        self.buttoms.append([more_options_buttom, "More options"])

    # text staff
    def blit_text(self):
        # width adjusting
        # text "Adjust drawing width" render staff
        text_rendering('Adjust drawing width', Colors.BLACK, Colors.LIGHT_GRAY,
                       (self.draw_surface_length + self.tool_menu_length // 2, Config.PIXEL_LENGTH))

        # blit actual width info
        if self.actual_color == Colors.BLACK:
            color = Colors.WHITE
        else:
            color = Colors.BLACK

        text_rendering('W: ' + str(self.actual_drawing_width), color, self.actual_color, (
            self.draw_surface_length + self.tool_menu_length * 3 // 4 + self.tool_menu_length // 16,
            Config.PIXEL_LENGTH * 3))

        # shapes
        text_rendering('Choose shape', Colors.BLACK, Colors.LIGHT_GRAY,
                       (self.draw_surface_length + self.tool_menu_length // 2, self.tool_menu_height // 10 * 2))


def text_rendering(text, front_color, back_color, textRect_center):
    text = font.render(text, True, front_color, back_color)
    textRect = text.get_rect()
    textRect.center = textRect_center
    WIN.blit(text, textRect)
