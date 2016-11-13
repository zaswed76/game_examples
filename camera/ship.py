import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen, speedx, speedy, x, y):
        """Инициализирует корабль и задает его начальную позицию."""

        super().__init__()
        self.speedx = speedx
        self.speedy = speedy
        self.speed_x = 0
        self.speed_y = 0
        self.screen = screen
        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('images/ship.png')
        # self.image.set_colorkey((255, 255, 255))
        # self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.height = self.rect.height
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = 150
        self.rect.bottom = self.screen_rect.bottom + 100

        # Сохранение вещественной координаты центра корабля.
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)



    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def update(self, up, down, left, right, running, platforms):
        """Обновляет позицию корабля с учетом флага."""
        if right :
            self.speed_x = self.speedx
            self.rect.centerx += self.speed_x
            self.collisions(platforms, self.speed_x, 0)

        if left:
            self.speed_x = -self.speedx
            self.rect.centerx += self.speed_x
            self.collisions(platforms, self.speed_x, 0)
        if up:
            self.speed_y = -self.speedy
            self.rect.centery += self.speed_y
            self.collisions(platforms, 0, self.speed_y)
        if down:
            self.speed_y = self.speedy
            self.rect.centery += self.speed_y
            self.collisions(platforms, 0, self.speed_y)

        if not(left or right or up or down): # стоим, когда нет указаний идти
            self.speed_x = 0
            self.speed_y = 0













    def collisions(self, platforms, speed_x, speed_y):
      for p in platforms:
          if pygame.sprite.collide_rect(self, p):
              if speed_x < 0:
                  self.rect.left = p.rect.right
              elif speed_x > 0:
                  self.rect.right = p.rect.left
              elif speed_y < 0:
                  self.rect.top = p.rect.bottom
              elif speed_y > 0:
                  self.rect.bottom = p.rect.top
