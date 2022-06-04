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

    def draw_the_window(self):
        WIN.fill(Colors.WHITE)
        self.generate_pixels()
        self.generate_tool_menu()
        pygame.display.update()

    def generate_pixels(self):
        offset_x = 0
        offset_y = 0

        for x in range(Config.WINDOW_LENGTH):
            for y in range(Config.WINDOW_HEIGHT):
                pixel = Pixel(offset_x, offset_y, Colors.RED)

                pygame.draw.rect(WIN, pixel.color, pixel, 1)

                offset_y += Config.PIXEL_HEIGHT - 1

            offset_x += Config.PIXEL_LENGTH - 1
            offset_y = 0

        # generate drawing space
        pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                         pygame.Rect(0, 0, self.draw_surface_length, self.draw_surface_height), Config.PIXEL_LENGTH)

    def generate_tool_menu(self):
        pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                         pygame.Rect(self.draw_surface_length, 0, self.tool_menu_length, self.tool_menu_height),
                         Config.PIXEL_LENGTH)



    def find_pixel_color(self):
        pass
class Paint:
    def __init__(self):
        self.run = True
        self.screen = Screen()
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


def main():
    Paint()


if __name__ == "__main__":
    main()
