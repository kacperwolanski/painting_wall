import pygame
import Config
import Colors

WIN = pygame.display.set_mode((Config.SCREEN_LENGTH, Config.SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()

'''
class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = Config.SCREEN_LENGTH
        self.height = Config.SCREEN_HEIGHT
        self.rect = pygame.Rect(x, y, self.length, self.height)

'''


class Screen:
    def __init__(self):
        pass

    def draw_the_window(self):
        WIN.fill(Colors.WHITE)
        self.generate_pixels()
        pygame.display.update()

    def generate_pixels(self):
        offset_x = 0
        offset_y = 0

        for x in range(Config.WINDOW_LENGTH):
            for y in range(Config.WINDOW_HEIGHT):
                pygame.draw.rect(WIN, Colors.BLACK,
                                 pygame.Rect(offset_x, offset_y, Config.PIXEL_LENGTH, Config.PIXEL_HEIGHT), 1)

                offset_y += Config.PIXEL_HEIGHT - 1

            offset_x += Config.PIXEL_LENGTH - 1
            offset_y = 0


        #generate drawing space
        pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                         pygame.Rect(0, 0, Config.WINDOW_LENGTH * (Config.PIXEL_LENGTH - 1), Config.WINDOW_HEIGHT * (Config.PIXEL_HEIGHT - 1)), Config.PIXEL_LENGTH)

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
