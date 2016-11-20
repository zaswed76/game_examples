import sys
import os

import pygame
from pygame.sprite import Group
import paths
from settings import Settings
from libs import level_map as lm

st = Settings()
level_1 = os.path.join(paths.maps, 'new.json')
def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((st.screen_width, st.screen_height))
    pygame.display.set_caption("Name Game")

    # все слои  для рисования
    all_layers = pygame.sprite.OrderedUpdates()

    # слои соответствуют слоям в Tiled
    bg_layer = Group()
    wall = Group()
    dors = Group()
    wall2 = Group()
    # box = Group()
    #
    # создаём уровень
    level = lm.LevelMap(level_1, screen, all_layers)
    level.create_background(bg_layer)
    level.create_map(wall, dors, wall2)


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