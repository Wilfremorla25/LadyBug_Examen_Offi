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
        
        #POSICION DE FILAS Y COLUMNAS
        self.row = start_row
        self.col = start_col
        self._update_pixels_position()
    def _update_pixels_position(self):
        self.rect.x = self.col * TILE_SIZE
        self.rect.y = self.row * TILE_SIZE
        
    def move(self, dx, dy, maze_map):
        new_col = self.col + dx
        new_row = self.row + dy
        
        #LIMITE DEL MAPA
        if not (0 <= new_row < len(maze_map) and 0 <= new_col < len(maze_map[0])):
            return
        target_tile = maze_map[new_row] [new_col]
        #VERIFICAR COLISIONES
        if target_tile == TILE_WALL:
            return