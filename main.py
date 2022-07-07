import pygame
import Config
import Main_menu
import Screen
import Buttom

WIN = pygame.display.set_mode((Config.SCREEN_LENGTH, Config.SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
pygame.display.set_caption('Painting wall')

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 10)
main_menu = True


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
                    self.screen.rubber = False

                    if pygame.mouse.get_pressed()[0]:
                        self.screen.actual_color = s[1]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    self.screen.keyboard_input += "0"
                elif event.key == pygame.K_1:
                    self.screen.keyboard_input += "1"
                elif event.key == pygame.K_2:
                    self.screen.keyboard_input += "2"
                elif event.key == pygame.K_3:
                    self.screen.keyboard_input += "3"
                elif event.key == pygame.K_4:
                    self.screen.keyboard_input += "4"
                elif event.key == pygame.K_5:
                    self.screen.keyboard_input += "5"
                elif event.key == pygame.K_6:
                    self.screen.keyboard_input += "6"
                elif event.key == pygame.K_7:
                    self.screen.keyboard_input += "7"
                elif event.key == pygame.K_8:
                    self.screen.keyboard_input += "8"
                elif event.key == pygame.K_9:
                    self.screen.keyboard_input += "9"


def main():
    paint = Paint()

    paint.main_loop()


if __name__ == "__main__":
    main()
