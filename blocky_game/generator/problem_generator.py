from abc import ABC, abstractmethod

import numpy as np
import random

from blocky_game.model.board_domain import BoardDomain
from blocky_game.model.game_objects import (
    GameObject, GameBoard, MapExit, Person, Room, Place, Direction, Entrance, Colour, Door,
)
from blocky_game.model.game_objects_container import GameObjectsContainer
from blocky_game.model.board_state import BoardState


class ProblemGenerator(ABC):
    def __init__(self, domain: BoardDomain, rows: int, columns: int, keys_count: int):
        self.domain = domain
        self.rows = rows
        self.columns = columns
        self.keys_count = keys_count

    @abstractmethod
    def generate(self) -> BoardState:
        pass


class SimpleProblemGenerator(ProblemGenerator):
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
        for colour in game_objects_container.get_colours().values():
            door_name = f"door_{entrance.name}_{colour}"
            entrance.add_door(door_name, colour)

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

        exit_x = random.randint(1, self.rows)
        possible_ys = [y for y in range(1, self.columns + 1) if not board[exit_x, y].is_free()]
        exit_y = random.choice(possible_ys)

        exit_position = np.array([exit_x, exit_y])

        room = board[exit_x, exit_y].room
        room.add_thing(map_exit)

        return map_exit, exit_position

    def __create_player(self, game_objects_container: GameObjectsContainer,
                        board: GameBoard, exit_position: np.ndarray) -> tuple[Person, np.ndarray]:
        person = Person("player")
        game_objects_container.add_object(person)

        exit_x, exit_y = exit_position

        player_x = random.randint(1, self.rows)
        possible_ys = [
            y for y in range(1, self.columns + 1)
            if not board[player_x, y].is_free() and (player_x, y) != (exit_x, exit_y)
        ]
        player_y = random.choice(possible_ys)

        player_position = np.array([player_x, player_y])

        room = board[player_x, player_y].room
        room.add_person(person)

        return person, player_position

    @staticmethod
    def __get_goal_representation(person: Person) -> str:
        return f"(escaped({person.name}))"

    def __select_colours(self, game_objects_container: GameObjectsContainer, board: GameBoard):
        possible_colours = list(Colour.colour_name_to_rgb.keys())
        colours_names = random.sample(possible_colours, self.keys_count)

        colours = [Colour(colour_name) for colour_name in colours_names]
        for colour in colours:
            game_objects_container.add_object(colour)

        board.colours = colours

    def __init__(self, domain: BoardDomain, rows: int, columns: int, keys_count: int):
        super().__init__(domain, rows, columns, keys_count)

    def generate(self) -> BoardState:
        game_objects_container = GameObjectsContainer()
        board = GameBoard(self.rows + 1, self.columns + 1)

        self.__select_colours(game_objects_container, board)

        self.__fill_with_places(game_objects_container, board)
        self.__fill_with_rooms(game_objects_container, board)

        _, exit_position = self.__create_map_exit(game_objects_container, board)
        person, _ = self.__create_player(game_objects_container, board, exit_position)

        goal_representation = self.__get_goal_representation(person)

        return BoardState(
            self.domain,
            board,
            game_objects_container.get_all_objects(),
            game_objects_container,
            goal_representation
        )

