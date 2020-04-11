# Script creado el 11/04/2020 por Xabier Gabiña ak.Xabierland
# Mi Github: https://github.com/Xabierland
# Mi Twitter: https://twitter.com/Xabierland
# Mi Instagram: https://www.instagram.com/xabierland/

#Basado en https://www.edureka.co/blog/snake-game-with-pygame/

import pygame
import time
import random

# Inicializacion del juego
pygame.init()

# Inicializacion de la pantalla
display_w=800
display_h=600

display=pygame.display.set_mode((display_w, display_h))

pygame.display.update()
pygame.display.set_caption('Snake by Xabier Gabiña')

# Inicializacion del personaje
x1=display_w/2
y1=display_h/2

x1_change=0
y1_change=0

snake_block=10  # Tamaño del jugador
snake_speed=30  # Velocidad del juegador

# Colores
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
red=(255,0,0)

# Reloj interno del juego
clk = pygame.time.Clock()

# Logica del scoreboard
font_style=pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_w/2, display_h/2])

#============================================================================================================================================================================================================================================#
# Logica del juego
game_over=False

while not game_over:
    for event in pygame.event.get():    # Se registra cualquier cambio, ya sea de raton, teclado o en la pantalla
        if event.type==pygame.QUIT:     # Se activa cuando se pulsa el boton de cerrar
            game_over=True
        if event.type==pygame.KEYDOWN:  # Se activa cuando se detecta la pulsacion de una tecla
            # Logica del movimiento de la serpiente
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            if event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            if event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            if event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    # Condicion de derrota - Salirse del mapa
    if x1>=display_w or x1<0 or y1>=display_h or y1<0:
        game_over=True

    # Actualizacion del movimiento del juegador
    x1 += x1_change
    y1 += y1_change
    
    # Rellena el tablero de juego
    display.fill(white)

    # Dibuja al jugador
    pygame.draw.rect(display, black, [x1,y1,10,10])

    pygame.display.update()

    clk.tick(snake_speed)

#Imprime el mensaje de derrota
message("Has perdido", red)
pygame.display.update()
time.sleep(2)

# Cerrar todo
pygame.quit()
quit()