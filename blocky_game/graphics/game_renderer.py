import pygame

from blocky_game.model.board_state import BoardState


class GameRenderer:
    def __init__(self, board_state: BoardState):
        self.board_state = board_state

    def render(self):
        pass
