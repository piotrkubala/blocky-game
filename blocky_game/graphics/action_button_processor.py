from abc import abstractmethod, ABC

from blocky_game.model.game_objects import GameObject, GameScreen


class GameObjectsAggregator(ABC):
    def __init__(self):
        self.container: dict[str, GameObject] = {}

    def add_object(self, game_object: GameObject):
        self.container[game_object.name] = game_object

    def get_object(self, name: str) -> GameObject:
        return self.container[name]

    def get_objects(self) -> list[GameObject]:
        return list(self.container.values())


class ActionProcessorActivity(ABC):
    pass


class ActionActivitiesSequence:
    def __init__(self, activities: list[ActionProcessorActivity]):
        self.activities = activities
        self.current_activity_index = 0

    def get_current_activity(self) -> ActionProcessorActivity | None:
        return self.activities[self.current_activity_index] \
            if self.current_activity_index < len(self.activities) else None

    def next_activity(self):
        self.current_activity_index += 1
        activities_count = len(self.activities)

        if self.current_activity_index >= activities_count:
            self.current_activity_index = activities_count - 1

    def previous_activity(self):
        self.current_activity_index -= 1
        if self.current_activity_index < 0:
            self.current_activity_index = 0

    def is_finished(self) -> bool:
        return self.current_activity_index >= len(self.activities)

    def reset(self):
        self.current_activity_index = 0


class GraphicalActionButtonProcessor(ABC):
    def __init__(self, game_screen: GameScreen):
        self.game_screen = game_screen

    @abstractmethod
    def get_name(self) -> str:
        pass


class GraphicalGoActionButtonProcessor(GraphicalActionButtonProcessor):
    def __init__(self, game_screen: GameScreen):
        super().__init__(game_screen)

    def get_name(self) -> str:
        return "go"


class GraphicalTakeActionButtonProcessor(GraphicalActionButtonProcessor):
    def __init__(self, game_screen: GameScreen):
        super().__init__(game_screen)

    def get_name(self) -> str:
        return "take"


class GraphicalEscapeActionButtonProcessor(GraphicalActionButtonProcessor):
    def __init__(self, game_screen: GameScreen):
        super().__init__(game_screen)

    def get_name(self) -> str:
        return "escape"


class GraphicalMoveActionButtonProcessor(GraphicalActionButtonProcessor):
    def __init__(self, game_screen: GameScreen):
        super().__init__(game_screen)

    def get_name(self) -> str:
        return "move"
