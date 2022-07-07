import pygame
import Config
import Colors
import main
WIN=main.WIN

class Slider:
    def __init__(self, x, y, length, height, frame_color, buttom_color):

        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.frame_color = frame_color
        self.buttom_color = buttom_color
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)
        self.buttom_x = self.x
        self.scalling = 1

    def draw_the_slider(self):

        # draw the frame
        pygame.draw.rect(WIN, self.frame_color,
                         pygame.Rect(self.x, self.y, self.length, self.height), Config.PIXEL_LENGTH)

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                if pygame.mouse.get_pos()[0] > self.x:
                    self.buttom_x = pygame.mouse.get_pos()[0]
                    if pygame.mouse.get_pos()[0] + 3 * Config.PIXEL_LENGTH > self.x + self.length:
                        self.buttom_x = self.x + self.length - 3 * Config.PIXEL_LENGTH
                if self.buttom_x != self.x:
                    self.scalling = int(((self.buttom_x - self.x) / self.length) * 50)

        # draw the buttom
        pygame.draw.rect(WIN, self.buttom_color,
                         pygame.Rect(self.buttom_x, self.y, Config.PIXEL_LENGTH * 2, self.height))

    def return_val(self):
        return self.scalling


# generate sliders

def generate_sliders(draw_surface_length, tool_menu_length, actual_color):
    sliders = []
    # generate width slider
    width_slider = Slider(draw_surface_length + tool_menu_length // 4,
                                 Config.PIXEL_LENGTH * 2,
                                 tool_menu_length // 2, Config.PIXEL_LENGTH * 5,
                                 Colors.LIGHT_GRAY, actual_color)

    sliders.append([width_slider, 'actual_drawing_width'])
    return sliders