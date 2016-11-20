import sys
import pygame
from pygame.sprite import Group
class Controller:
    def __init__(self):
        self.controll()

    def controll(self):


       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               sys.exit()

           elif event.type == pygame.MOUSEBUTTONDOWN:
               mouse_x, mouse_y = pygame.mouse.get_pos()
               self.but_click(mouse_x, mouse_y)

    def but_click(self, f, x, y):
        f( x, y)
