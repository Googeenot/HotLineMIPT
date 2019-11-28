from random import choice
import pygame
import GameObject


class Human(GameObject):
    def __init__(self, x, y, w, h, vel = (0, 0)):
        GameObject.__init__(x, y, w, h)
        self.color = choice('orange', 'pink')
        self.velocity = vel
        self.x = x
        self.y = y
        self.dx = 1
        self.dy = 1

    def handle(self, key):
        if key == pygame.K_a:
            self.dx = - 1
            self.dy = 0
            self.move(self.dx, 0)
        elif key == pygame.K_d:
            self.dx = 1
            self.dy = 0
            self.move(self.dx, 0)
        elif key == pygame.K_w:
            self.dx = 0
            self.dy = - 1
            self.move(0, self.dy)
        elif key == pygame.K_s:
            self.dx = 0
            self.dy = 1
            self.move(0, self.dy)

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.bounds)
