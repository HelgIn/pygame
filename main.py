#!/usr/bin/python

import pygame
from pygame.locals import *

from Player import *
from level import *
from Camera import *
from npc import *

WIN_WIDTH = 800
WIN_HEIGHT = 600
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#eeeeee"

HERO_X = 55
HERO_Y = 55


def create_level(screen):
    file = open("level.txt", "r")
    arFile = file.read().split("\n")
    entities = create(screen, arFile)
    level_width = len(arFile[0])
    level_height = len(arFile)
    return level_width, level_height, entities


def main():
    # Initialise screen
    pygame.init()
    screen = display.set_mode(DISPLAY)
    display.set_caption("Game")            

   # create npc
    npc_list = []
    npc = Npc(200, 120)
    npc_list.append(npc)

    # create player
    player = Player(HERO_X, HERO_X, npc)

    # Fill background
    background = pygame.Surface(screen.get_size())    
    background.fill(Color(BACKGROUND_COLOR))             

    #create level
    arLevelSize = create_level(background)
    LEVEL_WIDTH = arLevelSize[0] * 32
    LEVEL_HEIGHT = arLevelSize[1] * 32
    
    entities = arLevelSize[2]
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

        # Move the player if an arrow key is pressed
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_LEFT]:
            player.update(-1, 0)
        if key_press[pygame.K_RIGHT]:
            player.update(1, 0)
        if key_press[pygame.K_UP]:
            player.update(0, -1)
        if key_press[pygame.K_DOWN]:
            player.update(0, 1)
            # if event.type == KEYDOWN and event.key == K_RIGHT:
        #         right = True
        #     if event.type == KEYDOWN and event.key == K_LEFT:
        #         left = True
        #     if event.type == KEYDOWN and event.key == K_UP:
        #         up = True
        #     if event.type == KEYDOWN and event.key == K_DOWN:
        #         down = True
        #     if event.type == KEYUP and event.key == K_RIGHT:
        #         right = False
        #     if event.type == KEYUP and event.key == K_LEFT:
        #         left = False
        #     if event.type == KEYUP and event.key == K_UP:
        #         up = False
        #     if event.type == KEYUP and event.key == K_DOWN:
        #         down = False
        #
        # if player.rect.colliderect(npc.rect):
        #     player.is_moves = False
        #     if up:
        #         up = False
        #     if down:
        #         down = False
        #     if left:
        #         left = False
        #     if right:
        #         right = False

        # player.update(left, right, up, down)
        
        camera.update(player)
        
        for e in entities:
            screen.blit(e.image, camera.apply(e))
                    
        player.draw(screen, camera)
        npc.draw(screen, camera)

        display.flip()

if __name__ == '__main__': main()