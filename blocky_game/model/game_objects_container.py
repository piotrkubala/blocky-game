from .game_objects import GameObject


class GameObjectsContainer:
    def __init__(self):
        self.container: dict[str, dict[str, GameObject]] = {}

    def add_object(self, type_name: str, game_object: GameObject):
        if type_name not in self.container:
            self.container[type_name] = {}
        self.container[type_name][game_object.name] = game_object

    def __getitem__(self, type_name: str) -> dict[str, GameObject]:
        if type_name not in self.container:
            self.container[type_name] = {}

        return self.container[type_name]
