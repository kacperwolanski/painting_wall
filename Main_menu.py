import pygame

import Colors

import Screen
import main
close = False

def draw_main_menu():
    Screen.WIN.fill(Colors.WHITE)
    pygame.draw.rect(Screen.WIN, Colors.LIGHT_GRAY,
                     pygame.Rect(0, 0, 300,300), 2)

    return 1