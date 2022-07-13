import pygame
import Config
import Screen
import start_menu

WIN = pygame.display.set_mode((Config.SCREEN_LENGTH, Config.SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
pygame.display.set_caption('Painting wall')


class Paint:

    def __init__(self):
        self.screen = Screen.Screen()

    def main_loop(self):
        print(pygame.font.get_fonts())
        if Config.start_menu:
            start_menu.xxx()

        while Config.run:
            CLOCK.tick(Config.FPS)

            self.check_events()
            self.screen.draw_the_window()

    def check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Config.run = False

            for s in self.screen.samples:
                if s[0].collidepoint(pygame.mouse.get_pos()):
                    self.screen.color_choose = self.screen.samples.index(s)

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

                elif event.key == pygame.K_a:
                    self.screen.keyboard_input += "a"
                elif event.key == pygame.K_b:
                    self.screen.keyboard_input += "b"
                elif event.key == pygame.K_c:
                    self.screen.keyboard_input += "c"
                elif event.key == pygame.K_d:
                    self.screen.keyboard_input += "d"
                elif event.key == pygame.K_e:
                    self.screen.keyboard_input += "e"
                elif event.key == pygame.K_f:
                    self.screen.keyboard_input += "f"
                elif event.key == pygame.K_g:
                    self.screen.keyboard_input += "g"
                elif event.key == pygame.K_h:
                    self.screen.keyboard_input += "h"
                elif event.key == pygame.K_i:
                    self.screen.keyboard_input += "i"
                elif event.key == pygame.K_j:
                    self.screen.keyboard_input += "j"
                elif event.key == pygame.K_k:
                    self.screen.keyboard_input += "k"
                elif event.key == pygame.K_l:
                    self.screen.keyboard_input += "l"
                elif event.key == pygame.K_m:
                    self.screen.keyboard_input += "m"
                elif event.key == pygame.K_n:
                    self.screen.keyboard_input += "n"
                elif event.key == pygame.K_o:
                    self.screen.keyboard_input += "o"
                elif event.key == pygame.K_u:
                    self.screen.keyboard_input += "u"
                elif event.key == pygame.K_u:
                    self.screen.keyboard_input += "u"
                elif event.key == pygame.K_p:
                    self.screen.keyboard_input += "p"
                elif event.key == pygame.K_r:
                    self.screen.keyboard_input += "r"
                elif event.key == pygame.K_s:
                    self.screen.keyboard_input += "s"
                elif event.key == pygame.K_t:
                    self.screen.keyboard_input += "t"
                elif event.key == pygame.K_w:
                    self.screen.keyboard_input += "w"
                elif event.key == pygame.K_z:
                    self.screen.keyboard_input += "z"
                elif event.key == pygame.K_x:
                    self.screen.keyboard_input += "x"
                elif event.key == pygame.K_y:
                    self.screen.keyboard_input += "y"
                elif event.key == pygame.K_q:
                    self.screen.keyboard_input += "q"

                elif event.key == pygame.K_PERIOD:
                    self.screen.keyboard_input += "."

                elif event.key == pygame.K_COMMA:
                    self.screen.keyboard_input += ","

                elif event.key == pygame.K_SLASH:
                    self.screen.keyboard_input += "/"

                elif event.key == pygame.K_QUESTION:
                    self.screen.keyboard_input += "?"

                elif event.key == pygame.K_COLON:
                    self.screen.keyboard_input += ":"

                elif event.key == pygame.K_PLUS:
                    self.screen.keyboard_input += "+"

                elif event.key == pygame.K_LEFTPAREN:
                    self.screen.keyboard_input += "("

                elif event.key == pygame.K_RIGHTPAREN:
                    self.screen.keyboard_input += ")"

                elif event.key == pygame.K_EXCLAIM:
                    self.screen.keyboard_input += "!"

                elif event.key == pygame.K_HASH:
                    self.screen.keyboard_input += "#"

                elif event.key == pygame.K_EQUALS:
                    self.screen.keyboard_input += "="

                elif event.key == pygame.K_CAPSLOCK:
                    self.screen.keyboard_input += "caps"

                elif event.key == pygame.K_SPACE:
                    self.screen.keyboard_input += " "

                elif event.key == pygame.K_BACKSPACE:
                    self.screen.keyboard_input += "-"

                elif event.key == pygame.K_DOWN:
                    self.screen.keyboard_input += "down"

                elif event.key == pygame.K_UP:
                    self.screen.keyboard_input += "up"


def main():
    paint = Paint()

    paint.main_loop()


if __name__ == "__main__":
    main()
