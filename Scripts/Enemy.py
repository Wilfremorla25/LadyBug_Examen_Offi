import pygame 
from .Maze import TILE_SIZE, MAPA_INICIAL
from .A_Star import AStar

#NOMBRE = WILFRI A. DE MORLA
#MATRICULA = 23-SISN-2-025

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, start_row, start_col):
        super().__init__()
        
    #ASPECTO
        self.image = pygame.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill((255, 0, 0))#RED ENEMYS
        self.rect = self.image.get_rect()
        
    #POSICION INICIAL
        self.row = start_row
        self.col = start_col
        self._update_pixel_position()
        self.path = []
        #VELOCIDAD MAS LENTA QUE EL JUGADOR
        self.move_counter = 0
        self.move_frequency = 15
        
        def _
        
        