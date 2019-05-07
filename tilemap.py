import pygame
from scipy.ndimage import label
import numpy


textures = {
    -1: pygame.image.load('images/green_dot.png'),
    3: pygame.image.load('images/marked.png'),
    2: pygame.image.load('images/occ.png'),
    1: pygame.image.load('images/occ.png'),
    0: pygame.image.load('images/free.png')
}

tile_size = 24
tile_map = []
width = 0
height = 0
screen = None


def init(file):
    global tile_map, width, height, screen
    tile_map = [[int(n) for n in line.split()] for line in open(file, "r")]
    width = len(tile_map[0])
    height = len(tile_map)
    screen = pygame.display.set_mode((width * tile_size, height * tile_size))


def draw():
    global screen
    for row in range(height):
        for column in range(width):
            screen.blit(textures[tile_map[row][column]], (column * tile_size, row * tile_size))


def row_num(x):
    return int(x / tile_size)


def col_num(y):
    return int(y / tile_size)


def mark_area():
    s = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]

    a = numpy.array(tile_map)

    labeled_array, num_features = label(a <= 0, structure=s)

    if num_features == 1:
        return

    for i in range(1, num_features + 1):
        w = numpy.where(labeled_array == i)
        a = list(zip(*w))

        do = True

        for (x, y) in a:
            if tile_map[x][y] == -1:
                break
        else:
            for (x, y) in a:
                tile_map[x][y] = 1
