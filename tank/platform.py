import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, img, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(img)
        self.image.convert()
        print(self.image)
        self.rect = pygame.Rect(x, y, 32, 32)

    def blitme(self):
        """Выводит пришельца в текущем положении."""
        self.screen.blit(self.image, self.rect)