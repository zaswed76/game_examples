import pygame
from pygame import Color

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.window = pygame.Rect(0, 0, 640, 640)

        self.button = pygame.Rect(0, 0, 150, 50)
        self.button.center = self.screen_rect.center
        # self.window.fill(Color('green'), self.button)


    def draw(self):
        self.screen.fill(Color('#F3E2A9'), self.window)
        self.screen.fill(Color('green'), self.button)

