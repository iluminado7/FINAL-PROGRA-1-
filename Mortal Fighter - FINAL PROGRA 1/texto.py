import pygame
def dibujar_texto(text, font, text_col, x, y, screen):
  """    
  Args:
      text (str): El texto que se desea mostrar
      font (pygame.font.Font): Objeto de fuente que define el estilo y tamaño del texto
      text_col (tuple): Color del texto en formato RGB
      x (int): Coordenada x donde se posiciona el texto
      y (int): Coordenada y donde se posiciona el texto

  Detalles:
      - Utiliza el metodo render del objeto fuente para crear una imagen del texto
      - La imagen del texto se dibuja en la pantalla utilizando blit
      - Se puede usar para mostrar elementos como puntajes, temporizadores, y mensajes durante el juego
    """
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))