import pygame,sys
from pygame.locals import *

WIDTH  = 640
HEIGHT = 480

class pelota(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = 8 * HEIGHT / 9
        self.speed = [0.3,  - 0.5]
 
    def actualizar(self, time, pelota):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time

 
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
 
        if pygame.sprite.collide_rect(self, pelota):
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
class Bloques(pygame.sprite.Sprite):
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
    def ubicar(self,i ,z):
            self.image = pygame.image.load('images/pala - copia.png')
            self.rect = self.image.get_rect()
            self.rect.centerx = 60 +  i*WIDTH / 8
            self.rect.centery =  z * HEIGHT/ 8
            self.posicion = [60 +  i*WIDTH / 8, z * HEIGHT/ 8]
            self.vivo = True
    def choque(self):
         if self.vivo:
            self.vivo = False
            self.image = pygame.image.load('images/pala - copia - copia.png')
            self.rect = self.image.get_rect()
            self.rect.centerx = self.posicion[0]
            self.rect.centery = self.posicion[1]
            


class barra(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/pala.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = 13*HEIGHT/14
        self.speed = 0.5
 
    def mover(self, time, keys):
        if self.rect.left >= 0:
            if keys[K_LEFT]:
                self.rect.centerx -= self.speed * time
        if self.rect.right <= WIDTH:
            if keys[K_RIGHT]:
                self.rect.centerx += self.speed * time


def main():
    juego = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Demo')
    screen.fill([0,0,0])
    Pelota = pelota()
    Barra = barra() 
    bloq = []
    z = 1
    p = 1
    for i in range(1,26):
        bloq.append(Bloques())
    
    for i in bloq:
        if p > 5:
            p = 1
            z += 1
        i.ubicar(p,z)
        p += 1
    
    clock = pygame.time.Clock()
    while juego:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        contador = 0
        Barra.mover(time, keys)
        Pelota.actualizar(time, Barra)
        for g in bloq:
            if pygame.sprite.collide_rect(Pelota, g) and g.vivo:
                g.choque()
                Pelota.speed[1] = -Pelota.speed[1]
                Pelota.rect.centery += Pelota.speed[1] * time
            if not g.vivo:
                contador += 1
        if contador == 25:
            juego = False
            print('Ganaste')
            
        if Pelota.rect.bottom >= HEIGHT:
             juego = False   
             print('Perdiste')    
        screen.fill([0,0,0])
        for i in bloq:
            screen.blit(i.image,i.rect)
        screen.blit(Barra.image,Barra.rect)
        screen.blit(Pelota.image,Pelota.rect)
        for i in bloq:
            screen.blit(i.image,i.rect)
        pygame.display.flip()
    

if __name__ == '__main__':
    pygame.init()
    main()