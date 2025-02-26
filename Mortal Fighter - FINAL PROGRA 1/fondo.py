import pygame
def dibujar_fondo(screen, escenario, ancho_pantalla, alto_pantalla):
  """
   Detalles:
      - Utiliza la funcion "pygame.transform.scale" para ajustar la imagen de fondo 
      al tamaño de la pantalla definido por "PANTALLA_WIDTH" y "PANTALLA_HEIGHT"
      - La imagen escalada se dibuja en las coordenadas (0, 0), ocupando toda la pantalla
      - Ideal para mostrar fondos dinamicos o estaticos que mejoren la estetica del juego
  """
  escalar_bg = pygame.transform.scale(escenario, (ancho_pantalla, alto_pantalla))
  screen.blit(escalar_bg, (0, 0))