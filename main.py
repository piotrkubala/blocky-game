from blocky_game.game.blocky_game import BlockyGame
from blocky_game.config.config import PyGameConfig, BlockyGameConfig

if __name__ == '__main__':
    pygame_config = PyGameConfig()
    blocky_game_config = BlockyGameConfig()

    blocky_game = BlockyGame(pygame_config, blocky_game_config)
    blocky_game.main_loop()
