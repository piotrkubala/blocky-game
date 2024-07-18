import pygame
import numpy as np

from blocky_game.config.config import PyGameConfig, BlockyGameConfig
from blocky_game.graphics.game_renderer import GameRenderer
from blocky_game.model.board_state import BoardState
from blocky_game.model.board_domain import BoardDomain
from blocky_game.graphics.animations import AnimationsBox, PulsatingAnimation, LinearAnimation


class BlockyGame:
    def __process_mouse_click(self, x: int, y: int):
        point = np.array([x, y])
        colliding_object = self.renderer.get_object_colliding_with_point(point, self.animations_box)
        if colliding_object is None:
            return

        animation = self.animations_box[colliding_object]
        if animation is None:
            new_animation = PulsatingAnimation(1000, 0.1)
            self.animations_box[colliding_object] = new_animation
        else:
            current_transformation = self.renderer.get_object_transform(colliding_object)
            new_animation = LinearAnimation(1000, current_transformation)
            self.animations_box[colliding_object] = new_animation

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

        # TODO: delete this:
        print(self.board_state.serialize_state("blocky-problem-test"))


    def __update_display(self):
        pygame.display.update()

    def __clear_display(self):
        self.display.fill((255, 255, 255))

    def __wait_for_clock(self):
        self.clock.tick(self.game_config.frames_per_second)
        current_time = pygame.time.get_ticks()
        self.delta_time = current_time - self.last_tick_time
        self.last_tick_time = current_time

    def __render_game(self):
        self.renderer.render(self.animations_box)
        self.animations_box.update(self.delta_time)

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

        self.animations_box = AnimationsBox()
        self.renderer = GameRenderer(self.board_state, self.display)

        self.stopped = False
        self.last_tick_time = pygame.time.get_ticks()
        self.delta_time = 0

        self.__init_pygame()

    def main_loop(self):
        while not self.stopped:
            self.__wait_for_clock()
            self.__process_events()
            self.__clear_display()
            self.__render_game()
            self.__update_display()

        self.__quit_pygame()
