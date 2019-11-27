from random import choice
import pygame
import GameObject


class Human(GameObject):
    def __init__(self, x, y, w, h, vel):
        GameObject.__init__(x, y, w, h)
        self.color = choice('orange', 'pink')
        self.velocity = vel
        self.x = x
        self.y = y

    def handle(self, key):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.bounds)
