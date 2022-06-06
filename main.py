import pygame
import Config
import Colors
import random

WIN = pygame.display.set_mode((Config.SCREEN_LENGTH, Config.SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()


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
        self.samples = []
        self.color_choose = -1
        self.actual_drawing_width = 10

    def draw_the_window(self):
        WIN.fill(Colors.WHITE)
        self.draw_the_drawing()
        self.generate_tool_menu()
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

    def draw_Color_palette(self):

        palette_height = self.tool_menu_height // 10
        palettle_length = self.tool_menu_length

        # draw "colors" frame
        pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                         pygame.Rect(self.draw_surface_length + self.tool_menu_length // 4, Config.PIXEL_LENGTH * 2,
                                     self.tool_menu_length // 2, Config.PIXEL_LENGTH * 5),
                         Config.PIXEL_LENGTH)
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


class Paint:
    def __init__(self):
        self.run = True
        self.actual_color = Colors.BLACK

        self.screen = Screen()
        self.drawing = False

        self.main_loop()

    def main_loop(self):
        while self.run:
            CLOCK.tick(Config.FPS)
            self.screen.draw_the_window()
            self.check_events()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.drawing = True

            elif event.type == pygame.MOUSEBUTTONUP:
                self.drawing = False

            if self.drawing:
                for pixel in range(len(self.screen.pixels)):
                    if self.screen.pixels[pixel].rect.collidepoint(pygame.mouse.get_pos()):
                        for w in range(self.screen.actual_drawing_width):
                            if pixel+w < len(self.screen.pixels):
                                self.screen.pixels[pixel+w].color = self.actual_color
                                self.screen.pixels[pixel+w+Config.WINDOW_HEIGHT].color = self.actual_color

            for s in self.screen.samples:
                if s[0].collidepoint(pygame.mouse.get_pos()):
                    self.screen.color_choose = self.screen.samples.index(s)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.actual_color = s[1]


def main():
    Paint()


if __name__ == "__main__":
    main()
