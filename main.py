from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join, dirname, abspath

from support import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pirate Game")
        self.clock = pygame.time.Clock()
        self.import_assets()

        base_dir = dirname(abspath(__file__))
        tmx_path = join(base_dir, 'data', 'levels', 'omni.tmx')   
        self.tmx_map = {0: load_pygame(tmx_path)}

        self.current_stage = Level(self.tmx_map[0], self.level_frames)

    def import_assets(self):
        base_dir = dirname(abspath(__file__))
        self.level_frames = {
            'flag': import_folder(base_dir, 'data', 'graphics', 'level', 'flag'),
            'saw': import_folder(base_dir, 'data', 'graphics', 'enemies', 'saw', 'animation'),
            'floor_spike': import_folder(base_dir, 'data', 'graphics', 'enemies', 'floor_spikes'),
            'palms': import_sub_folders(base_dir, 'data', 'graphics', 'level', 'palms'),
            'candle': import_folder(base_dir, 'data', 'graphics', 'level', 'candle'),
            'window': import_folder(base_dir, 'data', 'graphics', 'level', 'window'),
            'big_chain': import_folder(base_dir, 'data', 'graphics', 'level', 'big_chains'),
            'small_chain': import_folder(base_dir, 'data', 'graphics', 'level', 'small_chains'),
            'candle_light': import_folder(base_dir, 'data', 'graphics', 'level', 'candle light'),
        }

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run(dt) 
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()

 