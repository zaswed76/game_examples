
import pygame

pygame.init()
screen = pygame.display.set_mode(
        (500, 500))
class SubSprite:
    def __init__(self, image, width, height):
        self.height = height
        self.width = width
        self.sprite = pygame.image.load(image).convert_alpha()
        self.sprite_rect = self.sprite.get_rect()
        self.w_count = self.sprite_rect.width // self.width
        print(self.w_count)
        self.h_count = self.sprite_rect.height // self.height
        print(self.sprite_rect.width)

    def get_coord(self, n):
        n_y = n // self.w_count
        x = self.width * int(n - (n_y * self.w_count))
        y = self.height * n_y
        return x, y

    def get_sprite(self, n):
        x, y = self.get_coord(n)
        return self.sprite.subsurface((x, y, self.width, self.height))

    def get_sprites(self, s=0, count=None):
        if count is None:
            print(self.h_count, 111)
            print(self.w_count, 'www')
            f = self.w_count * self.h_count
        else: f = s + count + 1
        return [self.get_sprite(x) for x in range(s, f)]

    def get_sprites_back(self, n=None):
        if n is None:
            n = int(self.w_count)
        lst = list(range(n))
        lst.extend(sorted(range(n), reverse=1))
        return [self.get_sprite(x) for x in lst]

    def get_sprite_time(self, s, t):
        return [(x, t) for x in s]

if __name__ == '__main__':
    sub = SubSprite('../images/man.png', 118, 136)
    print(sub.get_sprite(0))