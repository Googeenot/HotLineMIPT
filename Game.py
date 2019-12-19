import pygame
from collections import defaultdict
import sys
import config as c
import poligon
import Enemies

#<<<<<<< HEAD
import map
#=======

import weapon
#>>>>>>> 71f9dde31187ac4565402a9121e6687d84b23bf9
class Game():
      def __init__(self, surface):
            
            self.surfaceh = surface
#<<<<<<< HEAD
            self.surface = pygame.display.set_mode((c.widht, c.height), (pygame.NOFRAME and pygame.FULLSCREEN))
#=======
            self.surface =  pygame.Surface((c.widhtkarta, c.heightkarta))

#>>>>>>> d70afdfbf1f40f2dd0d5c0bf5fb9d3ff3f57755f
            self.frame_rate = c.frame_rate
            self.clock = pygame.time.Clock()
            print(self.clock)
            self.objects = []

            self.velocity = [0, 0]

            self.shina = defaultdict(list)
            self.keydown_handlers = defaultdict(list)
            self.keyup_handlers = defaultdict(list)
            self.mouse_handlers = defaultdict(list)
            self.game_over = False
            self.p = None
            self.pause_game = None
            #self.shina[x].append(0)
            #self.shina[y].append(0)


            self.dx = 0
            self.dy = 0

