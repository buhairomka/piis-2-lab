import pygame

from Bullet import Bullet
from sources import EGG_IMG


class Egg(Bullet):
    def __init__(self, x, y, vel=3):
        super(Egg, self).__init__(x, y, vel)
        self.image = EGG_IMG
        self.mask = pygame.mask.from_surface(self.image)
