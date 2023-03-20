import pygame, sys
from dati import *
# SB: from piastrella import Piastrella
from mappa import Mappa

# pygame setup
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
# SB: prova_piastrella = pygame.sprite.Group(Piastrella((screen_width/2, screen_height/2), 64))
mappa = Mappa(listaMappa, screen)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill("black")

	# SB: prova_piastrella.draw(screen)
	mappa.run()
	
	pygame.display.update()
	clock.tick(60)