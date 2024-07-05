from dataclasses import dataclass


@dataclass
class PyGameConfig:
    frames_per_second: int = 60
    screen_width: int = 800
    screen_height: int = 600
    screen_title: str = "Blocky Game"


@dataclass
class BlockyGameConfig:
    domain_definition_path: str = "domain/blocky_game.pddl"
    problem_definition_path: str = "problems/problem1.pddl"
