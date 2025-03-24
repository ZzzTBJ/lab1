import pygame
import sys
import datetime


pygame.init()
pygame.display.set_caption("LGBTU")
def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

size = (600, 600)
scr = pygame.display.set_mode(size)
scr.fill((255,255,255))

img1 = pygame.image.load("lab7/clockk.bmp")
img2 = pygame.image.load("lab7/left.bmp")
img3 = pygame.image.load("lab7/ruka1.bmp")

clock = pygame.time.Clock()
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()
        time = datetime.datetime.now()
        sec = time.second
        mins = time.minute + sec/60
        print(mins, sec)
        second_angle = -sec*6
        minute_angle = -mins*6
        
        scr.fill((255, 255, 255))
        scr.blit(img1, (0,50))

        blitRotateCenter(scr, img2, (-10, 50), minute_angle)
        blitRotateCenter(scr, img3, (0, 50), second_angle)
        
        clock.tick(60)