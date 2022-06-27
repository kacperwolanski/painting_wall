import pygame
import Config
import Screen
import Buttom

WIN = pygame.display.set_mode((Config.SCREEN_LENGTH, Config.SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
pygame.display.set_caption('Painting wall')

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 10)


class Paint:

    def __init__(self):
        self.run = True
        self.screen = Screen.Screen()

    def main_loop(self):

        while self.run:
            CLOCK.tick(Config.FPS)
            self.check_events()
            self.screen.draw_the_window()

    def check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.run = False

            for s in self.screen.samples:
                if s[0].collidepoint(pygame.mouse.get_pos()):
                    self.screen.color_choose = self.screen.samples.index(s)

                    if pygame.mouse.get_pressed()[0]:
                        self.screen.actual_color = s[1]


def main():
    paint = Paint()

    paint.main_loop()


if __name__ == "__main__":
    main()
