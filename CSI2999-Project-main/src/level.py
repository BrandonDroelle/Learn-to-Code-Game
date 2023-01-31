import pygame
from settings import *
from sprites import Generic, Tree
from player import Player
from pytmx.util_pygame import load_pygame

class Level:
	def __init__(self, current_map):

		# Get Display Surface
		self.display_surface = pygame.display.get_surface()

		# Sprite Groups
		self.all_sprites = CameraGroup()
		self.collision_sprites = pygame.sprite.Group()

		self.current_map = current_map

		self.setup()

	def setup(self):

		# Load Map Files
		try:
			tmx_map1 = load_pygame('./data/level1.tmx')
			tmx_map2 = load_pygame('./data/level2.tmx')
			tmx_map3 = load_pygame('./data/level3.tmx')
		except:
			tmx_map1 = load_pygame('../data/level1.tmx')
			tmx_map2 = load_pygame('../data/level2.tmx')
			tmx_map3 = load_pygame('../data/level3.tmx')

		# Set Currently Rendered Map
		if self.current_map == 'level1':
			current_map = tmx_map1
		elif self.current_map == 'level2':
			current_map = tmx_map2
		elif self.current_map == 'level3':
			current_map = tmx_map3

		# ---- Load Objects and Tiles from Map ----

		# Load Ground Tiles
		for x, y, surf in current_map.get_layer_by_name('Ground').tiles():
			Generic((x * TILE_SIZE,y * TILE_SIZE), surf, self.all_sprites, LAYERS['ground'])
		
		# Load Collision Tiles
		for x, y, surf in current_map.get_layer_by_name('Collision').tiles():
			Generic((x * TILE_SIZE, y * TILE_SIZE), pygame.Surface((TILE_SIZE, TILE_SIZE)), self.collision_sprites)

		# Load Tree Tiles
		for obj in current_map.get_layer_by_name('Trees'):
			Tree(
				pos = (obj.x, obj.y), 
				surf = obj.image, 
				groups = self.all_sprites)

		# Load Fence Sprites
		for x, y, surf in current_map.get_layer_by_name('Fencing').tiles():
			Generic((x * TILE_SIZE,y * TILE_SIZE), surf, [self.all_sprites], LAYERS['fencing'])

		# Load Player Sprite
		for obj in current_map.get_layer_by_name('Player'):
			if obj.name == 'Start':
				self.player = Player(
					pos = (obj.x,obj.y), 
					group = self.all_sprites,
					collision_sprites = self.collision_sprites)

	def run(self, dt):

		# Drawing Logic
		self.display_surface.fill('black')
		self.all_sprites.custom_draw()

		self.all_sprites.update(dt)

# Camara Group Class rendered sprites (assets)
# based on their y position on the screen.
# This means that if a sprite has a higher y position
# than another sprite, then the sprite with the higher y position
# is rendered behind the sprite with the lower y position 
class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.math.Vector2()
		self.offset.x = 0
		self.offset.y = 0

	def custom_draw(self):

		for layer in LAYERS.values():
			for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): # type: ignore
				if sprite.z == layer: # type: ignore
					offset_rect = sprite.rect.copy() # type: ignore
					offset_rect.center -= self.offset  # type: ignore
					self.display_surface.blit(sprite.image, offset_rect) # type: ignore
