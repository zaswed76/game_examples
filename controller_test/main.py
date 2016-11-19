import sys
import pygame
from pygame.sprite import Group
from player import Player

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Name Game")
    # Запуск основного цикла игры.
    sq = Player(screen)
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print(1)
        # Отображение последнего прорисованного экрана.
        sq.draw()
        pygame.display.flip()

run_game()