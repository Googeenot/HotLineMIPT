import pygame

import config as c
from GameObject import GameObject


class Poligon(GameObject):
    def __init__(self, x, y, w, h, color, offset):
        GameObject.__init__(self, x, y, w, h)
        self.x = x
        self.y = y
        self.color = color
        self.offset = offset
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.live = 1
        self.map_x = 0
        self.map_y = -370
        self.dx = 0
        self.dy = 0

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
        if self.live:
            self.dx = 0
            self.dy = 0
            if self.moving_left:
                self.dx = -1
            elif self.moving_right:
                self.dx = 1
            if self.moving_up:
                self.dy = -1
            elif self.moving_down:
                self.dy = 1
            if not self.dx and not self.dy:
                return
            h = self.dx
            self.dx  /= (1 / c.v) * (self.dx ** 2 + self.dy ** 2) ** 0.5
            self.dy  /= (1 / c.v) * (h ** 2 + self.dy ** 2) ** 0.5
            self.move(0, 0)
            self.map_x -= self.dx
            self.map_y -= self.dy
        else:
            pass

    def attack_check(self, weap, rival):
        if weap.mouse_button_pressed:
            if pygame.Rect.colliderect(weap, rival):
                rival.live = 0
            else:
                pass
        else:
            pass
