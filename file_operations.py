import pygame.image
import os

images_to_draw = {}

start_menu_image = pygame.image.load("images/start_menu.png")

for filename in os.listdir('images'):
    path = 'images/' + filename
    image = pygame.image.load(path)
    images_to_draw.update({filename: [image,()]})

def save_the_project(pixels):
    pass


def open_saved_project():
    pass