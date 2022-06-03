import pygame
import Config
import Colors

WIN = pygame.display.set_mode((Config.SCREEN_LENGTH, Config.SCREEN_HEIGHT ))
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
        pixels_x_amount = Config.SCREEN_LENGTH // Config.PIXEL_LENGTH
        pixels_y_amount = Config.SCREEN_HEIGHT // Config.PIXEL_HEIGHT

        print(pixels_x_amount,pixels_y_amount)
        offset_x = 0
        offset_y = 0

        filler_x = 0
        filler_y = 0


        for x in range(pixels_x_amount):
            for y in range(pixels_y_amount):
                pygame.draw.rect(WIN,Colors.BLACK,pygame.Rect(offset_x, offset_y, Config.PIXEL_LENGTH, Config.PIXEL_HEIGHT),1)

                offset_y += Config.PIXEL_HEIGHT -1
                filler_y += 1

                if filler_y == Config.PIXEL_HEIGHT -1:
                    print(y)
                    y-=1
                    print(y)
                    filler_y = 0

            offset_x += Config.PIXEL_LENGTH-1
            filler_x +=1
            offset_y = 0

            if filler_x == Config.PIXEL_LENGTH -1:
                x-=1
                filler_x = 0





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
