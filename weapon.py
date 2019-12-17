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
        self.owner = False

    def draw(self, surface):
        if not self.owner:
            pygame.draw.rect(surface, self.color, self.bounds)

    def handle(self, key, pos): #pos это координаты мыши
        if key == pygame.MOUSEBUTTONDOWN:
            self.mouse_button_pressed = True
        else:
            self.mouse_button_pressed = False

    def update(self):
        if not self.owner:
            dx =0
            dy =0
            if self.mouse_button_pressed:
                self.strike_movement()
            else:
                self.move(dx, dy)

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
        dx = r[0] - self.x
        dy = r[1] - self.y
        movement_vector = (dx, dy)
        return movement_vector


    def strike_calculations(self):
        mv = self.initialization_of_attack()
        line_length = (mv[0] ** 2 + mv[1] ** 2) ** 0.5
        cos = mv[0] / line_length
        sin = mv[1] / line_length
        norm_mv = (cos, sin)
        return norm_mv

    def strike_movement(self):
#<<<<<<< HEAD
        #if pygame.mouse.get_pressed()[0]:
            mv = self.strike_calculations()
            dx = mv[0]
            dy = mv[1]
            self.move(dx, dy)
        #else:
           # pass
#=======
##        mv = self.strike_calculations()
##        dx = mv[0]
##        dy = mv[1]
##        self.move(dx, dy)
#>>>>>>> df38d0490200f04b23912a12088960fd7545a497
