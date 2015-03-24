__author__ = 'Олег'

import pygame
from pygame import *

WIDTH = 800
HEIGHT = 600
DISPLAY = (WIDTH, HEIGHT)


def main():
    pygame.init()
    screen = display.set_mode(DISPLAY)
    display.set_caption("font")

    background = pygame.Surface(screen.get_size())
    background.fill(Color("#000000"))

    done = False

    #font
    font = pygame.font.Font(None, 25)
    text = font.render("test", True, [100, 100, 100])
    screen.blit(text, (100, 100))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        display.flip()

if __name__ == "__main__": main()