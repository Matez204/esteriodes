import pygame
from pygame.locals import *
from pygame.sprite import *
import math
class Ship(Sprite):
    def __init__(self,contenedor):
        self.puntos= 0
        self.vida =100
        self.velocidad = [0,0]   
        self.contenedor=contenedor
        self.imagen=pygame.image.load("nave.png")
        self.rect=self.imagen.get_rect()
        self.rect.move_ip(contenedor[0]/2,contenedor[1]/2)
    def update(self):
        teclas=pygame.key.get_pressed()

        if teclas[K_LEFT]:
            self.rotar(2)
        if teclas[K_RIGHT]:
            self.rotar(-2)
        if teclas[K_UP]:
            self.acelerar()
        if teclas[K_DOWN]:
            pass       
    def acelerar(self):
        self.velocidad[0]+=marh.cos(math.radians((self.angulo)%360))
        self.velocidad[1]-=marh.sin(math.radians((self.angulo)%360))
    def rotarar(self,angulo):
        self.angulo+=angulo
        centro_x = self.rect.centerx
        centro_y = self.rect.centery
        self.image = pygame.transform.rotate(self.imagen,self.angulo)
        self.rect.centerx=centro_x
        self.rect.centery=centro_y
        




