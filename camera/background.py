import pygame

class BackGround:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/bg.bmp').convert()
        self.rect = self.image.get_rect()

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)