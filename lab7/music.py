import pygame
import sys
pygame.init()
pygame.display.set_caption("Musica")
size = (600, 600)
scr = pygame.display.set_mode(size)
scr.fill((255,255,255))

text = ''' STOP - 1
    PREV - 3
    NEXT - 4
    PLAY - 2 '''
print(text)
_songs = ['songs/неотдам.mp3', 'songs/отпусти.mp3', 'songs/перепутала.mp3']
pygame.mixer.music.load('lab7/songs/неотдам.mp3')
pygame.mixer.music.play()
current = 1



while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_1:   
                pygame.mixer.music.pause()
            elif i.key == pygame.K_2:
                pygame.mixer.music.unpause()

        elif i.type == pygame.MOUSEBUTTONUP:
            if i.button == 1:
                if current == 1:
                    pygame.mixer.music.load('lab7/songs/отпусти.mp3')
                    pygame.mixer.music.play()
                    current += 1
                elif current == 2:
                    pygame.mixer.music.load('lab7/songs/перепутала.mp3')
                    pygame.mixer.music.play()
                    current += 1
                elif current == 3:
                    pygame.mixer.music.load('lab7/songs/неотдам.mp3')
                    pygame.mixer.music.play()
                    current = 1


            elif i.button == 3:
                if current == 1:
                    pygame.mixer.music.load('lab7/songs/перепутала.mp3')
                    pygame.mixer.music.play()
                    current = 3
                elif current == 2:
                    pygame.mixer.music.load('lab7/songs/неотдам.mp3')
                    pygame.mixer.music.play()
                    current -= 1
                elif current == 3:
                    pygame.mixer.music.load('lab7/songs/отпусти.mp3')
                    pygame.mixer.music.play()
                    current = 1
        pygame.display.flip()