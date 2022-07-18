import pygame

import Colors
import Config
import Screen
import main

average_letter_len_in_pixels = 5


class Text:
    def __init__(self, text, text_point, font_type, font_color, text_background_color, size):
        self.text = text
        self.text_point = text_point

        self.font_type = font_type
        self.font_color = font_color
        self.text_background_color = text_background_color
        self.size = size

    def pop_text(self):
        text_rendering(self.text, self.font_color, self.text_background_color, self.text_point,
                       pygame.font.Font(self.font_type, self.size))

filling_background_help_text = "To fill background with color:                               1. Click 'Fill background' button                                 2. Choose color you want to fill the background       from color palette                                                3. Click 'Ok' to fill background or 'Cancel' to close"
adding_image_help_text = "Waring: Before adding new image you have to put it in 'images' directory  1. Click 'Add image' button.  2. Select point on the screen where your image will be added.  3.Click 'Ok' to confirm point or 'Cancel' to choose another one. 4. Click ' Browse' to choose image you want to add  5. Directory with available images will appear "
adding_new_color_help_text = "1. Click 'Add color' button  2. Click 'press to add color in RGB' and write three RGB values   3. Remember that correct values for color in RGB is a number between 0 and 255   4. You can always click 'clear' to delete entered value and then try with another one   5. Add new color to color palette by clicking 'Add' "
adding_shape_help_text =""
adding_text_help_text = "1. Click 'Add text' to add text field  2. Select point on the screen where your text will be added. 3. There will appear window with four options to change font type, font size, color of your text and to enter text in point you selected earlier 4. To change color, firstly select color in color palette and then click corresponding button to change color of font or text background"
resetting_help_text = ""
save_open_help_text = ""


def long_text_rendering(text, front_color, back_color, textRect_center, font, text_space_len):
    x_pos = textRect_center[0]
    y_pos = textRect_center[1]
    offset = 0
    letters_per_row = text_space_len // 5
    text_rows = len(text) * average_letter_len_in_pixels // text_space_len
    for row in range(text_rows):
        offset+=2*Config.FONT_SIZE
        print(text[row * letters_per_row: (row + 1) * letters_per_row])
        text_rendering(text[row * letters_per_row: (row + 1) * letters_per_row], front_color, back_color,
                       (x_pos,y_pos+offset), font)


def text_rendering(text, front_color, back_color, textRect_center, font):
    text = font.render(text, True, front_color, back_color)
    textRect = text.get_rect()
    textRect.center = textRect_center

    main.WIN.blit(text, textRect)
