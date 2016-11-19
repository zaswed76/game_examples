import sys
import pygame

import functions as gf
from menu import Menu
from game_window import GameWindow




BG_COLOR = pygame.Color('#D8D8D8')

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("Tanks")
    game_run = False
    menu = Menu(screen)
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(BG_COLOR)
        # Отображение последнего прорисованного экрана.
        # platforms.draw(screen)
        # targets.draw(screen)
        if not game_run:
            menu.draw()
        pygame.display.flip()

run_game()