import pygame, random
from pygame.locals import *

class Player(pygame.sprite.Sprite):

	def __init__(self,image):
		self.image = image
		self.rect  = self.image.get_rect()
		self.rect.top,self.rect.left=300,200
		pygame.key.set_repeat(1, 25)
	def move(self,vx,vy):
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right >= 620:
			self.rect.right = 620
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= 400:
			self.rect.bottom = 400
		self.rect.move_ip(vx,vy)
	
	def update(self,surface,walk):
	#	if walk == "left":
	#		self.image = pygame.image.load('img_data/iosu_left.png')
	#	if walk == "right":
	#		self.image = pygame.image.load('img_data/iosu_right.png')
	#	if walk == "top":
		self.image = pygame.image.load('img_data/iosu_up.png')
	#	if walk == "down":
	#		self.image = pygame.image.load('img_data/iosu_down.png')
		surface.blit(self.image,self.rect)
	
	def col(self,obj):
		if self.rect.colliderect(obj):
			return True
	def pos(self):
		append = []
		append.append(self.rect.bottom)
		append.append(self.rect.top)
		append.append(self.rect.left)
		append.append(self.rect.right)	
		return append

	def hud(self,screen,kills,level,time,needed):
		font = pygame.font.Font(None, 20)
		kills = font.render("Kills: "+str(kills)+"/"+str(needed), 1, (255,255,255))
		level = font.render("Level: "+str(level), 1, (255,255,255))
		time = font.render("FPS: "+str(time), 1, (255,255,255))
		screen.blit(kills, (0,0))
		screen.blit(level, (80,0))
		screen.blit(time, (140,0))	
