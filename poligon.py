import pygame

import Karta

import Enemies

import Game

import config as c

from GameObject import GameObject
import math



class Poligon(GameObject):


    def __init__(self, x, y, w, h, color, offset):

        GameObject.__init__(self, x, y, w, h)

        self.x = x

        self.y = y

        self.color = color

        self.offset = offset

        self.moving_left = False

        self.moving_right = False

        self.moving_up = False

        self.moving_down = False
        
        self.beweapon = False

        self.live = 1

        self.map_x = 0

        self.map_y = -370

        self.dx = 0

        self.dy = 0

        self.imagestop = pygame.image.load(c.stop)
        self.imagestop = pygame.transform.scale(self.imagestop, (40, 40))
        self.image = self.imagestop
        self.imagegoright = pygame.image.load(c.goright)
        self.imagegoright = pygame.transform.scale(self.imagegoright, (40, 40))
        self.imagegoleft = pygame.image.load(c.goleft)
        self.imagegoleft = pygame.transform.scale(self.imagegoleft, (40, 40))

        self.imagestopwithgun = pygame.image.load(c.stopwithgun)
        self.imagestopwithgun = pygame.transform.scale(self.imagestopwithgun, (40, 40))
        self.imagegorightwithgun = pygame.image.load(c.gorightwithgun)
        self.imagegorightwithgun = pygame.transform.scale(self.imagegorightwithgun, (40, 40))
        self.imagegoleftwithgun = pygame.image.load(c.goleftwithgun)
        self.imagegoleftwithgun = pygame.transform.scale(self.imagegoleftwithgun, (40, 40))
        self.time = 0
        
        self.angle = 0

        self.left_right = True
        self.nonestop = False

    def draw(self, surface):
        #pygame.draw.rect(surface, self.color, self.bounds)
        if not self.beweapon:
            if (self.moving_left or self.moving_right or self.moving_up or self.moving_down):
                
                if self.nonestop:
                    self.image = self.imagestop
                    if ( pygame.time.get_ticks() - self.time)>100:
                        self.time = pygame.time.get_ticks()
                        self.nonestop = False

                        
                elif self.left_right:
                    self.image =  self.imagegoright
                    if ( pygame.time.get_ticks() - self.time)>100:
                        self.time = pygame.time.get_ticks()
                        self.left_right = not self.left_right
                        self.nonestop = True

                else:
                    self.image =  self.imagegoleft
                    if ( pygame.time.get_ticks() - self.time)>100:
                        self.time = pygame.time.get_ticks()
                        self.left_right = not self.left_right
                        self.nonestop = True

            else:    
                    self.image = self.imagestop
        else:
            if (self.moving_left or self.moving_right or self.moving_up or self.moving_down):
                
                if self.nonestop:
                    self.image = self.imagestopwithgun
                    if ( pygame.time.get_ticks() - self.time)>100:
                        self.time = pygame.time.get_ticks()
                        self.nonestop = False

                        
                elif self.left_right:
                    self.image =  self.imagegorightwithgun
                    if ( pygame.time.get_ticks() - self.time)>100:
                        self.time = pygame.time.get_ticks()
                        self.left_right = not self.left_right
                        self.nonestop = True

                else:
                    self.image =  self.imagegoleftwithgun
                    if ( pygame.time.get_ticks() - self.time)>100:
                        self.time = pygame.time.get_ticks()
                        self.left_right = not self.left_right
                        self.nonestop = True
            else:    
                    self.image = self.imagestopwithgun
            
            
 
        surface.blit(pygame.transform.rotate(self.image, self.angle), (self.bounds[0]-10, self.bounds[1]-10))


        self.fire = 0

    def handle(self, key):

        if key == pygame.K_LEFT:

            self.moving_left = not self.moving_left

        elif key == pygame.K_RIGHT:

            self.moving_right = not self.moving_right

        elif key == pygame.K_UP:

            self.moving_up = not self.moving_up

        elif key == pygame.K_DOWN:

            self.moving_down = not self.moving_down


    def update(self, p, deltax, deltay):
        x, y = pygame.mouse.get_pos()

        x = x - c.widht/2 + p[0] - deltax
        y = y - c.height/2 + p[1] - deltay

        
        self.angle = - 180*math.atan2(y-self.bounds[1]-10, (x-self.bounds[0]-10))/math.pi +90



        if self.live:

            self.dx = 0

            self.dy = 0

            if self.moving_left:

                self.dx = -1

            elif self.moving_right:

                self.dx = 1

            if self.moving_up:

                self.dy = -1

            elif self.moving_down:

                self.dy = 1

            if not self.dx and not self.dy:
                return
            if self.fire:
                self.shoot()

            h = self.dx

            self.dx /= (1 / c.v) * (self.dx ** 2 + self.dy ** 2) ** 0.5

            self.dy /= (1 / c.v) * (h ** 2 + self.dy ** 2) ** 0.5

            self.move(self.dx, self.dy)

            b = True

            for i in range(Karta.k):
                if self.bounds.colliderect(Karta.map_rect[i]) == True:
                    self.moving_left = False

                    self.moving_right = False

                    self.moving_up = False

                    self.moving_down = False

                    self.dx *= -1

                    self.dy *= -1

                    b = False

                    break

            if b:
                self.dx = 0

                self.dy = 0

            self.move(self.dx, self.dy)

            # self.map_x -= self.dx

            # self.map_y -= self.dy

        else:

            pass


    def shoot(self):
        pass

    def attack_check(self, weap, rival):

        if weap.mouse_button_pressed:

            if pygame.Rect.colliderect(weap, rival):

                rival.live = 0

            else:

                pass

        else:

            pass


