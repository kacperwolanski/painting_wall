import pygame
import Config
import Colors
import main
import Pixel
import Slider


WIN = main.WIN
Paint = main.Paint

font = main.font

class Screen:
    def __init__(self):

        self.draw_surface_length = Config.WINDOW_LENGTH * (Config.PIXEL_LENGTH - 1)
        self.draw_surface_height = Config.WINDOW_HEIGHT * (Config.PIXEL_HEIGHT - 1) + 1
        self.tool_menu_length = Config.SCREEN_LENGTH - self.draw_surface_length
        self.tool_menu_height = self.draw_surface_height
        self.pixels = []
        self.mouse_down = False
        # color staff
        self.actual_color = Colors.BLACK
        self.samples = []
        self.color_choose = -1
        self.actual_drawing_width = 1

        # tool staff
        self.sliders = []

    def check_if_mouse_is_down(self,drawing):
        self.mouse_down = drawing

    def generate_tools(self):
        self.generate_pixels()

        # generate width slider
        self.generate_sliders(WIN, self.draw_surface_length + self.tool_menu_length // 4,
                              Config.PIXEL_LENGTH * 2,
                              self.tool_menu_length // 2, Config.PIXEL_LENGTH * 5,
                              Colors.LIGHT_GRAY, self.actual_color, 'actual_drawing_width')

    def draw_the_window(self):

        WIN.fill(Colors.WHITE)
        self.draw_the_drawing()

        self.draw_color_palette()
        self.draw_the_sliders()
        self.draw_frames()
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

        if self.mouse_down:
            for pixel in range(len(self.pixels)):
                if self.pixels[pixel].rect.collidepoint(pygame.mouse.get_pos()):
                    for w_x in range(self.actual_drawing_width):
                        for w_y in range(self.actual_drawing_width):
                            if pixel + w_x * Config.WINDOW_HEIGHT + w_y < len(self.pixels):
                                self.pixels[pixel + w_x * Config.WINDOW_HEIGHT + w_y].color = self.actual_color

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

    def draw_color_palette(self):

        palette_height = self.tool_menu_height // 10
        palettle_length = self.tool_menu_length
        # draw palette surface
        pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                         pygame.Rect(self.draw_surface_length, Config.PIXEL_LENGTH * 6, palettle_length,
                                     palette_height),
                         Config.PIXEL_LENGTH)
        # draw color samples

        sample_length = (palette_height - Config.PIXEL_LENGTH) // 3

        x_pos = self.draw_surface_length + Config.PIXEL_LENGTH
        y_pos = Config.PIXEL_LENGTH * 7
        index = 0
        for i in range(3):
            for j in range(palettle_length // sample_length):

                sample = pygame.Rect(x_pos, y_pos, sample_length, sample_length)

                if index < len(Colors.COLORS):
                    color = Colors.COLORS[index]
                else:
                    color = Colors.WHITE

                self.samples.append([sample, color])

                pygame.draw.rect(WIN, color, sample)

                # grid
                pygame.draw.rect(WIN, Colors.LIGHT_GRAY, pygame.Rect(x_pos, y_pos, sample_length, sample_length), 1)

                x_pos += sample_length
                index += 1
            y_pos += sample_length
            x_pos = self.draw_surface_length + Config.PIXEL_LENGTH

            if self.color_choose != -1:
                pygame.draw.rect(WIN, Colors.BLACK, self.samples[self.color_choose][0], 4)

    def draw_the_sliders(self):

        for slider in self.sliders:
            slider[0].draw_the_slider(self.mouse_down)

            if slider[1] == 'actual_drawing_width':
                self.actual_drawing_width = slider[0].return_val()

    def generate_sliders(self, WIN, x, y, length, height, frame_color, buttom_color, variable):

        # generate slider
        slider = Slider.Slider(WIN, x, y, length, height, frame_color, buttom_color)

        self.sliders.append([slider, variable])

    def text_rendering(self, text, front_color, back_color, textRect_center):
        text = font.render(text, True, front_color, back_color)
        textRect = text.get_rect()
        textRect.center = textRect_center
        WIN.blit(text, textRect)

    def blit_text(self):
        # width adjusting
        # text "Adjust drawing width" render staff
        self.text_rendering('Adjust drawing width', Colors.BLACK, Colors.LIGHT_GRAY,
                            (self.draw_surface_length + self.tool_menu_length // 2, Config.PIXEL_LENGTH))

        # blit actual width info
        if self.actual_color == Colors.BLACK:
            color = Colors.WHITE
        else:
            color = Colors.BLACK

        self.text_rendering('W: ' + str(self.actual_drawing_width), color, self.actual_color, (
            self.draw_surface_length + self.tool_menu_length * 3 // 4 + self.tool_menu_length // 16,
            Config.PIXEL_LENGTH * 3))

