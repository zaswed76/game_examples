import sys
import pygame
from pygame.sprite import Group
import functions as gf
from maps import config



BG_COLOR = pygame.Color('#D8D8D8')

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("Tanks")

    platforms = pygame.sprite.Group()
    targets = pygame.sprite.Group()
    # Запуск основного цикла игры.
    gf.create_level(config.Map(), platforms, targets, screen)
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(BG_COLOR)
        # Отображение последнего прорисованного экрана.
        platforms.draw(screen)
        targets.draw(screen)
        pygame.display.flip()

run_game()