import pygame.image
import os

images_to_draw = {}

start_menu_image = pygame.image.load("start_menu.png")

for filename in os.listdir('images'):
    path = 'images/' + filename
    image = pygame.image.load(path)
    images_to_draw.update({filename: [image,()]})
print(images_to_draw)