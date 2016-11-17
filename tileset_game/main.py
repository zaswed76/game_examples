import sys
import os
import pygame
import paths
from settings import Settings
import level_map as lm

st = Settings()
level_1 = os.path.join(paths.maps, 'test_num_5.json')
def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((st.screen_width, st.screen_height))
    pygame.display.set_caption("Name Game")
    # Запуск основного цикла игры.
    level = lm.LevelMap(level_1, screen)
    # level.create_background()
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

run_game()