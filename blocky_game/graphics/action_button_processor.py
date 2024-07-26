from abc import abstractmethod, ABC

from blocky_game.model.game_objects import GameObject, GameScreen, Person
from blocky_game.model.game_objects_container import GameObjectsContainer


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
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        self.game_screen = game_screen
        self.game_objects_container = game_objects_container

    @abstractmethod
    def select_active(self) -> list[GameObject]:
        pass


class ActionProcessorPersonSelectionActivity(ActionProcessorActivity):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

    def select_active(self) -> list[GameObject]:
        return list(self.game_objects_container["person"].values())


class ActionProcessorRoomSelectionActivity(ActionProcessorActivity):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

    def select_active(self) -> list[GameObject]:
        return list(self.game_objects_container["room"].values())


class ActionProcessorTakeableThingSelectionActivity(ActionProcessorActivity):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

    def select_active(self) -> list[GameObject]:
        return list(self.game_objects_container["takeable"].values())


class ActionProcessorEscapeSelectionActivity(ActionProcessorActivity):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

    def select_active(self) -> list[GameObject]:
        return list(self.game_objects_container["escape"].values())


class ActionProcessorEmptyPlaceSelectionActivity(ActionProcessorActivity):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

    def select_active(self) -> list[GameObject]:
        return list(filter(lambda place: place.is_free(), self.game_objects_container["place"].values()))


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

        if self.current_activity_index > activities_count:
            self.current_activity_index = activities_count

    def previous_activity(self):
        self.current_activity_index -= 1
        if self.current_activity_index < 0:
            self.current_activity_index = 0

    def is_finished(self) -> bool:
        return self.current_activity_index >= len(self.activities)

    def reset(self):
        self.current_activity_index = 0


class GraphicalActionButtonProcessor(ABC):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        self.game_screen = game_screen
        self.game_objects_container = game_objects_container
        self.is_active = False

        self.activities = ActionActivitiesSequence([])
        self.selected_objects = []

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
        self.activities.reset()

        for selected_object in self.selected_objects:
            selected_object.graphics_component.deselect()

        self.selected_objects.clear()

    def select_object(self, game_object: GameObject) -> bool:
        if not self.is_active:
            return False

        if game_object not in self.get_active():
            return False

        self.selected_objects.append(game_object)
        game_object.graphics_component.select()
        self.activities.next_activity()

        return True

    def deselect_last_object(self):
        if not self.selected_objects:
            return

        self.selected_objects.pop().graphics_component.deselect()
        self.activities.previous_activity()

    def get_last_selected_object(self) -> GameObject | None:
        if not self.selected_objects:
            return None

        return self.selected_objects[-1]

    def get_active(self) -> list[GameObject]:
        current_activity = self.activities.get_current_activity()

        if current_activity is None:
            return []

        return current_activity.select_active()

    @abstractmethod
    def get_name(self) -> str:
        pass


class GraphicalGoActionButtonProcessor(GraphicalActionButtonProcessor):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

        self.activities = ActionActivitiesSequence([
            ActionProcessorPersonSelectionActivity(game_screen, game_objects_container),
            ActionProcessorRoomSelectionActivity(game_screen, game_objects_container)
        ])

    def get_name(self) -> str:
        return "go"


class GraphicalTakeActionButtonProcessor(GraphicalActionButtonProcessor):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

        self.activities = ActionActivitiesSequence([
            ActionProcessorPersonSelectionActivity(game_screen, game_objects_container),
            ActionProcessorTakeableThingSelectionActivity(game_screen, game_objects_container)
        ])

    def get_name(self) -> str:
        return "take"


class GraphicalEscapeActionButtonProcessor(GraphicalActionButtonProcessor):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

        self.activities = ActionActivitiesSequence([
            ActionProcessorPersonSelectionActivity(game_screen, game_objects_container)
        ])

    def get_name(self) -> str:
        return "escape"


class GraphicalMoveActionButtonProcessor(GraphicalActionButtonProcessor):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

        self.activities = ActionActivitiesSequence([
            ActionProcessorPersonSelectionActivity(game_screen, game_objects_container),
            ActionProcessorRoomSelectionActivity(game_screen, game_objects_container),
            ActionProcessorEmptyPlaceSelectionActivity(game_screen, game_objects_container)
        ])

    def get_name(self) -> str:
        return "move"
