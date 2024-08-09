from abc import ABC, abstractmethod

import numpy as np
import pygame

from blocky_game.graphics.graphics_component import GraphicsComponent, load_texture_with_max_size

from enum import Enum
from random import randint


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    def reverse(self):
        match self:
            case Direction.UP:
                return Direction.DOWN
            case Direction.DOWN:
                return Direction.UP
            case Direction.LEFT:
                return Direction.RIGHT
            case Direction.RIGHT:
                return Direction.LEFT

    @staticmethod
    def from_name(name: str) -> 'Direction':
        return {
            "UP": Direction.UP,
            "RIGHT": Direction.RIGHT,
            "DOWN": Direction.DOWN,
            "LEFT": Direction.LEFT
        }[name]


class GameObject(ABC):
    def __init__(self, name: str):
        self.name = name
        self.graphics_component: GraphicsComponent = GraphicsComponent()

    @abstractmethod
    def get_children(self) -> list['GameObject']:
        pass

    def serialize_relations(self) -> list[str]:
        return []

    def is_transitive_child(self, game_object: 'GameObject') -> bool:
        if any(child.name == game_object.name for child in self.get_children()):
            return True

        for child in self.get_children():
            if child.is_transitive_child(game_object):
                return True

        return False


class RectangularContainer(GameObject):
    def __init__(self, name: str, width: int, height: int):
        super().__init__(name)

        self.width = width
        self.height = height

        self.children: list[GameObject] = []

    def update_positions(self):
        if len(self.children) == 0:
            return

        child_space = self.height // len(self.children)

        for i, child in enumerate(self.children):
            child.graphics_component.clear_translate()
            child.graphics_component.translate(0, i * child_space - self.height // 2 + child_space // 2)

    def add_child(self, child: GameObject):
        self.children.append(child)
        self.update_positions()

    def remove_child(self, child: GameObject):
        self.children.remove(child)
        self.update_positions()

    def clear_children(self):
        self.children = []

    def get_children(self) -> list[GameObject]:
        return self.children

    def is_inside_by_name(self, name: str) -> bool:
        return any(child.name == name for child in self.children)


class Colour(GameObject):
    def __init__(self, name: str, width: int = 10):
        super().__init__(name)

        colour_name_to_rgb = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "yellow": (255, 255, 0),
            "black": (0, 0, 0),
            "white": (200, 200, 200)
        }

        self.colour_rgb = colour_name_to_rgb.get(name, tuple(randint(0, 255) for _ in range(3)))

        pygame_rect_surface = pygame.Surface((width, width))
        pygame_rect_surface.fill(self.colour_rgb)

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
    def prepare_visuals(self, max_size: int, colour_rgb: tuple[int, int, int] = (0, 0, 0)):
        self.graphics_component.clear_surfaces()

        sprite_surface = load_texture_with_max_size("../images/key.png", max_size).copy()

        sprite_image = pygame.surfarray.pixels3d(sprite_surface)

        threshold = 200
        part_to_replace = np.all(sprite_image < threshold, axis=-1)
        sprite_image[part_to_replace] = colour_rgb

        sprite_transformed_surface = pygame.surfarray.make_surface(sprite_image)

        self.graphics_component.add_surface(sprite_transformed_surface)

    def __init__(self, name: str, max_size: int = 20):
        super().__init__(name)

        self.colour: Colour | None = None
        self.max_size = max_size

        self.prepare_visuals(max_size)

    def set_colour(self, colour: Colour):
        self.colour = colour

        colour.graphics_component.hide()
        self.prepare_visuals(self.max_size, colour.colour_rgb)

    def get_children(self) -> list[GameObject]:
        return [self.colour]

    def serialize_relations(self) -> list[str]:
        return [f"is {self.name} {self.colour.name}"]

    def is_of_colour(self, colour: Colour) -> bool:
        return self.colour.name == colour.name


class Terminal(Thing):
    def prepare_visuals(self, max_size: int):
        self.graphics_component.clear_surfaces()

        sprite_surface = load_texture_with_max_size("../images/terminal.png", max_size)

        self.graphics_component.add_surface(sprite_surface)

    def __init__(self, name: str, max_size: int = 30):
        super().__init__(name)

        self.prepare_visuals(max_size)

    def get_children(self) -> list[GameObject]:
        return []


class MapExit(Thing):
    def prepare_visuals(self, max_size: int):
        self.graphics_component.clear_surfaces()

        sprite_surface = load_texture_with_max_size("../images/exit.png", max_size)

        self.graphics_component.add_surface(sprite_surface)

    def __init__(self, name: str, max_size: int = 40):
        super().__init__(name)

        self.prepare_visuals(max_size)

    def get_children(self) -> list[GameObject]:
        return []


