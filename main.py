import pygame, sys, time, random
import os
import player
from player import *

WIDTH  = 610
HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Zombie flood")
player_img = pygame.image.load('img_data/iosu_up.png')
player_rect = player_img.get_rect()
player  = Player(player_img)
speed = 15
bala = pygame.rect.Rect((0,0), (5,5))
clock = pygame.time.Clock()
numzomb = 10
zombie_img = pygame.image.load('img_data/zombie.png')
zombie_rect = zombie_img.get_rect()
cantzomb = { }

for i in range(0, 99999+1):
	cantzomb[i] = zombie_img.get_rect()
	cantzomb[i].left = random.randrange(0,400)
	cantzomb[i].top  = random.randrange(0,100)

def add_zombies(cantzomb,zombie_img, numzomb):
	for i in range(0, numzomb):
		cantzomb[i] = zombie_img.get_rect()
		cantzomb[i].left = random.randrange(0,400)
		cantzomb[i].top  = random.randrange(0,100)

def load(name,x,y):
	try:
		img = pygame.image.load("img_data/"+str(name))
		screen.blit(img, (x,y))
	except:
		print "Couldn't load: "+str(name)

def handle(what, level, numzomb):
	if what == "lose":
		font = pygame.font.Font(None, 80)
		text = "Game over"
		render = font.render(text, 1, (255,255,255))
		screen.fill((255,0,0))
		screen.blit(render, (150,170))
	else:
		font = pygame.font.Font(None, 80)
		text = "Next stage"
		render = font.render(text, 1, (255,255,255))
		screen.fill((10,66,120))
		screen.blit(render, (150,170))

def main():

	walk = False
	a_shot = False
	numzomb = 10 
	cont_zomb = 10
	end = False
	pygame.mixer.init()
	level = 1
	bala = pygame.rect.Rect((0,0), (5,5))
	zsound = pygame.mixer.Sound("sound_data/zombies.wav")
	
	while not end:
		vx,vy = 0,0

		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:sys.exit(0)

			keys = pygame.key.get_pressed()

			if keys[K_ESCAPE]:sys.exit(0)
			if keys[K_w]:vy = -speed
			if keys[K_s]:vy = speed
			if keys[K_a]:vx = -speed
			if keys[K_d]:vx = speed

			if keys[K_SPACE]:
				pygame.mixer.music.load("sound_data/shot.wav")
				pygame.mixer.music.play()
				pos = player.pos()
				a_shot = True
				for i in range (0,20):
					bala = pygame.rect.Rect((0,0), (5,5))
					bala.left = pos[2] - 10
					bala.top = pos[1] - 10
					bala.right = pos[3] - 10

		player.move(vx,vy)
		background = load("background.png",0,0)
		vel = { }
		for i in range(0,numzomb):
			vel[i] = random.randrange(0,2)
			screen.blit(zombie_img, cantzomb[i])
			if player.col(cantzomb[i]):
				handle('lose', level, numzomb)
				end = True
			if bala.colliderect(cantzomb[i]):
				cantzomb[i].inflate_ip(-99999,-999999)
				cont_zomb -= 1
			if cantzomb[i].bottom >= HEIGHT:
				handle('lose', level, numzomb)
				end = True
			if cont_zomb <= 0:
				handle('win', level, numzomb)
				level += 1			
				numzomb += 2
				add_zombies(cantzomb,zombie_img, numzomb)
				cont_zomb = numzomb
			cantzomb[i].move_ip(0, vel[i])
		
		if numzomb > 0:	zsound.play()

   		if a_shot:
			bala.top -= 15
			pygame.draw.rect(screen, (255,255,255), bala)
		

		kills = numzomb - cont_zomb
		fps = str(clock.get_time())
		time = fps.split(".")[0]
		player.hud(screen,kills,level,time,numzomb)
		player.update(screen,walk)
		pygame.display.flip()
		clock.tick(70)
		pos = player.pos()

	sys.exit()
main()
