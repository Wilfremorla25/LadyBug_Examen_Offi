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
         
         closed_list = (set) 
         
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
            