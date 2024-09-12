from abc import ABC, abstractmethod

from blocky_game.model.game_objects import (
    GameObject
)
from blocky_game.model.board_state import BoardState


class ProblemGenerator(ABC):
    @abstractmethod
    def generate(self) -> BoardState:
        pass


class SimpleProblemGenerator(ProblemGenerator):
    def __init__(self, columns: int, rows: int, keys_count: int):
        self.columns = columns
        self.rows = rows
        self.keys_count = keys_count

    def generate(self) -> BoardState:
        pass

