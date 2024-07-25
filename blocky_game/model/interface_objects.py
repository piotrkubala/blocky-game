import pygame

from blocky_game.graphics.action_button_processor import GraphicalActionButtonProcessor, \
    GraphicalGoActionButtonProcessor, GraphicalTakeActionButtonProcessor, GraphicalEscapeActionButtonProcessor, \
    GraphicalMoveActionButtonProcessor
from blocky_game.model.game_objects import GameObject, RectangularContainer, GameScreen
from blocky_game.graphics.graphics_component import get_font
from blocky_game.model.game_objects_container import GameObjectsContainer


class ActionButtonState(GameObject):
    def __init__(self, name: str):
        super().__init__(name)

    def get_children(self) -> list[GameObject]:
        return []


class ActionButton(GameObject):
    def prepare_visuals(self):
        self.graphics_component.clear_surfaces()

        rect = pygame.Surface((self.width, self.height))
        rect.fill(self.current_colour)

        action_name = self.action_processor.get_name().upper()

        roboto_font = get_font("roboto", "Roboto-Regular.ttf", 20)
        text_surface = roboto_font.render(action_name, True, (0, 0, 0))

        text_width, text_height = text_surface.get_size()

        rect.blit(text_surface, (self.width / 2 - text_width / 2, self.height - text_height / 2 * 3))

        self.graphics_component.add_surface(rect)

    def __init__(self, name: str, action_processor: GraphicalActionButtonProcessor,
                 width: int = 140, height: int = 120):
        super().__init__(name)

        self.action_button_state: ActionButtonState = ActionButtonState(f"{name}_action_button_state")
        self.action_processor = action_processor

        self.active_colour = (0, 200, 0)
        self.not_active_colour = (200, 200, 0)

        self.width = width
        self.height = height

        self.current_colour = self.not_active_colour

        self.prepare_visuals()

    def is_active(self) -> bool:
        return self.action_processor.is_active

    def activate(self):
        self.action_processor.activate()
        self.current_colour = self.active_colour
        self.prepare_visuals()

    def deactivate(self):
        self.action_processor.deactivate()
        self.current_colour = self.not_active_colour
        self.prepare_visuals()

    def get_children(self) -> list[GameObject]:
        return [self.action_button_state]


class ActionButtonContainer(GameObject):
    def set_position(self, screen_width: int, screen_height: int):
        self.action_buttons.graphics_component.clear_transform()
        self.action_buttons.graphics_component.translate(screen_width - self.width / 2, screen_height / 2)

    def __init__(self, name: str, game_screen: GameScreen,
                 game_objects_container: GameObjectsContainer,
                 width: int = 200, height: int = 700):
        super().__init__(name)

        self.game_screen = game_screen
        self.game_objects_container = game_objects_container

        self.width = width
        self.height = height

        self.action_buttons: RectangularContainer = \
            RectangularContainer("action_buttons_container", width, height)

        self.create_buttons()

    def add_action_button(self, action_button: ActionButton):
        self.action_buttons.add_child(action_button)

    def create_buttons(self):
        action_processors = [
            GraphicalGoActionButtonProcessor(self.game_screen, self.game_objects_container),
            GraphicalTakeActionButtonProcessor(self.game_screen, self.game_objects_container),
            GraphicalEscapeActionButtonProcessor(self.game_screen, self.game_objects_container),
            GraphicalMoveActionButtonProcessor(self.game_screen, self.game_objects_container)
        ]

        for action_processor in action_processors:
            action_name = action_processor.get_name()
            action_button = ActionButton(f"{action_name}_button", action_processor)
            self.add_action_button(action_button)

    def get_active_buttons(self) -> list[ActionButton]:
        return [action_button for action_button in self.action_buttons.get_children() if action_button.is_active()]

    def get_children(self) -> list[GameObject]:
        return [self.action_buttons]


