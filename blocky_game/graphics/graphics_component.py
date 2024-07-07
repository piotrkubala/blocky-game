from abc import ABC, abstractmethod
import pygame
import numpy as np
import cv2


class GraphicsComponent(ABC):
    def __init__(self):
        self.transform = np.identity(3)
        self.sprites: list[tuple[tuple[int, int, int] | None, pygame.sprite]] = []

    def add_sprite(self, sprite: pygame.sprite, colour: tuple[int, int, int] | None = None):
        self.sprites.append((colour, sprite))

    def clear_transform(self):
        self.transform = np.identity(3)

    def clear_sprites(self):
        self.sprites = []

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

    def get_transformed_corners(self, sprite: pygame.sprite) -> np.ndarray:
        corners = np.array([
            [0, 0, 1],
            [sprite.rect.width, sprite.rect.height, 1]
        ])
        return self.transform @ corners

    def get_transformed_image(self, sprite: pygame.sprite) -> pygame.Surface:
        source_image = sprite.image

        source_points = self.get_transformed_corners(sprite)
        max_x, max_y = np.max(source_points, axis=0)[:2]
        min_x, min_y = np.min(source_points, axis=0)[:2]
        width, height = int(max_x - min_x), int(max_y - min_y)

        transformed_image = cv2.warpAffine(
            pygame.surfarray.pixels3d(source_image),
            self.transform,
            (width, height)
        )
        return pygame.surfarray.make_surface(transformed_image)

    def draw(self, screen: pygame.Surface):
        for colour, sprite in self.sprites:
            if colour is not None:
                sprite.image.fill(colour)
            transformed_image = self.get_transformed_image(sprite)
            screen.blit(transformed_image, (0, 0)) # TODO: Check destination position
