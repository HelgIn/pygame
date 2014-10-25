
import pygame
from pygame.locals import *
from Platform import *

def create(background, ar):
    entities = pygame.sprite.Group()
    x = y = 0
    for row in ar:
        for col in row:
            if col == "g":
                block = Platform("ground.bmp", x, y)
                #background.blit(block, (x, y))
            if col == "t":
                block = Platform("gr1.bmp", x, y)
                #background.blit(block, (x, y))
            entities.add(block)
            x += block.get_width()
        y += block.get_height()            
        x = 0
    return entities
                

