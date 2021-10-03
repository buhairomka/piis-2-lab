import pygame

from Bullet import Bullet
from sources import LASER_IMG


class Laser(Bullet):
    def __init__(self, x, y, vel=-10):
        super(Laser, self).__init__(x, y, vel)
        self.image = LASER_IMG
        self.mask = pygame.mask.from_surface(self.image)

