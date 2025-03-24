import pygame
import sys
pygame.init()
pygame.display.set_caption("Musica")
size = (600, 600)
scr = pygame.display.set_mode(size)
scr.fill((255,255,255))


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()