from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join, dirname, abspath
from support import *
from data import Data
from debug import debug
from ui import UI

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pirate Game")
        self.clock = pygame.time.Clock()
        self.import_assets()

        self.ui = UI(self.font, self.ui_frames)
        self.data = Data(self.ui)
        base_dir = dirname(abspath(__file__))
        tmx_path = join(base_dir, 'data', 'levels', 'omni.tmx')   
        self.tmx_map = {0: load_pygame(tmx_path)}
        self.current_stage = Level(self.tmx_map[0], self.level_frames, self.data)

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
            'player': import_sub_folders(base_dir, 'data', 'graphics', 'player'),
            'saw': import_folder(base_dir, 'data', 'graphics', 'enemies', 'saw', 'animation'),
            'saw_chain': import_image(base_dir, 'data', 'graphics', 'enemies', 'saw', 'saw_chain'),
            'helicopter': import_folder(base_dir, 'data', 'graphics', 'level', 'helicopter'),
            'boat': import_folder(base_dir, 'data', 'graphics', 'objects', 'boat'), 
            'spike': import_image(base_dir, 'data', 'graphics', 'enemies', 'spike_ball', 'Spiked Ball'),
            'spike_chain': import_image(base_dir, 'data', 'graphics', 'enemies', 'spike_ball', 'Spiked_Chain'),
            'tooth': import_folder(base_dir, 'data', 'graphics', 'enemies', 'tooth', 'run'),
            'shell': import_sub_folders(base_dir, 'data', 'graphics', 'enemies', 'shell'),
            'pearl': import_image(base_dir, 'data', 'graphics', 'enemies', 'bullets', 'pearl'),
            'items': import_sub_folders(base_dir, 'data', 'graphics', 'items'),
            'particle': import_folder(base_dir, 'data', 'graphics', 'effects', 'particle'),
            'water_top': import_folder(base_dir, 'data', 'graphics', 'level', 'water', 'top'),
            'water_body': import_image(base_dir, 'data', 'graphics', 'level', 'water', 'body'),
            'bg_tiles': import_folder_dict(base_dir, 'data', 'graphics', 'level', 'bg', 'tiles'),
            'cloud_small': import_folder(base_dir, 'data', 'graphics', 'level', 'clouds', 'small'),
            'cloud_large': import_image(base_dir, 'data', 'graphics', 'level', 'clouds', 'large_cloud'),
        } 
        self.font = pygame.font.Font(join(base_dir, 'data', 'graphics', 'ui', 'runescape_uf.ttf'), 40)
        self.ui_frames = {
            'heart': import_folder(base_dir, 'data', 'graphics', 'ui', 'heart'),
            'coin': import_image(base_dir, 'data', 'graphics', 'ui', 'coin')
        }

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run(dt) 
            self.ui.update(dt)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()

 