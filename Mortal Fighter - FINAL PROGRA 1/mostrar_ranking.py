import pygame
def mostrar_ranking(screen, ranking_a_cargar, fuente_puntuacion):
    screen.fill((0, 0, 0))  # Fondo negro
    ranking = ranking_a_cargar

    # Mostrar el ranking
    y_offset = 50
    titulo = fuente_puntuacion.render("Ranking de Victorias", True, (255, 255, 255))
    screen.blit(titulo, (300, y_offset))
    y_offset += 50

    if ranking:
        for index, (jugador, victorias) in enumerate(sorted(ranking.items(), key=lambda x: -x[1])):
            if index >= 10:  # Mostrar solo los primeros 10
                break
            texto = f"{jugador}: {victorias} victorias"
            texto_renderizado = fuente_puntuacion.render(texto, True, (255, 255, 255))
            screen.blit(texto_renderizado, (300, y_offset))
            y_offset += 40
    else:
        mensaje = fuente_puntuacion.render("No hay datos en el ranking aun.", True, (255, 255, 255))
        screen.blit(mensaje, (300, y_offset))

    button_color = (200, 0, 0)  
    button_hover_color = (255, 50, 50)
    volver_button_rect = pygame.Rect(300, y_offset + 50, 200, 50)  
    pygame.draw.rect(screen, button_color, volver_button_rect)
    texto_volver = fuente_puntuacion.render("Volver", True, (255, 255, 255))
    texto_x = volver_button_rect.x + (volver_button_rect.width - texto_volver.get_width()) // 2
    texto_y = volver_button_rect.y + (volver_button_rect.height - texto_volver.get_height()) // 2
    # Calcular la posición centrada del texto dentro del botón
    screen.blit(texto_volver, (texto_x, texto_y))
    
    pygame.display.update()


    # Esperar interacción del usuario
    esperando = True
    while esperando:
        mouse_pos = pygame.mouse.get_pos()
        color_actual = button_color 
        if volver_button_rect.collidepoint(mouse_pos):
            color_actual = button_hover_color 
        else: 
            color_actual = button_color
        pygame.draw.rect(screen, color_actual, volver_button_rect)
        screen.blit(texto_volver, (350, y_offset + 60))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if volver_button_rect.collidepoint(event.pos):
                    esperando = False  # Volver al menu