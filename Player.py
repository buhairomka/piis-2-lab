import pygame

from Ship import Ship
from sources import SHIP_IMG, LASER_IMG


class Player(Ship):
    def __init__(self, x, y, lives=10):
        super().__init__(x, y)
        self.velocity = 8
        self.lives = lives
        self.image = SHIP_IMG
        self.bullet = LASER_IMG
        self.mask = pygame.mask.from_surface(self.image)