class Person(GameObject):
    def prepare_visuals(self, max_size: int):
        self.graphics_component.clear_surfaces()

        sprite_surface = load_texture_with_max_size("../images/person.png", max_size)

        self.graphics_component.add_surface(sprite_surface)

    def __init__(self, name: str, max_size: int = 40):
        super().__init__(name)
        self.equipment: dict[str, TakeableThing] = {}
        self.equipment_container: RectangularContainer = \
            RectangularContainer(f"{name}_equipment", 10, max_size)
        self.escaped: bool = False

        self.prepare_visuals(max_size)

    def escape(self):
        self.escaped = True
        self.graphics_component.hide()

        for equipment in self.equipment.values():
            equipment.graphics_component.hide()

    def add_equipment(self, equipment: TakeableThing):
        self.equipment[equipment.name] = equipment
        self.equipment_container.add_child(equipment)
        equipment.graphics_component.clickable = False

    def get_children(self) -> list[GameObject]:
        return [self.equipment_container]

    def serialize_relations(self) -> list[str]:
        return [
            f"owned {thing.name} {self.name}" for thing in self.equipment.values()
        ] + [
            f"escaped {self.name}"
            for _ in [0] if self.escaped
        ]

    def is_owned(self, thing: TakeableThing) -> bool:
        return thing.name in self.equipment

    def did_escape(self) -> bool:
        return self.escaped


class Door(GameObject):
    def prepare_visuals(self, width: int, height: int):
        self.graphics_component.clear_surfaces()

        outer_rect = pygame.Surface((width, height))
        outer_rect.fill((0, 0, 0))

        inner_rect = pygame.Surface((width - 2, height - 2))
        inner_rect.fill(self.colour.colour_rgb)

        outer_rect.blit(inner_rect, (1, 1))

        self.graphics_component.add_surface(outer_rect)

    def __init__(self, name: str, colour: Colour, width: int = 10, height: int = 10):
        super().__init__(name)

        self.width = width
        self.height = height

        self.colour: Colour = colour

        self.prepare_visuals(width, height)

    def get_children(self) -> list[GameObject]:
        return [self.colour]


class Entrance(GameObject):
    def prepare_doors(self):
        self.doors_container.clear_children()

        for i, colour in enumerate(self.colours):
            door = Door(f"{self.name}_{i}_door", colour)
            self.doors_container.add_child(door)

            if colour.name not in self.colours_dict:
                door.graphics_component.hide()

    def prepare_visuals(self, width: int, height: int):
        self.width = width
        self.height = height

        self.graphics_component.clear_surfaces()
        self.graphics_component.clear_transform()

        outer_rect = pygame.Surface((width, height))
        outer_rect.fill((200, 0, 0))
        inner_rect = pygame.Surface((width - 2, height - 2))
        inner_rect.fill((255, 255, 255))

        outer_rect.blit(inner_rect, (1, 1))

        self.graphics_component.add_surface(outer_rect)

        self.prepare_doors()

    def __init__(self, name: str, direction: Direction | None = None, width: int = 20, height: int = 80):
        super().__init__(name)

        self.direction: Direction | None = direction
        self.colours_dict: dict[str, Colour] = {}
        self.colours: list[Colour] = []  # should be a reference to the colours in the game board
        self.width = width
        self.height = height

        container_name = f"{name}_doors"
        self.doors_container: RectangularContainer = RectangularContainer(container_name, width, height)

        self.prepare_visuals(width, height)

    def set_direction(self, direction: Direction):
        self.direction = direction

    def add_door(self, door_name: str, colour: Colour):
        self.colours_dict[door_name] = colour
        self.prepare_doors()

    def get_children(self) -> list[GameObject]:
        return list(self.colours_dict.values()) + [self.doors_container]

    def set_colours(self, colours: list[Colour]):
        self.colours = colours
        self.prepare_doors()

    def serialize_relations(self) -> list[str]:
        return [
            f"has_door {self.name} {door.name}" for door in self.colours_dict.values()
        ]

    def has_door(self, colour: Colour) -> bool:
        return colour.name in self.colours_dict


