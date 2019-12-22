import pygame
import tilemap


class MovingObject():
    def __init__(self):
        self.width = tilemap.tile_size
        self.height = tilemap.tile_size
        self.img = pygame.image.load('images/yellow_dot.png')
        self.img_width, self.img_height = self.img.get_rect().size
        self.x = tilemap.tile_size * 17
        self.y = tilemap.tile_size * 17
        self.x_vec = 0
        self.y_vec = 0
        self.speed = 4
        self.marked_tiles = []

    def draw(self):
        img_x = self.x + (tilemap.tile_size - self.img_width) / 2
        img_y = self.y + (tilemap.tile_size - self.img_height) / 2
        tilemap.screen.blit(self.img, (img_x, img_y))

    def move(self):
        # check_move() is used only if object is in the middle of a tile
        if self.x % tilemap.tile_size == 0 and self.y % tilemap.tile_size == 0:
            self.check_move()
        self.x += self.speed * self.x_vec
        self.y += self.speed * self.y_vec

    def check_move(self):
        x_ind = tilemap.row_num(self.x + self.width / 2)
        y_ind = tilemap.col_num(self.y + self.height / 2)

        key = pygame.key.get_pressed()

        # pacman can stop only if is on occupied tile
        if tilemap.tile_map[y_ind][x_ind]:
            direction = (0, 0)
        else:
            direction = (self.x_vec, self.y_vec)

        if key[pygame.K_RIGHT]:
            direction = (1, 0)
        elif key[pygame.K_LEFT]:
            direction = (-1, 0)
        elif key[pygame.K_DOWN]:
            direction = (0, 1)
        elif key[pygame.K_UP]:
            direction = (0, -1)

        (self.x_vec, self.y_vec) = direction

        # ensures, that character stays inside the map
        if tilemap.tile_map[y_ind][x_ind] == 2:
            if y_ind == 0:
                self.y_vec = max(0, self.y_vec)
            elif y_ind == tilemap.height - 1:
                self.y_vec = min(0, self.y_vec)
            if x_ind == 0:
                self.x_vec = max(0, self.x_vec)
            elif x_ind == tilemap.width - 1:
                self.x_vec = min(0, self.x_vec)

    # jedna z opcji zaznaczania śladu pacmana
        self.mark_tile(x_ind, y_ind)


    def mark_tile(self, x_ind, y_ind):
        if tilemap.tile_map[y_ind][x_ind] == 0:
            tilemap.tile_map[y_ind][x_ind] = 3
            self.marked_tiles.append((x_ind, y_ind))
        elif self.marked_tiles:
            tilemap.mark_area()
            while self.marked_tiles:
                for x, y in self.marked_tiles:
                    if tilemap.tile_map[y][x] == 3:  # ten if wyleci - uderzenie duszka ma zabić pacmana
                        tilemap.tile_map[y][x] = 1
                    self.marked_tiles.remove((x, y))


    def action(self):
        self.move()
        self.draw()
