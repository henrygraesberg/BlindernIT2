import pygame, sys
from pygame.locals import *
from random import randint

class Food:
    def __init__(self, pos: "tuple[int, int]"):
        self.surface = pygame.Surface((25, 25))
        self.surface.fill((255, 0, 0))
        self.rect = self.surface.get_rect(center=pos)

    def check_eaten(self, player_rect) -> bool:
        return self.rect.colliderect(player_rect)

class Player:
    def __init__(self, pos: "tuple[int, int]"):
        self.surface = pygame.Surface((25, 25))
        self.surface.fill((0, 255, 0))
        self.rect = self.surface.get_rect(center = pos)
        self.velo = [25, 0]

    def move(self, direction: str):
        directions = {
            "up": [0, -25],
            "down": [0, 25],
            "left": [-25, 0],
            "right": [25, 0]
        }

        self.velo = directions[direction]

        self.rect.x += self.velo[0]
        self.rect.y += self.velo[1]

        if self.rect.collidelist(BORDERS_RECT) != -1:
            del self
            return True
        
        return False

pygame.init()

display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("nesten snake")

FPS = 5
game_clock = pygame.time.Clock()

score = 0

direction = "right"

stop_gameloop = False

player = Player((250, 250))

gamefont = pygame.font.Font("font/Pixeltype.ttf", 36)
text_surface = gamefont.render(f'Score: {score}', True, (255, 255, 255))
text_rect = text_surface.get_rect(center = (250, 50))

BORDERS_SURF = [
    pygame.Surface((25, 500)),
    pygame.Surface((25, 500)),
    pygame.Surface((500, 25)),
    pygame.Surface((500, 25))
]
BORDERS_RECT = [
    BORDERS_SURF[0].get_rect(),
    BORDERS_SURF[1].get_rect(topright = (500, 0)),
    BORDERS_SURF[2].get_rect(bottomleft = (0, 500)),
    BORDERS_SURF[3].get_rect()
]

for border in BORDERS_SURF:
    border.fill((100, 100, 100))

food = Food((randint(50, 450), randint(50, 450)))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = "up"
    if keys[pygame.K_DOWN]:
        direction = "down"
    if keys[pygame.K_LEFT]:
        direction = "left"
    if keys[pygame.K_RIGHT]:
        direction = "right"

    if stop_gameloop is not True:
        stop_gameloop = player.move(direction)

    if food.check_eaten(player.rect):
        score += 1
        text_surface = gamefont.render(f'Score: {score}', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center = (250, 50))

        food = Food((randint(50, 450), randint(50, 450)))
        
    display.fill((0, 0, 0))
    for i in range(len(BORDERS_SURF)):
        display.blit(BORDERS_SURF[i], BORDERS_RECT[i])
    display.blit(player.surface, player.rect)
    display.blit(food.surface, food.rect)
    display.blit(text_surface, text_rect)

    pygame.display.update()
    game_clock.tick(FPS)
