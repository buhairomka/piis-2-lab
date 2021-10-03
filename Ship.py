class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lives = 0
        self.image = None
        self.bullet = None
        self.bullets = []
    
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
