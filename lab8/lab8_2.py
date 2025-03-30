import pygame
import sys, math

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Рисовалки")
clock = pygame.time.Clock()

RED = (255, 0,0)
GREEN = (0, 255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
GRAY = (197, 197, 197)
draw = False
brs = 10
brc = WHITE

menu_rect = pygame.Rect(0,0, 100, 200)
scr_rect = pygame.Rect(100, 0, 500, 480)

red_r = pygame.Rect(15, 55, 20, 20)
green_r = pygame.Rect(40, 55, 20, 20)
blue_r = pygame.Rect(65, 55, 20, 20)
black_r = pygame.Rect(15, 77, 20, 20)
white_r = pygame.Rect(40, 77, 20, 20)
yellow_r = pygame.Rect(65, 77, 20, 20)

eraser_rect = pygame.Rect(27, 120, 40, 40)
eraser = pygame.image.load("lab8/images/eraser.jpg")
eraser = pygame.transform.scale(eraser, (40,40))


font = pygame.font.Font(None, 24)
menu_text = font.render("Цвет", True, BLACK)

def drawCircle(screen, x, y ):
    pygame.draw.circle( screen, brc, ( x, y ), 20 )
def drawRect(screen, x, y):
    pygame.draw.rect(screen, brc, (x,y, 100, 50))
def drawSq(screen, x, y):
    pygame.draw.rect(screen, brc, (x,y, 50, 50))
def drawET(screen, x, y, size = 100):
    height = (math.sqrt(3) / 2) * size 
    p1 = (x, y) 
    p2 = (x + size, y) 
    p3 = (x + size / 2, y + height) 
    pygame.draw.polygon(screen, brc, [p1, p2, p3])
def drawRT(screen, x, y, width=100, height=100):
    p1 = (x, y)
    p2 = (x + width, y)  
    p3 = (x, y + height)  
    pygame.draw.polygon(screen, brc, [p1, p2, p3])
def drawRH(screen, x, y, size=100):
    p1 = (x, y) 
    p2 = (x + size / 2, y + size / 2)
    p3 = (x, y + size) 
    p4 = (x - size / 2, y + size / 2)  
    pygame.draw.polygon(screen, brc, [p1, p2, p3, p4])
while True:
        pressed = pygame.key.get_pressed()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    (x,y) = pygame.mouse.get_pos()
                    drawCircle(screen, x, y)
                if event.key == pygame.K_x:
                    (x,y) = pygame.mouse.get_pos()
                    drawRect(screen, x,y )
                if event.key == pygame.K_z:
                    (x,y) = pygame.mouse.get_pos()
                    drawSq(screen, x, y)
                if event.key == pygame.K_v:
                    (x,y) = pygame.mouse.get_pos()
                    drawET(screen, x, y)
                if event.key == pygame.K_b:
                    (x,y) = pygame.mouse.get_pos()
                    drawRT(screen, x, y)
                if event.key == pygame.K_n:
                    (x,y) = pygame.mouse.get_pos()
                    drawRH(screen, x, y)
                
                if event.key == pygame.K_ESCAPE:
                    screen.fill((0,0,0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                draw = True
            if event.type == pygame.MOUSEBUTTONUP:
                draw = False
        mouse_pos = pygame.mouse.get_pos()
        if draw == True and mouse_pos[0] > 100:
            pygame.draw.circle(screen, brc, mouse_pos, brs)
        if draw == True:    
            if green_r.collidepoint(mouse_pos):
                brc = GREEN
            if red_r.collidepoint(mouse_pos):
                brc = RED
            if blue_r.collidepoint(mouse_pos):
                brc = BLUE
            if black_r.collidepoint(mouse_pos):
                brc = BLACK
            if white_r.collidepoint(mouse_pos):
                brc = WHITE
            if yellow_r.collidepoint(mouse_pos):
                brc = YELLOW

            if eraser_rect.collidepoint(mouse_pos):
                brc = BLACK
                brs = 10


        pygame.draw.rect(screen, GRAY, menu_rect)
        screen.blit(menu_text, (10, 20))
        pygame.draw.line(screen, BLACK, (0, 40), (100, 40))
        pygame.draw.line(screen, BLACK, (0, 45), (100, 45))


        pygame.draw.rect(screen, GREEN, green_r)
        if brc == GREEN:
            border = 3
        else:
            border = 1
        pygame.draw.rect(screen, BLACK, green_r, border)

        pygame.draw.rect(screen, RED, red_r)
        if brc == RED:
            border = 3
        else:
            border = 1
        pygame.draw.rect(screen, BLACK, red_r, border)
    
        pygame.draw.rect(screen, BLUE, blue_r)
        if brc == BLUE:
            border = 3
        else:
            border = 1
        pygame.draw.rect(screen, BLACK, blue_r, border)

        pygame.draw.rect(screen, WHITE, white_r)
        if brc == WHITE:
            border = 3
        else:
            border = 1
        pygame.draw.rect(screen, BLACK, white_r, border)

        pygame.draw.rect(screen, BLACK, black_r)
        if brc == BLACK:
            border = 3
        else:
            border = 1
        pygame.draw.rect(screen, BLACK, black_r, border)

        pygame.draw.rect(screen, YELLOW, yellow_r)
        if brc == YELLOW:
            border = 3
        else:
            border = 1
        pygame.draw.rect(screen, BLACK, yellow_r, border)

        screen.blit(eraser, eraser_rect)
        if brc == BLACK:
            border = 3
        else:
            border = 1
        pygame.draw.rect(screen, BLACK, eraser_rect, border)



        pygame.display.flip()
        clock.tick(60)
