import random

import pygame
import Config
import Button
import Colors
import file_operations
import Option_Window
import Screen
import main


def xxx():
    x = 0
    y = 0
    i = 0
    j = 400
    buttons = []
    windows = {}
    windows_names = []

    np_button = Button.Button(Config.SCREEN_LENGTH // 2, Config.SCREEN_HEIGHT // 2, 100, 40, "New Project", Colors.PINK,
                              Colors.AZURE, Colors.RED)
    op_button = Button.Button(Config.SCREEN_LENGTH // 2, Config.SCREEN_HEIGHT // 2 + 50, 100, 40, "Open Project",
                              Colors.PINK, Colors.AZURE, Colors.RED)
    qt_button = Button.Button(Config.SCREEN_LENGTH // 2, Config.SCREEN_HEIGHT // 2 + 100, 100, 40, "Quit", Colors.PINK,
                              Colors.AZURE, Colors.RED)

    np_window = Option_Window.Window(Config.SCREEN_LENGTH // 2 + 200, Config.SCREEN_HEIGHT // 2, 200, 200,
                                     "Do you want to create new project?", 2)
    np_window.generate_buttons(Config.SCREEN_LENGTH // 2 + 200, Config.SCREEN_HEIGHT // 2, "Yes", Colors.PINK,
                               Colors.WHITE, Colors.RED, "Yes")
    np_window.generate_buttons(Config.SCREEN_LENGTH // 2 + 200, Config.SCREEN_HEIGHT // 2, "Cancel", Colors.PINK,
                               Colors.WHITE, Colors.RED,
                               "Cancel")

    qt_window = Option_Window.Window(Config.SCREEN_LENGTH // 2 + 200, Config.SCREEN_HEIGHT // 2, 200, 200,
                                     "Do you want to close Painting wall?", 2)
    qt_window.generate_buttons(Config.SCREEN_LENGTH // 2 + 200, Config.SCREEN_HEIGHT // 2, "Yes", Colors.PINK,
                               Colors.WHITE, Colors.RED,
                               "Yes")
    qt_window.generate_buttons(Config.SCREEN_LENGTH // 2 + 200, Config.SCREEN_HEIGHT // 2, "Cancel", Colors.PINK,
                               Colors.WHITE, Colors.RED,
                               "Cancel")

    buttons.append([np_button, "NP"])
    buttons.append([op_button, "OP"])
    buttons.append([qt_button, "QT"])

    windows.update({np_window: [False, "NP"]})
    windows_names.append("NP")

    windows.update({qt_window: [False, "QT"]})
    windows_names.append("QT")
    main.WIN.fill(Colors.WHITE)

    while Config.start_menu:

        main.CLOCK.tick(Config.FPS)
        main.WIN.blit(file_operations.start_menu_image, (8, 8))

        for window in windows.keys():
            if len(windows_names) < len(windows):
                windows_names.append(windows[window][1])

            if windows[window][0]:
                window.is_active = True

                window.pop_window(pygame.Rect(0, 0, Config.WINDOW_LENGTH * (Config.PIXEL_LENGTH - 1),
                                              Config.WINDOW_HEIGHT * (Config.PIXEL_HEIGHT - 1) + 1))

                if windows[window][1] == "NP":

                    if window.allow:
                        Config.start_menu = False
                        window.allow = False
                    elif window.refuse:
                        window.is_active = False
                        window.refuse = False

                if windows[window][1] == "QT":
                    if window.allow:
                        Config.start_menu = False
                        Config.run = False
                    elif window.refuse:
                        window.is_active = False
                        window.refuse = False

                windows[window][0] = window.is_active

            else:
                pass

        for button in buttons:

            button[0].draw_the_button()
            if button[0].active_button:
                if button[1] == "OP":
                    pass

                elif button[1] in windows_names:

                    windows = activate_window(button[1], windows)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Config.start_menu = False

        if y < Config.SCREEN_HEIGHT - 8 and y >= 0 and x == 0:
            y += 1



        elif x >= 0 and x < Config.SCREEN_LENGTH - 8 and y == Config.SCREEN_HEIGHT - 8:

            x += 1

        elif x == Config.SCREEN_LENGTH - 8 and y <= Config.SCREEN_HEIGHT - 8 and y > 0:
            y -= 1


        elif y == 0 and x > 0:
            x -= 1

        pygame.draw.rect(main.WIN, Colors.WHITE, pygame.Rect(x, y, 8, 8))

        if j < Config.SCREEN_HEIGHT - 8 and j >= 0 and i == 0:
            j += 1


        elif i >= 0 and i < Config.SCREEN_LENGTH - 8 and j == Config.SCREEN_HEIGHT - 8:

            i += 1

        elif i == Config.SCREEN_LENGTH - 8 and j <= Config.SCREEN_HEIGHT - 8 and j > 0:
            j -= 1


        elif j == 0 and i > 0:

            i -= 1
        pygame.draw.rect(main.WIN, Colors.PINK, pygame.Rect(i, j, 8, 8))

        pygame.display.update()


def activate_window(name, windows):
    for window in list(windows.keys()):
        if windows[window][1] == name:
            windows[window][0] = True

    return windows
