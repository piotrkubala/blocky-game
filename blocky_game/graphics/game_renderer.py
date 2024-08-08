import pygame
import numpy as np
from collections import deque

from blocky_game.graphics.animations import AnimationsBox
from blocky_game.model.board_state import BoardState, GameObject


class GameRenderer:
    @staticmethod
    def __get_animated_transformation(game_object: GameObject,
                                      animations_box: AnimationsBox,
                                      transformation: np.ndarray) -> np.ndarray:
        animation = animations_box[game_object]

        if animation is None:
            return transformation

        return animation.apply(transformation)

    def __render_game_object(self, game_object: GameObject, transformation: np.ndarray, animations_box: AnimationsBox):
        queue = deque([(game_object, transformation)])

        while queue:
            current_game_object, current_transformation = queue.popleft()
            animated_transformation = GameRenderer.__get_animated_transformation(current_game_object, animations_box,
                                                                                 current_transformation)

            current_game_object.graphics_component.draw(self.screen, animated_transformation)

            self.current_transforms[current_game_object.name] = animated_transformation
            self.rendered_objects[current_game_object.name] = current_game_object

            for child in current_game_object.get_children():
                child_transformation = animated_transformation @ child.graphics_component.transform
                queue.append((child, child_transformation))

    def __get_objects_colliding_with_point(self, point: np.ndarray, game_object: GameObject,
                                           animation_box: AnimationsBox,
                                           transformation: np.ndarray = np.identity(3), depth: int = 0
                                           ) -> list[tuple[int, GameObject]]:
        queue = deque([(game_object, transformation, depth)])
        colliding_objects = []

        while queue:
            current_game_object, current_transformation, current_depth = queue.popleft()
            animated_transformation = GameRenderer.__get_animated_transformation(current_game_object, animation_box,
                                                                                 current_transformation)

            if current_game_object.graphics_component.is_point_inside(point, animated_transformation):
                colliding_objects.append((current_depth, current_game_object))

            for child in current_game_object.get_children():
                child_transformation = animated_transformation @ child.graphics_component.transform
                queue.append((child, child_transformation, current_depth + 1))

        return colliding_objects

    def __init__(self, board_state: BoardState, screen: pygame.Surface):
        self.board_state = board_state
        self.screen = screen
        self.current_transforms: dict[str, np.ndarray] = {}
        self.rendered_objects: dict[str, GameObject] = {}

    def render(self, animations_box: AnimationsBox):
        self.__render_game_object(self.board_state.game_screen, np.identity(3), animations_box)

    def get_objects_colliding_with_point(self, point: np.ndarray, animations_box: AnimationsBox
                                         ) -> list[tuple[int, GameObject]]:
        return self.__get_objects_colliding_with_point(point, self.board_state.game_screen, animations_box)

    def get_object_colliding_with_point(self, point: np.ndarray, animations_box: AnimationsBox) -> GameObject | None:
        objects_colliding_with_point = self.get_objects_colliding_with_point(point, animations_box)

        if not objects_colliding_with_point:
            return None

        best_object = max(objects_colliding_with_point, key=lambda x: x[0])[1]
        return best_object

    def get_object_transform(self, game_object: GameObject) -> np.ndarray:
        return self.current_transforms.get(game_object.name, np.identity(3))

    def get_object_by_name(self, name: str) -> GameObject | None:
        return self.rendered_objects.get(name, None)
