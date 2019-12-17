import pygame

import config as c
from GameObject import GameObject


class Map(GameObject):
    def __init__(self, x, y, w, h, color, offset):
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.offset = offset
        self.background_image = pygame.image.load(c.map)
        #self.surface.blit(self.background_image, (x,y))

    def draw(self, surface):
        surface.blit(self.background_image, self.bounds)
        #pygame.draw.rect(surface, self.color, self.bounds)

    def update(self):
        self.move(0, 0)
