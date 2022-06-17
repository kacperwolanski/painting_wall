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
    drawing = False

    def __init__(self):
        self.run = True
        self.screen = Screen.Screen()

    def main_loop(self):
        self.screen.generate_tools()
        while self.run:
            self.screen.check_if_mouse_is_down(Paint.drawing)
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

    paint = Paint()

    paint.main_loop()


if __name__ == "__main__":
    main()
