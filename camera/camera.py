import sys
import pygame
from pygame.sprite import Sprite

WIDTH = 500
HEIGHT = 500
BG_COLOR = (250, 250, 250)

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIDTH / 2, -t+HEIGHT / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIDTH), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return pygame.Rect(l, t, w, h)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen_rect = screen.get_rect()
    pygame.display.set_caption('camera test')
    timer = pygame.time.Clock()
    right = False
    while 1: # Основной цикл программы

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print('>>>')
                    right = True
        timer.tick(60)
        screen.fill(BG_COLOR)
        pygame.display.flip()

run_game()
