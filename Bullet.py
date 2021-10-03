# bullets
class Bullet:
    def __init__(self, x, y, vel):
        self.velocity = vel
        self.image = None
        self.x = x
        self.y = y
    
    def draw(self, window):
        window.blit(self.image, (self.x - self.image.get_width() / 2, self.y))
    
    def move(self):
        self.y += self.velocity
