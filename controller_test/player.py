
import pygame
from pygame.sprite import Sprite
from controller import Controller

class Player(Sprite, Controller):
    def __init__(self, screen, *groups):
        super().__init__(*groups)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.centerx = self.screen_rect.centerx

    def draw(self):
        self.screen.fill(pygame.Color('green'), self.rect)


