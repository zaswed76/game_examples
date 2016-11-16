import sys
import pygame
from anim.ship import Ship
from lib.subsprite import SubSprite
COLOR =  "#04304F"
def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((1600, 600))
    pygame.display.set_caption("Name Game")
    # Запуск основного цикла игры.

    bg = pygame.image.load('images/bg.jpg').convert()
    ship = Ship(screen)
    sb = SubSprite('../images/man.png', 118, 136)
    man1 = sb.get_sprite(8)
    timer = pygame.time.Clock()
    while True:
        timer.tick(120)
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Отображение последнего прорисованного экрана.
        screen.fill(pygame.Color(COLOR))
        screen.blit(bg, bg.get_rect())
        screen.blit(man1, man1.get_rect())
        ship.update()
        ship.blitme()


        pygame.display.flip()

run_game()