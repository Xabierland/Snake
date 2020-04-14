# Script creado el 11/04/2020 por Xabier Gabiña ak.Xabierland
# Mi Github: https://github.com/Xabierland
# Mi Twitter: https://twitter.com/Xabierland
# Mi Instagram: https://www.instagram.com/xabierland/

#Basado en https://www.edureka.co/blog/snake-game-with-pygame/

import pygame
import time
import random
import os

# Inicializacion del juego
pygame.init()

# Inicializacion de la pantalla
display_w=600
display_h=400

display=pygame.display.set_mode((display_w, display_h))

pygame.display.update()
pygame.display.set_caption('Snake by Xabier Gabiña')

# Inicializacion del personaje
snake_block=10  # Tamaño del jugador
snake_speed=15  # Velocidad del juegador

# Colores
white=(255,255,255)
black=(0,0,0)
blue=(50,153,213)
red=(255,0,0)
yellow=(255,255,102)
green=(0,255,0)
dark_green=(51,102,0)

# Reloj interno del juego
clk = pygame.time.Clock()

# Tipo de fuente
font_style=pygame.font.SysFont("bahnschrift",15)
score_font=pygame.font.SysFont("comicsansms",35)

# La logica de la puntuacion
def your_score(score):
    value = score_font.render("Tu puntuacion: " + str(score), True, yellow)
    display.blit(value, [0, 0])

# La logica de la serpiente
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

# La logica de los mensajes
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_w/6, display_h/3])

#============================================================================================================================================================================================================================================#
# Logica del juego

def gameLoop():
    # Inicializa las dos varibles para finalizar el juego y cerrar el juego
    game_over=False
    game_close=False

    # Logica de inicializacion de la posicion del jugador
    x1=display_w/2
    y1=display_h/2

    x1_change=0
    y1_change=0

    #Logica para generar el cuerpo de la serpiente
    snake_List=[]
    Lenght_of_snake=1

    # Velocidad del juegador
    snake_speed=15  

    # Inicializa las variables CHEAT CODE
    CHEAT_INV=False

    #Logica que genera los bloques de comida
    foodx=round(random.randrange(0, display_w - snake_block)/10)*10
    foody=round(random.randrange(0,display_h-snake_block)/10)*10

    # Todo lo que ocurre durante el juego
    while not game_over:

        # Logica del cierre del juego
        while game_close == True:
            display.fill(dark_green)
            message("¡Has perdido! Presiona Q para salir o R para jugar de nuevo", red)
            your_score(Lenght_of_snake-1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:     # Cerrar el juego por boton
                    game_over=True
                    game_close=False
                if event.type==pygame.KEYDOWN:  # Cerrar el juego
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_r:   # Reiniciar el juego
                        gameLoop()


        for event in pygame.event.get():    # Se registra cualquier cambio, ya sea de raton, teclado o en la pantalla
            # Se activa cuando se pulsa el boton de cerrar
            if event.type==pygame.QUIT:     # Logica del cierre del juego
                game_over=True
            
            # Se activa cuando se detecta la pulsacion de una tecla
            if event.type==pygame.KEYDOWN:  # Logica del movimiento de la serpiente
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

                # Cheat CODE
                if event.key == pygame.K_F7:    # INVIERTE EL JUEGO
                    CHEAT_INV=True
                if event.key == pygame.K_F8:    # DESINVIERTE EL JUEGO
                    CHEAT_INV=False
                if event.key == pygame.K_F9:    # MAS VELOCIDAD
                    snake_speed+=10
                if event.key == pygame.K_F10:   # MENOS VELOCIDAD
                    snake_speed-=10
                if event.key == pygame.K_F11:   # AUMENTAR PUNTUACION
                    Lenght_of_snake+=1
                if event.key == pygame.K_F12:   # DIMINUIR PUNTUACION
                    Lenght_of_snake-=1

        # Condicion de derrota - Salirse del mapa
        if x1>=display_w or x1<0 or y1>=display_h or y1<0:
            game_close=True
            pygame.mixer.music.load('util\dead.mp3')
            pygame.mixer.music.play()

        # Actualizacion del movimiento del juegador
        if not CHEAT_INV:
            x1 += x1_change
            y1 += y1_change
        else:
            x1 -= x1_change
            y1 -= y1_change
        
        # Rellena el tablero de juego
        display.fill(dark_green)

        # Dibuja la comida
        pygame.draw.rect(display, white, [foodx, foody, snake_block, snake_block])

        # Dibuja al jugador
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List)> Lenght_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x==snake_Head:
                game_close=True

        our_snake(snake_block, snake_List)
        your_score(Lenght_of_snake-1)

        # Actualiza en cada vuelta del while los graficos
        pygame.display.update()

        # Logica del comer
        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0, display_w - snake_block)/10)*10
            foody=round(random.randrange(0,display_h-snake_block)/10)*10
            Lenght_of_snake+=1
            # Logica del sonido de comer
            pygame.mixer.music.load('util\eat.mp3')
            pygame.mixer.music.play()
            # Aumentar Velocidad al comer
            snake_speed+=0.1

        # Velocidad del jugador
        clk.tick(snake_speed)
    
    # Cerrar todo
    pygame.quit()
    quit()

gameLoop()

# VERSION 1.3 Ult.edicion 14/04/2020