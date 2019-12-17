import pygame
from GameObject import GameObject
from random import choice, randrange as rnd
import colors


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
            if 615 < a < 640 and 0 < b < 15:
                pygame.quit()
            a -= self.x
            b -= self.y
            line_length = max(1, (a ** 2 + b ** 2) ** 0.5)
            a = round(a / line_length)
            b = round(b / line_length)
            self.move(5*a, 5*b)
        else:
            if self.x != self.owner.x + 20 or self.y != self.owner.y:
                self.move(self.owner.x + 20 - self.x, self.owner.y - self.y)
            else:
                self.move(0, 0)


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
        pygame.draw.oval(surface, self.color, self.bounds)

    def update(self):
        dx = 0
        dy = 0
        if self.mouse_button_pressed:
            self.strike_movement()
        else:
            self.move(dx, dy)