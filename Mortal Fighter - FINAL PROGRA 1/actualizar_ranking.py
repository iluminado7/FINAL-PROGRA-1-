def actualizar_ranking(ranking_cargar, nombre_jugador, ranking_guardar):
    # carga el ranking actual
    ranking = ranking_cargar
    # actualiza la cantidad de victorias del jugador
    if nombre_jugador in ranking:
        ranking[nombre_jugador] += 0
    else:
        ranking[nombre_jugador] = 0
    # Guardar los cambios en el archivo
    ranking_guardar


