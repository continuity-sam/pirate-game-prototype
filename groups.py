from settings import *
from sprites import Sprite

class AllSprites(pygame.sprite.Group):
	def __init__(self, width, height, clouds, bg_tile = None, top_limit = 0):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.offset = vector()
		self.width, self.height = width * TILE_SIZE, height * TILE_SIZE
		self.borders = {
			'left': 0, 
			'right': -self.width + WINDOW_WIDTH,
			'top': top_limit,
			'bottom': -self.height + WINDOW_HEIGHT
		}

		if bg_tile:
			for col in range(width):
				for row in range(-int(top_limit / TILE_SIZE) - 1, height):
					x, y = col * TILE_SIZE, row * TILE_SIZE
					Sprite((x,y), bg_tile, self, -1)
		else: # sky
			self.large_cloud = clouds['large']
			self.small_clouds = clouds['small']

	def camera_constraint(self):
		self.offset.x = self.offset.x if self.offset.x < self.borders['left'] else self.borders['left'] 
		self.offset.x = self.offset.x if self.offset.x > self.borders['right'] else self.borders['right']
		self.offset.y = self.offset.y if self.offset.y < self.borders['top'] else self.borders['top'] 
		self.offset.y = self.offset.y if self.offset.y > self.borders['bottom'] else self.borders['bottom']

	def draw(self, target_position):
		self.offset.x = -(target_position[0] - WINDOW_WIDTH / 2)
		self.offset.y = -(target_position[1] - WINDOW_HEIGHT / 2)
		self.camera_constraint()

		for sprite in sorted(self, key = lambda sprite: sprite.z):
			offset_position = sprite.rect.topleft + self.offset
			self.display_surface.blit(sprite.image, offset_position)