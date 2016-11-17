import json

import pygame
from pygame.sprite import Sprite

class AbsSprite(Sprite):
    def __init__(self, screen, image, alpha=False, *groups):
        super().__init__(*groups)
        if alpha:
            self.image = pygame.image.load(image).convert_alpha()
        else:
            self.image = pygame.image.load(image).convert()
        self.screen = screen
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Background(AbsSprite):
    def __init__(self, screen, image, alpha=False, *groups):
        super().__init__(screen, image, alpha, *groups)






class Layers:
    def __init__(self):
        """

        """
        pass


class MapParser:
    def __init__(self, level_map):
        self.level_map = self.get_level(level_map)
        self.layers = self.level_map['layers']
        self.tilewidth = self.level_map['tilewidth']
        self.bg_image = None

        self.parse_layers()

    def parse_layers(self):
        for layer in self.layers:
            if layer['type'] == 'imagelayer':
                self.bg_image = layer['image']



    def get_level(self, level_map):
        with open(level_map, "r") as f:
            return json.load(f)

    def print(self):
        for k, i in self.level_map.items():
            print(k, i, sep=' = ')

    def print_layers(self):
        for lay in self.level_map['layers']:
            print(lay)
            print('------------------')



class LevelMap:
    def __init__(self, level, screen):
        self.image_background = None
        self.screen = screen
        self.map_parser = MapParser(level)

    def create_background(self):
       return Background(self.screen, self.map_parser.bg_image)



if __name__ == '__main__':
    import os
    import paths
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((150, 150))
    pth_map = os.path.join(paths.maps, 'test_num_5.json')
    mp = LevelMap(pth_map, screen)
    # mp.map_parser.print()
    # mp.map_parser.print_layers()
    print(mp.map_parser.bg_image)