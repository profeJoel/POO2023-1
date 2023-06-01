import pygame
from pygame.locals import *

pygame.init()
ancho = 600
largo = 400
ventana = pygame.display.set_mode((ancho,largo))
pygame.display.set_caption("Jueguito POO")

while True:
    
    for evento in pygame.event.get():
        print(f"Evento actual: {evento.type}")
        if evento.type == pygame.QUIT:
            quit()

pygame.quit()

