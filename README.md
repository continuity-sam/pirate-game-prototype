# Pirate Game

A platformer adventure built with Pygame, featuring multiple levels, an overworld map, animated sprites, and classic game mechanics.

## Features

- **Overworld Map:** Navigate between levels using a node-based overworld.
- **Multiple Levels:** Progress through at least 6 levels, each with unique layouts and challenges.
- **Animated Sprites:** Player, enemies, and environmental objects are animated for a lively experience.
- **Health & UI:** Track your health and coins with a custom UI.
- **Level Unlocking:** Complete levels to unlock new ones on the overworld.
- **Audio:** Background music and sound effects enhance gameplay.

### Prerequisites

- Python 3.8+
- [Pygame](https://www.pygame.org/) (`pip install pygame`)
- [PyTMX](https://github.com/bitcraft/PyTMX) (`pip install pytmx`)
- TMX maps created with [Tiled](https://www.mapeditor.org/)

### Running the Game

1. Clone the repository or download the source code.
2. Ensure all dependencies are installed.
3. Run the game:

   ```sh
   python main.py
   ```

### Controls

- **Arrow Keys:** Move between nodes on the overworld and control the player in levels.
- **Space:** Select a level from the overworld or while in a level to attack.
- **Wall jump:** If on wall and push the up arrow key to jump of walls

## How It Works

- **Overworld Navigation:**  
  The player moves between nodes representing levels. Only unlocked levels can be entered.
- **Level Progression:**  
  Completing a level unlocks the next one. The game tracks progress and health.
- **Sprites & Assets:**  
  All graphics and sounds are loaded from the `data` folder using helper functions in `support.py`.
- **Game Loop:**  
  The main loop in `main.py` handles stage switching, rendering, and updates.

## Customization

- **Add Levels:**  
  Create new TMX files in `data/levels/` and update `main.py` to include them.
- **Edit Overworld:**  
  Use Tiled to modify `data/overworld/overworld.tmx` for new nodes and paths.
- **Change Sprites:**  
  Replace images in `data/graphics/` with your own artwork.

## Troubleshooting

- **Can't move to a level:**  
  Ensure the node exists in the TMX map and is connected via a path property.
- **Assets not loading:**  
  Check file paths and asset names in the `data` folder.
- **Game crashes:**  
  Run with a terminal to see error messages and debug using `debug.py`.

## Credits

- Developed with [Pygame](https://www.pygame.org/) and [PyTMX](https://github.com/bitcraft/PyTMX).
- Map editing with [Tiled](https://www.mapeditor.org/).
- Sprites, music, and sound effects from open-source or custom sources.

## Skulls

- Skulls will be hidden around the stages. Will you find them, young adventurers?