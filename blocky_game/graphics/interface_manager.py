import numpy as np

from blocky_game.graphics.animations import AnimationsBox, PulsatingAnimation, LinearAnimation
from blocky_game.graphics.game_renderer import GameRenderer
from blocky_game.model.game_objects import GameScreen, GameObject
from blocky_game.model.game_objects_container import GameObjectsContainer
from blocky_game.model.interface_objects import ActionButtonContainer, ActionButton
from blocky_game.model.board_state import BoardState


class InterfaceManager:
    def __mark_possible_objects(self, action_button: ActionButton):
        action_processor = action_button.action_processor
        possible_objects = action_processor.get_active()

        for game_object in possible_objects:
            self.mark_object(game_object)

    def __initialize_interface(self):
        self.action_button_container = ActionButtonContainer(
            "action_button_container", self.game_screen,
            self.game_objects_container
        )
        self.action_button_container.set_position(self.screen_width, self.screen_height)

        self.game_screen.interface.add_child(self.action_button_container)

    def __execute_action_if_possible(self, action_button: ActionButton):
        action_processor = action_button.action_processor
        if not action_processor.is_finished():
            return

        action = action_processor.generate_action(self.animations_box, self.renderer, self.board_state)
        action_button.deactivate()

        if action is None:
            return

        action.execute()

    def __toggle_objects(self, old_objects: list[GameObject], action_button: ActionButton):
        self.unmark_objects(old_objects)

        new_objects = action_button.action_processor.get_active()
        self.mark_objects(new_objects)

    def __toggle_select_object(self, clicked_button: ActionButton, colliding_object: GameObject):
        last_selected_object = clicked_button.action_processor.get_last_selected_object()
        current_active_objects = clicked_button.action_processor.get_active()

        if last_selected_object == colliding_object:
            clicked_button.action_processor.deselect_last_object()
            self.__toggle_objects(current_active_objects, clicked_button)
            return True

        if clicked_button.action_processor.select_object(colliding_object):
            self.toggle_mark_object(colliding_object)
            self.__toggle_objects(current_active_objects, clicked_button)
            self.__execute_action_if_possible(clicked_button)
            return True

        return False

    def __deactivate_button(self, button: ActionButton):
        active_objects = button.action_processor.get_active()
        self.unmark_objects(active_objects)
        button.deactivate()

    def __process_when_clicked(self, clicked_buttons: list[ActionButton], colliding_object: GameObject):
        match colliding_object:
            case ActionButton() as action_button:
                if action_button in clicked_buttons:
                    self.__deactivate_button(action_button)
            case GameObject():
                for button in clicked_buttons:
                    if self.__toggle_select_object(button, colliding_object):
                        return
            case _:
                raise ValueError(f"Unknown object type: {type(colliding_object)}")

    def __process_when_not_clicked(self, colliding_object: GameObject):
        match colliding_object:
            case ActionButton() as action_button:
                action_button.activate()
                self.__mark_possible_objects(action_button)
            case GameObject():
                pass
            case _:
                raise ValueError(f"Unknown object type: {type(colliding_object)}")

    def __init__(self, game_screen: GameScreen, renderer: GameRenderer, board_state: BoardState,
                 animations_box: AnimationsBox, game_objects_container: GameObjectsContainer,
                 screen_width: int, screen_height: int):
        self.game_screen = game_screen
        self.renderer = renderer
        self.board_state = board_state
        self.animations_box = animations_box
        self.game_objects_container = game_objects_container
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.__initialize_interface()

    def mark_object(self, game_object: GameObject):
        new_animation = PulsatingAnimation(1000, 0.1)
        self.animations_box[game_object] = new_animation

    def unmark_object(self, game_object: GameObject):
        current_transformation = self.renderer.get_object_transform(game_object)
        new_animation = LinearAnimation(1000, current_transformation)
        self.animations_box[game_object] = new_animation

    def toggle_mark_object(self, game_object: GameObject):
        animation = self.animations_box[game_object]
        if animation is None:
            self.mark_object(game_object)
        else:
            self.unmark_object(game_object)

    def mark_objects(self, game_objects: list[GameObject]):
        for game_object in game_objects:
            self.mark_object(game_object)

    def unmark_objects(self, game_objects: list[GameObject]):
        for game_object in game_objects:
            self.unmark_object(game_object)

    def toggle_mark_objects(self, game_objects: list[GameObject]):
        for game_object in game_objects:
            self.toggle_mark_object(game_object)

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
