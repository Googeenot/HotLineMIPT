from pygame.rect import Rect


class GameObject:
    def __init__(self, x, y, w, h, speed=(0,0)):
        self.x = x
        self.y = y
        self.bounds = Rect(x, y, w, h)
        self.speed = speed


    def draw(self, surface): #отрисовать
        pass

    def move(self, dx, dy): #
        self.bounds = self.bounds.move(dx, dy)

    def update(self): #обновить координаты
        if self.speed == [0, 0]:
            return

        
        self.move(*self.speed)
