from dataclasses import dataclass


@dataclass
class PyGameConfig:
    frames_per_second: int = 30
    screen_width: int = 1200
    screen_height: int = 750
    screen_title: str = "Blocky Game"
    size_ratio: float = 0.9


@dataclass
class BlockyGameConfig:
    domain_definition_path: str = "../domain/blocky_game.pddl"
    problem_definition_path: str = "../problems/problem1.pddl"
