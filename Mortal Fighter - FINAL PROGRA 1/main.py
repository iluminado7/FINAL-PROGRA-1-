import pygame
import pygame.mixer as mixer
from fighter import Fighter
import json
from cargar_ranking import cargar_ranking
from menu_principal import mostrar_pantalla_inicial
from guardar_ranking import guardar_ranking
from actualizar_ranking import actualizar_ranking
from mostrar_ranking import mostrar_ranking
from barra_de_vida import dibujar_barra_de_vida
from fondo import dibujar_fondo
from texto import dibujar_texto
from pantalla_de_usuario import pantalla_carga_usuario

pygame.init()
mixer.init()
pygame.display.set_caption("Mortal Fighter")
PANTALLA_WIDTH = 1000
PANTALLA_HEIGHT = 600
screen = pygame.display.set_mode((PANTALLA_WIDTH, PANTALLA_HEIGHT))
clock = pygame.time.Clock()   
FPS = 80   
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
BLANCO = (255, 255, 255)

#las variables para el desarrollo de la partida
intro_count = 4   #los segundos antes de iniciar la pelea
last_count_update = pygame.time.get_ticks()
score = [0, 0]
round_over = False #bandera de la finalizacion de round
ROUND_OVER_COOLDOWN = 2000 
ROUND_TIME_FIGHT = 180000

#Define las variables del guerrero y el mago
WARRIOR_SIZE = 162 
WARRIOR_SCALE = 4  
WARRIOR_OFFSET = [72, 47] #ajusta el sprite para alinearlo correctamente con el mago
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET] 
WIZARD_SIZE = 250 
WIZARD_SCALE = 3 
WIZARD_OFFSET = [112, 98] #ajusta el sprite para alinearlo correctamente con el guerrero
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET] 

#Musica y sonidos
pygame.mixer.music.load("assets/audio/music2.mp3") 
pygame.mixer.music.set_volume(0.75) #ajusta el volumen
pygame.mixer.music.play(-1, 0.0, 5000) #reproduce un bucle con desvanecimiento de 5 segundos
sword_fx = pygame.mixer.Sound("assets/audio/sword.wav") #carga sonido de la espada
sword_fx.set_volume(0.75) 
magic_fx = pygame.mixer.Sound("assets/audio/magic.wav") #carga sonido del hechizo 
magic_fx.set_volume(0.90)

# imagen de fondo
escenario = pygame.image.load("assets/imagenes/background/bg3.jpg").convert_alpha() 

# spritesheets de los personajes
warrior_sheet = pygame.image.load("assets/imagenes/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/imagenes/wizard/Sprites/wizard.png").convert_alpha()

#Icono de victoria
victory_img = pygame.image.load("assets/imagenes/icons/victory.png").convert_alpha()

#define la cantidad de fotogramas para cada animacion 
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

#define las fuentes
count_font = pygame.font.Font("assets/fonts/turok.ttf", 80) #Fuente grande para el contador.
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30) #Fuente chica para el puntaje.

#crea a los luchadores en base a la clase Fighter del modulo fighter
fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)  #guerrero
fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)  #mago

# Variable para controlar el estado del juego (True: en pantalla del tutorial, False: juego principal).
pantalla_inicial = True
button_font = pygame.font.Font("assets/fonts/turok.ttf", 50)  
button_text = "CLICK PARA EMPEZAR"
button_color = (255, 0, 0)  # Rojo para resaltar
button_hover_color = (200, 0, 0)  # Color al pasar el mouse
button_rect = pygame.Rect(250, 400, 500, 60) 
mostrar_pantalla_inicial(screen,score_font,PANTALLA_HEIGHT, PANTALLA_WIDTH, button_hover_color, button_color, button_font) 

# Ruta del archivo de ranking
RANKING_FILE = "ranking.txt"

# Cargar ranking desde archivo
ranking_cargado = cargar_ranking(RANKING_FILE)
      
