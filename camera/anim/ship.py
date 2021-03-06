import sys
import pygame
from pygame import Color
from pygame.sprite import Sprite
from anim import pyganim
from lib.subsprite import SubSprite


COLOR =  "#04304F"

ANIMATION_DELAY = 0.4 # скорость смены кадров
ANIMATION_RIGHT = [
            ('images/ship/ship1.png', 0.1),
            ('images/ship/ship2.png', 0.1),
            ('images/ship/ship3.png', 0.1),
            ('images/ship/ship4.png', 0.1),
            ('images/ship/ship5.png', 0.1),
            ('images/ship/ship4.png', 0.1),
            ('images/ship/ship3.png', 0.1),
            ('images/ship/ship2.png', 0.1)
]

sub = SubSprite('../images/numbers.png', 100, 100)
sp = sub.get_sprites(3, 4)

spr = sub.get_sprite_time(sub.get_sprites(), ANIMATION_DELAY)
ANIMATION_RIGHT2 = spr


ANIMATION2 = [
            ('images/sq/1.png', 0.1),
            ('images/sq/2.png', 0.1),
            ('images/sq/3.png', 0.1),
            ('images/sq/4.png', 0.1),
            ('images/sq/3.png', 0.1),
            ('images/sq/2.png', 0.1),
]



class Ship(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.Surface((100,100))
        self.image.set_colorkey(Color(COLOR)) # делаем фон прозрачным
        self.rect = pygame.Rect(0, 0, 100, 100) # прямоугольный объект

        self.screen_rect = screen.get_rect()
        self.center_x = float(self.rect.centerx)


        self.boltAnimRight = pyganim.PygAnimation(ANIMATION_RIGHT2)
        self.boltAnimRight.play()

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def update(self, *args):
        self.center_x += 0

        self.rect.centerx = self.center_x
        self.image.fill(Color(COLOR))
        self.boltAnimRight.blit(self.image, (0, 0))