import csv

from tank.platform import Platform
import pygame
from pygame.sprite import Group


# noinspection PyTupleAssignmentBalance
def create_level(cfg, platforms, targets, screen):
    x = y = 0
    all = []
    sprite = {}

    map = get_map(cfg['map'])
    print(map)
    for line in map:
        for name in line:
            sprite[name] = Platform(x, y, cfg[name][0], screen)
            all.append(sprite[name])



def get_map(map):
    reader = csv.reader(open(map), delimiter=',', quotechar='"')
    return ([x for x in reader])