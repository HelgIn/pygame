import pygame
from pygame import *


class Npc(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((20, 20))
        self.image.fill(Color("#a45b7c"))
        self.rect = Rect(x, y, 20, 20)

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self))

    def get_rect(self):
        return self.image