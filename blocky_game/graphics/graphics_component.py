from abc import ABC, abstractmethod

import pygame
import numpy as np
import cv2
from matplotlib import pyplot as plt


def load_texture_with_max_size(texture_path: str, max_size: int) -> pygame.Surface:
    sprite_surface = pygame.image.load(texture_path)
    texture_width, texture_height = sprite_surface.get_size()
    max_dimension = max(texture_width, texture_height)
    scale_factor = max_size / max_dimension
    new_width, new_height = int(texture_width * scale_factor), int(texture_height * scale_factor)
    return pygame.transform.smoothscale(sprite_surface, (new_width, new_height))


class GraphicsComponent(ABC):
    def __init__(self):
        self.transform = np.identity(3)
        self.surfaces: list[pygame.surface] = []
        self.hidden = False
        self.start_rotate = False

    def add_surface(self, surface: pygame.surface):
        self.surfaces.append(surface)

    def clear_transform(self):
        self.transform = np.identity(3)

    def clear_surfaces(self):
        self.surfaces = []

    def hide(self):
        self.hidden = True

    def show(self):
        self.hidden = False

    def translate(self, x: float, y: float):
        translation_matrix = np.array([
            [1, 0, x],
            [0, 1, y],
            [0, 0, 1]
        ])
        self.transform = translation_matrix @ self.transform

    def rotate(self, angle_degrees: float):
        angle = np.radians(angle_degrees)

        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1]
        ])
        self.transform = rotation_matrix @ self.transform

    def scale(self, x: float, y: float):
        scale_matrix = np.array([
            [x, 0, 0],
            [0, y, 0],
            [0, 0, 1]
        ])
        self.transform = scale_matrix @ self.transform

    @staticmethod
    def get_transformed_corners(surface: pygame.surface, accumulated_transform: np.ndarray) -> np.ndarray:
        width, height = surface.get_size()

        corners = np.array([
            [-width / 2, -height / 2, 1],
            [width / 2, height / 2, 1],
        ]).T

        return (accumulated_transform @ corners)[:2].T

    @staticmethod
    def get_transformed_image(surface: pygame.surface,
                              accumulated_transform: np.ndarray,
                              source_corner_points: np.ndarray) -> tuple[pygame.Surface, np.ndarray, np.ndarray]:
        source_image = pygame.surfarray.pixels3d(surface)

        max_x, max_y = np.max(source_corner_points[:2], axis=0)
        min_x, min_y = np.min(source_corner_points[:2], axis=0)

        point_min = np.array([min_x, min_y])
        point_max = np.array([max_x, max_y])

        accumulated_transform_modified = accumulated_transform.copy()
        accumulated_transform_modified[:2, -1] = 0

        point_bottom_right = np.array(source_image.shape[:2][::-1] + (1,))
        point_bottom_left = np.array([0, source_image.shape[0], 1])
        point_top_right = np.array([source_image.shape[1], 0, 1])

        point_bottom_right_transformed = (accumulated_transform_modified @ point_bottom_right)[0:2]
        point_bottom_left_transformed = (accumulated_transform_modified @ point_bottom_left)[0:2]
        point_top_right_transformed = (accumulated_transform_modified @ point_top_right)[0:2]

        x_translate = max(0, -point_bottom_right_transformed[0], -point_top_right_transformed[0],
                          -point_bottom_left_transformed[0])
        y_translate = max(0, -point_bottom_right_transformed[1], -point_top_right_transformed[1],
                          -point_bottom_left_transformed[1])

        accumulated_transform_modified[0, -1] = x_translate
        accumulated_transform_modified[1, -1] = y_translate

        max_x_pixel_position = max(0.0, point_bottom_right_transformed[0], point_top_right_transformed[0],
                                   point_bottom_left_transformed[0]) + x_translate
        max_y_pixel_position = max(0.0, point_bottom_right_transformed[1], point_top_right_transformed[1],
                                   point_bottom_left_transformed[1]) + y_translate

        min_x_pixel_position = min(0.0, point_bottom_right_transformed[0], point_top_right_transformed[0],
                                      point_bottom_left_transformed[0]) + x_translate
        min_y_pixel_position = min(0.0, point_bottom_right_transformed[1], point_top_right_transformed[1],
                                        point_bottom_left_transformed[1]) + y_translate

        internal_delta = np.array([0.0, 0.0])

        point_min += internal_delta
        point_max += internal_delta

        width = int(max_x_pixel_position)
        height = int(max_y_pixel_position)

        transformed_image = cv2.warpAffine(
            source_image,
            accumulated_transform_modified[:2],
            (width, height),
            # borderMode=cv2.BORDER_TRANSPARENT
        )
        # plt.title("source")
        # plt.imshow(source_image)
        # plt.show()
        # plt.title(str(accumulated_transform_modified))
        # plt.imshow(transformed_image)
        # plt.show()

        return pygame.surfarray.make_surface(transformed_image), point_min, point_max

    def draw(self, screen: pygame.Surface, accumulated_transform: np.ndarray = np.identity(3)):
        if self.hidden:
            return

        if self.start_rotate:
            self.rotate(0.05)

        for surface in self.surfaces:
            source_corner_points = GraphicsComponent.get_transformed_corners(surface, accumulated_transform)
            transformed_image, point_min, _ = GraphicsComponent.get_transformed_image(
                surface, accumulated_transform, source_corner_points
            )
            new_x, new_y = point_min
            casted_x, casted_y = int(new_x), int(new_y)

            screen.blit(transformed_image, (casted_x, casted_y))
