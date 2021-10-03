from Egg import Egg
from Laser import Laser
from sources import HEIGHT


class BulletsHolder:
    def __init__(self):
        self.bullets = []
        self.lasers = []
    
    def create_laser(self, x, y):
        self.lasers.append(Laser(int(x), y,vel=-20))
    
    def create_egg(self, x, y):
        self.bullets.append(Egg(x, y, 7))
    
    def draw_all_bullets(self, window):
        for bullet in self.bullets:
            bullet.draw(window)
        
        for laser in self.lasers:
            laser.draw(window)
    
    def move_all(self):
        for i in self.bullets:
            if i.y < HEIGHT and i.y > 0:
                i.move()
            else:
                self.bullets.pop(self.bullets.index(i))
        for i in self.lasers:
            if i.y < HEIGHT and i.y + 50 > 0:
                i.move()
            else:
                self.lasers.pop(self.lasers.index(i))
