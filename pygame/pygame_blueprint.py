import pygame, sys
from pygame.locals import *

pygame.init()

display = pygame.display.set_mode((400, 700))
pygame.display.set_caption("multipong")

FPS = 24
game_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Keypress example
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pass
    if keys[pygame.K_RIGHT]:
        pass

    pygame.display.update()
    game_clock.tick(FPS)