from abc import ABC, abstractmethod
import pygame

from blocky_game.graphics.graphics_component import GraphicsComponent, load_texture_with_max_size

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

        sprite_surface = load_texture_with_max_size("../images/key.png", max_size)

        sprite_image = pygame.surfarray.pixels3d(sprite_surface)
        sprite_image[sprite_image[:, :, 0] < 200] = colour_rgb

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
    def prepare_visuals(self, max_size: int):
        self.graphics_component.clear_surfaces()

        sprite_surface = load_texture_with_max_size("../images/person.png", max_size)

        self.graphics_component.add_surface(sprite_surface)

    def __init__(self, name: str, max_size: int = 50):
        super().__init__(name)
        self.equipment: dict[str, TakeableThing] = {}
        self.escaped: bool = False

        self.prepare_visuals(max_size)

    def escape(self):
        self.escaped = True

    def add_equipment(self, equipment: TakeableThing):
        self.equipment[equipment.name] = equipment

    def get_children(self) -> list[GameObject]:
        return list(self.equipment.values())


class Entrance(GameObject):
    def prepare_visuals(self, width: int, height: int):
        self.graphics_component.clear_surfaces()

        outer_rect = pygame.Surface((width, height))
        outer_rect.fill((200, 0, 0))
        inner_rect = pygame.Surface((width - 2, height - 2))
        inner_rect.fill((255, 255, 255))

        outer_rect.blit(inner_rect, (1, 1))

        self.graphics_component.add_surface(outer_rect)

    def __init__(self, name: str, width: int = 80, height: int = 20):
        super().__init__(name)

        self.doors: dict[str, Colour] = {}
        self.colours: list[Colour] = []  # should be a reference to the colours in the game board

        self.prepare_visuals(width, height)

    def add_door(self, door_name: str, colour: Colour):
        self.doors[door_name] = colour

    def get_children(self) -> list[GameObject]:
        return list(self.doors.values())

    def set_colours(self, colours: list[Colour]):
        self.colours = colours


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

    def __init__(self, name: str, width: int = 100):
        super().__init__(name)

        self.people: dict[str, Person] = {}
        self.things_contained: dict[str, Thing] = {}
        self.entrances: dict[Direction, Entrance] = {}

        self.width = width
        self.wall_width = 6

        self.prepare_visuals(width)

    def add_person(self, person: Person):
        self.people[person.name] = person

    def add_thing(self, thing: Thing):
        self.things_contained[thing.name] = thing

    def add_entrance(self, entrance: Entrance, direction: Direction, entrance_width: int = 10):
        self.entrances[direction] = entrance

        entrance_height = int(self.width * 0.8)
        entrance.prepare_visuals(entrance_width, entrance_height)
        entrance.graphics_component.translate(self.width // 2 - entrance_width // 2 + self.wall_width // 2, 0)

        match direction:
            case Direction.UP:
                entrance.graphics_component.rotate(-90)
            case Direction.DOWN:
                entrance.graphics_component.rotate(90)
            case Direction.LEFT:
                entrance.graphics_component.rotate(180)
            case Direction.RIGHT:
                pass

    def get_children(self) -> list[GameObject]:
        return list(self.people.values()) + list(self.things_contained.values()) + list(self.entrances.values())


class Place(GameObject):
    def prepare_visuals(self, width: int):
        self.graphics_component.clear_surfaces()

        outer_rect = pygame.Surface((width, width))
        outer_rect.fill((0, 0, 0))
        inner_rect = pygame.Surface((width - 2, width - 2))
        inner_rect.fill((255, 255, 255))

        outer_rect.blit(inner_rect, (1, 1))

        self.graphics_component.add_surface(outer_rect)

    def __init__(self, name: str, width: int = 100):
        super().__init__(name)

        self.room: Room | None = None
        self.prepare_visuals(width)

    def set_room(self, room: Room):
        self.room = room

    def unset_room(self):
        self.room = None

    def get_children(self) -> list[GameObject]:
        return [self.room] if self.room is not None else []


class GameBoard(GameObject):
    def __init__(self, rows: int, columns: int, place_width: int = 150):
        super().__init__("")

        self.place_width = place_width
        self.rows: int = rows
        self.columns: int = columns
        self.board: list[list[None | Place]] = [[None for _ in range(columns)] for _ in range(rows)]
        self.colours: list[Colour] = []

    def __getitem__(self, key: tuple[int, int]) -> Place | None:
        row, column = key
        return self.board[row][column]

    def __setitem__(self, key: tuple[int, int], value: Place | None):
        row, column = key
        self.board[row][column] = value
        delta = self.place_width - 1
        value.prepare_visuals(self.place_width)
        value.graphics_component.clear_transform()
        value.graphics_component.translate(row * delta, column * delta)

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
