from dataclasses import dataclass

from blocky_game.config.config_helper import GeneratorConfig
from blocky_game.generator.problem_generator import SimpleProblemGenerator


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


@dataclass
class BlockyGameConfig:
    domain_definition_name: str = "blocky_game"
    problem_definition_path: str = "test-problem.pddl"
    state_serialization_name: str | None = None # "test-problem"
    actions_list_name: str | None = "test-problem-solution"
    generator_config: GeneratorConfig | None = None # \
        #GeneratorConfig(7, 7, 8, 150, SimpleProblemGenerator)
