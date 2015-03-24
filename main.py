#!/usr/bin/python

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
    npc1 = Npc(300, 160)
    npc_list.append(npc)
    npc_list.append(npc1)

    # create player
    player = Player(HERO_X, HERO_X, npc_list)

    # Fill background
    background = pygame.Surface(screen.get_size())    
    background.fill(Color(BACKGROUND_COLOR))             

    #create level
    ar_level_size = create_level(background)
    level_width = ar_level_size[0] * 32
    level_height = ar_level_size[1] * 32
    
    entities = ar_level_size[2]
    timer = time.Clock()    
   
    camera = Camera(level_width, level_height)
    
    while 1:
        timer.tick(240)
        
        if player.rect.x + player.rect.width >= level_width:
            right = False 
        if player.rect.x <= 0:
            left = False
        if player.rect.y + player.rect.height >= level_height:
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
        
        camera.update(player)
        
        for e in entities:
            screen.blit(e.image, camera.apply(e))
                    
        player.draw(screen, camera)

        for npc in npc_list:
            npc.draw(screen, camera)

        display.flip()

if __name__ == '__main__': main()