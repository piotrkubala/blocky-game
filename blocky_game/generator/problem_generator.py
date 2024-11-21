from abc import ABC, abstractmethod
from typing import Callable

import copy
import numpy as np
import random
from queue import Queue

from blocky_game.model.board_domain import BoardDomain
from blocky_game.model.game_objects import (
    GameObject, GameBoard, MapExit, Person, Room, Place, Direction, Entrance, Colour, Door, Terminal, Key,
)
from blocky_game.model.game_objects_container import GameObjectsContainer
from blocky_game.model.board_state import BoardState


class ProblemGenerator(ABC):
    def __init__(self, domain: BoardDomain, rows: int, columns: int, keys_count: int, mixing_steps: int):
        self.domain = domain
        self.rows = rows
        self.columns = columns
        self.keys_count = keys_count
        self.mixing_steps = mixing_steps

    @staticmethod
    def __restore_path(previous_positions: dict[tuple[int, int], tuple[int, int] | None],
                       end_position: np.ndarray) -> list[np.ndarray]:
        path = []
        current_position = end_position
        while current_position is not None:
            path.append(current_position)
            position_x, position_y = current_position
            current_position = previous_positions[(position_x, position_y)]

        path.reverse()
        return path

    @staticmethod
    def _does_door_with_colour_exist(game_board: GameBoard, position: np.ndarray,
                                     direction: Direction, colours: set[Colour]):
        x, y = position
        place = game_board[x, y]

        if place is None or place.room is None:
            return False

        room = place.room

        if direction not in room.entrances:
            return False

        entrance = room.entrances[direction]

        if entrance is None:
            return False

        return any(colour in colours for colour in entrance.colours_dict.values())

    @staticmethod
    def _does_passage_with_colour_exist(game_board: GameBoard,
                                        first_position: np.ndarray, second_position: np.ndarray,
                                        direction: Direction, colours: set[Colour]) -> bool:
        if not ProblemGenerator._does_door_with_colour_exist(game_board, first_position, direction, colours):
            return False

        if not ProblemGenerator._does_door_with_colour_exist(game_board, second_position, direction.reverse(), colours):
            return False

        return True

    def _does_doors_with_colour_exist_any_direction(self, game_board: GameBoard, position: np.ndarray,
                                                    colours: set[Colour]) -> bool:
        directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]

        for direction in directions:
            if self._does_door_with_colour_exist(game_board, position, direction, colours):
                return True

        return False

    @staticmethod
    def _check_room_exists(game_board: GameBoard, position: np.ndarray) -> bool:
        x, y = position
        place = game_board[x, y]
        return place is not None and place.room is not None

    @staticmethod
    def _get_random_path(game_board: GameBoard, start_position: np.ndarray,
                         end_position: np.ndarray, colours: set[Colour] | None,
                         correct_room_predicate: Callable[[int, int], bool]) -> list[np.ndarray]:
        start_position_x, start_position_y = start_position

        previous_positions: dict[tuple[int, int], tuple[int, int] | None] = {(start_position_x, start_position_y): None}
        visited = {tuple(start_position)}

        q = Queue()
        q.put(start_position)
        while q:
            current_position = q.get()
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

                if new_position_tuple in visited or not game_board.does_place_exist(*new_position):
                    continue

                if not correct_room_predicate(new_position_x, new_position_y):
                    continue

                if colours is None:
                    if not ProblemGenerator._check_room_exists(game_board, new_position):
                        continue
                else:
                    if not ProblemGenerator._check_room_exists(game_board, new_position) and \
                            not ProblemGenerator._does_passage_with_colour_exist(
                                game_board, current_position, new_position,
                                direction, colours):
                        continue

                visited.add(new_position_tuple)
                q.put(new_position)
                previous_positions[new_position_tuple] = current_position

        return []

    @staticmethod
    def _get_all_reachable_coords_recursive(game_board: GameBoard, start_position: np.ndarray,
                                            correct_room_predicate: Callable[[int, int], bool],
                                            visited: set[tuple[int, int]]) -> set[tuple[int, int]]:
        x, y = start_position

        if (x, y) in visited or not game_board.does_place_exist(x, y) or not correct_room_predicate(x, y):
            return set()

        visited.add((x, y))

        result = {(x, y)}
        for direction in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]:
            new_position = start_position + np.array(direction.value)
            new_x, new_y = new_position
            if not game_board.does_place_exist(new_x, new_y):
                continue

            result |= ProblemGenerator._get_all_reachable_coords_recursive(
                game_board, new_position, correct_room_predicate, visited
            )

        return result


    @staticmethod
    def _get_all_reachable_coords(game_board: GameBoard, start_position: np.ndarray,
                                  correct_room_predicate: Callable[[int, int], bool]) -> set[tuple[int, int]]:
        visited = set()
        return ProblemGenerator._get_all_reachable_coords_recursive(
            game_board, start_position, correct_room_predicate, visited
        )


    @abstractmethod
    def generate(self) -> tuple[BoardState, list[BoardState]]:
        pass


