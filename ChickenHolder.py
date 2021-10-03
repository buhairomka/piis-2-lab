# chicken holder
import random

import pygame

from Chick import Chick
from sources import size_of_chick, WIDTH

def invert(img):
    return pygame.transform.flip(img, True, False)


class ChicksHolder:
    def __init__(self):
        self.chicks = []
        self.len = len(self.chicks)
    
    def set_chicks(self):
        Chick.velocity = 1
        for i in range(1):
            for j in range(3):
                self.chicks.append(Chick((j + 1) * (size_of_chick + random.randint(0,40)), (i + 2) * (size_of_chick + random.randint(0,30))))
    
    def draw_all(self, window):
        if len(self.chicks) > 0:
            for each in self.chicks:
                each.draw(window)
    
    def move(self):
        for i in self.chicks:
            if i.x + i.image.get_width() + Chick.velocity > WIDTH or i.x + Chick.velocity < 0:
                Chick.velocity *= -1
                for i in self.chicks:
                    i.image = invert(i.image)
                break
            else:
                i.move()
