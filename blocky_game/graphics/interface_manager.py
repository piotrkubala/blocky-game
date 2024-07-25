import numpy as np

from blocky_game.graphics.animations import AnimationsBox, PulsatingAnimation, LinearAnimation
from blocky_game.graphics.game_renderer import GameRenderer
from blocky_game.model.game_objects import GameScreen, GameObject
from blocky_game.model.game_objects_container import GameObjectsContainer
from blocky_game.model.interface_objects import ActionButtonContainer, ActionButton


class InterfaceManager:
    def __initialize_interface(self):
        self.action_button_container = ActionButtonContainer(
            "action_button_container", self.game_screen,
            self.game_objects_container
        )
        self.action_button_container.set_position(self.screen_width, self.screen_height)

        self.game_screen.interface.add_child(self.action_button_container)

    def __process_when_clicked(self, clicked_buttons: list[ActionButton], colliding_object: GameObject):
        pass

    def __process_when_not_clicked(self, colliding_object: GameObject):
        pass

    def __init__(self, game_screen: GameScreen, renderer: GameRenderer,
                 animations_box: AnimationsBox, game_objects_container: GameObjectsContainer,
                 screen_width: int, screen_height: int):
        self.game_screen = game_screen
        self.renderer = renderer
        self.animations_box = animations_box
        self.game_objects_container = game_objects_container
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.__initialize_interface()

    def click_object(self, game_object: GameObject):
        new_animation = PulsatingAnimation(1000, 0.1)
        self.animations_box[game_object] = new_animation

    def unclick_object(self, game_object: GameObject):
        current_transformation = self.renderer.get_object_transform(game_object)
        new_animation = LinearAnimation(1000, current_transformation)
        self.animations_box[game_object] = new_animation

    def toggle_object_click(self, game_object: GameObject):
        animation = self.animations_box[game_object]
        if animation is None:
            self.click_object(game_object)
        else:
            self.unclick_object(game_object)

    def process_click(self, x: int, y: int):
        point = np.array([x, y])
        colliding_object = self.renderer.get_object_colliding_with_point(point, self.animations_box)
        if colliding_object is None:
            return

        clicked_buttons = self.action_button_container.get_active_buttons()

        if len(clicked_buttons) != 0:
            self.__process_when_clicked(clicked_buttons, colliding_object)
        else:
            self.__process_when_not_clicked(colliding_object)
