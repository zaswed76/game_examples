import pygame
from pygame.sprite import Sprite


class Platform(Sprite):
    def __init__(self, screen, image, x, y):
        # todo Ограничение перемещений
        super().__init__()
        self.image = image
        self.screen = screen
        # Загрузка изображения корабля и получение прямоугольника.



        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(x, y, 100, 100)



    def blitme(self):
        self.screen.blit(self.image, self.rect)

