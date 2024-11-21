from blocky_game.generator.problem_generator import ProblemGenerator, SimpleProblemGenerator


class GeneratorConfig:
    def __init__(self, rows: int, columns: int, keys_count: int, mixing_steps: int,
                 generator: type[ProblemGenerator] = SimpleProblemGenerator):
        self.generator = generator
        self.rows = rows
        self.columns = columns
        self.keys_count = keys_count
        self.mixing_steps = mixing_steps
