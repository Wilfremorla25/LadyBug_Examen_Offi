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

#VELOCIDAD DE JUEGO
clock = pygame.time.Clock()
FPS = 60

#FUNCION DE JUEGO
def game_loop():
    running = True
    while running:
        
  #EVENTOS
     for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        #SALIR CON ESC
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                #LOGICA DEL JUEGO
                #DIBUJO
                screen.fill((0, 0, 0))
                #CONTROL DE FPS
                pygame.display.flip()
                clock.tick(FPS)
                #SALIR
                pygame.quit()
                sys.exit()
                #EJECUCION DE CODIGO
                if __name__ == "__main__":
                    game_loop()