import pygame
from GameObject import GameObject
from random import choice, randrange as rnd
import colors
import Karta



class Pen(GameObject):
    def __init__(self, x, y, w, h, owner):
        GameObject.__init__(self, x, y, w, h)
        self.color = choice([colors.BLACK, colors.RED2])
        self.owner = owner
        self.x = x
        self.y = y
        self.r = (w ** 2 + h ** 2) ** 0.5
        self.mouse_button_pressed = False

    def draw(self, surface):
        print(self.owner.x)
        pygame.draw.rect(surface, self.color, self.bounds)

    def handle(self, key, pos): #pos это координаты мыши
        if key == pygame.MOUSEBUTTONDOWN:
            self.mouse_button_pressed = True
        else:
            self.mouse_button_pressed = False

    def update(self, p):
        if self.mouse_button_pressed:
            a = pygame.mouse.get_pos()[0] + 180
            b = pygame.mouse.get_pos()[1] + 50
            a -= self.x
            b -= self.y
            line_length = max(1, (a ** 2 + b ** 2) ** 0.5)
            self.dx = round(5 * a / line_length)
            self.dy = round(5 * b / line_length)
            self.move(self.dx, self.dy)
            b = True
            for i in range(Karta.k):
                if self.bounds.colliderect(Karta.map_rect[i]) == True:
                    self.dx *= -1
                    self.dy *= -1
                    b = False
                    break
            if b:
                self.dx = 0
                self.dy = 0
            self.move(self.dx, self.dy)

        else:
            if self.x != p.x + 10 or self.y != p.y:
                self.move(p.x + 10 - self.x, p.y - self.y)
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
    def __init__(self, x, y, w, h, dots):
        GameObject.__init__(self, x, y, w, h)
        self.color = choice([colors.BLACK, colors.RED2])
        self.r = (w ** 2 + h ** 2) ** 0.5
        self.mouse_button_pressed = False
        self.live = 0
        self.dots = dots

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def hittests(self, en):
        if pygame.Rect.colliderect(self, en):
            en.live = 0
            self.live = 0
            self.kill()
        else:
            self.live = 1

    def m_position(self):
        a = pygame.mouse.get_pos()[0] + 180
        b = pygame.mouse.get_pos()[1] + 50
        mp = (a, b)
        return mp

    def update(self, p):
        dots = self.dots
        a = dots[0]
        b = dots[1]
        a -= self.x
        b -= self.y
        line_length = max(1, (a ** 2 + b ** 2) ** 0.5)
        a = round(5 * a / line_length)
        b = round(5 * b / line_length)
        self.move(a, b)
