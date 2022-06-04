import pygame
import Config
import Colors

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

    def generate_tool_menu(self):

        pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                         pygame.Rect(0, 0, self.draw_surface_length, self.draw_surface_height), Config.PIXEL_LENGTH)

        pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                         pygame.Rect(self.draw_surface_length, 0, self.tool_menu_length, self.tool_menu_height),
                         Config.PIXEL_LENGTH)

    def draw_the_drawing(self):
        for i in self.pixels:
            pygame.draw.rect(WIN, i.color, i)


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
                for pixel in self.screen.pixels:
                    if pixel.rect.collidepoint(pygame.mouse.get_pos()):
                        pixel.color = Colors.BLUE


def main():
    Paint()


if __name__ == "__main__":
    main()
