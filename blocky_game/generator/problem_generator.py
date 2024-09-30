from abc import ABC, abstractmethod
from typing import Callable

import numpy as np
import random

from blocky_game.model.board_domain import BoardDomain
from blocky_game.model.game_objects import (
    GameObject, GameBoard, MapExit, Person, Room, Place, Direction, Entrance, Colour, Door, Terminal, Key,
)
from blocky_game.model.game_objects_container import GameObjectsContainer
from blocky_game.model.board_state import BoardState


class ProblemGenerator(ABC):
    def __init__(self, domain: BoardDomain, rows: int, columns: int, keys_count: int):
        self.domain = domain
        self.rows = rows
        self.columns = columns
        self.keys_count = keys_count

    @staticmethod
    def __restore_path(previous_positions: dict[tuple[int, int], tuple[int, int] | None],
                       end_position: np.ndarray) -> list[np.ndarray]:
        path = []
        current_position = tuple(end_position)
        while current_position:
            path.append(np.array(current_position))
            current_position = previous_positions[current_position]

        path.reverse()
        return path

    @staticmethod
    def __check_door_colour_exists(game_board: GameBoard,
                                   first_position: np.ndarray, second_position: np.ndarray,
                                   direction: Direction, colours: set[Colour]) -> bool:
        first_position_x, first_position_y = first_position
        second_position_x, second_position_y = second_position

        first_place = game_board[first_position_x, first_position_y]
        second_place = game_board[second_position_x, second_position_y]

        if first_place is None or second_place is None:
            return False

        first_room = first_place.room
        second_room = second_place.room

        if first_room is None or second_room is None:
            return False

        opposite_direction = direction.reverse()

        if direction not in first_room.entrances or opposite_direction not in second_room.entrances:
            return False

        first_entrance = first_room.entrances[direction]
        second_entrance = second_room.entrances[opposite_direction]

        if first_entrance is None or second_entrance is None:
            return False

        first_colours = set(first_entrance.colours)
        second_colours = set(second_entrance.colours)

        common_colours = first_colours.intersection(second_colours).intersection(colours)

        return len(common_colours) > 0

    @staticmethod
    def _get_random_path_using_keys(game_board: GameBoard, keys: set[Key],
                                    start_position: np.ndarray, end_position: np.ndarray) -> list[np.ndarray]:
        start_position_x, start_position_y = start_position

        colours = set(key.colour for key in keys)

        previous_positions: dict[tuple[int, int], tuple[int, int] | None] = {(start_position_x, start_position_y): None}
        visited = {tuple(start_position)}

        stack = [start_position]
        while stack:
            current_position = stack.pop()
            if np.array_equal(current_position, end_position):
                return ProblemGenerator.__restore_path(previous_positions, end_position)

            directions = [
                Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT
            ]
            random.shuffle(directions)

            for direction in directions:
                direction_vector = np.array(direction.value)
                new_position = current_position + direction_vector
                new_position_x, new_position_y = new_position
                new_position_tuple = (new_position_x, new_position_y)

                if new_position_tuple in visited or not game_board.is_position_valid(*new_position) or \
                        not ProblemGenerator.__check_door_colour_exists(
                            game_board, current_position, new_position,
                            direction, colours):
                    continue

                visited.add(new_position_tuple)
                stack.append(new_position)
                previous_positions[new_position_tuple] = current_position

        return []

    @abstractmethod
    def generate(self) -> BoardState:
        pass