# Fuentes para la pantalla de carga
input_font = pygame.font.Font("assets/fonts/turok.ttf", 40)
# Pantalla de carga de usuario
nombre_j1 = pantalla_carga_usuario(screen, input_font, RANKING_FILE, "Jugador 1: Ingrese su nombre", dibujar_texto,cargar_ranking,guardar_ranking)
nombre_j2 = pantalla_carga_usuario(screen, input_font, RANKING_FILE, "Jugador 2: Ingrese su nombre",dibujar_texto,cargar_ranking,guardar_ranking)
#actualizar el ranking en base a los nombres cargados
from actualizar_ranking import actualizar_ranking
ranking_jugador_1 = actualizar_ranking(ranking_cargado, nombre_j1, guardar_ranking(ranking_cargado, RANKING_FILE))
ranking_jugador_2 = actualizar_ranking(ranking_cargado, nombre_j2, guardar_ranking(ranking_cargado, RANKING_FILE))


# Bucle del juego
run = True  
while run:
    clock.tick(FPS)  
    
    # Pantalla del tutorial
    if pantalla_inicial:
        # Mostrar pantalla inicial y recibir rectangulos de botones
        boton_empezar_rect, ranking_button_rect, exit_button_rect = mostrar_pantalla_inicial(screen,score_font,PANTALLA_HEIGHT, PANTALLA_WIDTH, button_hover_color, button_color, button_font)  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Cierra el juego
            elif event.type == pygame.MOUSEBUTTONDOWN:  
                if boton_empezar_rect.collidepoint(event.pos):  
                    pantalla_inicial = False 
                elif ranking_button_rect.collidepoint(event.pos):  
                    mostrar_ranking(screen, ranking_cargado, score_font)
                    pantalla_inicial = True  
                  # Funcion para mostrar el ranking 
                elif exit_button_rect.collidepoint(event.pos): 
                    run = False  
    else:
        # Pantalla de juego principal
        dibujar_fondo(screen, escenario, PANTALLA_WIDTH, PANTALLA_HEIGHT)

        # Muestra las estadisticas de los jugadores
        dibujar_barra_de_vida(fighter_1.health, 20, 20, screen, BLANCO, ROJO, AMARILLO)
        dibujar_barra_de_vida(fighter_2.health, 580, 20, screen, BLANCO, ROJO, AMARILLO)
        dibujar_texto("P1: " + str(score[0]), score_font, ROJO, 20, 60, screen)
        dibujar_texto("P2: " + str(score[1]), score_font, ROJO, 580, 60, screen)

        # Inicio del combate
        if intro_count <= 0:  # Si finaliza el contador, el combate arranca
            # Mover a los luchadores
            fighter_1.moverse(PANTALLA_WIDTH, PANTALLA_HEIGHT, screen, fighter_2, round_over)
            fighter_2.moverse(PANTALLA_WIDTH, PANTALLA_HEIGHT, screen, fighter_1, round_over)
        else:
            dibujar_texto(str(intro_count), count_font, ROJO, PANTALLA_WIDTH / 2, PANTALLA_HEIGHT / 3, screen)
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
                intro_count -= 1
                last_count_update = pygame.time.get_ticks()

        # Actualiza y renderiza a los luchadores
        fighter_1.update()
        fighter_2.update()
        fighter_1.dibujar(screen)
        fighter_2.dibujar(screen)

        # Verifica el game over y actualiza el marcador para el ganador
        if round_over == False:
            if fighter_1.alive == False:
                score[1] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
                if score[1] == 2:
                    #actualizar_ranking("Jugador 2")
                    ranking_cargado[nombre_j2] = ranking_cargado.get(nombre_j2, 0) + 1
                    guardar_ranking(ranking_cargado, RANKING_FILE)  # Guarda los cambios en el archivo
                    screen.blit(victory_img, (360, 150))
            elif fighter_2.alive == False:
                score[0] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
                if score[0] == 2:
                    #actualizar_ranking("Jugador 1")
                    ranking_cargado[nombre_j1] = ranking_cargado.get(nombre_j1, 0) + 1
                    guardar_ranking(ranking_cargado, RANKING_FILE)  # Guarda los cambios en el archivo
                    screen.blit(victory_img, (360, 150))
        else:
            screen.blit(victory_img, (360, 150))
            pygame.display.update()         
            if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                round_over = False
                intro_count = 3
                fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
                fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)
                if score[0] == 2 or score[1] == 2:
                    pantalla_inicial = True
                    score = [0, 0]

        # Detecta eventos para cerrar la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    # Actualiza la pantalla
    pygame.display.update()

# Cierra pygame
pygame.quit()
