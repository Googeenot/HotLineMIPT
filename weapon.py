import pygame as pg



class Weapon():
    def __init__(self):
        self.r = None
        self.id = None
    def hold(self):
        pass


class Pen(Weapon):
    def __init__(self):
        self.r = None
        self.id = None

    def stab(self):
        self.move()
        self.hit()

    def move(self):
        pass

    def hit(self):
        pass


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