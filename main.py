import pygame
import Config
import Colors

WIN = pygame.display.set_mode((Config.SCREEN_HEIGHT, Config.SCREEN_LENGHT))
CLOCK = pygame.time.Clock()

class Screen:
    def __init__(self):
        self.height = Config.SCREEN_HEIGHT
        self.lenght = Config.SCREEN_LENGHT



class Paint:
    def __init__(self):
        self.run = True
        self.main_loop()


    def main_loop(self):
        while self.run:
            self.draw_the_window()
            self.check_events()


    def draw_the_window(self):
        WIN.fill(Colors.WHITE)
        pygame.display.update()







    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False






def main():
    Paint()



if __name__ == "__main__":
    main()