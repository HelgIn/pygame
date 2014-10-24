#!/usr/bin/python

import pygame
from pygame.locals import *

import Player
from Player import *

import level
from level import *

from Camera import *

WIN_WIDTH = 800
WIN_HEIGHT = 600
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#eeeeee"

HERO_X = 55
HERO_Y = 55

def create_level(screen):
    file = open("../level.txt", "r")
    arFile = file.read().split("\n")
    entities = level.create(screen, arFile)
    level_width = len(arFile[0])
    level_height = len(arFile)
    return level_width, level_height, entities


def main():
    # Initialise screen
    pygame.init()
    screen = display.set_mode(DISPLAY)
    display.set_caption("Game")            
   
    # create player
    player = Player(HERO_X, HERO_X) 
    left = right = up = down = False
    
    # Fill background
    background = pygame.Surface(screen.get_size())    
    background.fill(Color(BACKGROUND_COLOR))             

    #create level
    arLevelSize = create_level(background)
    LEVEL_WIDTH = arLevelSize[0] * 32
    LEVEL_HEIGHT = arLevelSize[1] * 32
    
    entities = arLevelSize[2]
    #entities.add(player)
    timer = time.Clock()    
   
    camera = Camera(LEVEL_WIDTH, LEVEL_HEIGHT) 
    
    while 1:
        timer.tick(240)
        
        if player.rect.x + player.rect.width >= LEVEL_WIDTH:
            right = False 
        if player.rect.x <= 0:
            left = False
        if player.rect.y + player.rect.height >= LEVEL_HEIGHT:
            down = False 
        if player.rect.y <= 0:
            up = False  
        
        for event in pygame.event.get():                        
            if event.type == QUIT:
                return
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
            if event.type == KEYDOWN and event.key == K_UP:
                up = True
            if event.type == KEYDOWN and event.key == K_DOWN:
                down = True            
            if event.type == KEYUP and event.key == K_RIGHT:
                right = False
            if event.type == KEYUP and event.key == K_LEFT:
                left = False
            if event.type == KEYUP and event.key == K_UP:
                up = False
            if event.type == KEYUP and event.key == K_DOWN:
                down = False                                        
     
        
        
        #screen.blit(background, camera.apply(background))  
        player.update(left, right, up, down)              
        
        camera.update(player)
        
        for e in entities:
            screen.blit(e.image, camera.apply(e))
                    
        player.draw(screen, camera)
        display.flip()

if __name__ == '__main__': main()