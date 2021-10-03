from numpy.random import choice

from Ship import Ship
from sources import *


class Chick(Ship):
    velocity = 1
    
    def __init__(self, x, y, ):
        super().__init__(x, y, )
        self.type = choice(['yellow', 'blue', 'red'], p=[.2, .3, .5])
        self.image = YELLOW_CHICK_IMG if self.type == 'yellow' else BLUE_CHICK_IMG if self.type == 'blue' else RED_CHICK_IMG if self.type == 'red' else ''
        self.lives = 1 if self.type == 'yellow' else 2 if self.type == 'blue' else 3 if self.type == 'red' else 0
        self.bullet = EGG_IMG
        
        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        # print('chick', self.x, self.y)
        self.x += Chick.velocity
