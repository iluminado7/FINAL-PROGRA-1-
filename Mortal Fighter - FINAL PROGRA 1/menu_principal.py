import pygame
def mostrar_pantalla_inicial(pantalla,score_font,PANTALLA_HEIGHT, PANTALLA_WIDTH, button_hover_color, button_color, button_font):
    """
    Muestra la pantalla inicial del juego con tutorial de controles y botones para iniciar,
    acceder al ranking y salir del juego.
    """
    pantalla.fill((0, 0, 0))  # Rellena la pantalla de negro

    # Tutorial de controles
    controles_p1 = (
        "Jugador 1 Controles:",
        "Moverse Izq,Der: A D",
        "Saltar: W",
        "Ataque 1: R",
        "Ataque 2: T",
    )
    controles_p2 = (
        "Jugador 2 Controles:",
        "Moverse Izq,Der: Flechas IZQ/DER",
        "Saltar: Flecha Arriba",
        "Ataque 1: Teclado Numerico 1",
        "Ataque 2: Teclado Numerico 2",
    )

    # renderizar controles
    y_controles_j1 = 50  # altura inicial para controles del J1
    for text in controles_p1:
        manual_text = score_font.render(text, True, (255, 255, 255))
        pantalla.blit(manual_text, (50, y_controles_j1))
        y_controles_j1 += 40  

    y_controles_j2 = 50  # Altura inicial para controles del J2
    for text in controles_p2:
        manual_text = score_font.render(text, True, (255, 255, 255))
        pantalla.blit(manual_text, (550, y_controles_j2))
        y_controles_j2 += 40  

    # Posicion y tamaño de los botones
    button_width = 300
    button_height = 50
    button_y_start = PANTALLA_HEIGHT - 250  # Posicion vertical inicial de los botones
    button_spacing = 20  # Espaciado entre botones
    center_x = (PANTALLA_WIDTH - button_width) // 2  # Centrar horizontalmente

    # Obtener la posicion del mouse
    mouse_pos = pygame.mouse.get_pos()

    # Boton para iniciar el juego
    button_rect = pygame.Rect(center_x, button_y_start, button_width, button_height)
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(pantalla, button_hover_color, button_rect)
    else:
        pygame.draw.rect(pantalla, button_color, button_rect)

    button_label = button_font.render("Iniciar Juego", True, (255, 255, 255))
    pantalla.blit(
        button_label,
        (button_rect.x + (button_rect.width - button_label.get_width()) // 2,
         button_rect.y + (button_rect.height - button_label.get_height()) // 2),
    )

    # Boton para acceder al ranking
    ranking_button_rect = pygame.Rect(center_x, button_y_start + button_height + button_spacing, button_width, button_height)
    if ranking_button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(pantalla, button_hover_color, ranking_button_rect)
    else:
        pygame.draw.rect(pantalla, button_color, ranking_button_rect)

    ranking_label = button_font.render("Ranking", True, (255, 255, 255))
    pantalla.blit(
        ranking_label,
        (ranking_button_rect.x + (ranking_button_rect.width - ranking_label.get_width()) // 2,
         ranking_button_rect.y + (ranking_button_rect.height - ranking_label.get_height()) // 2),
    )

    # Boton para salir del juego
    exit_button_rect = pygame.Rect(center_x, button_y_start + 2 * (button_height + button_spacing), button_width, button_height)
    if exit_button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(pantalla, button_hover_color, exit_button_rect)
    else:
        pygame.draw.rect(pantalla, button_color, exit_button_rect)

    exit_label = button_font.render("Salir", True, (255, 255, 255))
    pantalla.blit(
        exit_label,
        (exit_button_rect.x + (exit_button_rect.width - exit_label.get_width()) // 2,
         exit_button_rect.y + (exit_button_rect.height - exit_label.get_height()) // 2),
    )

    # Devolver las areas de los botones para deteccion de clics
    return button_rect, ranking_button_rect, exit_button_rect
