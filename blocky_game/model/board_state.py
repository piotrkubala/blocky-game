import pddl

from .board_domain import BoardDomain
from .game_objects import (
    Direction,
    GameBoard,
    GameObject,
    Colour,
    Place,
    Room,
    Person,
    Thing,
    TakeableThing,
    Key,
    Terminal,
    MapExit,
    Entrance, GameScreen, )


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


def direction_name_to_direction(direction_name: str) -> Direction:
    match direction_name:
        case "right":
            return Direction.RIGHT
        case "down":
            return Direction.DOWN
        case "left":
            return Direction.LEFT
        case "up":
            return Direction.UP
        case _:
            raise ValueError(f"Invalid direction name {direction_name}")


def pddl_type_to_object(pddl_type: str, *params) -> GameObject | None:
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
        case "place":
            return Place(*params)
        case "direction":
            return None
        case _:
            raise ValueError(f"Invalid PDDL type {pddl_type}")


def assert_game_object_type(game_object: GameObject, expected_type: str):
    def get_assert_message(expected_type_name: str, got_game_object: GameObject):
        return f"Expected {expected_type_name}, got {type(got_game_object)}"

    match expected_type:
        case "place":
            assert isinstance(game_object, Place), get_assert_message(expected_type, game_object)
        case "room":
            assert isinstance(game_object, Room), get_assert_message(expected_type, game_object)
        case "person":
            assert isinstance(game_object, Person), get_assert_message(expected_type, game_object)
        case "thing":
            assert isinstance(game_object, Thing), get_assert_message(expected_type, game_object)
        case "takeable":
            assert isinstance(game_object, TakeableThing), get_assert_message(expected_type, game_object)
        case "key":
            assert isinstance(game_object, Key), get_assert_message(expected_type, game_object)
        case "terminal":
            assert isinstance(game_object, Terminal), get_assert_message(expected_type, game_object)
        case "exit":
            assert isinstance(game_object, MapExit), get_assert_message(expected_type, game_object)
        case "entrance":
            assert isinstance(game_object, Entrance), get_assert_message(expected_type, game_object)
        case "direction":
            assert isinstance(game_object, Direction), get_assert_message(expected_type, game_object)
        case "colour":
            assert isinstance(game_object, Colour), get_assert_message(expected_type, game_object)
        case _:
            raise ValueError(f"Invalid expected type {expected_type}")


