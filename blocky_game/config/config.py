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
    fullscreen = False
    use_native_screen_resolution = False


class GeneratorConfig:
    def __init__(self, rows: int, columns: int, keys_count: int, mixing_steps: int,
                 generator: type[ProblemGenerator] = SimpleProblemGenerator):
        self.generator = generator
        self.rows = rows
        self.columns = columns
        self.keys_count = keys_count
        self.mixing_steps = mixing_steps


@dataclass
class BlockyGameConfig:
    domain_definition_path: str = "../domain/blocky_game.pddl"
    problem_definition_path: str = "../problems/problem1.pddl" # "../problems/problem1.pddl"
    state_serialization_path: str | None = None # "../problems/problem2-serialized.pddl"
    actions_list_path: str | None = "../solutions/problem2-solution.actions"
    generator_config: GeneratorConfig | None = None #\
        #GeneratorConfig(6, 6, 6, 150, SimpleProblemGenerator)
