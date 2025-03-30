#Imports
import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
SCORE2 = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("lab8/images/AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Типа формула 1")




class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab8/images/Enemy.png")
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab8/images/Player.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.image = pygame.image.load("lab8/images/coin.jpg")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10, SCREEN_WIDTH-40), 0)
        self.collected = False
    def move(self):
        global SCORE2
        self.rect.move_ip(0,SPEED)
        if pygame.sprite.collide_rect(self, P1) and not self.collected:
                SCORE2 +=1 
                self.collected = True
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(10, SCREEN_WIDTH - 40), 0)
            self.collected = False

class Coin2(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.image = pygame.image.load("lab8/images/coin2.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.image.set_colorkey(WHITE)  
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(10, SCREEN_WIDTH-40), 0)
        self.collected = False
    def move(self):
        global SCORE2
        self.rect.move_ip(0,SPEED)
        if pygame.sprite.collide_rect(self, P1) and not self.collected:
                SCORE2 +=3 
                self.collected = True
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(10, SCREEN_WIDTH - 40), 0)
            self.collected = False

P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin2()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
coins.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


while True:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
                SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(f"Очко: {SCORE}", True, BLACK)
    coin = font_small.render(f"Деньги: {SCORE2}", True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coin, (10, 30))


    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

            
    if pygame.sprite.spritecollideany(P1, enemies):
            
            time.sleep(0.5)
                    
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30,250))
        
            pygame.display.update()
            for entity in all_sprites:
                    entity.kill() 
            pygame.quit()
            sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)