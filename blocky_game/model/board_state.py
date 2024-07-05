import pddl

from .board_domain import BoardDomain
from .game_objects import (
    Direction,
    GameBoard,
    GameObject,
    Colour,
    Room,
    Person,
    Thing,
    TakeableThing,
    Key,
    Terminal,
    MapExit,
    Entrance,
)


def place_name_to_coordinates(place_name: str) -> tuple[int, int]:
    prefix = "place"
    prefix_length = len(prefix)
    numbers = place_name[prefix_length:]
    numbers_len = len(numbers)

    if numbers_len % 2 != 0:
        raise ValueError(f"Odd number of digits in place name {place_name}")

    numbers_half_len = numbers_len // 2

    row = int(numbers[:numbers_half_len])
    column = int(numbers[numbers_half_len:])

    return row, column


class BoardState:
    def __pddl_type_to_object(self, pddl_type: str, *params) -> GameObject | None:
        match pddl_type:
            case "colour":
                return Colour(*params)
            case "room":
                return Room(*params)
            case "person":
                return Person(*params)
            case "thing":
                return Thing(*params)
            case "takeable":
                return TakeableThing(*params)
            case "key":
                return Key(*params)
            case "terminal":
                return Terminal(*params)
            case "exit":
                return MapExit(*params)
            case "entrance":
                return Entrance(*params)
            case _:
                return None

    def __generate_representation(self) -> GameBoard:
        max_row, max_column = 0, 0

        for obj in self.problem.objects:
            if obj.type_name == "place":
                row, column = place_name_to_coordinates(obj.name)
                max_row = max(max_row, row)
                max_column = max(max_column, column)

        game_board = GameBoard(max_row + 1, max_column + 1)
        game_objects = {}

        for obj in self.problem.objects:
            game_object = self.__pddl_type_to_object(obj.type_name, obj.name)

            if game_object is None:
                continue

            game_objects[obj.name] = game_object

        for relation in self.problem.init:
            match relation.predicate:
                case "at":
                    room_name, place_name = relation.args
                    row, column = place_name_to_coordinates(place_name)
                    game_board[(row, column)] = game_objects[room_name]
                case "in":
                    person_name, room_name = relation.args
                    game_objects[room_name].add_person(game_objects[person_name])
                case "contains":
                    room_name, thing_name = relation.args
                    game_objects[room_name].add_thing(game_objects[thing_name])
                # TODO: Add more cases here for other predicates

        raise NotImplementedError("Not implemented")

    def __init__(self, board_domain: BoardDomain, problem_definition_path: str):
        self.problem = pddl.parse_problem(problem_definition_path)
        self.domain = board_domain

        self.problem.check(self.domain.domain)

        self.game_board = self.__generate_representation()
