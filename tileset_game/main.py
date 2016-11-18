import sys
import os

import pygame
from pygame.sprite import Group
import paths
from settings import Settings
import level_map as lm

st = Settings()
level_1 = os.path.join(paths.maps, 'test_num_6_500.json')
def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((st.screen_width, st.screen_height))
    pygame.display.set_caption("Name Game")

    all_layers = pygame.sprite.LayeredUpdates()
    level = lm.LevelMap(level_1, screen, all_layers)
    # фон
    bg_layer = Group()
    level.create_background(bg_layer)


    # карта
    wall = Group()
    dors = Group()
    box = Group()
    all_layers.add(wall, dors, box)
    level.create_map(wall, dors, box)

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Отображение последнего прорисованного экрана.
        level.draw_layers()
        pygame.display.flip()

run_game()