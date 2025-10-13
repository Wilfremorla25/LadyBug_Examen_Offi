#NOMBRE = WILFRI A. DE MORLA
#MATRICULA = 23-SISN-2-025
import math
#EVITAR PARED
from .Maze import TILE_WALL, TILE_PATH

class Node:
    def __init__(self, parent = None, position = None):
        self.parent = parent