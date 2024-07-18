from abc import ABC, abstractmethod

import pygame
import numpy as np
import cv2


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

    def flip_horizontal(self):
        flip_matrix = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        self.transform = flip_matrix @ self.transform

    def flip_vertical(self):
        flip_matrix = np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
        self.transform = flip_matrix @ self.transform

    def clear_translate(self):
        self.transform[0, -1] = 0
        self.transform[1, -1] = 0

    @staticmethod
    def get_transformed_corners(surface: pygame.surface, accumulated_transform: np.ndarray) -> np.ndarray:
        width, height = surface.get_size()

        corners = np.array([
            [-width / 2, -height / 2, 1],
            [width / 2, height / 2, 1],
            [-width / 2, height / 2, 1],
            [width / 2, -height / 2, 1]
        ]).T

        return (accumulated_transform @ corners)[:2].T

    @staticmethod
    def get_transformed_size(surface: pygame.surface, accumulated_transform: np.ndarray) -> np.ndarray:
        corners = GraphicsComponent.get_transformed_corners(surface, accumulated_transform)
        return np.max(corners, axis=0) - np.min(corners, axis=0)

    @staticmethod
    def get_transformed_position(accumulated_transform: np.ndarray) -> np.ndarray:
        return accumulated_transform[:2, -1]

    @staticmethod
    def is_point_inside_of_surface(point: np.ndarray, accumulated_reverse_transform: np.ndarray, surface: pygame.surface) -> bool:
        width, height = surface.get_size()
        point_extended = np.array([point[0], point[1], 1])
        point_transformed = accumulated_reverse_transform @ point_extended

        is_x_inside = -width / 2 <= point_transformed[0] <= width / 2
        is_y_inside = -height / 2 <= point_transformed[1] <= height / 2

        return is_x_inside and is_y_inside

    @staticmethod
    def get_transformed_image(surface: pygame.surface,
                              accumulated_transform: np.ndarray) -> tuple[pygame.Surface, np.ndarray]:
        source_image = pygame.surfarray.pixels3d(surface)

        accumulated_transform_modified = accumulated_transform.copy()
        accumulated_transform_modified[:2, -1] = 0

        point_bottom_right = np.array([source_image.shape[1] - 1, source_image.shape[0] - 1, 1])
        point_bottom_left = np.array([0, source_image.shape[0] - 1, 1])
        point_top_right = np.array([source_image.shape[1] - 1, 0, 1])

        point_bottom_right_transformed = (accumulated_transform_modified @ point_bottom_right)[:2]
        point_bottom_left_transformed = (accumulated_transform_modified @ point_bottom_left)[:2]
        point_top_right_transformed = (accumulated_transform_modified @ point_top_right)[:2]

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

        min_pixel_position = np.array([min_x_pixel_position, min_y_pixel_position])
        max_pixel_position = np.array([max_x_pixel_position, max_y_pixel_position])

        width = int(round(max_x_pixel_position)) + 1
        height = int(round(max_y_pixel_position)) + 1

        image_size = np.array([height, width])

        transformed_image = cv2.warpAffine(
            source_image,
            accumulated_transform_modified[:2],
            (width, height),
            borderValue=(255, 255, 255)
        )

        return pygame.surfarray.make_surface(transformed_image), image_size

    def is_point_inside(self, point: np.ndarray, accumulated_transform: np.ndarray) -> bool:
        if self.hidden:
            return False

        reverse_transform = np.linalg.inv(accumulated_transform)
        return any(
            GraphicsComponent.is_point_inside_of_surface(point, reverse_transform, surface)
            for surface in self.surfaces
        )

    def draw(self, screen: pygame.Surface, accumulated_transform: np.ndarray = np.identity(3)):
        if self.hidden:
            return

        for surface in self.surfaces:
            transformed_position = GraphicsComponent.get_transformed_position(accumulated_transform)
            transformed_image, image_size = GraphicsComponent.get_transformed_image(
                surface, accumulated_transform
            )

            new_x, new_y = transformed_position - image_size / 2
            casted_x, casted_y = int(new_x), int(new_y)

            screen.blit(transformed_image, (casted_x, casted_y))
