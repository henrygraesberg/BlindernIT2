import pygame, sys
from pygame.locals import *

class Ball:
    def __init__(self,
                 color = "Tuple[int, int, int]",
                 start_pos = "Tuple[int,int]",
                 start_velo = "list[int,int]"
                 ):
        self.surface = pygame.Surface((25, 25))
        self.surface.fill(color)
        self.rect = self.surface.get_rect(center = start_pos)
        self.velo = start_velo

    def move(self,
             wall_list: list,
             roof: pygame.rect,
             floor: pygame.rect,
             player: pygame.rect):
        hit_player = False
        if self.rect.colliderect(roof):
            self.velo[1] = -self.velo[1]

        if self.rect.colliderect(player):
            self.velo[1] = - self.velo[1]
            hit_player = True

        if self.rect.collidelist(wall_list) != -1:
            self.velo[0] = -self.velo[0]
            
        if self.rect.colliderect(floor):
            del self
            return
        
        self.rect.x += self.velo[0]
        self.rect.y += self.velo[1]

        return hit_player

pygame.init()

display = pygame.display.set_mode((400, 700))
pygame.display.set_caption("multipong")

FPS = 24
game_clock = pygame.time.Clock()

player_surf = pygame.Surface((100, 50))
player_surf.fill((255, 0, 0))
player_rect = player_surf.get_rect(center = (200, 700))

walls_surf = [
    pygame.Surface((10, 700)),
    pygame.Surface((10, 700))
]

walls_surf[0].fill((255, 255, 255))
walls_surf[1].fill((255, 255, 255))

walls_rect = [walls_surf[0].get_rect(),
         walls_surf[1].get_rect(topright = (400, 0))]

floor = pygame.Surface((800, 10))
floor.fill((255, 255, 255))
floor_rect = floor.get_rect(midbottom = (0, 700))
roof = pygame.Surface((800, 10))
roof.fill((255, 255, 255))
roof_rect = roof.get_rect()

balls = [Ball((255, 0, 255), (350, 30), [10, 10])]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display.fill((0, 0, 0))
    display.blit(walls_surf[0], walls_rect[0])
    display.blit(walls_surf[1], walls_rect[1])
    display.blit(floor, floor_rect)
    display.blit(roof, roof_rect)
    display.blit(player_surf, player_rect)

    for ball in balls:
        display.blit(ball.surface, ball.rect)
        ball.move(walls_rect, roof_rect, floor_rect, player_rect)

    pygame.display.update()
    game_clock.tick(FPS)
