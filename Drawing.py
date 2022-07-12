import pygame
import Config
import Colors
import Screen
import main

WIN = main.WIN
palette_height = 1


def draw_frames(draw_surface_length, draw_surface_height, tool_menu_length, tool_menu_height, actual_color,
                x_amount_of_shapes, shapes):
    # draw surface
    pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                     pygame.Rect(0, 0, draw_surface_length, draw_surface_height), Config.PIXEL_LENGTH)
    # main menu
    pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                     pygame.Rect(draw_surface_length, 0, tool_menu_length, tool_menu_height),
                     Config.PIXEL_LENGTH)

    # draw width adjusting frame
    pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                     pygame.Rect(
                         draw_surface_length + tool_menu_length * 3 // 4 - Config.PIXEL_LENGTH,
                         Config.PIXEL_LENGTH,
                         tool_menu_length // 8 + 2 * Config.PIXEL_LENGTH, Config.PIXEL_LENGTH * 5),
                     Config.PIXEL_LENGTH)

    pygame.draw.rect(WIN, actual_color,
                     pygame.Rect(draw_surface_length + tool_menu_length * 3 // 4, Config.PIXEL_LENGTH,
                                 tool_menu_length // 8, Config.PIXEL_LENGTH * 5))

    # draw palette surface

    pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                     pygame.Rect(draw_surface_length, Config.PIXEL_LENGTH * 6, tool_menu_length,
                                 tool_menu_height // 10),
                     Config.PIXEL_LENGTH)

    # drawing shape choosing
    x_offset = draw_surface_length
    y_offset = tool_menu_height // 10 * 2
    shape_index = 0

    # draw shapes frame
    pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
                     pygame.Rect(
                         draw_surface_length, tool_menu_height // 10 * 2, tool_menu_length,
                                              tool_menu_height // 3 + Config.PIXEL_LENGTH),
                     Config.PIXEL_LENGTH)

    # draw shapes grid
    grid_length = tool_menu_length // x_amount_of_shapes
    grid_height = tool_menu_height // (2 * x_amount_of_shapes)

    for x in range(x_amount_of_shapes):
        for y in range(len(shapes) // x_amount_of_shapes):

            pygame.draw.rect(WIN, Colors.LIGHT_GRAY,
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
            pygame.draw.rect(WIN, Colors.LIGHT_GRAY, pygame.Rect(x_pos, y_pos, sample_length, sample_length), 1)

            x_pos += sample_length
            index += 1
        y_pos += sample_length
        x_pos = draw_surface_length + Config.PIXEL_LENGTH

        # color choosing

    if color_choose != -1:
        pygame.draw.rect(WIN, Colors.BLACK, samples[color_choose][0], 4)


    return samples

