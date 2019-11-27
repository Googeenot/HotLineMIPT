import pygame
from collections import defaultdict
import sys
import config as c
import Game
class HotlineMIPT:
      def __init__(self):
            #print(c.caption)
            pygame.init() 
            pygame.font.init()
            pygame.display.set_caption(c.caption)
            self.surface = pygame.display.set_mode((c.widht, c.height),  (pygame.NOFRAME and pygame.FULLSCREEN))
            
            self.frame_rate = c.frame_rate
            self.clock = pygame.time.Clock()
            print(self.clock)
            self.objects = []
            self.clock = pygame.time.Clock()

            
##            self.keydown_handlers = defaultdict(list)
##            self.keyup_handlers = defaultdict(list)
##            self.mouse_handlers = []
            
            self.game_over = False

##      def handle_events(self):
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                pygame.quit()
##                sys.exit()
##            elif event.type == pygame.KEYDOWN:
##                for handler in self.keydown_handlers[event.key]:
##                    handler(event.key)
##            elif event.type == pygame.KEYUP:
##                for handler in self.keydown_handlers[event.key]:
##                    handler(event.key)
##            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
##                for handler in self.mouse_handlers:
##                    handler(event.type, event.pos)
      def zastavka(self):
            self.background_image = pygame.image.load(c.back_image_filename)
            self.surface.blit(self.background_image, (-420, 0))
            pygame.display.update()
            self.clock.tick(1)            
      def menu(self):
            start_game = pygame.rect.Rect(40, 40, 20, 20)
            pygame.draw.rect(self.surface, (100, 100,100) , start_game)
            self.surface.blit(pygame.font.SysFont(c.font, 20).render('текст', False, (100, 200, 50)), (40, 40))
            pygame.display.update()
            while  not self.game_over:
                  for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                              if start_game.collidepoint(event.pos):
                                    Game.Game(self.surface).run() #функция вызывает основную игру

      def run(self):
            self.zastavka()
            self.menu()
            
def main():
    HotlineMIPT().run()


if __name__ == '__main__':
    main()            
