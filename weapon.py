import pygame
import GameObject
from random import choice, randrange as rnd



class Weapon():
    def __init__(self):
        self.r = None
        self.id = None
    def hold(self):
        pass


class Pen(GameObject):
    def __init__(self, x, y, w, h, vel):
        GameObject.__init__(self, x, y, w, h, vel)
        self.color = choice('black', 'red')
        self.velocity = rnd(1, 10)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def update(self):
        self.move(self.velocity)



class Hands(Weapon):
    def __init__(self):
        self.r = None
        self.id = None

    def punch(self):
        self.move()
        self.hit()

    def move(self):
        pass

    def hit(self):
        pass


class Knife(Weapon):
    def __init__(self):
        self.r = None
        self.id = None


class Baton(Weapon):
    pass


class Pistol(Weapon):
    pass


class Machine_gun(Weapon):
    pass


class Shot_gun(Weapon):
    pass


class Mop(Weapon):
    pass