import pygame
import Config
import Colors
import Screen
import main

WIN = main.WIN
palette_height = 1


def draw_frames(draw_surface_length, draw_surface_height, tool_menu_length, tool_menu_height, actual_color,
                x_amount_of_shapes, shapes, images, shapes_to_draw):
    # draw images
    for image in images:
        WIN.blit(image[0], image[1])

    # draw shapes
    for key in shapes_to_draw:
        if shapes_to_draw[key][0]:

            x = shapes_to_draw[key][0][0]
            y = shapes_to_draw[key][0][1]
            size = shapes_to_draw[key][1]
            width = shapes_to_draw[key][2]
            color = shapes_to_draw[key][3]
            key = key[:key.index(" ")]
            if key == "Rectangle":

                pygame.draw.rect(main.WIN, color,
                                 pygame.Rect(x, y, size * 20, size * 10), width * 2)

            elif key == "Circle":
                pygame.draw.circle(main.WIN, color, (x, y), 10 * size, width)
            elif key == "Square":
                pygame.draw.rect(main.WIN, color, pygame.Rect(x, y, size * 10, size * 10), width)
            elif key == "Polygon":
                pygame.draw.polygon(main.WIN, color,
                                    [(x, y), (x, y + size), (x + size, y + size), (x + 2 * size, y + size)])
            elif key == "Triangle":
                pygame.draw.polygon(main.WIN, color,
                                    [(x, y), (x, y + 10 * size), (x + 10 * size, y + 10 * size), ], width)
            elif key == "Line":
                pass

    # draw limiting white rects
    pygame.draw.rect(WIN, Colors.BACKGROUND,
                     pygame.Rect(Config.DRAW_SURFACE_LENGTH, 0, Config.TOOL_MENU_LENGTH, Config.DRAW_SURFACE_HEIGHT))
    pygame.draw.rect(WIN, Colors.BACKGROUND, pygame.Rect(0, Config.DRAW_SURFACE_HEIGHT, Config.SCREEN_LENGTH,
                                                         Config.SCREEN_HEIGHT - Config.DRAW_SURFACE_HEIGHT))

    # draw surface
    pygame.draw.rect(WIN, Colors.FRAMES,
                     pygame.Rect(0, 0, draw_surface_length, draw_surface_height), Config.PIXEL_LENGTH)
    # main menu
    pygame.draw.rect(WIN, Colors.FRAMES,
                     pygame.Rect(draw_surface_length, 0, tool_menu_length, tool_menu_height),
                     Config.PIXEL_LENGTH)

    # draw width adjusting frame
    pygame.draw.rect(WIN, Colors.FRAMES,
                     pygame.Rect(
                         draw_surface_length + tool_menu_length * 3 // 4 - Config.PIXEL_LENGTH,
                         Config.PIXEL_LENGTH,
                         tool_menu_length // 8 + 2 * Config.PIXEL_LENGTH, Config.PIXEL_LENGTH * 5),
                     Config.PIXEL_LENGTH)

    pygame.draw.rect(WIN, actual_color,
                     pygame.Rect(draw_surface_length + tool_menu_length * 3 // 4, Config.PIXEL_LENGTH,
                                 tool_menu_length // 8, Config.PIXEL_LENGTH * 5))

    # draw palette surface

    pygame.draw.rect(WIN, Colors.FRAMES,
                     pygame.Rect(draw_surface_length, Config.PIXEL_LENGTH * 6, tool_menu_length,
                                 tool_menu_height // 10),
                     Config.PIXEL_LENGTH)

    # drawing shape choosing
    x_offset = draw_surface_length
    y_offset = tool_menu_height // 10 * 2
    shape_index = 0

    # draw shapes frame
    pygame.draw.rect(WIN, Colors.FRAMES,
                     pygame.Rect(
                         draw_surface_length, tool_menu_height // 10 * 2, tool_menu_length,
                                              tool_menu_height // 3 + Config.PIXEL_LENGTH),
                     Config.PIXEL_LENGTH)

    # draw shapes grid
    grid_length = tool_menu_length // x_amount_of_shapes
    grid_height = tool_menu_height // (2 * x_amount_of_shapes)

    for x in range(x_amount_of_shapes):
        for y in range(len(shapes) // x_amount_of_shapes):

            pygame.draw.rect(WIN, Colors.FRAMES,
                             pygame.Rect(
                                 x_offset, y_offset, tool_menu_length // x_amount_of_shapes,
                                                     tool_menu_height // (2 * x_amount_of_shapes)),
                             Config.PIXEL_LENGTH)

            if len(shapes[list(shapes.keys())[shape_index]]) == 0:
                shapes[list(shapes.keys())[shape_index]] = [x_offset, y_offset]

            shape_index += 1

            y_offset += grid_height
        y_offset = tool_menu_height // 10 * 2
        x_offset += grid_length


def draw_color_palette(tool_menu_length, tool_menu_height, draw_surface_length, color_choose, samples, palette_height):
    # draw color samples

    sample_length = (tool_menu_height // 10 - Config.PIXEL_LENGTH) // 3

    x_pos = draw_surface_length + Config.PIXEL_LENGTH
    y_pos = Config.PIXEL_LENGTH * 7
    index = 0

    if len(Colors.COLORS) / (tool_menu_length // sample_length) > palette_height:
        palette_height += 1

    for i in range(palette_height):
        for j in range(tool_menu_length // sample_length):

            sample = pygame.Rect(x_pos, y_pos, sample_length, sample_length)

            if index < len(Colors.COLORS):
                color = Colors.COLORS[index]
            else:
                break

            samples.append([sample, color])

            pygame.draw.rect(WIN, color, sample)

            # grid
            pygame.draw.rect(WIN, Colors.FRAMES, pygame.Rect(x_pos, y_pos, sample_length, sample_length), 1)

            x_pos += sample_length
            index += 1
        y_pos += sample_length
        x_pos = draw_surface_length + Config.PIXEL_LENGTH

        # color choosing

    if color_choose != -1:
        pygame.draw.rect(WIN, Colors.BLACK, samples[color_choose][0], 4)

    return samples
