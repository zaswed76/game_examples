import sys
import pygame
from pygame.sprite import Group
from player import Player
from controller import Controller

def asd(*args):
    print(args)

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Name Game")
    # Запуск основного цикла игры.
    sq = Player(screen)
    controll = Controller()
    while True:
        # Отслеживание событий клавиатуры и мыши.

        # Отображение последнего прорисованного экрана.
        sq.draw()
        sq.but_click(asd, x, y)
        pygame.display.flip()

run_game()