class Enemies(Poligon):

    def __init__(self, x, y, w, h, color, offset, k, p):

        Poligon.__init__(self, x, y, w, h, color, offset)

        self.attack = p

        self.r_attack = 100

        self.k = k

    def draw(self, surface):

        pygame.draw.rect(surface, self.color, self.bounds)

<<<<<<< HEAD
    def update(self, p):

=======

    def update(self, p, deltax, deltay):

>>>>>>> c0db51ee5458ca83e76bb2b6bf0cb19b2bd2ac05
        self.attack = p

        self.dx = 0

        self.dy = 0
<<<<<<< HEAD


        if ((self.x - self.attack[0]) ** 2 + (self.y - self.attack[1]) ** 2) ** 0.5 <= self.r_attack:

=======

        if 5 <= ((self.x - self.attack[0]) ** 2 + (self.y - self.attack[1]) ** 2) ** 0.5 <= self.r_attack:
>>>>>>> c0db51ee5458ca83e76bb2b6bf0cb19b2bd2ac05
            ro = ((self.x - self.attack[0]) ** 2 + (self.y - self.attack[1]) ** 2) ** 0.5

            x = (self.attack[0] - self.x) / ro

            y = (self.attack[1] - self.y) / ro

            self.dx = 1 * x // 1
            self.dy = 1 * y // 1
            self.move(self.dx, self.dy)

<<<<<<< HEAD

            b = True
=======
        b = True
>>>>>>> c0db51ee5458ca83e76bb2b6bf0cb19b2bd2ac05

            for i in range(Karta.k):

                if self.bounds.colliderect(Karta.map_rect[i]):
                    self.moving_left = False

                    self.moving_right = False

                    self.moving_up = False

                    self.moving_down = False

                    self.dx *= -1

                    self.dy *= -1

                    b = False

                    break

            if b:
                self.dx = 0

                self.dy = 0

            self.move(self.dx, self.dy)

    def handle(self, key):
<<<<<<< HEAD
=======



>>>>>>> c0db51ee5458ca83e76bb2b6bf0cb19b2bd2ac05
        pass

x = 0
y = 0

