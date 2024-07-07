import pygame
import numpy as np

from blocky_game.model.board_state import BoardState, GameObject


class GameRenderer:
    def __render_game_object(self, game_object: GameObject, transformation: np.ndarray):
        game_object.graphics_component.draw(self.screen, transformation)

        transformation = transformation @ game_object.graphics_component.transform
        for child in game_object.get_children():
            self.__render_game_object(child, transformation)

    def __init__(self, board_state: BoardState, screen: pygame.Surface):
        self.board_state = board_state
        self.screen = screen

    def render(self):
        self.__render_game_object(self.board_state.game_board, np.identity(3))
