import sys
import pygame
from pygame.sprite import Sprite

WIDTH = 500
HEIGHT = 500
BG_COLOR = pygame.Color('#D8D8D8')



def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen_rect = screen.get_rect()
    pygame.display.set_caption('map_tesr')
    timer = pygame.time.Clock()
    right = False
    while 1: # Основной цикл программы

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:

                    right = True
        timer.tick(60)
        screen.fill(BG_COLOR)
        pygame.display.flip()

run_game()
