from abc import ABC, abstractmethod

from blocky_game.graphics.animations import AnimationsBox
from blocky_game.graphics.game_renderer import GameRenderer
from blocky_game.model.board_state import BoardState
from blocky_game.model.game_objects import (
    Person, Direction, Key, Colour, Entrance, Place, Room, GameBoard, GameObject,
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


