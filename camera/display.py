import sys
import pygame
from pygame.sprite import Group


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    info = pygame.display.Info()
    _size = (500, 500)

    screen = pygame.display.set_mode(_size)

    pygame.display.set_caption("Name Game")
    # Запуск основного цикла игры.
    r_color = pygame.Color('#088A08')
    rect_1_rect = pygame.Rect((10,10),(100,100))
    image = 'images/tileset.png'
    sprite = pygame.image.load(image).convert_alpha()
    sub_image = sprite.subsurface((32,0,32,32))

    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Отображение последнего прорисованного экрана.
        screen.fill(pygame.Color('#D8D8D8'))
        # pygame.draw.rect(screen, r_color, rect_1_rect, 15)
        screen.blit(sub_image, sub_image.get_rect())
        pygame.display.flip()

run_game()