import pygame
def dibujar_barra_de_vida(health, x, y, screen, color_borde, color_vacio, color_vida):
  """
    Args:
        health (int): El nivel de salud actual del jugador, en un rango de 0 a 100
        x (int): La coordenada x de la esquina superior izquierda de la barra de salud
        y (int): La coordenada y de la esquina superior izquierda de la barra de salud

    Detalles:
        - La barra de salud consta de tres componentes:
            1. Un marco blanco que rodea la barra
            2. Una barra roja que representa la salud maxima
            3. Una barra amarilla proporcional al nivel de salud actual
        - El ancho de la barra es de 400 pixeles, y la altura es de 30 pixeles
        - El "ratio" se calcula dividiendo la salud actual por 100, para determinar el porcentaje de la barra amarilla visible
    """
  ratio = health / 100
  pygame.draw.rect(screen, color_borde, (x - 2, y - 2, 404, 34))
  pygame.draw.rect(screen, color_vacio, (x, y, 400, 30))
  pygame.draw.rect(screen, color_vida, (x, y, 400 * ratio, 30))