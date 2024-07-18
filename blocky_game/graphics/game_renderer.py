import pygame
import numpy as np

from blocky_game.model.board_state import BoardState, GameObject


class GameRenderer:
    def __render_game_object(self, game_object: GameObject, transformation: np.ndarray):
        transformation = transformation @ game_object.graphics_component.transform
        game_object.graphics_component.draw(self.screen, transformation)

        for child in game_object.get_children():
            self.__render_game_object(child, transformation)

    def __get_objects_colliding_with_point(self, point: np.ndarray, game_object: GameObject,
                                           transformation: np.ndarray = np.identity(3), depth: int = 0
                                           ) -> list[tuple[int, GameObject]]:
        transformation = transformation @ game_object.graphics_component.transform

        colliding_objects = []
        if game_object.graphics_component.is_point_inside(point, transformation):
            colliding_objects.append((depth, game_object))

        for child in game_object.get_children():
            colliding_objects.extend(self.__get_objects_colliding_with_point(point, child, transformation, depth + 1))

        return colliding_objects

    def __init__(self, board_state: BoardState, screen: pygame.Surface):
        self.board_state = board_state
        self.screen = screen

    def render(self):
        self.__render_game_object(self.board_state.game_board, np.identity(3))

    def get_objects_colliding_with_point(self, point: np.ndarray) -> list[tuple[int, GameObject]]:
        return self.__get_objects_colliding_with_point(point, self.board_state.game_board)

    def get_object_colliding_with_point(self, point: np.ndarray) -> GameObject | None:
        objects_colliding_with_point = self.get_objects_colliding_with_point(point)

        if not objects_colliding_with_point:
            return None

        best_object = max(objects_colliding_with_point, key=lambda x: x[0])[1]
        return best_object
