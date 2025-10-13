import pygame
import sys

#INICIALIZACION
pygame.init()

#CONFIGURACION DE PANTALLA Y RELOJ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#PATALLA COMPLETA
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Lady Bug Game")