class SimpleProblemGenerator(ProblemGenerator):
    def __get_random_coordinates(self, is_correct: Callable[[int, int], bool]) -> tuple[int, int]:
        while True:
            x = random.randint(1, self.rows)
            y = random.randint(1, self.columns)

            if is_correct(x, y):
                return x, y

    def __fill_with_places(self, game_objects_container: GameObjectsContainer, board: GameBoard):
        max_coordinate = max(self.rows, self.columns)
        digits_per_coordinate = int(np.floor(np.log10(max_coordinate))) + 1

        for x in range(1, self.rows + 1):
            for y in range(1, self.columns + 1):
                place_name = f"place{x:0{digits_per_coordinate}d}{y:0{digits_per_coordinate}d}"
                place = Place(place_name)

                board[x, y] = place
                game_objects_container.add_object(place)

    def __create_doors(self, game_objects_container: GameObjectsContainer, entrance: Entrance):
        for colour_name, colour in game_objects_container.get_colours().items():
            entrance.add_door(colour_name, colour)

    def __create_entrance(self, game_objects_container: GameObjectsContainer,
                          game_board: GameBoard, room: Room, direction: Direction):
        entrances_count = len(game_objects_container.get_entrances())
        entrance_name = f"entrance_{entrances_count + 1}"

        entrance = Entrance(entrance_name, direction)
        game_objects_container.add_object(entrance)

        entrance.colours = game_board.colours

        room.add_entrance(entrance, direction)

        self.__create_doors(game_objects_container, entrance)

    def __create_entrances(self, game_objects_container: GameObjectsContainer, game_board: GameBoard, room: Room):
        directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]

        for direction in directions:
            self.__create_entrance(game_objects_container, game_board, room, direction)

    def __fill_with_rooms(self, game_objects_container: GameObjectsContainer, board: GameBoard):
        added_rooms_count = 0

        empty_coordinates_x = random.randint(1, self.rows)
        empty_coordinates_y = random.randint(1, self.columns)

        for x in range(1, self.rows + 1):
            for y in range(1, self.columns + 1):
                if x == empty_coordinates_x and y == empty_coordinates_y:
                    continue

                room_name = f"room_{added_rooms_count}"
                room = Room(room_name)

                place_to_add = board[x, y]
                place_to_add.set_room(room)

                game_objects_container.add_room(room)
                added_rooms_count += 1

                self.__create_entrances(game_objects_container, board, room)

    def __create_map_exit(self, game_objects_container: GameObjectsContainer, board: GameBoard) -> \
            tuple[MapExit, np.ndarray]:
        map_exit = MapExit("main_exit")
        game_objects_container.add_object(map_exit)

        exit_x, exit_y = self.__get_random_coordinates(
            lambda x, y: not board[x, y].is_free()
        )

        exit_position = np.array([exit_x, exit_y])

        room = board[exit_x, exit_y].room
        room.add_thing(map_exit)

        return map_exit, exit_position

    def __create_player(self, game_objects_container: GameObjectsContainer,
                        board: GameBoard, exit_position: np.ndarray) -> tuple[Person, np.ndarray]:
        person = Person("player")
        game_objects_container.add_object(person)

        exit_x, exit_y = exit_position

        player_x, player_y = self.__get_random_coordinates(
            lambda x, y: not board[x, y].is_free() and (x, y) != (exit_x, exit_y)
        )

        player_position = np.array([player_x, player_y])

        room = board[player_x, player_y].room
        room.add_person(person)

        return person, player_position

    def __create_terminal_with_path(self, game_objects_container: GameObjectsContainer,
                                    board: GameBoard, person: Person, person_position: np.ndarray,
                                    exit_position: np.ndarray) -> tuple[Terminal, np.ndarray]:
        terminal = Terminal("terminal")
        game_objects_container.add_object(terminal)

        person_x, person_y = person_position
        exit_x, exit_y = exit_position

        terminal_x, terminal_y = self.__get_random_coordinates(
            lambda x, y: not board[x, y].is_free() and (x, y) != (exit_x, exit_y) and (x, y) != (person_x, person_y)
        )

        terminal_room = board[terminal_x, terminal_y].room
        person_room = board[person_x, person_y].room

        initial_colour = self.__get_random_not_used_colour(board)

        terminal_room.add_thing(terminal)
        terminal_position = np.array([terminal_x, terminal_y])

        initial_key = Key(f"key_{initial_colour.name}")
        initial_key.set_colour(initial_colour)
        game_objects_container.add_object(initial_key)

        person_room.add_thing(initial_key)

        return terminal, terminal_position

    @staticmethod
    def __get_goal_representation(person: Person) -> str:
        return f"(escaped({person.name}))"

    def __get_random_not_used_colour(self, board: GameBoard) -> Colour:
        possible_colours = [colour for colour in board.colours if colour not in self.used_colours]

        colour = random.choice(possible_colours)
        self.used_colours.add(colour)

        return colour

    def __select_colours(self, game_objects_container: GameObjectsContainer, board: GameBoard):
        possible_colours = list(Colour.colour_name_to_rgb.keys())
        colours_names = random.sample(possible_colours, self.keys_count)

        colours = [Colour(colour_name) for colour_name in colours_names]
        for colour in colours:
            game_objects_container.add_object(colour)

        board.colours = colours

    def __init__(self, domain: BoardDomain, rows: int, columns: int, keys_count: int):
        super().__init__(domain, rows, columns, keys_count)

        self.used_colours = set()

    def generate(self) -> BoardState:
        game_objects_container = GameObjectsContainer()
        board = GameBoard(self.rows + 1, self.columns + 1)

        self.__select_colours(game_objects_container, board)

        self.__fill_with_places(game_objects_container, board)
        self.__fill_with_rooms(game_objects_container, board)

        _, exit_position = self.__create_map_exit(game_objects_container, board)
        person, person_position = self.__create_player(game_objects_container, board, exit_position)

        terminal, _ = \
            self.__create_terminal_with_path(game_objects_container, board, person, person_position, exit_position)

        goal_representation = self.__get_goal_representation(person)

        return BoardState(
            self.domain,
            board,
            game_objects_container.get_all_objects(),
            game_objects_container,
            goal_representation
        )

