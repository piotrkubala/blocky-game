from abc import abstractmethod, ABC

from blocky_game.graphics.animations import AnimationsBox
from blocky_game.graphics.game_renderer import GameRenderer
from blocky_game.model.actions import Action, GoAction, TakeAction, EscapeAction, MoveAction
from blocky_game.model.board_state import BoardState
from blocky_game.model.game_objects import GameObject, GameScreen, Person, Room, Place, Key, MapExit, Terminal
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
        return list(self.game_objects_container.get_people().values())


class ActionProcessorRoomSelectionActivity(ActionProcessorActivity):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

    def select_active(self) -> list[GameObject]:
        return list(self.game_objects_container.get_rooms().values())


class ActionProcessorTakeableThingSelectionActivity(ActionProcessorActivity):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

    def select_active(self) -> list[GameObject]:
        return list(self.game_objects_container.get_takeables().values())


class ActionProcessorEscapeSelectionActivity(ActionProcessorActivity):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

    def select_active(self) -> list[GameObject]:
        return list(self.game_objects_container.get_map_exits().values())


class ActionProcessorEmptyPlaceSelectionActivity(ActionProcessorActivity):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

    def select_active(self) -> list[GameObject]:
        return list(filter(lambda place: place.is_free(), self.game_objects_container.get_places().values()))


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

    def is_finished(self) -> bool:
        return self.is_active and self.activities.is_finished()

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

    @abstractmethod
    def generate_action(self, animations_box: AnimationsBox, renderer: GameRenderer,
                        board_state: BoardState) -> Action | None:
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

    def generate_action(self, animations_box: AnimationsBox, renderer: GameRenderer,
                        board_state: BoardState) -> Action | None:
        if not self.is_finished():
            return None

        person: Person = self.selected_objects[0]
        room2: Room = self.selected_objects[1]

        potential_places_person = [place for place in self.game_objects_container.get_places().values()
                                   if place.is_transitive_child(person)]
        potential_places_room2 = [place for place in self.game_objects_container.get_places().values()
                                  if place.is_transitive_child(room2)]

        if not potential_places_person or not potential_places_room2:
            return None

        place1: Place = potential_places_person[0]
        place2: Place = potential_places_room2[0]

        if place1.is_free() or place2.is_free():
            return None

        adjacency_direction = self.game_screen.game_board.get_adjacency_direction(place1, place2)
        if adjacency_direction is None:
            return None
        reverse_direction = adjacency_direction.reverse()

        room1 = place1.room

        entrance1 = room1.entrances[adjacency_direction]
        entrance2 = room2.entrances[reverse_direction]

        common_colours = set(colour for colour in entrance1.colours_dict.values()
                             if colour.name in entrance2.colours_dict)

        correct_keys: list[Key] = [key for key in self.game_objects_container.get_keys().values()
                                   if person.is_owned(key) and key.colour in common_colours]

        if not correct_keys:
            return None

        key = correct_keys[0]
        colour = key.colour

        return GoAction(animations_box, renderer, board_state,
                        person, room1, room2, place1, place2,
                        entrance1, entrance2, adjacency_direction, colour, key)


class GraphicalTakeActionButtonProcessor(GraphicalActionButtonProcessor):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

        self.activities = ActionActivitiesSequence([
            ActionProcessorPersonSelectionActivity(game_screen, game_objects_container),
            ActionProcessorTakeableThingSelectionActivity(game_screen, game_objects_container)
        ])

    def get_name(self) -> str:
        return "take"

    def generate_action(self, animations_box: AnimationsBox, renderer: GameRenderer,
                        board_state: BoardState) -> Action | None:
        if not self.is_finished():
            return None

        person: Person = self.selected_objects[0]
        takeable_thing = self.selected_objects[1]

        possible_rooms = [room for room in self.game_objects_container.get_rooms().values()
                          if room.is_transitive_child(takeable_thing)]

        if not possible_rooms:
            return None

        room: Room = possible_rooms[0]

        return TakeAction(animations_box, renderer, board_state, person, takeable_thing, room)


class GraphicalEscapeActionButtonProcessor(GraphicalActionButtonProcessor):
    def __init__(self, game_screen: GameScreen, game_objects_container: GameObjectsContainer):
        super().__init__(game_screen, game_objects_container)

        self.activities = ActionActivitiesSequence([
            ActionProcessorPersonSelectionActivity(game_screen, game_objects_container)
        ])

    def get_name(self) -> str:
        return "escape"

    def generate_action(self, animations_box: AnimationsBox, renderer: GameRenderer,
                        board_state: BoardState) -> Action | None:
        if not self.is_finished():
            return None

        person: Person = self.selected_objects[0]

        possible_rooms: list[Room] = [room for room in self.game_objects_container.get_rooms().values()
                                      if room.is_transitive_child(person)]

        if not possible_rooms:
            return None

        room = possible_rooms[0]

        possible_exits: list[MapExit] = [map_exit for map_exit in self.game_objects_container.get_map_exits().values()
                                         if room.is_transitive_child(map_exit)]

        if not possible_exits:
            return None

        map_exit = possible_exits[0]

        return EscapeAction(animations_box, renderer, board_state, person, map_exit, room)


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

    def generate_action(self, animations_box: AnimationsBox, renderer: GameRenderer,
                        board_state: BoardState) -> Action | None:
        if not self.is_finished():
            return None

        person: Person = self.selected_objects[0]
        moved_room: Room = self.selected_objects[1]
        place2: Place = self.selected_objects[2]

        possible_rooms_person: list[Room] = [room for room in self.game_objects_container.get_rooms().values()
                                             if room.is_transitive_child(person)]

        if not possible_rooms_person:
            return None

        dwelled_room = possible_rooms_person[0]

        possible_terminals: list[Terminal] = [terminal for terminal in
                                              self.game_objects_container.get_terminals().values()
                                              if dwelled_room.is_transitive_child(terminal)]

        if not possible_terminals:
            return None

        terminal = possible_terminals[0]

        possible_places_room: list[Place] = [place for place in self.game_objects_container.get_places().values()
                                             if place.is_transitive_child(moved_room)]

        if not possible_places_room:
            return None

        place1 = possible_places_room[0]

        adjacency_direction = self.game_screen.game_board.get_adjacency_direction(place1, place2)

        if adjacency_direction is None:
            return None

        return MoveAction(animations_box, renderer, board_state, moved_room, place1, place2,
                          adjacency_direction, person, dwelled_room, terminal)
