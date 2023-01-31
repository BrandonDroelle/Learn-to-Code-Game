import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, group, collision_sprites):
		super().__init__(group)

		self.frame_index = 0
		self.collision_sprites = collision_sprites

		# general setup
		try:
			self.image = pygame.image.load('./graphics/character/bear.png')
		except:
			self.image = pygame.image.load('../graphics/character/bear.png')

		self.rect = self.image.get_rect(center = pos)
		self.z = LAYERS['main']

		# Movement Attributes
		self.direction = pygame.math.Vector2()
		self.pos = pygame.math.Vector2(self.rect.center)
		self.old_pos = pygame.math.Vector2(self.rect.center)
		self.key_pressed = False

		# Hitbox
		self.hitbox = self.rect.copy().inflate((-126,-70))


	def input(self):

		# Get all Pressed Keys
		keys = pygame.key.get_pressed()
		
		if not any(pygame.key.get_pressed()) and self.key_pressed == True:
			self.key_pressed = False

		if any(pygame.key.get_pressed()) and self.key_pressed == False:
			# directions 
			if keys[pygame.K_UP]:
				self.move_up()
			elif keys[pygame.K_DOWN]:
				self.move_down()
			else:
				pass

			if keys[pygame.K_RIGHT]:
				self.move_right()
			elif keys[pygame.K_LEFT]:
				self.move_left()
			else:
				pass
			
			self.key_pressed = True


	def move_up(self):
		new_pos = self.pos.y - MOVE_CONSTANT
		self.pos.y = new_pos
	
	def move_down(self):
		new_pos = self.pos.y + MOVE_CONSTANT
		self.pos.y = new_pos
	
	def move_left(self):
		new_pos = self.pos.x - MOVE_CONSTANT
		self.pos.x = new_pos
	
	def move_right(self):
		new_pos = self.pos.x + MOVE_CONSTANT
		self.pos.x = new_pos

	def collision(self):
		for sprite in self.collision_sprites.sprites():
			if hasattr(sprite, 'hitbox'):
				if sprite.hitbox.colliderect(self.hitbox):
					# Set X Coordinate to Previous Value
					self.rect.centerx = self.old_pos.x # type: ignore
					self.pos.x = self.old_pos.x
					# Set Y Coordinate to Previous Value
					self.rect.centery = self.old_pos.y # type: ignore
					self.pos.y = self.old_pos.y

	def move(self):

		# Horizontal Movement
		self.hitbox.centerx = round(self.pos.x)
		self.rect.centerx = self.hitbox.centerx # type: ignore

		# Vertical Movement
		self.hitbox.centery = round(self.pos.y)
		self.rect.centery = self.hitbox.centery # type: ignore

		self.collision()

		if self.rect.center != self.old_pos: # type: ignore
			self.old_pos.x = self.rect.centerx # type: ignore
			self.old_pos.y = self.rect.centery # type: ignore

	def update(self, dt):
		self.input()
		self.move()
