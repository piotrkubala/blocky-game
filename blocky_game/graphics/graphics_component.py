from abc import ABC, abstractmethod
import pygame
import numpy as np
import cv2


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
        self.transform = self.transform @ translation_matrix

    def rotate(self, angle: float):
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1]
        ])
        self.transform = self.transform @ rotation_matrix

    def scale(self, x: float, y: float):
        scale_matrix = np.array([
            [x, 0, 0],
            [0, y, 0],
            [0, 0, 1]
        ])
        self.transform = self.transform @ scale_matrix

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
                              source_corner_points: np.ndarray) -> pygame.Surface:
        source_image = pygame.surfarray.pixels3d(surface)

        max_x, max_y = np.max(source_corner_points, axis=0)[:2]
        min_x, min_y = np.min(source_corner_points, axis=0)[:2]
        width, height = int(max_x - min_x), int(max_y - min_y)

        accumulated_transform_zeroed = accumulated_transform.copy()[:2]
        accumulated_transform_zeroed[:, -1] = 0
        transformed_image = cv2.warpAffine(
            source_image,
            accumulated_transform_zeroed,
            (width, height)
        )
        return pygame.surfarray.make_surface(transformed_image)

    def draw(self, screen: pygame.Surface, accumulated_transform: np.ndarray = np.identity(3)):
        if self.hidden:
            return

        for surface in self.surfaces:
            source_corner_points = GraphicsComponent.get_transformed_corners(surface, accumulated_transform)
            transformed_image = GraphicsComponent.get_transformed_image(
                surface, accumulated_transform, source_corner_points
            )
            new_x, new_y = source_corner_points[0]
            casted_x, casted_y = int(new_x), int(new_y)

            screen.blit(transformed_image, (casted_x, casted_y))
