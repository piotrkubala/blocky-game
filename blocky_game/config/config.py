from dataclasses import dataclass

from blocky_game.generator.problem_generator import ProblemGenerator, SimpleProblemGenerator


@dataclass
class PyGameConfig:
    frames_per_second: int = 30
    screen_width: int = 1200
    screen_height: int = 750
    screen_title: str = "Blocky Game"
    size_ratio: float = 0.9
    actions_delay = 250.0
    animation_duration = 500.0


class GeneratorConfig:
    def __init__(self, rows: int, columns: int, keys_count: int,
                 generator: type[ProblemGenerator] = SimpleProblemGenerator):
        self.generator = generator
        self.rows = rows
        self.columns = columns
        self.keys_count = keys_count


@dataclass
class BlockyGameConfig:
    domain_definition_path: str = "../domain/blocky_game.pddl"
    problem_definition_path: str = "../problems/problem1.pddl"
    state_serialization_path: str | None = "../problems/problem1-serialized.pddl"
    actions_list_path: str | None = None# "../solutions/problem1-solution.actions"
    generator_config: GeneratorConfig | None = GeneratorConfig(5, 4, 4, SimpleProblemGenerator)
