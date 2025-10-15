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
        
        def _update_pixel_position(self):
            self.rect.x = self.col * TILE_SIZE
            self.rect.y = self.row * TILE_SIZE
            def calculate_path(self, player_row, player_col):
                start = (self.row, self.col)
                end = (player_row, player_col)
                
                #LLAMAR A* STAR
                self.path = AStar(MAPA_INICIAL, start, end)
                
                def move_along_path(self):
                    if self.path:
                        next_step = self.pop(0)
                        self.row = next_step[0]
                        self.col = next_step[1]
                        self._update_pixel_position()
                        return True
                    return False
        
        