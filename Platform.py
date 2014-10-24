#!/usr/bin/env python

import pygame
from pygame import *

PLATFORM_WIDTH = PLATFORM_HEIGHT = 32


PLATFORM_COLOR = "#000001";

class Platform(sprite.Sprite):
    def __init__(self, file, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load(file)             
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    
    def get_width(self):
        return PLATFORM_WIDTH
    
    def get_height(self):
        return PLATFORM_HEIGHT