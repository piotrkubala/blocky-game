import pddl
from enum import Enum


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)


class GameBoard:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.board = [[None for _ in range(columns)] for _ in range(rows)]

    def __getitem__(self, key: tuple[int, int]):
        row, column = key
        return self.board[row][column]

    def __setitem__(self, key: tuple[int, int], value):
        row, column = key
        self.board[row][column] = value

    def get_neighbour(self, row: int, column: int, direction: Direction):
        row_offset, column_offset = direction.value
        new_row = row + row_offset
        new_column = column + column_offset

        assert 0 <= new_row < self.rows, f"Row {new_row} is out of bounds"
        assert 0 <= new_column < self.columns, f"Column {new_column} is out of bounds"

        return self.board[new_row][new_column]


class GameObject:
    def __init__(self, name: str):
        self.name = name


class Colour(GameObject):
    def __init__(self, name: str):
        super().__init__(name)


class Person(GameObject):
    def __init__(self, name: str):
        super().__init__(name)
        self.equipment: dict[str, TakeableThing] = {}


class Thing(GameObject):
    def __init__(self, name: str):
        super().__init__(name)


class Room(GameObject):
    def __init__(self, name: str):
        super().__init__(name)

        self.people: dict[str, Person] = {}
        self.things_contained: dict[str, Thing] = {}

    def add_person(self, person: Person):
        self.people[person.name] = person

    def add_thing(self, thing: Thing):
        self.things_contained[thing.name] = thing


class TakeableThing(Thing):
    def __init__(self, name: str):
        super().__init__(name)


class Key(TakeableThing):
    def __init__(self, name: str):
        super().__init__(name)

        self.colour: Colour | None = None

    def set_colour(self, colour: Colour):
        self.colour = colour


class Terminal(Thing):
    def __init__(self, name: str):
        super().__init__(name)


class MapExit(Thing):
    def __init__(self, name: str):
        super().__init__(name)


class Entrance(GameObject):
    def __init__(self, name: str):
        super().__init__(name)