class Room(GameObject):
    def prepare_visuals(self, width: int, wall_width: int = 6):
        self.graphics_component.clear_surfaces()

        outer_rect = pygame.Surface((width, width))
        outer_rect.fill((100, 100, 100))
        inner_rect = pygame.Surface((width - 2 * wall_width, width - 2 * wall_width))
        inner_rect.fill((255, 255, 255))

        outer_rect.blit(inner_rect, (wall_width, wall_width))

        self.graphics_component.add_surface(outer_rect)
        self.wall_width = wall_width

        width_part = width // 4
        self.people_container.graphics_component.clear_transform()
        self.people_container.graphics_component.translate(-width_part, 0)

        self.things_container.graphics_component.clear_transform()
        self.things_container.graphics_component.translate(width_part, 0)

        self.width = width
        self.wall_width = wall_width

    def __init__(self, name: str, width: int = 100):
        super().__init__(name)

        self.entrances: dict[Direction, Entrance] = {}

        width_part = width // 3
        height_part = width * 9 // 10
        self.people_container = RectangularContainer(f"{name}_people", width_part, height_part)
        self.things_container = RectangularContainer(f"{name}_things", width_part, height_part)

        self.width = width
        self.wall_width = 6

        self.prepare_visuals(width)

    def add_person(self, person: Person):
        self.people_container.add_child(person)

    def remove_person(self, person: Person):
        self.people_container.remove_child(person)

    def add_thing(self, thing: Thing):
        self.things_container.add_child(thing)

    def remove_thing(self, thing: Thing):
        self.things_container.remove_child(thing)

    def set_entrance_position(self, entrance: Entrance, entrance_width: int):
        direction = entrance.direction

        entrance_height = int(self.width * 0.8)
        entrance.prepare_visuals(entrance_width, entrance_height)
        entrance.graphics_component.translate(self.width // 2 - entrance_width // 2 + self.wall_width // 2, 0)

        match direction:
            case Direction.UP:
                entrance.graphics_component.rotate(-90)
            case Direction.DOWN:
                entrance.graphics_component.flip_vertical()
                entrance.graphics_component.rotate(90)
            case Direction.LEFT:
                entrance.graphics_component.flip_vertical()
                entrance.graphics_component.rotate(180)
            case Direction.RIGHT:
                pass
            case _:
                raise ValueError(f"Invalid direction {direction}")

    def set_all_entrances_positions(self, entrance_width: int = 10):
        for entrance in self.entrances.values():
            self.set_entrance_position(entrance, entrance_width)

    def add_entrance(self, entrance: Entrance, direction: Direction, entrance_width: int = 10):
        self.entrances[direction] = entrance
        entrance.set_direction(direction)

        self.set_entrance_position(entrance, entrance_width)

    def get_children(self) -> list[GameObject]:
        return [self.people_container, self.things_container] + list(self.entrances.values())

    def serialize_relations(self) -> list[str]:
        direction_to_str = {
            Direction.UP: "up",
            Direction.DOWN: "down",
            Direction.LEFT: "left",
            Direction.RIGHT: "right"
        }

        return [
            f"passage {self.name} {entrance.name} {direction_to_str[direction]}"
            for direction, entrance in self.entrances.items()
        ] + [
            f"contains {self.name} {thing.name}"
            for thing in self.things_container.children
        ] + [
            f"in {person.name} {self.name}"
            for person in self.people_container.children
        ]

    def is_person_in(self, person: Person) -> bool:
        return self.people_container.is_inside_by_name(person.name)

    def does_contain(self, thing: Thing) -> bool:
        return self.things_container.is_inside_by_name(thing.name)

    def has_passage(self, entrance: Entrance, direction: Direction) -> bool:
        return self.entrances.get(direction).name == entrance.name


class Place(GameObject):
    def prepare_visuals(self, width: int):
        self.graphics_component.clear_surfaces()

        outer_rect = pygame.Surface((width, width))
        outer_rect.fill((0, 0, 0))
        inner_rect = pygame.Surface((width - 2, width - 2))
        inner_rect.fill((255, 255, 255))

        outer_rect.blit(inner_rect, (1, 1))

        self.graphics_component.add_surface(outer_rect)
        self.width = width

    def __init__(self, name: str, width: int = 100, room_size_ratio: float = 0.9):
        super().__init__(name)

        self.width = width
        self.room: Room | None = None
        self.prepare_visuals(width)
        self.room_size_ratio = room_size_ratio

    def set_room(self, room: Room):
        self.room = room
        room_width = int(self.width * self.room_size_ratio)
        room.prepare_visuals(room_width)
        room.set_all_entrances_positions()

    def unset_room(self):
        self.room = None

    def get_children(self) -> list[GameObject]:
        return [self.room] if self.room is not None else []

    def serialize_relations(self) -> list[str]:
        return [
            f"free {self.name}" if self.room is None else f"at {self.room.name} {self.name}"
        ]

    def is_room_at(self, room: Room) -> bool:
        return self.room is not None and self.room.name == room.name

    def is_free(self) -> bool:
        return self.room is None


class GameBoard(GameObject):
    def center_board(self, screen_width: int, screen_height: int, size_ratio: float = 0.8):
        real_columns_count = self.max_row_index - self.min_row_index + 1
        real_rows_count = self.max_column_index - self.min_column_index + 1

        board_width = real_columns_count * self.place_width
        board_height = real_rows_count * self.place_width

        board_size = max(board_width, board_height)
        max_board_size = min(screen_width, screen_height) * size_ratio

        scale_factor = max_board_size / board_size

        self.graphics_component.scale(scale_factor, scale_factor)
        new_board_width = board_width * scale_factor
        new_board_height = board_height * scale_factor

        empty_columns_size = self.min_row_index * self.place_width * scale_factor
        empty_rows_size = self.min_column_index * self.place_width * scale_factor

        top_left_x_offset = (screen_width - new_board_width - empty_columns_size) / 2
        top_left_y_offset = (screen_height - new_board_height - empty_rows_size) / 2

        self.graphics_component.translate(top_left_x_offset, top_left_y_offset)

    def __init__(self, rows: int, columns: int, place_width: int = 150):
        super().__init__("")

        self.place_width = place_width
        self.rows: int = rows
        self.columns: int = columns
        self.board: list[list[None | Place]] = [[None for _ in range(columns)] for _ in range(rows)]
        self.colours: list[Colour] = []
        self.place_name_to_coordinates: dict[str, tuple[int, int]] = {}

        self.min_row_index = rows
        self.min_column_index = columns
        self.max_row_index = 0
        self.max_column_index = 0

    def __getitem__(self, key: tuple[int, int]) -> Place | None:
        row, column = key
        return self.board[row][column]

    def __setitem__(self, key: tuple[int, int], value: Place | None):
        row, column = key
        self.board[row][column] = value

        if value is None:
            return

        self.place_name_to_coordinates[value.name] = (row, column)
        delta = self.place_width - 1
        value.prepare_visuals(self.place_width)
        value.graphics_component.clear_transform()
        value.graphics_component.translate(row * delta, column * delta)

        self.min_row_index = min(self.min_row_index, row)
        self.min_column_index = min(self.min_column_index, column)

        self.max_row_index = max(self.max_row_index, row)
        self.max_column_index = max(self.max_column_index, column)

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

    def serialize_relations(self) -> list[str]:
        relations_representation = []

        for i in range(self.rows):
            for j in range(self.columns):
                this_place = self.board[i][j]

                if this_place is None:
                    continue
                this_place_name = this_place.name

                if i > 0 and self.board[i - 1][j] is not None:
                    up_place_name = self.board[i - 1][j].name
                    relations_representation.append(f"adjacent {this_place_name} {up_place_name} up")
                if i < self.rows - 1 and self.board[i + 1][j] is not None:
                    down_place_name = self.board[i + 1][j].name
                    relations_representation.append(f"adjacent {this_place_name} {down_place_name} down")
                if j > 0 and self.board[i][j - 1] is not None:
                    left_place_name = self.board[i][j - 1].name
                    relations_representation.append(f"adjacent {this_place_name} {left_place_name} left")
                if j < self.columns - 1 and self.board[i][j + 1] is not None:
                    right_place_name = self.board[i][j + 1].name
                    relations_representation.append(f"adjacent {this_place_name} {right_place_name} right")

        return relations_representation

    def are_adjacent(self, place1: Place, place2: Place) -> bool:
        row1, column1 = self.place_name_to_coordinates[place1.name]
        row2, column2 = self.place_name_to_coordinates[place2.name]

        if abs(row1 - row2) + abs(column1 - column2) != 1:
            return False

        return row1 == row2 or column1 == column2

    def get_adjacency_direction(self, place1: Place, place2: Place) -> Direction | None:
        row1, column1 = self.place_name_to_coordinates[place1.name]
        row2, column2 = self.place_name_to_coordinates[place2.name]

        if row1 == row2:
            if column1 + 1 == column2:
                return Direction.DOWN
            if column1 - 1 == column2:
                return Direction.UP
        if column1 == column2:
            if row1 + 1 == row2:
                return Direction.RIGHT
            if row1 - 1 == row2:
                return Direction.LEFT

        return None


class GameInterface(GameObject):
    def __init__(self, name: str):
        super().__init__(name)

        self.children = []

    def get_children(self) -> list[GameObject]:
        return self.children

    def add_child(self, child: GameObject):
        self.children.append(child)


class GameScreen(GameObject):
    def __init__(self, game_board: GameBoard):
        super().__init__("screen")

        self.game_board = game_board
        self.interface = GameInterface("interface")

    def get_children(self) -> list[GameObject]:
        return [self.game_board, self.interface]
