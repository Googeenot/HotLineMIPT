import pygame
import GameObject
from random import choice, randrange as rnd

class Pen(GameObject):
    def __init__(self, x, y, w, h, vel):
        GameObject.__init__(x, y, w, h)
        self.color = choice('black', 'red')
        self.r = (w ** 2 + h ** 2) ** 0.5
        self.velocity = vel

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def update(self):
        self.move()

    def hit_test(self, obj):
        if abs(obj.x - self.x) <= (self.r + obj.r) and abs(ob.y - self.y) <= (self.r + obj.r):
            return True
        else:
            return False

    def aiming(self):
        pass





























