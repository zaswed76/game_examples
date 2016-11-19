
import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, screen, *groups):
        super().__init__(*groups)
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.centerx = self.screen.center_x

    def draw(self):
        self.screen.fill(pygame.Color('green'), self.rect)


