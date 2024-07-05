import pygame

from blocky_game.config.config import PyGameConfig, BlockyGameConfig
from blocky_game.graphics.game_renderer import GameRenderer
from blocky_game.model.board_state import BoardState
from blocky_game.model.board_domain import BoardDomain


class BlockyGame:
    def __process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stopped = True

    def __init_pygame(self):
        pygame.init()

    def __quit_pygame(self):
        pygame.quit()

    def __update_display(self):
        pygame.display.update()

    def __clear_display(self):
        self.display.fill((255, 255, 255))

    def __init__(self, game_config: PyGameConfig, blocky_game_config: BlockyGameConfig):
        self.game_config = game_config
        self.blocky_game_config = blocky_game_config

        self.board_domain = BoardDomain(blocky_game_config.domain_definition_path)
        self.board_state = BoardState(self.board_domain, blocky_game_config.problem_definition_path)

        self.renderer = GameRenderer(self.board_state)

        width = self.game_config.screen_width
        height = self.game_config.screen_height
        self.display = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.stopped = False

        self.__init_pygame()

    def main_loop(self):
        while not self.stopped:
            self.__process_events()
            self.__clear_display()
            self.renderer.render()
            self.__update_display()

        self.__quit_pygame()
