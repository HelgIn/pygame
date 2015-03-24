#!/usr/bin/env python

from pygame import *


MOVE_SPEED = 1
WIDTH = 22
HEIGHT = 32
COLOR = "#000000"


class Player(sprite.Sprite):
    def __init__(self, x, y, npc_list):
        sprite.Sprite.__init__(self)
        self.start_x = x
        self.start_y = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.npc_list = npc_list

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        index = self.rect.collidelist(self.npc_list)
        if index > -1:
            if dx > 0:
                self.rect.right = self.npc_list[index].rect.left
            if dx < 0:
                self.rect.left = self.npc_list[index].rect.right
            if dy > 0:
                self.rect.bottom = self.npc_list[index].rect.top
            if dy < 0:
                self.rect.top = self.npc_list[index].rect.bottom

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self))

    def get_rect(self):
        return self.image