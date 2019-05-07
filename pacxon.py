import tilemap
import moving_objects
import pygame


clock = pygame.time.Clock()
done = False

pygame.init()
tilemap.init("default_tilemap.txt")

dot = moving_objects.MovingObject()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            (x, y) = pygame.mouse.get_pos()
            tilemap.tile_map[tilemap.col_num(y)][tilemap.row_num(x)] = -1

    tilemap.draw()

    dot.action()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