class BoardState:
    def __generate_representation(self) -> tuple[GameBoard, dict[str, GameObject]]:
        max_row, max_column = 0, 0

        for obj in self.problem.objects:
            if obj.type_tag == "place":
                row, column = place_name_to_coordinates(obj.name)
                max_row = max(max_row, row)
                max_column = max(max_column, column)

        game_board = GameBoard(max_row + 1, max_column + 1)
        game_objects = {}

        for obj in self.problem.objects:
            game_object = pddl_type_to_object(obj.type_tag, obj.name)

            if game_object is None:
                continue

            game_objects[obj.name] = game_object

            if obj.type_tag == "place":
                row, column = place_name_to_coordinates(obj.name)

                assert_game_object_type(game_object, "place")
                game_board[(row, column)] = game_object
            if obj.type_tag == "colour":
                assert_game_object_type(game_object, "colour")
                game_board.colours.append(game_object)

        for relation in self.problem.init:
            match relation.name:
                case "at":
                    room, place = relation.terms
                    room_name, place_name = room.name, place.name

                    assert_game_object_type(game_objects[room_name], "room")
                    assert_game_object_type(game_objects[place_name], "place")
                    game_objects[place_name].set_room(game_objects[room_name])
                case "in":
                    person, room = relation.terms
                    person_name, room_name = person.name, room.name

                    assert_game_object_type(game_objects[person_name], "person")
                    assert_game_object_type(game_objects[room_name], "room")
                    game_objects[room_name].add_person(game_objects[person_name])
                case "contains":
                    room, thing = relation.terms
                    room_name, thing_name = room.name, thing.name

                    assert_game_object_type(game_objects[room_name], "room")
                    assert_game_object_type(game_objects[thing_name], "thing")
                    game_objects[room_name].add_thing(game_objects[thing_name])
                case "passage":
                    room, entrance, direction = relation.terms
                    room_name, entrance_name, direction_name = room.name, entrance.name, direction.name

                    assert_game_object_type(game_objects[room_name], "room")
                    assert_game_object_type(game_objects[entrance_name], "entrance")

                    direction = direction_name_to_direction(direction_name)
                    room_object = game_objects[room_name]
                    entrance_object = game_objects[entrance_name]

                    room_object.add_entrance(
                        entrance_object, direction
                    )
                    entrance_object.set_colours(game_board.colours)
                case "has_door":
                    entrance, colour = relation.terms
                    entrance_name, colour_name = entrance.name, colour.name

                    assert_game_object_type(game_objects[entrance_name], "entrance")
                    assert_game_object_type(game_objects[colour_name], "colour")

                    game_objects[entrance_name].add_door(
                        colour_name, game_objects[colour_name]
                    )
                case "owned":
                    thing, person = relation.terms
                    thing_name, person_name = thing.name, person.name

                    assert_game_object_type(game_objects[thing_name], "takeable")
                    assert_game_object_type(game_objects[person_name], "person")

                    game_objects[person_name].add_equipment(game_objects[thing_name])
                case "is":
                    key, colour = relation.terms
                    key_name, colour_name = key.name, colour.name

                    assert_game_object_type(game_objects[key_name], "key")
                    assert_game_object_type(game_objects[colour_name], "colour")

                    game_objects[key_name].set_colour(game_objects[colour_name])
                case "escaped":
                    person = relation.terms[0]
                    person_name = person.name

                    assert_game_object_type(game_objects[person_name], "person")
                    game_objects[person_name].escape()
                case "reversed" | "free" | "adjacent":
                    pass
                case _:
                    raise ValueError(f"Invalid predicate {relation.name}")

        game_objects[game_board.name] = game_board

        return game_board, game_objects

    def __serialize_objects(self) -> list[str]:
        objects_representation = []

        for obj in sorted(self.problem.objects, key=lambda x: (x.type_tag, x.name)):
            objects_representation.append(f"{obj.name} - {obj.type_tag}")

        return objects_representation

    def __serialize_relations(self) -> list[str]:
        relations_representation = []

        for obj in self.game_objects.values():
            object_relations_representation = obj.serialize_relations()
            relations_representation.extend(object_relations_representation)

        preprocessed_relations = [f"({relation})" for relation in relations_representation]
        preprocessed_relations.sort()
        return preprocessed_relations

    def __serialize_goals(self) -> list[str]:
        goals_representation = [str(self.problem.goal)]

        return goals_representation

    def __init__(self, board_domain: BoardDomain, problem_definition_path: str):
        self.problem = pddl.parse_problem(problem_definition_path)
        self.domain = board_domain

        self.problem.check(self.domain.domain)

        self.game_board, self.game_objects = self.__generate_representation()
        self.game_screen = GameScreen(self.game_board, self.game_objects)

    def center_board(self, screen_width: int, screen_height: int, size_ratio: float):
        self.game_board.center_board(screen_width, screen_height, size_ratio)

    def serialize_state(self, problem_name: str) -> str:
        separator = "\n            "

        objects_representation = separator.join(self.__serialize_objects())
        relations_representation = separator.join(self.__serialize_relations())
        goals_representation = separator.join(self.__serialize_goals())

        return f'''
(define (problem {problem_name})
    (:domain {self.domain.domain.name})
        (:objects
            {objects_representation})
        (:init
            (reversed right left)
            (reversed up down)
            (reversed down up)
            (reversed left right)
            
            {relations_representation})
        (:goal
            {goals_representation})
)
        '''
