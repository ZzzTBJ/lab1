import pygame  
pygame.init()
screen = pygame.display.set_mode((600, 600))

r = pygame.Rect(50, 200, 100, 200)
pygame.draw.rect(screen, (255, 255, 255), r, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()