import sys
import pygame

import functions as gf
import map_config



BG_COLOR = pygame.Color('#D8D8D8')

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("Tanks")

    platforms = pygame.sprite.Group()
    targets = pygame.sprite.Group()
    # Запуск основного цикла игры.
    map1 = map_config.map1
    gf.create_level(map1, platforms, targets, screen)
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(BG_COLOR)
        # Отображение последнего прорисованного экрана.
        # platforms.draw(screen)
        # targets.draw(screen)
        pygame.display.flip()

run_game()