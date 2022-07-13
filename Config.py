# pixels
import pygame

import Colors

PIXEL_LENGTH = 4
PIXEL_HEIGHT = 4

WINDOW_LENGTH = 350
WINDOW_HEIGHT = 220

# screen
SCREEN_LENGTH = WINDOW_LENGTH * PIXEL_LENGTH
SCREEN_HEIGHT = WINDOW_HEIGHT * PIXEL_HEIGHT

FPS = 144
pygame.font.init()
FONT_SIZE = 15
FONT_TYPE = 'freesansbold.ttf'
TYPING_COLOR = Colors.BLACK
BACKGROUND_TYPING_COLOR = Colors.WHITE
#verdana
#dejavusansmono
#dejavusans

BASIC_FONT = pygame.font.SysFont('freesansbold.ttf', 15)
TYPING_FONT = pygame.font.SysFont(FONT_TYPE,FONT_SIZE)
palette_height = 1
start_menu = False
run = True