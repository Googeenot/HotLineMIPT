import pygame

import config as c
from GameObject import GameObject


class Poligon(GameObject):
    def __init__(self, x, y, w, h, color, offset):
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.offset = offset
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def handle(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = not self.moving_left
        elif key ==pygame.K_RIGHT:
            self.moving_right = not self.moving_right
        elif key == pygame.K_UP:
            self.moving_up = not self.moving_up
        elif key == pygame.K_DOWN:
            self.moving_down = not self.moving_down
    def update(self):
        dx =0
        dy =0
        if self.moving_left:
            dx = -1
        elif self.moving_right:
            dx = 1

        if self.moving_up:
            dy = -1
        elif self.moving_down:
            dy = 1
        if not dx and not dy:
            return
        h = dx
        dx  /= (1 / c.v) * (dx ** 2 + dy ** 2) ** 0.5
        dy  /= (1 / c.v) * (h ** 2 + dy ** 2) ** 0.5


        self.move(dx, dy)
