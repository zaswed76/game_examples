import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen, speed, x, y):
        """Инициализирует корабль и задает его начальную позицию."""

        super().__init__()
        self.speed = speed
        self.screen = screen
        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.Surface((32,32))
        self.image.fill(pygame.Color("#0000FF"))
        self.image.convert()
        self.rect = pygame.Rect(x, y, 32, 32)
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = 50
        self.rect.bottom = self.screen_rect.bottom + 100

        # Сохранение вещественной координаты центра корабля.
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)



    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def update(self, up, down, left, right, running, platforms):
        """Обновляет позицию корабля с учетом флага."""
        if right and self.rect.right < self.screen_rect.right:
            self.center_x += self.speed

        if left and self.rect.left > 0:
            self.center_x -= self.speed

        if up and self.rect.top > 0:
            self.center_y -= self.speed

        if down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.speed

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

