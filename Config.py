# pixels
import pygame
import Colors

#screen staff
FPS = 144

PIXEL_LENGTH = 4
PIXEL_HEIGHT = 4

WINDOW_LENGTH = 350
WINDOW_HEIGHT = 220

palette_height = 1

# screen
SCREEN_LENGTH = WINDOW_LENGTH * PIXEL_LENGTH
SCREEN_HEIGHT = WINDOW_HEIGHT * PIXEL_HEIGHT

# text staff
pygame.font.init()
FONT_SIZE = 10
FONT_TYPE = 'fonts/freesansbold.ttf'
TYPING_COLOR = Colors.BLACK
BACKGROUND_TYPING_COLOR = Colors.WHITE
BASIC_FONT = pygame.font.Font('fonts/freesansbold.ttf', 10)


start_menu = False
run = True
