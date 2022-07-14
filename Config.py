# pixels
import pygame

import Colors

pygame.font.init()


PIXEL_LENGTH = 4
PIXEL_HEIGHT = 4

WINDOW_LENGTH = 350
WINDOW_HEIGHT = 220

# screen
SCREEN_LENGTH = WINDOW_LENGTH * PIXEL_LENGTH
SCREEN_HEIGHT = WINDOW_HEIGHT * PIXEL_HEIGHT

FPS = 144

FONT_SIZE = 10

FONT_TYPE = 'freesansbold.ttf'
TYPING_COLOR = Colors.BLACK
BACKGROUND_TYPING_COLOR = Colors.WHITE


BASIC_FONT = pygame.font.Font('freesansbold.ttf',10)

TYPING_FONT = pygame.font.Font(FONT_TYPE,FONT_SIZE)
palette_height = 1
start_menu = False
run = True