#=======
#>>>>>>> 0d69b4ec636b4ba156815197162ca66d105c8009
      def menu(self):
          x = 620
          y = 0
          w = 20
          h = 10
          self.exit_game = exit_game = pygame.rect.Rect(x, y, w, h)
          pygame.draw.rect(self.surfaceh, (100, 0, 0), exit_game)
          self.surfaceh.blit(pygame.font.SysFont(c.font, 10).render('XXX', False, (200, 100, 50)), (x, y))
          self.pause_game = pause_game = pygame.rect.Rect(x - 30, y, w + 10, h)
          pygame.draw.rect(self.surfaceh, (0, 100, 0), pause_game)
          self.surfaceh.blit(pygame.font.SysFont(c.font, 10).render('Pause', False, (200, 100, 50)), (x - 30, y))

      def update(self, ):
          for i in self.objects:
              i.update(self.shina[poligon][0].bounds, self.dx, self.dy)



      def draw(self):
            for i in self.objects:
                  i.draw(self.surface)

                  
      def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
                    
            elif event.type == pygame.KEYUP:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)


            elif event.type in (pygame.MOUSEBUTTONDOWN, 
                                pygame.MOUSEBUTTONUP, 
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers[event.type]:
                        handler(event.type, event.pos)
                if event.type == pygame.MOUSEBUTTONDOWN and self.pause_game.collidepoint(event.pos):
                    self.pause()
                elif event.type == pygame.MOUSEBUTTONDOWN and self.exit_game.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                else:
                    self.create_bullet(event.pos)


      def pause(self):

        pause_menu = pygame.rect.Rect(280, 150, 90, 45)
        pygame.draw.rect(self.surfaceh, (0, 200, 0), pause_menu)
        self.surfaceh.blit(pygame.font.SysFont(c.font, 40).render('Go on', False, (0, 50, 0)), (280, 150))

        exit_menu = pygame.rect.Rect(280, 200, 90, 45)
        pygame.draw.rect(self.surfaceh, (200, 10, 0), exit_menu)
        self.surfaceh.blit(pygame.font.SysFont(c.font, 40).render('  Exit', False, (0, 0, 0)), (280, 200))

        pygame.display.update()

        i = 0

        while i != 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pause_menu.collidepoint(event.pos):
                        i = 1
                    elif exit_menu.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

      def create_bullet(self, pos):
        p = self.shina[poligon][0].bounds
        x = self.shina[poligon][0].bounds[0] + self.dx
        y = self.shina[poligon][0].bounds[1] + self.dy
        pos = list(pos)
        pos[0] += x - c.widht/2
        pos[1] += y - c.height/2
        b = weapon.Bullet(p.x + 5, p.y + 5, 3, 3, pos)
        self.objects.append(b)



      def create_poligon(self):
        global poligonn
        poligonn = poligon.Poligon(500, 250, 20, 20, (100, 100,100), 5)
        self.keydown_handlers[pygame.K_LEFT].append(poligonn.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(poligonn.handle)
        self.keydown_handlers[pygame.K_UP].append(poligonn.handle)
        self.keydown_handlers[pygame.K_DOWN].append(poligonn.handle)
        self.objects.append(poligonn)
        
        #self.keydown_handlers[pygame.K_DOWN]
            
        
##        self.keyup_handlers[pygame.K_LEFT].append(poligonn.handle)
##        self.keyup_handlers[pygame.K_RIGHT].append(poligonn.handle)
#<<<<<<< HEAD
        self.shina[poligon].append(poligonn)
##        print(self.shina[poligon][0][0])
        self.objects.append(poligonn)

      def create_enemies(self):
        r_en = []
        for i in range(Enemies.k_en):
            r_en.append(poligon.Enemies(Enemies.b[i][0], Enemies.b[i][1], 10, 10, (100, 100, 100), 5, i, self.shina[poligon][0].bounds))
        #self.keydown_handlers[pygame.K_LEFT].append(r_en[i].handle)
        #self.keydown_handlers[pygame.K_RIGHT].append(r_en[i].handle)
        #self.keydown_handlers[pygame.K_UP].append(r_en[i].handle)
        #self.keydown_handlers[pygame.K_DOWN].append(r_en[i].handle)
            self.objects.append(r_en[i])
        ##        self.keyup_handlers[pygame.K_LEFT].append(poligonn.handle)
        ##        self.keyup_handlers[pygame.K_RIGHT].append(poligonn.handle)
        # <<<<<<< HEAD
            #self.shina[poligon].append(r_en[i])
        ##        print(self.shina[poligon][0][0])

      def map(self):
            poligonn = map.Map(20, 20, 10, 10, (100, 100, 100), 5)


            self.keydown_handlers[pygame.K_LEFT].append(poligonn.handle)
            self.keydown_handlers[pygame.K_RIGHT].append(poligonn.handle)
            self.keydown_handlers[pygame.K_UP].append(poligonn.handle)
            self.keydown_handlers[pygame.K_DOWN].append(poligonn.handle)
            print(self.keydown_handlers)
            ##        self.keyup_handlers[pygame.K_LEFT].append(poligonn.handle)
            ##        self.keyup_handlers[pygame.K_RIGHT].append(poligonn.handle)

            self.objects.append(poligonn)
      def create_objects(self):
          self.map()
          self.create_poligon()
          self.create_enemies()
          self.create_pen()

      def create_pen(self):
            pen = weapon.Pen(550, 250, 10, 10, self.p)
            self.mouse_handlers[pygame.MOUSEBUTTONDOWN].append(pen.handle)
            self.mouse_handlers[pygame.MOUSEBUTTONUP].append(pen.handle)
            self.objects.append(pen)

      def create_rival(self):
          riv_1 = poligon.Rival(20, 40, 10, 10, (100, 100, 50), 5, self.p)
          self.objects.append(riv_1)

      def create_objects(self):
            self.create_poligon()
            #self.create_pen()
            self.create_enemies()
            #self.create_rival()
      def movecamera(self):
            dx = -2
            dy = -2
            if self.shina[poligon][0].moving_left:
                  if self.dx < 24:
                        self.dx -=dx
            elif self.shina[poligon][0].moving_right:
                  if self.dx> -24:
                        self.dx +=dx
            else:
                        
                  if self.dx>0:
                        self.dx+=dx
                  elif self.dx<0:
                        self.dx-=dx
                  
            if self.shina[poligon][0].moving_up:
                  if self.dy < 24:
                        self.dy -=dy
            elif self.shina[poligon][0].moving_down:
                  if self.dy > -24:
                        self.dy +=dy
            else:
                  if self.dy>0:
                        self.dy+=dy
                  elif self.dy<0:
                        self.dy-=dy
                  
                  
            x= c.widht/2 - (self.shina[poligon][0].bounds[0]+self.dx)
            
            y= c.height/2 - (self.shina[poligon][0].bounds[1]+self.dy)
            self.surfaceh.blit(self.surface, (x, y))

      def run(self):
            self.background_image = pygame.image.load(c.back_image)
            self.surfaceh.blit(self.background_image, (0, 0))
            
            pygame.display.update()

            self.create_objects()
            self.background_image = pygame.image.load(c.map)

            #self.clock.tick(300000)
            #self.surface.blit(self.background_image, (-420, 0))
            while not self.game_over:

                  self.surface.blit(self.background_image, (0, 0))
                  self.handle_events()
                  self.update()
                  self.draw()
                  self.movecamera()
                  self.menu()


                  pygame.display.update()
                  self.clock.tick(self.frame_rate)
            #self.clock.tick(30000)
      def uploadlevel(self):
            pass


