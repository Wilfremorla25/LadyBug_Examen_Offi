#NOMBRE = WILFRI A. DE MORLA
#MATRICULA = 23-SISN-2-025

import math
#ESTADOS
SUCCESS = 1
FAILURE = 2
RUNNING = 3

class Node:
    def __init__(self, name=""):
        self.name = name
        
        def execute(self, agent, player):
            raise NotImplementedError("El metodo execute debe ser implementado por la subclase")
        
        class Composite(Node):
            #CLASE PARA NODOS CON HIJOS
            def __init__(self, children= None, name=""):
                super().__init__(name)
                self.children = children if children is not None else []
            