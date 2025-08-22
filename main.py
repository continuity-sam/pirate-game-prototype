from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join, dirname, abspath
from support import *
from data import Data
from debug import debug
from ui import UI
from overworld import Overworld

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
        self.tmx_map = {
            0: load_pygame(join(base_dir, 'data', 'levels', '0.tmx')),
            1: load_pygame(join(base_dir, 'data', 'levels', '1.tmx')),
            2: load_pygame(join(base_dir, 'data', 'levels', '2.tmx')),
            3: load_pygame(join(base_dir, 'data', 'levels', '3.tmx')),
            4: load_pygame(join(base_dir, 'data', 'levels', '4.tmx')),
            5: load_pygame(join(base_dir, 'data', 'levels', '5.tmx'))
                        }
        self.tmx_overworld = load_pygame(join(base_dir, 'data', 'overworld', 'overworld.tmx'))
        self.current_stage = Level(self.tmx_map[self.data.current_level], self.level_frames, self.audio_files, self.data, self.switch_stage)
        self.bg_music.play(-1)

    def switch_stage(self, target, unlock = 0):
        if target == 'level':
            self.current_stage =  Level(self.tmx_map[self.data.current_level], self.level_frames, self.audio_files, self.data, self.switch_stage)
        else: # overworld
            if unlock > 0:
                self.data.unlocked_level = unlock
            else:
                self.data.health -= 1
            self.current_stage = Overworld(self.tmx_overworld, self.data, self.overworld_frames, self.switch_stage)

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
        self.overworld_frames = {
            'palms': import_folder(base_dir, 'data', 'graphics', 'overworld', 'palm'),
            'water': import_folder(base_dir, 'data', 'graphics', 'overworld', 'water'),
            'path': import_folder_dict(base_dir, 'data', 'graphics', 'overworld', 'path'),
            'icon': import_sub_folders(base_dir, 'graphics', 'overworld', 'icon'),
        }

        self.audio_files = {
            'coin': pygame.mixer.Sound(join(base_dir, 'audio', 'coin.wav')),
            'attack': pygame.mixer.Sound(join(base_dir, 'audio', 'attack.wav')),
            'jump': pygame.mixer.Sound(join(base_dir, 'audio', 'jump.wav')),
            'damage' : pygame.mixer.Sound(join(base_dir, 'audio', 'damage.wav')),
            'pearl': pygame.mixer.Sound(join(base_dir, 'audio', 'pearl.wav')),
        }

        self.bg_music = pygame.mixer.Sound(join(base_dir, 'audio', 'starlight_city.mp3'))
        
    def check_game_over(self):
        if self.data.health <= 0:
            pygame.quit()
            sys.exit()

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.check_game_over()
            self.current_stage.run(dt) 
            self.ui.update(dt)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()