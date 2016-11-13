import csv

from tank.platform import Platform
import pygame
from pygame.sprite import Group


# noinspection PyTupleAssignmentBalance
def create_level(cfg, platforms, targets, screen):
    x = y = 0

    map = get_map(cfg.map)
    print(map)
    for line in map:
        for object in line:
            print(cfg.wall[0])
            if object == cfg.wall[0]:
                print('wall')
                platform = Platform(x, y, cfg.wall[1], screen)
                platforms.add(platform)
            if object == cfg.target[0]:
                target = Platform(x, y, cfg.target[1], screen)
                targets.add(target)

            x += 32
        y += 32
        x = 0


def get_map(map):
    reader = csv.reader(open(map), delimiter=',', quotechar='"')
    return ([x for x in reader])