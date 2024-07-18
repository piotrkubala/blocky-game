import pygame
import numpy as np

from blocky_game.config.config import PyGameConfig, BlockyGameConfig
from blocky_game.graphics.game_renderer import GameRenderer
from blocky_game.model.board_state import BoardState
from blocky_game.model.board_domain import BoardDomain


class BlockyGame:
    def __process_mouse_click(self, x: int, y: int):
        point = np.array([x, y])
        print(self.renderer.get_object_colliding_with_point(point))

    def __process_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.stopped = True
                case pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.__process_mouse_click(x, y)

    def __init_pygame(self):
        pygame.init()
        pygame.display.set_caption(self.game_config.screen_title)

    def __quit_pygame(self):
        pygame.quit()

    def __update_display(self):
        pygame.display.update()

    def __clear_display(self):
        self.display.fill((255, 255, 255))

    def __wait_for_clock(self):
        self.clock.tick(self.game_config.frames_per_second)

    def __init__(self, game_config: PyGameConfig, blocky_game_config: BlockyGameConfig):
        self.game_config = game_config
        self.blocky_game_config = blocky_game_config

        self.board_domain = BoardDomain(blocky_game_config.domain_definition_path)
        self.board_state = BoardState(self.board_domain, blocky_game_config.problem_definition_path)

        width = self.game_config.screen_width
        height = self.game_config.screen_height
        self.display = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.board_state.center_board(width, height, self.game_config.size_ratio)

        self.renderer = GameRenderer(self.board_state, self.display)

        self.stopped = False

        self.__init_pygame()

    def main_loop(self):
        while not self.stopped:
            self.__wait_for_clock()
            self.__process_events()
            self.__clear_display()
            self.renderer.render()
            self.__update_display()

        self.__quit_pygame()
