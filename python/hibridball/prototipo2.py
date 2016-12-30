import pygame, sys, time
from pygame.locals import *



# Establece pygame
pygame.init()
# Establece la ventana
ANCHOVENTANA = 800
ALTOVENTANA = 600
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA), 0,32)
pygame.display.set_caption('PIMBAL1')
# Establece las variables de direccion
ABAJOIZQUIERDA = 1
ABAJO = 2
ABAJODERECHA = 3
IZQUIERDA = 4
CENTRO = 5
DERECHA =6
ARRIBAIZQUIERDA = 7
ARRIBA = 8
ARRIBADERECHA = 9
VELOCIDADMOVIMIENTO = 4
# Establece los colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
ODOO=(102,0,102)
BLANCO=(255,255,255)
# Establece la estructura de datos de los bloques.
b0 = {'rect':pygame.Rect(0,580, 100, 20), 'color':BLANCO,'dir':IZQUIERDA}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':ROJO,'dir':ARRIBAIZQUIERDA}

bloques = [ b2]
jugador1 = pygame.Rect(400,580, 100, 20)
# configurar variables de movimiento
moverseIzquierda = False
moverseDerecha = False


while True:


	for evento in pygame.event.get():

		if evento.type == QUIT:
			pygame.quit()

			sys.exit()
	if evento.type == KEYDOWN:
		
		if evento.key == K_LEFT :

				moverseDerecha = False

				moverseIzquierda = True
		if evento.key == K_RIGHT :

				moverseIzquierda = False

				moverseDerecha = True
	if evento.type == KEYUP:
		


		if evento.key == K_LEFT :

				moverseIzquierda = False

		if evento.key == K_RIGHT :

				moverseDerecha = False
	
		
	# mover al jugador

	if moverseIzquierda and jugador1.left > 0:

		jugador1.left -= VELOCIDADMOVIMIENTO
	if moverseDerecha and jugador1.right < ANCHOVENTANA:

		jugador1.right += VELOCIDADMOVIMIENTO
	
	
			
	# Dibuja el fondo negro sobre la superficie
	superficieVentana.fill(NEGRO)


	for b in bloques:

	# mueve la estructura de datos de bloques
	
		if b['dir'] == ABAJOIZQUIERDA:

			b['rect'].left -= VELOCIDADMOVIMIENTO

			b['rect'].top += VELOCIDADMOVIMIENTO

		if b['dir'] == ABAJODERECHA:

			b['rect'].left += VELOCIDADMOVIMIENTO

			b['rect'].top += VELOCIDADMOVIMIENTO

		if b['dir'] == ARRIBAIZQUIERDA:

			b['rect'].left -= VELOCIDADMOVIMIENTO

			b['rect'].top -= VELOCIDADMOVIMIENTO

		if b['dir'] == ARRIBADERECHA:

			b['rect'].left += VELOCIDADMOVIMIENTO

			b['rect'].top -= VELOCIDADMOVIMIENTO
			
		if b['dir'] == ABAJO :
			b['rect'].bottom += VELOCIDADMOVIMIENTO
			
		if b['dir'] == ARRIBA :
			b['rect'].top -= VELOCIDADMOVIMIENTO
			
		if b['dir'] == DERECHA :
			b['rect'].right += VELOCIDADMOVIMIENTO
		if b['dir'] == IZQUIERDA :
			b['rect'].left -= VELOCIDADMOVIMIENTO
	
		# Verifica si el bloque se movio fuera de
		if b['rect'].top < 0:

			# el bloque se movio por arriba de la

			if b['dir'] == ARRIBAIZQUIERDA:

				b['dir'] = ABAJOIZQUIERDA

			if b['dir'] == ARRIBADERECHA:

				b['dir'] = ABAJODERECHA
			if b['dir'] == ARRIBA :
				
				b['dir'] = ABAJO

		if b['rect'].bottom > ALTOVENTANA:

		# el bloque se movio por debajo de la

			if b['dir'] == ABAJOIZQUIERDA:

				b['dir'] = ARRIBAIZQUIERDA

			if b['dir'] == ABAJODERECHA:

				b['dir'] = ARRIBADERECHA
			if b['dir'] == ABAJO :
				
				b['dir'] = ARRIBA

		if b['rect'].left < 0:
			
			pygame.draw.rect(superficieVentana, b['color'], b['rect'])
			
			# el bloque se movio por la izquierda

			if b['dir'] == ABAJOIZQUIERDA:
		
				b['dir'] = ABAJODERECHA

			if b['dir'] == ARRIBAIZQUIERDA:

				b['dir'] = ARRIBADERECHA
			if b['dir'] == IZQUIERDA:

				b['dir'] = DERECHA
		if b['rect'].right > ANCHOVENTANA:
			# el bloque se
			if b['dir'] ==ABAJODERECHA:
				b['dir'] =ABAJOIZQUIERDA
			if b['dir'] ==ARRIBADERECHA:
				b['dir'] =ARRIBAIZQUIERDA
			if b['dir'] ==DERECHA:
				b['dir'] =IZQUIERDA 


		# Dibuja el bloque en la superficie
		pygame.draw.rect(superficieVentana, b['color'], b['rect'])
		pygame.draw.rect(superficieVentana, BLANCO, jugador1)
		# Dibuja la ventana en la pantalla
	pygame.display.update()
	time.sleep(0.02)
