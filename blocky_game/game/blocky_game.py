import pygame

from blocky_game.config.config import PyGameConfig, BlockyGameConfig
from blocky_game.game.actions_list import ActionsList
from blocky_game.graphics.game_renderer import GameRenderer
from blocky_game.graphics.interface_manager import InterfaceManager
from blocky_game.model.board_state import BoardState
from blocky_game.model.board_domain import BoardDomain
from blocky_game.graphics.animations import AnimationsBox


class BlockyGame:
    def __process_mouse_click(self, x: int, y: int):
        if self.actions_list.done():
            self.interface_manager.process_click(x, y)

    def __process_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.stopped = True
                case pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.__process_mouse_click(x, y)

    def __is_delay_time_over(self):
        return pygame.time.get_ticks() - self.last_static_action_time > \
               self.game_config.animation_duration + self.game_config.actions_delay

    def __process_noninteractive_actions(self):
        if self.actions_list.done() or self.animations_box.is_animation_active():
            return

        if not self.__is_delay_time_over():
            return

        action = self.actions_list.get_action()
        self.actions_list.update_index()

        if action is not None:
            action.execute(self.game_config.animation_duration)
            self.last_static_action_time = pygame.time.get_ticks()

    def __check_if_game_is_over(self):
        if not self.__is_delay_time_over():
            return

        if self.board_state.game_objects_container.is_game_ended():
            self.stopped = True

    def __init_pygame(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(self.game_config.screen_title)

    def __quit_pygame(self):
        pygame.quit()

        serialization_path = self.blocky_game_config.state_serialization_path

        if serialization_path is None:
            return

        file_name = serialization_path.split("/")[-1]
        problem_name = file_name.split(".")[0]

        with open(serialization_path, "w") as file:
            file.write(self.board_state.serialize_state(problem_name))

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

        self.__init_pygame()

        self.board_domain = BoardDomain(blocky_game_config.domain_definition_path)
        self.board_state = BoardState(self.board_domain, blocky_game_config.problem_definition_path)

        width = self.game_config.screen_width
        height = self.game_config.screen_height
        self.display = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.board_state.center_board(width, height, self.game_config.size_ratio)

        self.animations_box = AnimationsBox()
        self.renderer = GameRenderer(self.board_state, self.display)

        self.interface_manager = InterfaceManager(
            self.board_state.game_screen,
            self.renderer,
            self.board_state,
            self.animations_box,
            self.board_state.game_objects_container,
            width, height
        )

        self.actions_list = ActionsList(
            self.blocky_game_config.actions_list_path,
            self.animations_box,
            self.renderer,
            self.board_state
        )

        self.stopped = False
        self.last_tick_time = pygame.time.get_ticks()
        self.delta_time = 0
        self.last_static_action_time = pygame.time.get_ticks() - self.game_config.animation_duration

    def main_loop(self):
        while not self.stopped:
            self.__wait_for_clock()
            self.__process_events()
            self.__process_noninteractive_actions()
            self.__clear_display()
            self.__render_game()
            self.__update_display()
            self.__check_if_game_is_over()

        self.__quit_pygame()
