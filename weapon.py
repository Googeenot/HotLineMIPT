import pygame
from GameObject import GameObject
from random import choice, randrange as rnd
import colors

class Bullet(GameObject):
    def __init__(self):
        GameObject.__init__(self, x, y, w, h)
        self.color = choice([colors.BLACK, colors.RED2])
        self.r = (w ** 2 + h ** 2) ** 0.5
        self.velocity = vel
        self.x = x
        self.y = y
        self.mouse_button_pressed = False

    def draw(self, surface):
        if not self.owner:
            pygame.draw.oval(surface, self.color, self.bounds)

    def update(self):
        if not self.owner:
            dx = 0
            dy = 0
            if self.mouse_button_pressed:
                self.strike_movement()
            else:
                self.move(dx, dy)


class Pen(GameObject):
    def __init__(self, x, y, w, h, owner, vel = (0, 0)):
        GameObject.__init__(self, x, y, w, h)
        self.color = choice([colors.BLACK, colors.RED2])
        self.r = (w ** 2 + h ** 2) ** 0.5
        self.velocity = vel
        self.x = x
        self.y = y
        self.mouse_button_pressed = False
        self.owner = owner

    def draw(self, surface):
        if not self.owner:
            pygame.draw.rect(surface, self.color, self.bounds)

    def handle(self, key, pos): #pos это координаты мыши
        if key == pygame.MOUSEBUTTONDOWN:
            self.mouse_button_pressed = True
        else:
            self.mouse_button_pressed = False

    def update(self):
        if self.mouse_button_pressed:
            a = pygame.mouse.get_pos()[0]
            b = pygame.mouse.get_pos()[1]
            if 440 < a < 540 and 40 < b < 90:
                pygame.quit()
            a -= self.x
            b -= self.y
            line_length = max(1, (a ** 2 + b ** 2) ** 0.5)
            a = round(a / line_length, 2)
            b = round(b / line_length, 2)
            self.move(5*a, 5*b)
        else:
            self.move(self.owner.dx, self.owner.dy)


    def move(self, dx, dy):  #
        self.bounds = self.bounds.move(dx, dy)
        self.x += dx
        self.y += dy

    def hit_test(self, obj):
        if obj != self.owner:
            if abs(obj.x - self.x) <= (self.r + obj.r) and abs(obj.y - self.y) <= (self.r + obj.r):
                return True
            else:
                return False
        else:
            pass

    def initialization_of_attack(self):
        r = pygame.mouse.get_pos()
        c = r[0] - self.x
        d = r[1] - self.y
        movement_vector = [c, d]
        return movement_vector


    def strike_calculations(self):
        mv = self.initialization_of_attack()
        line_length = (a ** 2 + b ** 2) ** 0.5
        cos = a / line_length
        sin = b / line_length
        norm_mv = [cos, sin]
        return norm_mv

    def strike_movement(self):
        mv = self.strike_calculations()
        a = a
        b = b
        self.move(a, b)
