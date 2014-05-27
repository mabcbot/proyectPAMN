import pygame
from pygame.locals import *
import sys
import random

ancho=800
alto=600
class marciano(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagen=pygame.image.load("nave.png")
		self.velocidad=[3,3]
		self.rect=self.imagen.get_rect()
		self.rect.centerx=200
		self.rect.centery=100
		self.visible=True

	def update(self):
		if self.rect.left<0 or self.rect.right>ancho:
			self.velocidad[0]=-self.velocidad[0]
		if self.rect.top<0 or self.rect.bottom>alto:
			self.velocidad[1]=-self.velocidad[1]
		self.rect.move_ip((self.velocidad[0], self.velocidad[1]))

class ufo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagen=pygame.image.load("ufo.png")
		self.velocidad=[3,0]
		self.rect=self.imagen.get_rect()
		self.rect.centerx=ancho/2
		self.rect.centery=50
		self.visible=True

	def update(self):
		if self.rect.left<0 or self.rect.right>ancho:
			self.velocidad[0]=-self.velocidad[0]
		self.rect.move_ip((self.velocidad[0], self.velocidad[1]))

class tanque(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagen=pygame.image.load("tanque.png")
		self.velocidad=[3,0]
		self.rect=self.imagen.get_rect()
		self.rect.centerx=ancho/2
		self.rect.centery=alto-50

class disparo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagen=pygame.image.load("disparo.png")
		self.velocidad=[0,-4]
		self.rect=self.imagen.get_rect()
		self.rect.centerx=0
		self.rect.centery=0
		self.fuego=False

	def update(self):
		self.rect.move_ip((self.velocidad[0], self.velocidad[1]))
		if self.rect.centery<=0:
			self.fuego=False

def colision(objetivo1,objetivo2):
	if objetivo1.rect.colliderect(objetivo2.rect):
		return True


pygame.init()
pantalla=pygame.display.set_mode((ancho,alto))
nave=marciano()
jefe=ufo()
defensor=tanque()
bala=disparo()

pygame.key.set_repeat(1,10)
reloj=pygame.time.Clock()
while True:
	reloj.tick(40)
	nave.update()
	jefe.update()
	bala.update()

	if nave.visible:
		if colision(defensor,nave):
			sys.exit()

		if bala.fuego:
			if colision(bala,nave):
				nave.visible=False
				bala.fuego=False

	if bala.fuego:
		if colision(bala,jefe):
			jefe.visible=False
			bala.fuego=False

	if not jefe.visible and not nave.visible:
		sys.exit()

	if defensor.rect.centerx>=ancho:
		defensor.rect.centerx=0
	elif defensor.rect.centerx<=0:
		defensor.rect.centerx=ancho

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			if event.key==K_LEFT:
				defensor.rect.centerx-=4
			if event.key==K_RIGHT:
				defensor.rect.centerx+=4
			if event.key==K_SPACE and bala.fuego==False:
				bala.fuego=True
				bala.rect.centerx=defensor.rect.centerx
				bala.rect.centery=defensor.rect.centery-25
			if event.key==K_ESCAPE:
				sys.exit()

	pantalla.fill((0,0,0))
	if nave.visible:
		pantalla.blit(nave.imagen,nave.rect)
	if jefe.visible:
		pantalla.blit(jefe.imagen,jefe.rect)
	if bala.fuego==True:
		pantalla.blit(bala.imagen,bala.rect)
	pantalla.blit(defensor.imagen,defensor.rect)
	pygame.display.flip()
pygame.quit()
