import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/platform.jpg')
        self.image.convert()

        self.rect = pygame.Rect(x, y, 32, 32)

    def update(self):
        pass