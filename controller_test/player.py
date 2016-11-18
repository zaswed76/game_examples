
import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, screen, *groups):
        super().__init__(*groups)
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 50, 50)

    def draw(self):
        self.screen.fill(pygame.Color('green'), self.rect)


