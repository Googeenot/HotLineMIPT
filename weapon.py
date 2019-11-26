import pygame
import GameObject
from random import choice, randrange as rnd

class Pen(GameObject):
    def __init__(self, x, y, w, h, vel):
        GameObject.__init__(x, y, w, h)
        self.color = choice('black', 'red')
        self.r = (w ** 2 + h ** 2) ** 0.5
        self.velocity = vel
        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def update(self):
        self.move()

    def hit_test(self, obj):
        if abs(obj.x - self.x) <= (self.r + obj.r) and abs(obj.y - self.y) <= (self.r + obj.r):
            return True
        else:
            return False

    def initialization_of_attack(self, event):
        if event.button == 1:
            r = event.pos
            dx = r[0] - self.x
            dy = r[1] - self.y
            movement_vector = (dx, dy)
            return movement_vector
        else:
            pass

    def strike(self, event):
        mv = self.initialization_of_attack(event)

        #self.move(mv[0], mv[1])
