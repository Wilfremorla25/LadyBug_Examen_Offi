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
                
                class Selector(Composite):
                    def execute(self, agent, player):
                        for child in self.children:
                            result = child.execute(agent, player)
                            if result == SUCCESS:
                                return SUCCESS
                            if result == RUNNING:
                                return RUNNING
                            return FAILURE
                        class Sequence(Composite):
                            def execute(self, agent, player):
                                for child in self.children:
                                    result = child.execute(agent, player)
                                    
                                    if result == FAILURE:
                                        return FAILURE
                                    if result == RUNNING:
                                        return RUNNING
                                    return SUCCESS
                                #ACCIONES Y CONDICIONES
                                class Task_CheckPlayerRange(Node):
                                    def __init__(self,range_limit = 5):
                                        super().__init__("CheckRange")
                                        self.range_limit = range_limit
                                        
                                        def execute(self, agent, player):
                                            dist = abs(agent.row - player.row) + abs(agent.col -player.col)
                                            if dist <= self.range_limit:
                                                return SUCCESS
                                            else:
                                                return FAILURE
                                            class Task_PursuePlayer(Node):
                                                # USO DE A* STAR PARA CALCULAR RUTA
                                                def __init__(self, name="Pursue"):
                                                    super().__init__(name)
                                                    
                                                    def execute(self, agent, player):
                                                        #CALCULA RUTA
                                                        agent.calculate_path(player.row, player.col)
                                                        
                                                        if agent.move_along_path():
                                                            return SUCCESS
                                                        else:
                                                            return FAILURE
                                                        
                                                        class Task_Patrol(Node):
                                                            #MOVER AGENTRE ENTRE PUNTOS PREDEFINIDOS
                                                            def __init__(self, points, name="Patrol"):
                                                                super().__init__(name)
                                                                self.patrol_points = points
                                                                self.current_target_index = 0
                                                                
                                                                def execute(self, agent, player):
                                                                    target = self.patrol_points[self.current_target_index]
                                                                    if (agent.row, agent.col) == target_pos:
                                                                        self.current_target_index = (self.current_target_index + 1) % len(self.patrol_points)
                                                                        target_pos = self.patrol_points[self.current_target_index]
                                                                        
                                                                        if not agent.path or agent.path[-1] != target_pos:
                                                                            agent.calculate_path(target_pos[0], target_pos[1])
                                                                            if agent.move_along_path():
                                                                                return RUNNING
                                                                            else:
                                                                                return FAILURE
                                                                        
                                        
            