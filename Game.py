import pygame
from collections import defaultdict
import sys
import config as c
import poligon
import Enemies
import map
import weapon


class Game():
      def __init__(self, surface):
            self.surfaceh = surface

            self.surface = pygame.display.set_mode((c.widht, c.height), (pygame.NOFRAME and pygame.FULLSCREEN))
            self.surface = pygame.Surface((c.widhtkarta, c.heightkarta))

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
            self.p = poligon.Poligon(500, 250, 10,10, (100, 100,100), 5)
            self.pause_game = None
            self.dx = 0
            self.dy = 0

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

      def update(self):
          for i in self.objects:
              i.update()



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
                if event.type == pygame.MOUSEBUTTONDOWN and self.exit_game.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

      def pause(self):
          pause_menu = pygame.rect.Rect(300, 150, 90, 45)
          pygame.draw.rect(self.surfaceh, (0, 100, 0), pause_menu)
          self.surfaceh.blit(pygame.font.SysFont(c.font, 40).render('Go on', False, (200, 100, 50)), (300, 150))
          pygame.display.update()
          i = 0
          while i != 1:
              for event in pygame.event.get():
                  if event.type == pygame.MOUSEBUTTONDOWN:
                      if pause_menu.collidepoint(event.pos):
                          i = 1

      def map(self):
          poligonn = map.Map(20, 20, 10, 10, (100, 100, 100), 5)
          self.keydown_handlers[pygame.K_LEFT].append(poligonn.handle)
          self.keydown_handlers[pygame.K_RIGHT].append(poligonn.handle)
          self.keydown_handlers[pygame.K_UP].append(poligonn.handle)
          self.keydown_handlers[pygame.K_DOWN].append(poligonn.handle)
          print(self.keydown_handlers)

      def create_poligon(self):
        poligonn = poligon.Poligon(500, 250, 10,10, (100, 100,100), 5 )
        self.keydown_handlers[pygame.K_LEFT].append(poligonn.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(poligonn.handle)
        self.keydown_handlers[pygame.K_UP].append(poligonn.handle)
        self.keydown_handlers[pygame.K_DOWN].append(poligonn.handle)
        self.objects.append(poligonn)
        self.shina[poligon].append(poligonn)
        self.objects.append(poligonn)


      def create_enemies(self):
            r_en = []
            for i in range(Enemies.k_en):
                r_en.append(poligon.Poligon(Enemies.b[i][0], Enemies.b[i][1], 10, 10, (100, 100, 100), 5))
                self.objects.append(r_en[i])
                self.shina[poligon].append(r_en[i])
                r_en.append(poligon.Enemies(Enemies.b[i][0], Enemies.b[i][1], 10, 10, (100, 100, 100), 5, i, self.shina[poligon][0]))
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

            ##        self.keyup_handlers[pygame.K_LEFT].append(poligonn.handle)
            ##        self.keyup_handlers[pygame.K_RIGHT].append(poligonn.handle)
      def create_objects(self):
          #self.map()
          self.create_poligon()
          self.create_enemies()
          self.create_pen()

      def create_pen(self):
            pen = weapon.Pen(550, 250, 10, 10, self.p)
            self.mouse_handlers[pygame.MOUSEBUTTONDOWN].append(pen.handle)
            self.mouse_handlers[pygame.MOUSEBUTTONUP].append(pen.handle)
            self.objects.append(pen)

      def create_rival(self):
          riv_1 = poligon.Rival(200, 200, 10, 10, (100, 100, 50), 5, self.p)
          self.objects.append(riv_1)

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
                  
                  
            x = self.shina[poligon][0].bounds[0]+self.dx
            y = self.shina[poligon][0].bounds[1]+self.dy
            self.surfaceh.blit(self.surface, (c.widht/2 - x, c.height/2 - y))

      def run(self):
            self.background_image = pygame.image.load(c.back_image)
            self.surfaceh.blit(self.background_image, (0, 0))
            
            pygame.display.update()

            self.create_objects()
            self.background_image = pygame.image.load(c.map)

            while not self.game_over:

                  self.surface.blit(self.background_image, (0, 0))
                  self.handle_events()
                  self.update()
                  self.draw()
                  self.movecamera()
                  self.menu()


                  pygame.display.update()
                  self.clock.tick(self.frame_rate)

      def uploadlevel(self):
            pass


