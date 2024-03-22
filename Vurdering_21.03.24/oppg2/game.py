import pygame, sys
from pygame.locals import *
from random import randint

FPS = 10

PLAYER_SPEED = 30

SIZE = [(50, 50), (100, 50), (150, 50)]
SPEED = [5, 10, 15]

COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 0, 255),
    (255, 255, 0)
    ]

PIECE_POSITION = [(50, 0), (750, 0)]

SCREEN_SCALE = (800, 500)

class ColumnPiece:
    def __init__(self, type: "tuple[int, int]", pos: str) -> None:
        self.speed = SPEED[type[0]]
        self.color = COLORS[type[1]]
        self.size = SIZE[type[0]]

        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.color)

        self.rect = self.surface.get_rect(topleft = PIECE_POSITION[0]) if pos == "left" else self.surface.get_rect(topright = PIECE_POSITION[1])

    def move(self):
        self.rect.y += self.speed

    def check_collision(self, player_rect: pygame.Rect, floor_rect: pygame.Rect) -> "list[bool, bool]":
        """Checks if the piece collides with the player or the floor

        Args:
            player_rect (pygame.Rect): The rect of the player object
            floor_rect (pygame.Rect): The rect of the floor object

        Returns:
            list[bool, bool]: The first element is if the piece has collided with something and should be deleted, the second element is if the piece has collided with the player
        """
        if self.rect.colliderect(player_rect):
            column_add.add_column_piece(self.size, self.color)
            return [True, True]
        if self.rect.colliderect(floor_rect):
            return [True, False]

        return [False, False]

class Column:
    def __init__(self, bottom_center: "tuple[int, int]"):
        self.bottom_center = bottom_center
        self.surfaces = []
        self.rects = []
        self.height = 0
    
    def add_column_piece(self, size, color):
        self.surfaces.append(pygame.Surface((size[1], size[0])))
        self.surfaces[-1].fill(color)

        mid_bottom = (self.bottom_center[0], self.bottom_center[1] - self.height)
        self.rects.append(self.surfaces[-1].get_rect(midbottom = mid_bottom))

        self.height += size[0]
    
    def draw(self):
        for i, surf in enumerate(self.surfaces):
            display.blit(surf, self.rects[i])

    def get_height(self) -> int:
        return self.height
        
pygame.init()

try:
    hi_score_file = open("hi_score.txt", "r")

    for line in hi_score_file:
        player, hi_score = line.strip().split(";")

    hi_score_file.close()
except:
    print("Could not find high score file")

    hi_score = 0
    player = "No one"

display = pygame.display.set_mode(SCREEN_SCALE)
pygame.display.set_caption("multipong")

game_clock = pygame.time.Clock()

columns = [Column((325, 500)), Column((475, 500))]
column_add = columns[1]
columns_finished = 0

pieces_falling = [
    ColumnPiece((randint(0, 2), randint(0, 4)), "left"),
    ColumnPiece((randint(0, 2), randint(0, 4)), "right")
    ]

floor = pygame.Surface((SCREEN_SCALE[0], 10))
floor_rect = floor.get_rect(center = (SCREEN_SCALE[0]/2, SCREEN_SCALE[1]))

player_surf = pygame.image.load("player_stand.png")
player_rect = player_surf.get_rect(midbottom = (400, 500))

lives = 3

gamefont = pygame.font.Font("Pixeltype.ttf", 250)
text_surface = gamefont.render(f'{lives}', True, (255, 255, 255))
text_rect = text_surface.get_rect(center = (400, 250))

gamefont_small = pygame.font.Font("Pixeltype.ttf", 50)
hi_score_text_surface = gamefont_small.render(f'High score: {hi_score} by {player}', True, (255, 255, 255))
hi_score_text_rect = text_surface.get_rect(center = (400, 100))

game_won = False
game_over = False
game_finish_counter = 2
while game_finish_counter > 0:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display.fill((0, 0, 0))
    display.blit(floor, floor_rect)
    for column in columns:
        column.draw()
    
    display.blit(text_surface, text_rect)
    display.blit(hi_score_text_surface, hi_score_text_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED

    display.blit(player_surf, player_rect)

    for i, piece in enumerate(pieces_falling):
        piece.move()
        delete, hit_player = piece.check_collision(player_rect, floor_rect)
        display.blit(piece.surface, piece.rect)
    
        if delete is True:
            pieces_falling[i] = ColumnPiece(
                (randint(0, 2), randint(0, 4)),
                "left" if i == 0 else "right")
            
            if hit_player is not True:
                lives -= 1

                text_surface = gamefont.render(f'{lives}', True, (255, 255, 255))
                text_rect = text_surface.get_rect(center = (400, 250))

    if column_add.get_height() >= 500 and columns_finished == 0:
        column_add = columns[0]
        columns_finished += 1
    elif (column_add.get_height() >= 500 and columns_finished == 1):
        game_won = True

        score = 0
        for column in columns:
            score += column.get_height()
    
    if lives <= 0:
        game_over = True

        score = 0
        for column in columns:
            score += column.get_height()

    if (game_won is True or game_over) and game_finish_counter >= 0:
        game_finish_counter -= 1

    if game_over:
        text_surface = gamefont.render(f'Game Over', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center = (400, 250))
    
    if game_won:
        text_surface = gamefont.render(f'WINNER!', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center = (400, 250))

    pygame.display.update()
    game_clock.tick(FPS)

if score > int(hi_score):
    player_name = input("You beat the high score, input your playertag: ")

    file = open("hi_score.txt", "w")

    file.write(f'{player_name};{score}')