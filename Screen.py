import pygame
import Config
import Colors
import Option_Window
import main
import Pixel
import Slider
import math
import Buttom

WIN = main.WIN
Paint = main.Paint

font = main.font


class Screen:
    def __init__(self):

        self.draw_surface_length = Config.WINDOW_LENGTH * (Config.PIXEL_LENGTH - 1)
        self.draw_surface_height = Config.WINDOW_HEIGHT * (Config.PIXEL_HEIGHT - 1) + 1
        self.tool_menu_length = Config.SCREEN_LENGTH - self.draw_surface_length
        self.tool_menu_height = self.draw_surface_height
        self.palette_height = self.tool_menu_height // 10
        self.palettle_length = self.tool_menu_length
        self.pixels = []

        # color staff
        self.actual_color = Colors.BLACK
        self.samples = []
        self.color_choose = -1
        self.actual_drawing_width = 1

        # tool staff
        self.sliders = []
        self.buttoms = []
        self.info_windows = {}
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
        self.draw_the_drawing()
        self.draw_color_palette()
        self.draw_frames()
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

    def draw_the_drawing(self):

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

    def draw_frames(self):
        # draw surface
        pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                         pygame.Rect(0, 0, self.draw_surface_length, self.draw_surface_height), Config.PIXEL_LENGTH)
        # main menu
        pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                         pygame.Rect(self.draw_surface_length, 0, self.tool_menu_length, self.tool_menu_height),
                         Config.PIXEL_LENGTH)

        # draw width adjusting frame
        pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                         pygame.Rect(
                             self.draw_surface_length + self.tool_menu_length * 3 // 4 - Config.PIXEL_LENGTH,
                             Config.PIXEL_LENGTH,
                             self.tool_menu_length // 8 + 2 * Config.PIXEL_LENGTH, Config.PIXEL_LENGTH * 5),
                         Config.PIXEL_LENGTH)

        pygame.draw.rect(WIN, self.actual_color,
                         pygame.Rect(self.draw_surface_length + self.tool_menu_length * 3 // 4, Config.PIXEL_LENGTH,
                                     self.tool_menu_length // 8, Config.PIXEL_LENGTH * 5))

        # draw palette surface

        pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                         pygame.Rect(self.draw_surface_length, Config.PIXEL_LENGTH * 6, self.palettle_length,
                                     self.palette_height),
                         Config.PIXEL_LENGTH)

        # drawing shape choosing
        x_offset = self.draw_surface_length
        y_offset = self.palette_height * 2
        shape_index = 0

        # draw shapes frame
        pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                         pygame.Rect(
                             self.draw_surface_length, self.palette_height * 2, self.tool_menu_length,
                                                       self.tool_menu_height // 3 + Config.PIXEL_LENGTH),
                         Config.PIXEL_LENGTH)

        # draw shapes grid
        grid_length = self.tool_menu_length // self.x_amount_of_shapes
        grid_height = self.tool_menu_height // (2 * self.x_amount_of_shapes)

        for x in range(self.x_amount_of_shapes):
            for y in range(len(self.shapes) // self.x_amount_of_shapes):

                pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                                 pygame.Rect(
                                     x_offset, y_offset, self.tool_menu_length // self.x_amount_of_shapes,
                                                         self.tool_menu_height // (2 * self.x_amount_of_shapes)),
                                 Config.PIXEL_LENGTH)

                if len(self.shapes[list(self.shapes.keys())[shape_index]]) == 0:
                    self.shapes[list(self.shapes.keys())[shape_index]] = [x_offset, y_offset]

                shape_index += 1

                y_offset += grid_height
            y_offset = self.palette_height * 2
            x_offset += grid_length

    def draw_color_palette(self):
        # draw color samples

        sample_length = (self.palette_height - Config.PIXEL_LENGTH) // 3

        x_pos = self.draw_surface_length + Config.PIXEL_LENGTH
        y_pos = Config.PIXEL_LENGTH * 7
        index = 0
        for i in range(3):
            for j in range(self.palettle_length // sample_length):

                sample = pygame.Rect(x_pos, y_pos, sample_length, sample_length)

                if index < len(Colors.COLORS):
                    color = Colors.COLORS[index]
                else:
                    color = Colors.WHITE

                if len(self.samples) < len(Colors.COLORS) * 3:
                    self.samples.append([sample, color])

                pygame.draw.rect(WIN, color, sample)

                # grid
                pygame.draw.rect(WIN, Colors.LIGHT_GRAY, pygame.Rect(x_pos, y_pos, sample_length, sample_length), 1)

                x_pos += sample_length
                index += 1
            y_pos += sample_length
            x_pos = self.draw_surface_length + Config.PIXEL_LENGTH

            # color choosing
            if self.color_choose != -1:
                pygame.draw.rect(WIN, Colors.BLACK, self.samples[self.color_choose][0], 4)

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
                    Buttom.reset_buttom(self.pixels)
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


                elif buttom[1] == "Add color":
                    self.activate_window("Add color")

    def activate_window(self, name):
        for key in list(self.info_windows.keys()):
            if self.info_windows[key][1] == name:
                self.info_windows[key][0] = True

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
                                      self.palette_height + 7 * Config.PIXEL_LENGTH,
                                      2 * function_buttom_length, function_buttom_height, "Rubber", Colors.BLACK,
                                      Colors.LIGHT_GRAY,
                                      Colors.AQUA)

        self.buttoms.append([rubber_buttom, "Rubber"])

    def realize_info_windows(self):
        for key in list(self.info_windows.keys()):
            if self.info_windows[key][0] == True:
                key.pop_window()

    def generate_info_windows(self):
        # add color window
        add_color_window = Option_Window.Window(0, self.draw_surface_height, 400, 200, "Add color", 5)
        # add color window buttoms

        add_color_window.generate_buttoms(self.tool_menu_height,"HUJ", Colors.BLACK, Colors.LIGHT_GRAY, Colors.AQUA)

        self.info_windows.update({add_color_window: [False, "Add color"]})

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
                       (self.draw_surface_length + self.tool_menu_length // 2, self.palette_height * 2))


def text_rendering(text, front_color, back_color, textRect_center):
    text = font.render(text, True, front_color, back_color)
    textRect = text.get_rect()
    textRect.center = textRect_center
    WIN.blit(text, textRect)
