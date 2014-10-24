#!/usr/bin/env python

from pygame import *


MOVE_SPEED = 1
WIDTH = 22
HEIGHT = 32
COLOR =  "#000000"

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)

    def update(self,  left, right, up, down):
        
        if (left and (up or down)) or (right and (up or down)):
            left = up = right = down = False            
        if left:
            self.xvel = -MOVE_SPEED 
        if right:
            self.xvel = MOVE_SPEED         
        if up:
            self.yvel = -MOVE_SPEED            
        if down:
            self.yvel = MOVE_SPEED             
        if not(left or right):
            self.xvel = 0                        
        if not(up or down):
            self.yvel = 0                    

        self.rect.x += self.xvel 
        self.rect.y += self.yvel
   
    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self))
        
    def get_rect(self):
        return  self.image
    