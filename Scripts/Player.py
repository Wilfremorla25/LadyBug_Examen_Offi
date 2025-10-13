import pygame
from .Maze import TILE_SIZE, TILE_WALL, TILE_COLLECTIBLE, TILE_DINAMIC, switch_dynamic_block

#NOMBRE = WILFRI A. DE MORLA
#MATRICULA = 23-SISN-2-025

class Player(pygame.sprite.Sprite):
    def __init__(self, start_row, start_col):
        super().__init__()
        
        #DEFINICON DEL SPRITE
        self.image = pygame.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()