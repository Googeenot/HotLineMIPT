import pygame
from collections import defaultdict
import sys
import config as c

class Game:
      def __init__(self):
            #print(c.caption)
            self.surface = pygame.display.set_mode((c.widht, c.height))
            self.frame_rate = c.frame_rate
            self.clock = pygame.time.Clock()
            print(self.clock)
            self.objects = []
            self.clock = pygame.time.Clock()
            
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

      def run(self):
            while not self.game_over:
                  self.surface.blit(self.background_image, (0, 0))

                  self.handle_events()
                  self.update()
                  self.draw()

                  pygame.display.update()
                  self.clock.tick(self.frame_rate)
                  
      def uploadlevel(self):
            pass

Game().run()
