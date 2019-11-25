import pygame
from collections import defaultdict
import sys
import config as c
import poligon
class Game:
      def __init__(self, surface):
            #print(c.caption)
            self.surface = surface
            self.frame_rate = c.frame_rate
            self.clock = pygame.time.Clock()
            print(self.clock)
            self.objects = []

            
            self.keydown_handlers = defaultdict(list)
            self.keyup_handlers = defaultdict(list)
            self.mouse_handlers = []
            self.game_over = False

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
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)
      def create_poligon(self):
        paddle = poligon.Poligon(20, 20, 10,10, (100, 100,100), 5 )
        
        self.keydown_handlers[pygame.K_LEFT].append(paddle.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(paddle.handle)
        
        self.keyup_handlers[pygame.K_LEFT].append(paddle.handle)
        self.keyup_handlers[pygame.K_RIGHT].append(paddle.handle)
        
        self.objects.append(paddle)
      def create_objects(self):
            self.create_poligon()

      def run(self):
            while not self.game_over:
                  #self.surface.blit(self.background_image, (0, 0))

                  self.handle_events()
                  self.update()
                  self.draw()

                  #pygame.display.update()
                  self.clock.tick(self.frame_rate)
      def uploadlevel(self):
            pass


