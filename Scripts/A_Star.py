#NOMBRE = WILFRI A. DE MORLA
#MATRICULA = 23-SISN-2-025
import math
#EVITAR PARED
from .Maze import TILE_WALL, TILE_PATH

class Node:
    def __init__(self, parent = None, position = None):
        self.parent = parent 
        self.position = position
        
        #COSTOS DE A* STARS
        self.g = 0
        self.h = 0
        self.f = 0
        
        def __eq__(self, other):
            return self.position == other.position
        
        def AStar(maze_map, start_pos, end_pos):
            
            #INICIALIZACION DE A* STAR
            start_node = Node(None, start_pos)
            end_node = Node(None, end_pos)
            
            open_list = [start_node]
            
            # CORREGIDO
            closed_list = set() 
            
            while open_list:
                current_node = min(open_list, key=lambda node: node.f)
                open_list.remove(current_node)
                closed_list.add(current_node.position)
                
                #PRUEBA DE META
                if current_node.position == end_pos:
                    path = []
                    current = current_node
                    while current is not None:
                         path.append(current.position)
                         current = current.parent
                         return path[::-1][1:]
                         
                #GENERAR NODOS VECINOS
                neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                for new_position in neighbors:
                    node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                    map_rows = len(maze_map)
                    map_cols = len(maze_map[0])
                    
                    #VALIDACION DE LIMITAS
                    if not (0 <= node_position[0] < map_rows and 0 <= node_position[1] < map_cols):
                         continue
                    
                    #Si, ES PARED NO SE PUEDE PASAR
                    if maze_map[node_position[0]][node_position[1]] == TILE_WALL:
                         continue
                         
                    #NO, EVALUAR NODO CERRADOS 
                    if node_position in closed_list:
                         continue
