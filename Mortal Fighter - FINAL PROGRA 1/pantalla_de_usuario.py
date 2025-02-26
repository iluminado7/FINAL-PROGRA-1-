import pygame
def pantalla_carga_usuario(screen, font, ranking_file, mensaje, funcion_texto,funcion_cargar_ranking,funcion_guardar_ranking):
    """Pantalla para que un jugador ingrese su nombre (máximo 8 caracteres, sin espacios)."""
    nombre_usuario = ""
    cargando = True
    input_rect = pygame.Rect(250, 250, 500, 60)
    color_inactivo = (200, 200, 200)
    color_activo = (255, 255, 255)
    color_error = (255, 0, 0)
    color = color_inactivo
    activo = False
    mensaje_error = ""

    while cargando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    activo = True
                else:
                    activo = False
                if activo:
                    color = color_activo
                else:
                    color = color_inactivo
            elif event.type == pygame.KEYDOWN and activo:
                if event.key == pygame.K_RETURN:
                    # Validar que no haya espacios y el largo sea <= 20
                    if " " in nombre_usuario:
                        mensaje_error = "El nombre no puede tener espacios."
                        color = color_error
                    elif len(nombre_usuario) > 20:
                        mensaje_error = "Maximo 20 caracteres permitidos."
                        color = color_error
                    elif len(nombre_usuario) == 0:
                        mensaje_error = "El nombre no puede estar vacio."
                        color = color_error
                    else:
                        cargando = False
                elif event.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[:-1]
                    mensaje_error = ""  # Limpiar mensaje de error al modificar el texto
                    color = color_activo
                else:
                    if len(nombre_usuario) <= 20 and event.unicode != " ":
                        nombre_usuario += event.unicode
                        nombre_usuario = nombre_usuario.capitalize()
                    elif len(nombre_usuario) >= 20:
                        mensaje_error = "Maximo 20 caracteres permitidos."
                        color = color_error
                    elif event.unicode == " ":
                        mensaje_error = "El nombre no puede tener espacios."
                        color = color_error

        screen.fill((0, 0, 0))  # Fondo negro
        funcion_texto(mensaje, font, (255, 255, 255), 250, 150, screen)
        pygame.draw.rect(screen, color, input_rect, 2)
        texto_nombre = font.render(nombre_usuario, True, (255, 255, 255))
        screen.blit(texto_nombre, (input_rect.x + 10, input_rect.y + 10))

        # Mostrar mensaje de error si existe
        if mensaje_error:
            error_text = font.render(mensaje_error, True, color_error)
            screen.blit(error_text, (250, 320))

        pygame.display.update()

    # Actualizar el ranking con el nuevo usuario
    ranking = funcion_cargar_ranking(ranking_file)
    if nombre_usuario not in ranking:
        ranking[nombre_usuario] = 0
        funcion_guardar_ranking(ranking, ranking_file)

    return nombre_usuario
