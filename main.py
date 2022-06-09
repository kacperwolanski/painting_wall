import pygame
import Config
import Colors
import random

import Slider

WIN = pygame.display.set_mode((Config.SCREEN_LENGTH, Config.SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
pygame.display.set_caption('Painting wall')

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 10)


class Pixel:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.length = Config.PIXEL_LENGTH
        self.height = Config.PIXEL_HEIGHT
        self.rect = pygame.Rect(x, y, self.length, self.height)




class Screen:
    def __init__(self):
        self.draw_surface_length = Config.WINDOW_LENGTH * (Config.PIXEL_LENGTH - 1)
        self.draw_surface_height = Config.WINDOW_HEIGHT * (Config.PIXEL_HEIGHT - 1) + 1
        self.tool_menu_length = Config.SCREEN_LENGTH - self.draw_surface_length
        self.tool_menu_height = self.draw_surface_height
        self.pixels = []
        self.generate_pixels()

        # color staff
        self.actual_color = Colors.BLACK
        self.samples = []
        self.color_choose = -1
        self.actual_drawing_width = 1
        self.seksik = 1
        self.width_adjust = True

    def draw_the_window(self):

        WIN.fill(Colors.WHITE)
        self.draw_the_drawing()
        self.generate_tool_menu()
        self.blit_text()
        pygame.display.update()

    def generate_pixels(self):

        offset_x = 0
        offset_y = 0

        for x in range(Config.WINDOW_LENGTH):
            for y in range(Config.WINDOW_HEIGHT):
                self.pixels.append(Pixel(offset_x, offset_y, Colors.WHITE))
                offset_y += Config.PIXEL_HEIGHT - 1

            offset_x += Config.PIXEL_LENGTH - 1
            offset_y = 0

    def draw_the_drawing(self):

        if Paint.drawing:
            for pixel in range(len(self.pixels)):
                if self.pixels[pixel].rect.collidepoint(pygame.mouse.get_pos()):
                    for w_x in range(self.actual_drawing_width):
                        for w_y in range(self.actual_drawing_width):
                            self.pixels[
                                pixel + w_x * Config.WINDOW_HEIGHT + w_y].color = self.actual_color

        for i in self.pixels:
            pygame.draw.rect(WIN, i.color, i)

    def generate_tool_menu(self):
        self.draw_frames()
        self.draw_Color_palette()

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

    def draw_Color_palette(self):

        palette_height = self.tool_menu_height // 10
        palettle_length = self.tool_menu_length

        # width adjusting
        if self.width_adjust:
            self.width_adjusting()


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

    def width_adjusting(self):

        # generate slider
        slider = Slider.Slider(WIN,self.draw_surface_length + self.tool_menu_length // 4, Config.PIXEL_LENGTH * 2,
                                self.tool_menu_length // 2, Config.PIXEL_LENGTH * 5,
                               Colors.LIGHT_GRAY, self.actual_color,Paint.drawing)

        self.actual_drawing_width = slider.return_val()





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


class Paint:
    drawing = False
    def __init__(self):

        self.run = True
        self.screen = Screen()
        self.main_loop()


    def main_loop(self):
        while self.run:
            CLOCK.tick(Config.FPS)
            self.check_events()
            self.screen.draw_the_window()


    def check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                Paint.drawing = True

            elif event.type == pygame.MOUSEBUTTONUP:
                Paint.drawing = False

            for s in self.screen.samples:
                if s[0].collidepoint(pygame.mouse.get_pos()):
                    self.screen.color_choose = self.screen.samples.index(s)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.screen.actual_color = s[1]


def main():
    Paint()


if __name__ == "__main__":
    main()
