#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, os

class Animation:
    def __init__(self, sprites=None, time=100):
        self.sprites = sprites
        self.time = time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0
        if type(time) == list:
            self.__update = self.__update_any_time
        else:
            self.__update = self.__update_const_time

    def update(self, dt):
        self.work_time += dt
        self.__update(dt)

    def __update_const_time(self, dt):
        self.skip_frame = int(self.work_time / self.time)
        if self.skip_frame > 0:
            self.work_time = self.work_time % self.time
            self.frame += self.skip_frame
            if self.frame >= len(self.sprites):
                self.frame = 0

    def __update_any_time(self, dt):
        while self.work_time - self.time[self.frame] > 0:
            self.work_time -= self.time[self.frame]
            self.frame += 1
            if self.frame >= len(self.sprites):
                self.frame = 0

    def get_sprite(self):

        return self.sprites[self.frame]

if __name__ == '__main__':
    pygame.init()

    display = pygame.display.set_mode((132*5,132))

    screen = pygame.Surface((16*5,16))

    robots = list()
    time = 180
    sprite = pygame.image.load('../images/robot.png').convert_alpha()

    # Создание анимации.
    for x in range(5):
        anim = list()
        offset = 16*x

        anim.append(sprite.subsurface((0, offset,16,16)))
        anim.append(sprite.subsurface((16,offset,16,16)))
        anim.append(sprite.subsurface((32,offset,16,16)))
        anim.append(sprite.subsurface((16,offset,16,16)))

        if x == 4:
            robots.append(Animation(anim, [2000, 150, 150, 150]))
        else:
            robots.append(Animation(anim, time))

    clock = pygame.time.Clock()

    done = False
    dt = 0
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True

        # Обновление каждого объекта анимации
        for robot in robots:
            robot.update(dt)

        screen.fill((255,255,255))

        # Рисуем анимацию.
        x = 0
        for robot in robots:
            screen.blit(robot.get_sprite(), (x, 0))
            x += 16

        display.blit(pygame.transform.scale(screen,(32*5,32)),(0,0))
        pygame.display.flip()

        dt = clock.tick(40)