class SimpleProblemGenerator(ProblemGenerator):
    def __get_random_coordinates(self, is_correct: Callable[[int, int], bool]) -> tuple[int, int] | None:
        tries_limit = 4

        for _ in range(tries_limit):
            x = random.randint(1, self.rows)
            y = random.randint(1, self.columns)

            if is_correct(x, y):
                return x, y

        possible_coordinates = [(x, y) for x in range(1, self.rows + 1) for y in range(1, self.columns + 1)
                                if is_correct(x, y)]

        if len(possible_coordinates) == 0:
            return None

        return random.choice(possible_coordinates)

    def __fill_with_places(self, game_objects_container: GameObjectsContainer, board: GameBoard):
        max_coordinate = max(self.rows, self.columns)
        digits_per_coordinate = int(np.floor(np.log10(max_coordinate))) + 1

        for x in range(1, self.rows + 1):
            for y in range(1, self.columns + 1):
                place_name = f"place{x:0{digits_per_coordinate}d}{y:0{digits_per_coordinate}d}"
                place = Place(place_name)

                board[x, y] = place
                game_objects_container.add_object(place)

    @staticmethod
    def __create_doors(game_objects_container: GameObjectsContainer, entrance: Entrance):
        for colour_name, colour in game_objects_container.get_colours().items():
            entrance.add_door(colour_name, colour)

    @staticmethod
    def __create_entrance(game_objects_container: GameObjectsContainer,
                          game_board: GameBoard, room: Room, direction: Direction):
        entrances_count = len(game_objects_container.get_entrances())
        entrance_name = f"entrance_{entrances_count + 1}"

        entrance = Entrance(entrance_name, direction)
        game_objects_container.add_object(entrance)

        entrance.colours = game_board.colours
        room.add_entrance(entrance, direction)

    @staticmethod
    def __create_entrances(game_objects_container: GameObjectsContainer, game_board: GameBoard, room: Room):
        directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]

        for direction in directions:
            SimpleProblemGenerator.__create_entrance(game_objects_container, game_board, room, direction)

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

    def __create_map_exit(self, game_objects_container: GameObjectsContainer, board: GameBoard) -> \
            tuple[MapExit, np.ndarray]:
        map_exit = MapExit("main_exit")
        game_objects_container.add_object(map_exit)

        exit_position_tuple = self.__get_random_coordinates(
            lambda x, y: not board[x, y].is_free()
        )

        if exit_position_tuple is None:
            raise ValueError("No place for exit")
        exit_x, exit_y = exit_position_tuple

        exit_position = np.array([exit_x, exit_y])

        room = board[exit_x, exit_y].room
        room.add_thing(map_exit)

        return map_exit, exit_position

    def __create_player(self, game_objects_container: GameObjectsContainer,
                        board: GameBoard, exit_position: np.ndarray) -> tuple[Person, np.ndarray]:
        person = Person("player")
        game_objects_container.add_object(person)

        exit_x, exit_y = exit_position

        player_position_tuple = self.__get_random_coordinates(
            lambda x, y: not board[x, y].is_free() and (x, y) != (exit_x, exit_y)
        )

        if player_position_tuple is None:
            raise ValueError("No place for player")
        player_x, player_y = player_position_tuple

        player_position = np.array([player_x, player_y])

        room = board[player_x, player_y].room
        room.add_person(person)

        return person, player_position

    def __create_terminal_init_key(self, game_objects_container: GameObjectsContainer,
                                   board: GameBoard, person_position: np.ndarray,
                                   exit_position: np.ndarray) -> tuple[Terminal, np.ndarray]:
        terminal = Terminal("terminal")
        game_objects_container.add_object(terminal)

        person_x, person_y = person_position
        exit_x, exit_y = exit_position

        terminal_position_tuple = self.__get_random_coordinates(
            lambda x, y: not board[x, y].is_free() and (x, y) != (exit_x, exit_y) and (x, y) != (person_x, person_y)
        )

        if terminal_position_tuple is None:
            raise ValueError("No place for terminal")

        terminal_x, terminal_y = terminal_position_tuple

        terminal_room = board[terminal_x, terminal_y].room
        person_room = board[person_x, person_y].room

        initial_colour = self.__get_next_not_used_colour(board)
        self.__update_to_next_colour(board)

        terminal_room.add_thing(terminal)
        terminal_position = np.array([terminal_x, terminal_y])

        initial_key = Key(f"key_{initial_colour.name}")
        initial_key.set_colour(initial_colour)
        game_objects_container.add_object(initial_key)

        person_room.add_thing(initial_key)

        return terminal, terminal_position

    @staticmethod
    def __add_doors(game_objects_container: GameObjectsContainer, board: GameBoard,
                    first_room: Room, second_room: Room, direction: Direction, colour: Colour):
        reverse_direction = direction.reverse()

        if direction not in first_room.entrances:
            SimpleProblemGenerator.__create_entrance(game_objects_container, board, first_room, direction)
        if reverse_direction not in second_room.entrances:
            SimpleProblemGenerator.__create_entrance(game_objects_container, board, second_room, reverse_direction)

        first_entrance = first_room.entrances[direction]
        second_entrance = second_room.entrances[reverse_direction]

        first_entrance.add_door(colour.name, colour)
        second_entrance.add_door(colour.name, colour)

        first_entrance.prepare_doors()
        second_entrance.prepare_doors()

    def __prepare_doors_path(self, game_objects_container: GameObjectsContainer, board: GameBoard,
                             start_position: np.ndarray, end_position: np.ndarray,
                             correct_room_predicate: Callable[[int, int], bool], colours: list[Colour]):
        colours_set = set(colours)
        random_path = self._get_random_path(board, start_position, end_position, colours_set, correct_room_predicate)

        def select_random_colour(index: int) -> Colour:
            if (index >= len(random_path) - 2 and random.randint(0, 1) == 0) or len(colours) == 1:
                return colours[-1]

            colours_count = len(colours)
            triangle_value = colours_count * (colours_count - 1) // 2

            random_number = random.randint(0, triangle_value - 1)

            values_sum = 0
            for j in range(1, colours_count + 1):
                new_sum = values_sum + j
                if new_sum >= random_number:
                    return colours[j - 1]
                values_sum = new_sum

        for i, (previous_position, next_position) in enumerate(zip(random_path[:-1], random_path[1:])):
            previous_x, previous_y = previous_position
            next_x, next_y = next_position

            previous_room = board[previous_x, previous_y].room
            next_room = board[next_x, next_y].room

            position_difference = next_position - previous_position

            difference_x, difference_y = position_difference
            direction = Direction.from_vector(difference_x, difference_y)

            if ProblemGenerator._does_passage_with_colour_exist(
                    board, previous_position,
                    next_position, direction, colours_set):
                continue

            colour = select_random_colour(i)

            SimpleProblemGenerator.__add_doors(game_objects_container, board, previous_room,
                                               next_room, direction, colour)

    @staticmethod
    def __get_goal_representation(person: Person) -> str:
        return f"(escaped {person.name})"

    def __get_next_not_used_colour(self, board: GameBoard) -> Colour:
        return board.colours[self.not_used_colour_index]

    def __update_to_next_colour(self, board: GameBoard):
        self.used_colours.append(board.colours[self.not_used_colour_index])
        self.not_used_colour_index += 1

    def __are_all_colours_used(self, board: GameBoard) -> bool:
        return self.not_used_colour_index >= len(board.colours)

    def __select_colours(self, game_objects_container: GameObjectsContainer, board: GameBoard):
        possible_colours = list(Colour.colour_name_to_rgb.keys())
        colours_names = random.sample(possible_colours, self.keys_count)
        random.shuffle(colours_names)

        colours = [Colour(colour_name) for colour_name in colours_names]
        for colour in colours:
            game_objects_container.add_object(colour)
        self.not_used_colour_index = 0

        board.colours = colours

    def __get_positions_to_rooms(self, board: GameBoard) -> dict[tuple[int, int], Room | None]:
        positions_to_rooms = {}
        for x in range(1, self.rows + 1):
            for y in range(1, self.columns + 1):
                place = board[x, y]
                if place is not None:
                    positions_to_rooms[(x, y)] = place.room

        return positions_to_rooms

    def __mix_rooms(self, board: GameBoard, steps: int, change_probability: float = 0.25):
        empty_position = next(np.array((x, y)) for x in range(1, self.rows + 1) for y in range(1, self.columns + 1)
                              if board[x, y].room is None)
        directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        last_direction = random.choice(directions)

        for _ in range(steps):
            possible_directions = [direction for direction in directions
                                   if board.does_place_exist(*(empty_position + direction.to_vector()))
                                   and direction != last_direction.reverse()]
            new_direction = random.choice(possible_directions) \
                if last_direction not in possible_directions or random.random() < change_probability \
                else last_direction

            new_position = empty_position + new_direction.to_vector()

            empty_position_x, empty_position_y = empty_position
            new_position_x, new_position_y = new_position

            empty_place = board[empty_position_x, empty_position_y]
            new_place = board[new_position_x, new_position_y]

            moved_room = new_place.room

            empty_place.set_room(moved_room)
            new_place.unset_room()

            empty_position = new_position
            last_direction = new_direction

    def __prepare_one_key_path(self, game_objects_container: GameObjectsContainer, board: GameBoard,
                               correct_room_predicate: Callable[[int, int], bool], terminal_position: np.ndarray)\
            -> Key:
        key_colour = self.__get_next_not_used_colour(board)
        key_name = f"key_{key_colour.name}"
        key = Key(key_name)
        key.set_colour(key_colour)
        game_objects_container.add_object(key)

        liberal_condition_predicate = lambda x, y: (not board[x, y].is_free()
                                                    and len(board[x, y].room.things_container.get_children()) == 0)
        door_not_exists_predicate = lambda x, y: not self._does_doors_with_colour_exist_any_direction(
            board, np.array([x, y]), set(self.used_colours)
        )

        terminal_position_x, terminal_position_y = terminal_position
        terminal_position_tuple = (terminal_position_x, terminal_position_y)

        reachable_positions = ProblemGenerator._get_all_reachable_coords(
            board, terminal_position,
            lambda x, y: (liberal_condition_predicate(x, y)
                         and door_not_exists_predicate(x, y))
                         or (x, y) == terminal_position_tuple
        ) - {terminal_position_tuple}

        random_position_tuple = self.__get_random_coordinates(
            lambda x, y: (x, y) in reachable_positions
        )

        if random_position_tuple is None:
            random_position_tuple = self.__get_random_coordinates(
                lambda x, y: liberal_condition_predicate(x, y)
                             and door_not_exists_predicate(x, y)
            )

        if random_position_tuple is None:
            random_position_tuple = self.__get_random_coordinates(liberal_condition_predicate)

        if random_position_tuple is None:
            raise ValueError("No place for key")

        random_target_x, random_target_y = random_position_tuple

        random_target_position = np.array([random_target_x, random_target_y])

        random_target_room = board[random_target_x, random_target_y].room
        random_target_room.add_thing(key)

        self.__prepare_doors_path(
            game_objects_container,
            board, terminal_position,
            random_target_position,
            correct_room_predicate,
            self.used_colours
        )

        self.__update_to_next_colour(board)

        return key

    def __find_things_and_people_positions(self, board: GameBoard) -> dict[str, np.ndarray]:
        things_positions = {}
        for x in range(1, self.rows + 1):
            for y in range(1, self.columns + 1):
                place = board[x, y]
                if place is not None and place.room is not None:
                    room = place.room
                    things = room.things_container.children
                    people = room.people_container.children
                    for thing in things + people:
                        things_positions[thing.name] = np.array([x, y])

        return things_positions

    @staticmethod
    def __move_person_to_position(person_position: np.ndarray, new_position: np.ndarray,
                                  person: Person, board: GameBoard):
        person_position_x, person_position_y = person_position
        new_position_x, new_position_y = new_position

        board[person_position_x, person_position_y].room.remove_person(person)
        board[new_position_x, new_position_y].room.add_person(person)

    @staticmethod
    def __move_keys_to_equipment(board: GameBoard, game_objects_container: GameObjectsContainer,
                                 person: Person, things_positions: dict[str, np.ndarray]):
        keys = game_objects_container.get_keys()

        for key in keys.values():
            key_position = things_positions[key.name]
            key_position_x, key_position_y = key_position

            board[key_position_x, key_position_y].room.remove_thing(key)
            person.add_equipment(key)

    @staticmethod
    def __prepare_subproblem(game_objects_container: GameObjectsContainer, board: GameBoard,
                             terminal_position: np.ndarray, new_key_position: np.ndarray,
                             person_position: np.ndarray, person: Person, things_positions: dict[str, np.ndarray]):
        SimpleProblemGenerator.__move_person_to_position(person_position, terminal_position, person, board)
        SimpleProblemGenerator.__move_keys_to_equipment(board, game_objects_container, person, things_positions)
        new_exit = MapExit("new_exit")

        game_objects_container.add_object(new_exit)
        new_key_position_x, new_key_position_y = new_key_position
        board[new_key_position_x, new_key_position_y].room.add_thing(new_exit)

    @staticmethod
    def __create_subproblem_copy(game_objects_container: GameObjectsContainer, board: GameBoard,
                                 things_positions: dict[str, np.ndarray], terminal_position: np.ndarray,
                                 person_position: np.ndarray, person: Person, new_key: Key)\
            -> tuple[GameObjectsContainer, GameBoard]:
        board_copy, game_objects_container_copy = copy.deepcopy((board, game_objects_container))
        real_person = game_objects_container_copy.get_people()[person.name]

        new_key_position = things_positions[new_key.name]

        SimpleProblemGenerator.__prepare_subproblem(
            game_objects_container_copy, board_copy,
            terminal_position, new_key_position,
            person_position, real_person, things_positions
        )

        return game_objects_container_copy, board_copy

    def __create_last_subproblem_copy(self, game_objects_container: GameObjectsContainer, board: GameBoard,
                                      terminal_position: np.ndarray, person_position: np.ndarray,
                                      person: Person, things_position: dict[str, np.ndarray])\
            -> tuple[GameObjectsContainer, GameBoard]:
        board_copy, game_objects_container_copy = copy.deepcopy((board, game_objects_container))
        real_person = game_objects_container_copy.get_people()[person.name]

        SimpleProblemGenerator.__move_person_to_position(person_position, terminal_position, real_person, board_copy)
        SimpleProblemGenerator.__move_keys_to_equipment(
            board_copy, game_objects_container_copy,
            real_person, things_position
        )

        return game_objects_container_copy, board_copy

    def __prepare_other_keys_with_paths(self, game_objects_container: GameObjectsContainer, board: GameBoard,
                                        terminal: Terminal, person: Person,
                                        map_exit: MapExit, mixing_steps: int)\
            -> list[tuple[GameObjectsContainer, GameBoard]]:
        subproblems_list: list[tuple[GameObjectsContainer, GameBoard]] = []
        new_key = None
        while not self.__are_all_colours_used(board):
            self.__mix_rooms(board, mixing_steps)
            things_positions = self.__find_things_and_people_positions(board)
            terminal_position = things_positions[terminal.name]
            exit_position = things_positions[map_exit.name]
            person_position = things_positions[person.name]

            if new_key is not None:
                new_subproblem = SimpleProblemGenerator.__create_subproblem_copy(
                    game_objects_container, board, things_positions,
                    terminal_position, person_position, person, new_key
                )
                subproblems_list.append(new_subproblem)

            new_key = self.__prepare_one_key_path(
                game_objects_container, board,
                lambda x, y: not board[x, y].is_free()
                             and len(board[x, y].room.people_container.children) == 0
                             and (x, y) != tuple(exit_position),
                terminal_position
            )

        self.__mix_rooms(board, mixing_steps)
        things_positions = self.__find_things_and_people_positions(board)
        terminal_position = things_positions[terminal.name]
        exit_position = things_positions[map_exit.name]
        person_position = things_positions[person.name]

        if new_key is not None:
            new_subproblem = SimpleProblemGenerator.__create_subproblem_copy(
                game_objects_container, board, things_positions,
                terminal_position, person_position, person, new_key
            )
            subproblems_list.append(new_subproblem)

        person_position_x, person_position_y = person_position
        person_position_tuple = (person_position_x, person_position_y)

        self.__prepare_doors_path(
            game_objects_container, board, terminal_position,
            exit_position,
            lambda x, y: not board[x, y].is_free() and (x, y) != person_position_tuple,
            self.used_colours
        )

        things_positions = self.__find_things_and_people_positions(board)
        last_subproblem = self.__create_last_subproblem_copy(
            game_objects_container, board,
            terminal_position, person_position,
            person, things_positions
        )
        subproblems_list.append(last_subproblem)

        return subproblems_list

    @staticmethod
    def __revert_rooms_positions(board: GameBoard, positions_to_rooms: dict[tuple[int, int], Room | None]):
        for (x, y), room in positions_to_rooms.items():
            place = board[x, y]
            if room is None:
                place.unset_room()
            else:
                place.set_room(room)

    def __generate_subproblems_board_states(self, subproblems_list: list[tuple[GameObjectsContainer, GameBoard]],
                                            person: Person)\
            -> list[BoardState]:
        return [
            BoardState(
                self.domain, board, game_objects_container.get_all_objects(),
                game_objects_container, self.__get_goal_representation(person)
            )
            for game_objects_container, board in subproblems_list
        ]

    def __init__(self, domain: BoardDomain, rows: int, columns: int, keys_count: int, mixing_steps: int):
        super().__init__(domain, rows, columns, keys_count, mixing_steps)

        self.used_colours = []
        self.not_used_colour_index = 0

    def generate(self) -> tuple[BoardState, list[BoardState]]:
        game_objects_container = GameObjectsContainer()
        board = GameBoard(self.rows + 1, self.columns + 1)

        self.__select_colours(game_objects_container, board)

        self.__fill_with_places(game_objects_container, board)
        self.__fill_with_rooms(game_objects_container, board)

        rooms_original_positions = self.__get_positions_to_rooms(board)

        map_exit, exit_position = self.__create_map_exit(game_objects_container, board)
        person, person_position = self.__create_player(game_objects_container, board, exit_position)

        terminal, terminal_position = \
            self.__create_terminal_init_key(game_objects_container, board, person_position, exit_position)

        exit_position_x, exit_position_y = exit_position
        exit_position_tuple = (exit_position_x, exit_position_y)

        self.__prepare_doors_path(
            game_objects_container, board, person_position,
            terminal_position,
            lambda x, y: not board[x, y].is_free() and (x, y) != exit_position_tuple,
            self.used_colours
        )

        subproblems_list = self.__prepare_other_keys_with_paths(
            game_objects_container, board, terminal,
            person, map_exit,
            self.mixing_steps
        )

        SimpleProblemGenerator.__revert_rooms_positions(board, rooms_original_positions)
        goal_representation = self.__get_goal_representation(person)

        full_problem_state = BoardState(
            self.domain,
            board,
            game_objects_container.get_all_objects(),
            game_objects_container,
            goal_representation
        )
        subproblems_board_states = self.__generate_subproblems_board_states(subproblems_list, person)

        return full_problem_state, subproblems_board_states
