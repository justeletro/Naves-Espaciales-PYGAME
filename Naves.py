import keyboard
import pygame
import sys 
# modificacion 1.3333333

class Nave:
    imagen = pygame.image.load("nave.png")
    def __init__(self,pos):
        self.pos = pos[:]
        self.cambio =  [0,0]
        pass

    def dibujar(self,screen):
        screen.blit(self.imagen, self.pos)
        pass
    def actualizar(self):
        self.pos[0] += self.cambio[0]
        self.pos[1] += self.cambio[1]
        pass

class Misil:
    imagen = pygame.image.load("misil.png")
    misiles = []

    def __init__(self, pos):
        self.pos = pos[:]
        self.cambio = 5
        Misil.misiles.append(self)

    def dibujar(self,screen):
        screen.blit(self.imagen, self.pos)

    def actualizar(self):
        self.pos[1] -= self.cambio
        if self.pos[1] <= 0:
            self.explotar()
    
    def explotar(self):
        Misil.misiles.remove(self)

pygame.init()
working = True
nave = Nave([500,500])
clock = pygame.time.Clock()  
screen = pygame.display.set_mode([700,600])
pygame.display.set_caption("Naves Espaciales")
fondo = pygame.image.load("espacio.jpg")
icon = pygame.image.load("nave.png")
pygame.display.set_icon(icon)

while working:
    clock.tick(50)
    screen.blit(fondo,(0,0))
    nave.actualizar()
    for misil in Misil.misiles:
        misil.actualizar()
    nave.dibujar(screen)
    for misil in Misil.misiles:
        misil.dibujar(screen)
    

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == 1073741906:        # Arriba
                nave.cambio[1] = -5
            elif event.key == 1073741905:      # Abajo
                nave.cambio[1] = 5
            elif event.key == 1073741904:      # Izquierda
                nave.cambio[0] = -5
            elif event.key == 1073741903:      # Derecha
                nave.cambio[0] = 5
            elif event.key == 32:
                print("disparo")
                Misil(nave.pos)
        elif event.type == pygame.KEYUP:
            if event.key == 1073741906:        # Arriba
                nave.cambio[1] = 0
            elif event.key == 1073741905:      # Abajo
                nave.cambio[1] = 0
            elif event.key == 1073741904:      # Izquierda
                nave.cambio[0] = 0
            elif event.key == 1073741903:      # Derecha
                nave.cambio[0] = 0