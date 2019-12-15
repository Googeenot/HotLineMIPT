import pygame
from collections import defaultdict
import sys
import config as c
import poligon

#<<<<<<< HEAD
import map
#=======
import weapon
#>>>>>>> 71f9dde31187ac4565402a9121e6687d84b23bf9
class Game():
      def __init__(self, surface):
            #print(c.caption)
            self.surface = surface
            self.frame_rate = c.frame_rate
            self.clock = pygame.time.Clock()
            print(self.clock)
            self.objects = []

            self.velocity = [0, 0]

            
            self.keydown_handlers = defaultdict(list)
            self.keyup_handlers = defaultdict(list)
            self.mouse_handlers = defaultdict(list)
            self.game_over = False

      def update(self):
          for i in self.objects:
                  i.update()
          exit_game = pygame.rect.Rect(440, 40, 100, 50)
          pygame.draw.rect(self.surface, (100, 0, 0), exit_game)
          self.surface.blit(pygame.font.SysFont(c.font, 40).render('Выход', False, (200, 100, 50)), (440, 40))


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

      def create_poligon(self):
        poligonn = poligon.Poligon(20, 20, 10,10, (100, 100,100), 5 )
        
        self.keydown_handlers[pygame.K_LEFT].append(poligonn.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(poligonn.handle)
        self.keydown_handlers[pygame.K_UP].append(poligonn.handle)
        self.keydown_handlers[pygame.K_DOWN].append(poligonn.handle)
        self.objects.append(poligonn)
##        self.keyup_handlers[pygame.K_LEFT].append(poligonn.handle)
##        self.keyup_handlers[pygame.K_RIGHT].append(poligonn.handle)
#<<<<<<< HEAD
        
        self.objects.append(poligonn)

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

      def create_pen(self):
            pen = weapon.Pen(60, 60, 10, 10, (100, 200, 100), 0)
            self.mouse_handlers[pygame.MOUSEBUTTONDOWN].append(pen.handle)
            self.mouse_handlers[pygame.MOUSEBUTTONUP].append(pen.handle)           
            self.objects.append(pen)
      def create_objects(self):
            self.create_poligon()
            self.create_pen()

      def run(self):
            #self.background_image = pygame.image.load(c.back_image_filename)
            #self.surface.blit(self.background_image, (-420, 0))
            #pygame.display.update()

            self.create_objects()
            self.background_image = pygame.image.load(c.map)
            xx = 0
            yy = 0

            #self.clock.tick(300000)
            #self.surface.blit(self.background_image, (-420, 0))
            while not self.game_over:

                  self.surface.blit(self.background_image, (xx, yy))
                  self.handle_events()
                  self.update()
                  self.draw()
                  #xx += dx.Poligon(GameObject)
                  #yy += dy.Poligon(GameObject)

                  pygame.display.update()
                  self.clock.tick(self.frame_rate)
            #self.clock.tick(30000)
      def uploadlevel(self):
            pass


