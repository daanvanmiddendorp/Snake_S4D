import pygame,sys,random
from pygame.math import Vector2

pygame.init()
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)

