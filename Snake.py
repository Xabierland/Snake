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

def gameLoop():
    game_over=False
    game_close=False

    x1=display_w/2
    y1=display_h/2

    x1_change=0
    y1_change=0

    foodx=round(random.randrange(0, display_w - snake_block)/10.0)*10.0
    foody=round(random.randrange(0,display_h-snake_block)/10.0)*10.0

    while not game_over:

        while game_close == True:
            display.fill(white)
            message("¡Has perdido! Presiona Q para salir o R para jugar de nuevo", red)
            pygame().display.update()
            
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_r:
                        gameLoop()


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

        # Dibuja la comida
        pygame.draw.rect(display, blue, [foodx, foody, snake_block, snake_block])

        # Dibuja al jugador
        pygame.draw.rect(display, black, [x1,y1,10,10])

        # Actualiza en cada vuelta del while los graficos
        pygame.display.update()

        # Logica del comer
        if x1==foodx and y1==foody:
            print("Sabroso!")

        # Velocidad del jugador
        clk.tick(snake_speed)
    
    # Cerrar todo
    pygame.quit()
    quit()

gameLoop()