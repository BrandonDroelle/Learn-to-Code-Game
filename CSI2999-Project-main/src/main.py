import pygame, sys
from level import Level
from settings import *

class Game:
	def __init__(self):

		# Load Pygame into File
		pygame.init()
		
		# Set Screen Width and Length from Variables in Settings
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		
		# Set Window Caption
		pygame.display.set_caption("Gilded Grizzlies Coding Adventure")

		# Creating Objects
		self.clock = pygame.time.Clock()
		self.level = Level()

	def run(self):

		while True:
			for event in pygame.event.get():
				# If the Quit Event is triggered, close the game
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			# Create Delta Time for Game Physics
			dt = self.clock.tick() / 20

			# Run Game
			self.level.run(dt)
			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()