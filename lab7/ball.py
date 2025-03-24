import pygame as pg
import sys

pg.init()
size = (600, 600)
pos = [300, 300]
scr = pg.display.set_mode(size)
scr.fill((255,255,255))
pg.draw.circle(scr, (136,8,8), (300, 300), 25)

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            sys.exit()

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and pos[0] >= 45:
                    pos[0] -= 20
        if keys[pg.K_RIGHT] and pos[0] <= 555:
                    pos[0] += 20
        if keys[pg.K_DOWN] and pos[1] <= 555:
                    pos[1] += 20
        if keys[pg.K_UP] and pos[1] >= 45:
                    pos[1] -= 20

        
            
    scr.fill((255,255,255))
    pg.draw.circle(scr, (136,8,8), (pos[0], pos[1]), 25)
    pg.display.flip()