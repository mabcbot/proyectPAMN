import pygame
from pygame.locals import *
import sys

anchoPantalla=640
largoPantalla=480
def cargarImagen(nombre,alpha=False):
	imagen=pygame.image.load(nombre)
	if(alpha==True):
		imagen=imagen.convert_alpha()
	else:
		imagen=imagen.convert()
	return imagen

def cargarSonido(nombre):
	sonido=pygame.mixer.Sound(nombre)
	return sonido

class pelota(pygame.sprite.Sprite):
	def __init__(self,sonidoGolpe,sonidoPunto):
		pygame.sprite.Sprite.__init__(self)
		self.imagen=cargarImagen("bola.png",True)
		self.rect=self.imagen.get_rect()
		self.rect.centerx=anchoPantalla/2
		self.rect.centery=largoPantalla/2
		self.speed=[5,5]
		self.sonidoGolpe=sonidoGolpe
		self.sonidoPunto=sonidoPunto

	def update(self):
		if self.rect.left<0 or self.rect.right>anchoPantalla:
			self.speed[0]=-self.speed[0]
			self.sonidoPunto.play() #se reproducirá un sonido si la pelota toca alguno de los laterales de la pantalla
			self.centery=largoPantalla/2
			self.centerx=anchoPantalla/2

		if self.rect.top<0 or self.rect.bottom>largoPantalla:
			self.speed[1]=-self.speed[1]
		self.rect.move_ip((self.speed[0], self.speed[1]))

	def colision(self,objetivo):
		if self.rect.colliderect(objetivo.rect):
			self.speed[0]=-self.speed[0]
			self.sonidoGolpe.play() #se reproducirá un sonido al impactar la bola con alguna paleta


class raqueta(pygame.sprite.Sprite):
	def __init__(self,x):
		pygame.sprite.Sprite.__init__(self)
		self.imagen=cargarImagen("raqueta.png",True)
		self.rect=self.imagen.get_rect()
		self.rect.centerx=x
		self.rect.centery=largoPantalla/2

	def humano(self):
		if self.rect.top<=0:
			self.rect.top=0
		elif self.rect.bottom>=largoPantalla:
			self.rect.bottom=largoPantalla

	def cpu(self,pelota):
		self.speed=[0, 3]
		if pelota.speed[0]>=0 and pelota.rect.centerx>largoPantalla/2:
			if self.rect.centery>pelota.rect.centery:
				self.rect.centery-=self.speed[1]
			elif self.rect.centery<pelota.rect.centery:
				self.rect.centery+=self.speed[1]

def main():
	pygame.init()
	pygame.mixer.init()
	screen=pygame.display.set_mode((anchoPantalla,largoPantalla))
	pygame.display.set_caption("Pong")
	fondo=cargarImagen("fondoPong.jpg",False)
	sonidoGolpe=cargarSonido("circus.wav")
	sonidoPunto=cargarSonido("goal.wav")
	bola=pelota(sonidoGolpe,sonidoPunto)
	jugador1=raqueta(20)
	jugador2=raqueta(anchoPantalla-20)
	clock=pygame.time.Clock()
	pygame.key.set_repeat(1,10)
	pygame.mouse.set_visible(False)

	while True:
		clock.tick(60)
		jugador1.humano()
		jugador2.cpu(bola)
		bola.update()

		#con esto comprobamos cuando los objetos en pantalla colisionan
		bola.colision(jugador1)
		bola.colision(jugador2)
		
		#con estas instrucciones obtenemos la posición del mouse
		posicionMouse=pygame.mouse.get_pos()
		movimientoMouse=pygame.mouse.get_rel()

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit(0)
			elif movimientoMouse[1]!=0:
				jugador1.rect.centery=posicionMouse[1]
			elif event.type==pygame.KEYDOWN:
				if event.key==K_UP:
					jugador1.rect.centery-=5
				elif event.key==K_DOWN:
					jugador1.rect.centery+=5
				elif event.key==K_ESCAPE:
					sys.exit(0)
			elif event.type==pygame.KEYUP:
				if event.key==K_UP:
					jugador1.rect.centery+=0
				elif event.key==K_DOWN:
					jugador1.rect.centery+=0

		screen.blit(fondo,(0,0))
		screen.blit(bola.imagen,bola.rect)
		screen.blit(jugador1.imagen,jugador1.rect)
		screen.blit(jugador2.imagen,jugador2.rect)
		pygame.display.flip()
main()
