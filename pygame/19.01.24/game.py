import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
game_clock = pygame.time.Clock()

display = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("game.py")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    game_clock.tick(FPS)
