from abc import ABC, abstractmethod
import numpy as np

from blocky_game.model.board_state import GameObject


class Animation(ABC):
    def __init__(self, duration: float | None):
        self.duration = duration
        self.current_time = 0

    def update(self, delta_time: float):
        self.current_time += delta_time

    def is_finished(self) -> bool:
        return self.duration is not None and self.current_time >= self.duration

    def get_progress(self) -> float:
        return min(max(self.current_time / self.duration, 0), 1) if self.duration is not None else 0

    @abstractmethod
    def apply(self, target_transformation: np.ndarray):
        pass


class LinearAnimation(Animation):
    def __init__(self, duration: float, start_transformation: np.ndarray):
        super().__init__(duration)
        self.start_transformation = start_transformation

    def apply(self, target_transformation: np.ndarray):
        progress = self.get_progress()

        return self.start_transformation * (1 - progress) + target_transformation * progress


class PulsatingAnimation(Animation):
    def __init__(self, time_period: float, scale_factor: float):
        super().__init__(None)
        self.time_period = time_period
        self.scale_factor = scale_factor

    def apply(self, target_transformation: np.ndarray):
        scale = 1 + self.scale_factor * (np.cos(2 * np.pi * self.current_time / self.time_period) - 1.0) / 2
        scale_matrix = np.array([
            [scale, 0, 0],
            [0, scale, 0],
            [0, 0, 1]
        ])

        return target_transformation @ scale_matrix


class AnimationsBox:
    def __init__(self):
        self.animations: dict[str, Animation] = {}

    def __getitem__(self, game_object: GameObject) -> Animation | None:
        key = game_object.name
        animation = self.animations.get(key)

        if animation is None or animation.is_finished():
            if animation is not None:
                del self.animations[key]
            return None

        return animation

    def __setitem__(self, game_object: GameObject, value: Animation):
        key = game_object.name
        self.animations[key] = value

    def __delitem__(self, game_object: GameObject):
        key = game_object.name
        del self.animations[key]

    def update(self, delta_time: float):
        animations_key_to_delete = []
        for key, animation in self.animations.items():
            animation.update(delta_time)
            if animation.is_finished():
                animations_key_to_delete.append(key)

        for key in animations_key_to_delete:
            del self.animations[key]

