import pygame
from pygame.locals import *
import os
import sys
import math

pygame.init()

w, h = 800, 447
win = pygame.display.set_mode((w, h))
pygame.display.set_caption('Subway 2D')

backg = pygame.image.load(os.path.join('images', 'backg.png')).convert()
backgA = 0
backgA2 = backg.get_width()

clock = pygame.time.Clock()

class player(object):
    ticha = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(8, 16)]
    skacha = False
    pluzgase = False
    skachaanim = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(1, 8)]
    pluzgaseanim = [pygame.image.load(os.path.join('images', 'S1.png')), pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')),
             pygame.image.load(os.path.join('images', 'S3.png')), pygame.image.load(os.path.join('images', 'S4.png')),
             pygame.image.load(os.path.join('images', 'S5.png'))]
    skoklist = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1,
                -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.pluzgaseCount = 0
        self.skachaCount = 0
        self.tichaCount = 0
        self.pluzgaseUp = False

    def draw(self, win):
        if self.skacha:
            self.y -= self.skoklist[self.skachaCount] * 1.2
            win.blit(self.skachaanim[self.skachaCount // 18], (self.x, self.y))
            self.skachaCount += 1
            if self.skachaCount > 108:
                self.skachaCount = 0
                self.skacha = False
                self.tichaCount = 0
        elif self.pluzgase or self.pluzgaseUp:
            if self.pluzgaseCount < 20:
                self.y += 1
            elif self.pluzgaseCount == 80:
                self.y -= 19
                self.pluzgase = False
                self.pluzgaseUp = True
            if self.pluzgaseCount >= 110:
                self.pluzgaseCount = 0
                self.pluzgaseUp = False
                self.tichaCount = 0
            win.blit(self.pluzgaseanim[self.pluzgaseCount // 10], (self.x, self.y))
            self.pluzgaseCount += 1

        else:
            if self.tichaCount > 42:
                self.tichaCount = 0
            win.blit(self.ticha[self.tichaCount // 6], (self.x, self.y))
            self.tichaCount += 1


class saw(object):
    image = [pygame image ]
    def __init__(self, x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x,y,width,height)

    def draw(self, win):
        self.hitbox = ()
        win.blit(self.img, (self.x,self.y))
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

def redrawWindow():
    win.blit(backg, (backgA, 0))
    win.blit(backg, (backgA2, 0))
    choveche.draw(win)
    pygame.display.update()


choveche = player(200, 313, 64, 64)
pygame.time.set_timer(USEREVENT+1,500)
skorost = 30
ticha = True
while ticha:
    redrawWindow()
    clock.tick(skorost)
    backgA -= 1.4
    backgA2 -= 1.4
    if backgA < backg.get_width() * -1:
        backgA = backg.get_width
    if backgA2 < backg.get_width() * -1:
        backgA2 = backg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ticha = False
            pygame.quit()
            quit()
        if event.type == USEREVENT+1:
            skorost += 1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not(choveche.skacha):
            choveche.skacha = True

    if keys[pygame.K_DOWN]:
        if not(choveche.pluzgase):
            choveche.pluzgase = True






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ticha = False
            pygame = quit()
            quit()




