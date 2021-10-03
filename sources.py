import pygame

WIDTH = 500
HEIGHT = 400
FPS = 60
точність_побудови_маршруту=40 #...1 одиниця це найточніший пошук але менше 10 це просто слайдшоу
FONT=20
size_of_chick = 30
SPACE_IMG = pygame.transform.scale(pygame.image.load('imgs/Nebula Blue.png'), (WIDTH, HEIGHT))
SHIP_IMG = pygame.transform.scale(pygame.image.load('imgs/player.png'), (30, 30))
BLUE_CHICK_IMG = pygame.transform.scale(pygame.image.load('imgs/blue.png'), (size_of_chick, size_of_chick))
YELLOW_CHICK_IMG = pygame.transform.scale(pygame.image.load('imgs/yellow.png'), (size_of_chick, size_of_chick))
RED_CHICK_IMG = pygame.transform.scale(pygame.image.load('imgs/red.png'), (size_of_chick, size_of_chick))
EGG_IMG = pygame.transform.scale(pygame.image.load('imgs/egg.png'), (10, 10))
LASER_IMG = pygame.transform.scale(pygame.image.load('imgs/laser.png'), (10, 50))



def snext(method):
    
    if method == 'star':
        return 'dfs'
    elif method == 'dfs':
        return 'bfs'
    elif method == 'bfs':
        return 'ucs'
    elif method == 'ucs':
        return 'star'


serach_method = 'star'
