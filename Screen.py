import pygame
import Config
import Colors
import Option_Window
import main
import Pixel
import Slider
import Button
import Drawing
import Text

WIN = main.WIN
Paint = main.Paint

basic_font = Config.BASIC_FONT


class Screen:
    def __init__(self):
        self.draw_surface_length = Config.WINDOW_LENGTH * (Config.PIXEL_LENGTH - 1)
        self.draw_surface_height = Config.WINDOW_HEIGHT * (Config.PIXEL_HEIGHT - 1) + 1
        self.tool_menu_length = Config.SCREEN_LENGTH - self.draw_surface_length
        self.tool_menu_height = self.draw_surface_height
        self.draw_surface = pygame.Rect(0, 0, self.draw_surface_length, self.draw_surface_height)
        self.pixels = []

        # color staff
        self.keyboard_input = ""
        self.palette_height = 1
        self.actual_color = Colors.BLACK
        self.samples = []
        self.color_choose = -1
        self.actual_drawing_width = 1

        # tool staff
        self.value = ()
        self.sliders = []
        self.buttons = []
        self.info_windows = {}
        self.info_windows_names = []
        self.append_tools = True
        self.rubber = False
        self.counter = 0
        self.actual_item = -1

        # text staff
        self.typing_text = ""
        self.texts = []
        self.text_point = ()
        self.capital = False
        self.cords = []

        # shapes staff
        self.x_amount_of_shapes = 3
        self.shapes = {'Rectangle': [], 'Circle': [], 'Ellipse': [], 'Line': [], 'Square': [], 'Triangle': []}

        # images staff
        self.images = []

    def generate_tools(self):
        if self.append_tools:
            self.generate_pixels()
            self.sliders = Slider.generate_sliders(self.draw_surface_length, self.tool_menu_length, self.actual_color)
            self.buttons = Button.generate_buttons(self.tool_menu_length, self.tool_menu_height,
                                                   self.draw_surface_length, self.draw_surface_height, self.shapes,
                                                   self.x_amount_of_shapes)
            self.info_windows = Option_Window.generate_info_windows(self.draw_surface_height, self.tool_menu_height)
            self.append_tools = False

    # drawing staff
    def draw_the_window(self):

        WIN.fill(Colors.WHITE)

        self.make_the_drawing()
        Drawing.draw_frames(self.draw_surface_length, self.draw_surface_height, self.tool_menu_length,
                            self.tool_menu_height, self.actual_color, self.x_amount_of_shapes, self.shapes, self.images)

        self.blit_text()
        self.realize_info_windows()
        self.samples = []

        self.samples = Drawing.draw_color_palette(self.tool_menu_length, self.tool_menu_height,
                                                  self.draw_surface_length, self.color_choose, self.samples,
                                                  Config.palette_height)
        self.realize_the_tools()
        self.generate_tools()

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

        # buttons
        for button in self.buttons:
            button[0].draw_the_button()
            if button[0].active_button:
                # Reset button
                if button[1] == "Reset":
                    Button.reset_button(self.pixels, Colors.WHITE)
                # save draw button

                elif button[1] == "Rubber":

                    if self.rubber:
                        self.rubber = False
                    else:
                        self.rubber = True
                        self.actual_color = Colors.WHITE

                elif button[1] == "Save_draw":
                    pass


                # open draw button
                elif button[1] == "Open_draw":
                    pass


                # shapes
                elif button[1] in self.shapes:
                    if button[1] == 'Rectangle':
                        pass

                elif button[1] == "Help":
                    self.activate_window("Help window")


                elif button[1] in self.info_windows_names:
                    if self.check_if_other_windows_work(button[1]):
                        self.activate_window(button[1])

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
                window.pop_window(self.draw_surface)

                # fill background
                if self.info_windows[window][1] == "Fill background":
                    pygame.draw.rect(WIN, self.actual_color,
                                     pygame.Rect(window.x + 50 + window.length / 2, window.y + window.height / 5,
                                                 15,
                                                 15))

                    if window.allow:
                        Button.reset_button(self.pixels, self.actual_color)
                        window.allow = False
                    elif window.refuse:
                        window.is_active = False
                        window.refuse = False

                # add color

                elif self.info_windows[window][1] == "Add color":

                    if window.color_adding:
                        if window.clear:
                            window.clear = False

                            self.keyboard_input = ""
                            self.value = ()

                        if len(self.keyboard_input) == 3:
                            self.value += (int(self.keyboard_input),)

                            self.keyboard_input = ""

                        if (len(self.value)) == 3:
                            window.text = "Add color       ?"

                            window.color_adding = False

                        if len(self.keyboard_input) != 0:

                            window.value = self.keyboard_input

                        else:
                            window.value = self.value

                    else:
                        self.keyboard_input = ""

                    if len(self.value) == 3:
                        if window.allow:

                            Colors.COLORS.append(self.value)
                            window.value = ""
                            self.value = ()
                            self.keyboard_input = ""
                            window.allow = False
                            window.text = "Add color by writing RGB values"
                            window.done = True

                        else:
                            pygame.draw.rect(WIN, self.value, pygame.Rect(215, 705, 15, 15))


                elif self.info_windows[window][1] == "Add text":
                    if self.actual_color == Colors.BLACK:
                        self.actual_color = Colors.WHITE
                    if window.chosen_point:
                        self.value = window.chosen_point
                        Text.text_rendering("text here", Colors.BLACK, Colors.GRAY, window.chosen_point, basic_font)

                    if window.allow:
                        window.is_active = False

                        self.typing_text = ""
                        self.text_point = self.value
                        self.actual_item += 1
                        new_text = Text.Text(self.typing_text, self.text_point, Config.FONT_TYPE,
                                             Config.TYPING_COLOR, Config.BACKGROUND_TYPING_COLOR, Config.FONT_SIZE)
                        if len(self.texts) == self.actual_item:
                            self.texts.append(new_text)

                        self.text_point = ()
                        window.chosen_point = ()
                        self.activate_window("Add text2")
                        window.allow = False

                    elif window.refuse:
                        window.chosen_point = ""
                        window.refuse = False
                        window.text = "Choose place for text"


                elif self.info_windows[window][1] == "Add text2":

                    if window.choosing_font_type:
                        self.activate_window("Choose font type")
                        window.choosing_font_type = False
                    elif window.choosing_font_size:
                        self.activate_window("Choose font size")
                        window.choosing_font_size = False
                    elif window.choosing_text_color:
                        self.activate_window("Choose text color")
                        window.choosing_text_color = False

                    elif window.typing_text:
                        actual_text = self.typing_text

                        self.cords = [int(self.value[0]) + 2.45 * len(self.typing_text), int(self.value[1]) - 10]
                        self.counter += 1

                        if self.keyboard_input == "caps" and not self.capital:
                            self.capital = True

                        elif self.keyboard_input == "caps" and self.capital:
                            self.capital = False

                        elif self.keyboard_input == "down":
                            lista = list(self.value)
                            lista[1] += 2 * Config.FONT_SIZE
                            self.value = tuple(lista)

                        elif self.keyboard_input == "up":
                            lista = list(self.value)
                            lista[1] -= 2 * Config.FONT_SIZE
                            self.value = tuple(lista)

                        elif self.keyboard_input == "-":
                            self.typing_text = self.typing_text[:-1]

                        elif self.keyboard_input != "caps" and self.keyboard_input != "ent":

                            if self.capital:
                                self.keyboard_input = self.keyboard_input.upper()
                            self.typing_text += self.keyboard_input

                        if self.counter % 28:
                            pygame.draw.line(WIN, Colors.BLACK, (self.cords[0], self.cords[1]),
                                             (self.cords[0], self.cords[1] + int(Config.FONT_SIZE)))

                        self.texts[self.actual_item].text = self.typing_text

                elif self.info_windows[window][1] == "Choose font type":
                    self.texts[self.actual_item].font_type = window.actual_font

                elif self.info_windows[window][1] == "Choose font size":
                    Config.FONT_SIZE = window.value
                    self.texts[self.actual_item].size = window.value
                    if window.allow:
                        window.value = ""
                        window.allow = False
                        window.is_active = False

                elif self.info_windows[window][1] == "Choose text color":
                    if window.choosing_font_color:
                        window.choosing_font_color = False
                        self.texts[self.actual_item].font_color = self.actual_color

                    if window.choosing_text_background_color:
                        window.choosing_text_background_color = False
                        self.texts[self.actual_item].text_background_color = self.actual_color

                    Text.text_rendering("Actual font color:", Colors.BLACK, Colors.LIGHT_GRAY,
                                        (800, self.tool_menu_height + 80), basic_font)

                    pygame.draw.rect(WIN, Config.TYPING_COLOR,
                                     pygame.Rect(750, self.tool_menu_height + 90, 100, 20))

                    Text.text_rendering("Actual background color:", Colors.BLACK, Colors.LIGHT_GRAY,
                                        (800, self.tool_menu_height + 160), basic_font)

                    pygame.draw.rect(WIN, Config.BACKGROUND_TYPING_COLOR,
                                     pygame.Rect(750, self.tool_menu_height + 170, 100, 20))

                elif self.info_windows[window][1] == "Select image point":
                    self.activate_window("Select image point")
                    if window.chosen_point:
                        if window.allow:
                            window.allow = False
                            self.value = window.chosen_point
                            window.chosen_point = ()
                            self.activate_window("Add image")

                elif self.info_windows[window][1] == "Add image":

                    if window.adding_images:
                        window.adding_images = False
                        self.activate_window("Select image")

                elif self.info_windows[window][1] == "Select image":
                    if window.image_to_add:
                        self.images.append([window.image_to_add, self.value])
                        window.image_to_add = ""

                elif self.info_windows[window][1] == "Help window":
                    if window.how_to:
                        self.activate_window(window.how_to)
                        Text.long_text_rendering(window.text, Colors.BLACK, Colors.LIGHT_GRAY,
                                                 (500, 700),
                                                 Config.BASIC_FONT, 150)

                        window.how_to = ""

                # reset values
                self.info_windows[window][0] = window.is_active
                self.keyboard_input = ""

    # text staff
    def blit_text(self):
        # width adjusting
        # text "Adjust drawing width" render staff
        Text.text_rendering('Adjust drawing width', Colors.BLACK, Colors.LIGHT_GRAY,
                            (self.draw_surface_length + self.tool_menu_length // 2, Config.PIXEL_LENGTH), basic_font)

        # blit actual width info
        if self.actual_color == Colors.BLACK:
            color = Colors.WHITE
        else:
            color = Colors.BLACK

        Text.text_rendering('W: ' + str(self.actual_drawing_width), color, self.actual_color, (
            self.draw_surface_length + self.tool_menu_length * 3 // 4 + self.tool_menu_length // 16,
            Config.PIXEL_LENGTH * 3), basic_font)

        # shapes
        Text.text_rendering('Choose shape', Colors.BLACK, Colors.LIGHT_GRAY,
                            (self.draw_surface_length + self.tool_menu_length // 2, self.tool_menu_height // 10 * 2),
                            basic_font)

        # adding text
        for text in self.texts:
            if text.text_point:
                text.pop_text()
