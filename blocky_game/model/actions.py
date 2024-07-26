from abc import ABC, abstractmethod

from blocky_game.graphics.animations import AnimationsBox
from blocky_game.graphics.game_renderer import GameRenderer
from blocky_game.model.board_state import BoardState
from blocky_game.model.game_objects import (
    Person, Direction, Key, Colour, Entrance, Place, Room, GameBoard, GameObject, TakeableThing, MapExit, Terminal,
)


class Action(ABC):
    def __init__(self, animations_box: AnimationsBox, renderer: GameRenderer, board_state: BoardState):
        self.animations_box = animations_box
        self.renderer = renderer
        self.board_state = board_state

    def set_move_animation(self, game_object: GameObject, duration: float):
        initial_transform = self.renderer.get_object_transform(game_object)
        self.animations_box.set_move_animation(game_object, duration, initial_transform)

    @abstractmethod
    def check_preconditions(self) -> bool:
        pass

    @abstractmethod
    def execute(self) -> bool:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_params_names(self) -> list[str]:
        pass

    def __str__(self):
        params = self.get_params_names()
        params_str = ", ".join(params)

        return f"{self.get_name()}({params_str})"


class GoAction(Action):
    def __init__(self, animations_box: AnimationsBox, renderer: GameRenderer, board_state: BoardState,
                 person: Person, room1: Room, room2: Room,
                 place1: Place, place2: Place,
                 entrance1: Entrance, entrance2: Entrance,
                 direction: Direction, colour: Colour, key: Key):
        super().__init__(animations_box, renderer, board_state)

        self.person = person
        self.room1 = room1
        self.room2 = room2
        self.place1 = place1
        self.place2 = place2
        self.entrance1 = entrance1
        self.entrance2 = entrance2
        self.direction = direction
        self.colour = colour
        self.key = key

    def check_preconditions(self) -> bool:
        are_rooms_adjacent = self.board_state.game_board.are_adjacent(self.room1, self.room2)
        is_room1_at_place1 = self.place1.is_room_at(self.room1)
        is_room2_at_place2 = self.place2.is_room_at(self.room2)
        has_passage_room1 = self.room1.has_passage(self.entrance1, self.direction)
        has_passage_room2 = self.room2.has_passage(self.entrance2, self.direction.reverse())
        has_door_entrance1 = self.entrance1.has_door(self.colour)
        has_door_entrance2 = self.entrance2.has_door(self.colour)
        is_person_in_room1 = self.room1.is_person_in(self.person)
        is_key_owned = self.person.is_owned(self.key)
        is_key_of_colour = self.key.is_of_colour(self.colour)

        return are_rooms_adjacent \
            and is_room1_at_place1 \
            and is_room2_at_place2 \
            and has_passage_room1 \
            and has_passage_room2 \
            and has_door_entrance1 \
            and has_door_entrance2 \
            and is_person_in_room1 \
            and is_key_owned \
            and is_key_of_colour

    def execute(self) -> bool:
        if not self.check_preconditions():
            return False

        self.room1.remove_person(self.person)
        self.room2.add_person(self.person)

        self.set_move_animation(self.person, 0.5)

        return True

    def get_name(self) -> str:
        return "go"

    def get_params_names(self) -> list[str]:
        return [
            self.person.name,
            self.room1.name,
            self.room2.name,
            self.place1.name,
            self.place2.name,
            self.entrance1.name,
            self.entrance2.name,
            self.direction.name,
            self.colour.name,
            self.key.name,
        ]


class TakeAction(Action):
    def __init__(self, animations_box: AnimationsBox, renderer: GameRenderer, board_state: BoardState,
                 person: Person, thing: TakeableThing, room: Room):
        super().__init__(animations_box, renderer, board_state)

        self.person = person
        self.thing = thing
        self.room = room

    def check_preconditions(self) -> bool:
        is_thing_in_room = self.room.does_contain(self.thing)
        is_person_in_room = self.room.is_person_in(self.person)

        return is_thing_in_room and is_person_in_room

    def execute(self) -> bool:
        if not self.check_preconditions():
            return False

        self.room.remove_thing(self.thing)
        self.person.add_equipment(self.thing)

        return True

    def get_name(self) -> str:
        return "take"

    def get_params_names(self) -> list[str]:
        return [
            self.person.name,
            self.thing.name,
            self.room.name,
        ]


class EscapeAction(Action):
    def __init__(self, animations_box: AnimationsBox, renderer: GameRenderer, board_state: BoardState,
                 person: Person, map_exit: MapExit, room: Room):
        super().__init__(animations_box, renderer, board_state)

        self.person = person
        self.map_exit = map_exit
        self.room = room

    def check_preconditions(self) -> bool:
        is_exit_in_room = self.room.does_contain(self.map_exit)
        is_person_in_room = self.room.is_person_in(self.person)

        return is_exit_in_room and is_person_in_room

    def execute(self) -> bool:
        if not self.check_preconditions():
            return False

        self.person.escape()

        return True

    def get_name(self) -> str:
        return "escape"

    def get_params_names(self) -> list[str]:
        return [
            self.person.name,
            self.room.name,
            self.map_exit.name,
        ]


class MoveAction(Action):
    def __init__(self, animations_box: AnimationsBox, renderer: GameRenderer, board_state: BoardState,
                 moved_room: Room, place1: Place, place2: Place,
                 direction: Direction, person: Person,
                 dwelled_room: Room, terminal: Terminal):
        super().__init__(animations_box, renderer, board_state)

        self.moved_room = moved_room
        self.place1 = place1
        self.place2 = place2
        self.direction = direction
        self.person = person
        self.dwelled_room = dwelled_room
        self.terminal = terminal

    def check_preconditions(self) -> bool:
        is_person_in_dwelled_room = self.dwelled_room.is_person_in(self.person)
        contains_terminal = self.dwelled_room.does_contain(self.terminal)
        is_place2_free = self.board_state.game_board.is_place_free(self.place2)
        is_moved_room_at_place1 = self.place1.is_room_at(self.moved_room)
        are_places_adjacent = self.board_state.game_board.are_adjacent(self.place1, self.place2, self.direction)

        return is_person_in_dwelled_room \
            and contains_terminal \
            and is_place2_free \
            and is_moved_room_at_place1 \
            and are_places_adjacent

    def execute(self) -> bool:
        if not self.check_preconditions():
            return False

        self.place1.unset_room()
        self.place2.set_room(self.moved_room)

        self.set_move_animation(self.moved_room, 0.5)

        return True

    def get_name(self) -> str:
        return "move"

    def get_params_names(self) -> list[str]:
        return [
            self.moved_room.name,
            self.place1.name,
            self.place2.name,
            self.direction.name,
            self.person.name,
            self.dwelled_room.name,
            self.terminal.name,
        ]
