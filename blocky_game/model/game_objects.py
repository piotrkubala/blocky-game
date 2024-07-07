from abc import ABC, abstractmethod
import pygame

from blocky_game.graphics.graphics_component import GraphicsComponent

from enum import Enum
from random import randint


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)


class GameObject(ABC):
    def __init__(self, name: str):
        self.name = name
        self.graphics_component: GraphicsComponent = GraphicsComponent()

    @abstractmethod
    def get_children(self) -> list['GameObject']:
        pass


class Colour(GameObject):
    def __init__(self, name: str, width: int = 10):
        super().__init__(name)

        colour_name_to_rgb = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "yellow": (255, 255, 0),
            "black": (0, 0, 0),
            "white": (255, 255, 255)
        }

        colour_rgb = colour_name_to_rgb.get(name, tuple(randint(0, 255) for _ in range(3)))

        pygame_rect_surface = pygame.Surface((width, width))
        pygame_rect_surface.fill(colour_rgb)

        self.graphics_component.add_surface(pygame_rect_surface)

    def get_children(self) -> list[GameObject]:
        return []


class Thing(GameObject):
    def __init__(self, name: str):
        super().__init__(name)

    def get_children(self) -> list[GameObject]:
        return []


class TakeableThing(Thing):
    def __init__(self, name: str):
        super().__init__(name)

    def get_children(self) -> list[GameObject]:
        return []


class Key(TakeableThing):
    def __init__(self, name: str):
        super().__init__(name)

        self.colour: Colour | None = None

    def set_colour(self, colour: Colour):
        self.colour = colour

    def get_children(self) -> list[GameObject]:
        return [self.colour]


class Terminal(Thing):
    def __init__(self, name: str):
        super().__init__(name)

    def get_children(self) -> list[GameObject]:
        return []


class MapExit(Thing):
    def __init__(self, name: str):
        super().__init__(name)

    def get_children(self) -> list[GameObject]:
        return []


class Person(GameObject):
    def __init__(self, name: str):
        super().__init__(name)
        self.equipment: dict[str, TakeableThing] = {}
        self.escaped: bool = False

    def escape(self):
        self.escaped = True

    def add_equipment(self, equipment: TakeableThing):
        self.equipment[equipment.name] = equipment

    def get_children(self) -> list[GameObject]:
        return list(self.equipment.values())


class Entrance(GameObject):
    def __init__(self, name: str):
        super().__init__(name)

        self.doors: dict[str, Colour] = {}

    def add_door(self, door_name: str, colour: Colour):
        self.doors[door_name] = colour

    def get_children(self) -> list[GameObject]:
        return list(self.doors.values())


class Room(GameObject):
    def __init__(self, name: str):
        super().__init__(name)

        self.people: dict[str, Person] = {}
        self.things_contained: dict[str, Thing] = {}
        self.entrances: dict[Direction, Entrance] = {}

    def add_person(self, person: Person):
        self.people[person.name] = person

    def add_thing(self, thing: Thing):
        self.things_contained[thing.name] = thing

    def add_entrance(self, entrance: Entrance, direction: Direction):
        self.entrances[direction] = entrance

    def get_children(self) -> list[GameObject]:
        return list(self.people.values()) + list(self.things_contained.values()) + list(self.entrances.values())


class Place(GameObject):
    def __init__(self, name: str):
        super().__init__(name)

        self.room: Room | None = None

    def set_room(self, room: Room):
        self.room = room

    def unset_room(self):
        self.room = None

    def get_children(self) -> list[GameObject]:
        return [self.room] if self.room is not None else []


class GameBoard(GameObject):
    def __init__(self, rows: int, columns: int):
        super().__init__("")

        self.rows: int = rows
        self.columns: int = columns
        self.board: list[list[None | Place]] = [[None for _ in range(columns)] for _ in range(rows)]

    def __getitem__(self, key: tuple[int, int]) -> Place | None:
        row, column = key
        return self.board[row][column]

    def __setitem__(self, key: tuple[int, int], value: Place | None):
        row, column = key
        self.board[row][column] = value

    def get_neighbour(self, row: int, column: int, direction: Direction) -> Place | None:
        row_offset, column_offset = direction.value
        new_row = row + row_offset
        new_column = column + column_offset

        is_valid_row = 0 <= new_row < self.rows
        is_valid_column = 0 <= new_column < self.columns

        if not is_valid_row or not is_valid_column:
            return None

        return self.board[new_row][new_column]

    def get_children(self) -> list[GameObject]:
        return [place for row in self.board for place in row if place is not None]
