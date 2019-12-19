import pygame
from GameObject import GameObject
from random import choice, randrange as rnd
import colors
import Karta
import config as c



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
        pygame.draw.rect(surface, self.color, self.bounds)

    def handle(self, key, pos): #pos это координаты мыши
        if key == pygame.MOUSEBUTTONDOWN:
            self.mouse_button_pressed = True
        else:
            self.mouse_button_pressed = False

    def update(self, p, deltax, deltay, button):
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

        

class Gun:
    def __init__(self, x, y, w, h, owner):
        GameObject.__init__(self, x, y, w, h)
        self.owner = owner
        self.beowner = False
        self.image = pygame.image.load(c.gun)
        self.image = pygame.transform.scale(self.image, (40, 40))
        
    def move(self, dx, dy):  
        self.bounds = self.bounds.move(dx, dy)

    def update(self, p, deltax, deltay):

            self.dx = 0
            self.dy = 0
            self.move(self.dx, self.dy)

    def draw(self, surface):
        if not self.beowner:
            surface.blit(self.image, (self.bounds[0]+25, self.bounds[1]+25))
            
    def handle(self, key, pos, button, owner): #pos это координаты мыши
        self.owner = owner
        if  self.beowner:
            self.bounds[0] = self.owner.bounds[0]
            self.bounds[1] = self.owner.bounds[1]
        if key == pygame.MOUSEBUTTONDOWN:
            if button == 3:
                if self.bounds.colliderect(self.owner.bounds):
                    self.beowner = not self.beowner
                    self.owner.beweapon =  not self.owner.beweapon
                    

            

class Bullet(GameObject):
    def __init__(self, x, y, w, h, dots):
        GameObject.__init__(self, x+10, y+10, w, h)
        self.color = choice([colors.BLACK, colors.RED2])
        self.r = (w ** 2 + h ** 2) ** 0.5
        self.mouse_button_pressed = False
        self.live = 0
        self.mo = True
        self.dots = dots
        self.time = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def hittests(self, en):
        if pygame.Rect.colliderect(self, en):
            en.live = 0
            self.live = 0
            self.kill()
            self.live = 1
    def delete(self):
        pass

    def kill(self):
        pass
        
    def m_position(self):
        a = pygame.mouse.get_pos()[0] + 180
        b = pygame.mouse.get_pos()[1] + 50
        mp = (a, b)
        return mp


    def update(self, p, deltax, deltay):
        self.time += 1
        if self.time >= 100:
            self.kill()
        if self.mo:
            dots = self.dots
            a = dots[0]
            b = dots[1]
            a -= self.x
            b -= self.y
            line_length = max(1, (a ** 2 + b ** 2) ** 0.5)
            a = round(5 * a / line_length)
            b = round(5 * b / line_length)


            for i in range(Karta.k):
                if self.bounds.colliderect(Karta.map_rect[i]):
                    self.mo = False
                    break
            self.move(a, b)
        return self.mo


