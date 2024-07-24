import pygame

from blocky_game.graphics.action_button_processor import GraphicalActionButtonProcessor, \
    GraphicalGoActionButtonProcessor, GraphicalTakeActionButtonProcessor, GraphicalEscapeActionButtonProcessor, \
    GraphicalMoveActionButtonProcessor
from blocky_game.model.game_objects import GameObject, RectangularContainer, GameScreen
from blocky_game.graphics.graphics_component import get_font


class ActionButtonState(GameObject):
    def __init__(self, name: str):
        super().__init__(name)

    def get_children(self) -> list[GameObject]:
        return []


class ActionButton(GameObject):
    def prepare_visuals(self, width: int = 140, height: int = 120):
        rect = pygame.Surface((width, height))
        rect.fill((255, 255, 0))

        action_name = self.action_processor.get_name().upper()

        roboto_font = get_font("roboto", "Roboto-Regular.ttf", 20)
        text_surface = roboto_font.render(action_name, True, (0, 0, 0))

        text_width, text_height = text_surface.get_size()

        rect.blit(text_surface, (width / 2 - text_width / 2, height - text_height / 2 * 3))

        self.graphics_component.add_surface(rect)

    def __init__(self, name: str, action_processor: GraphicalActionButtonProcessor):
        super().__init__(name)

        self.action_button_state: ActionButtonState = ActionButtonState(f"{name}_action_button_state")
        self.action_processor = action_processor

        self.prepare_visuals()

    def get_children(self) -> list[GameObject]:
        return [self.action_button_state]


class ActionButtonContainer(GameObject):
    def set_position(self, screen_width: int, screen_height: int):
        self.action_buttons.graphics_component.clear_transform()
        self.action_buttons.graphics_component.translate(screen_width - self.width / 2, screen_height / 2)

    def __init__(self, name: str, game_screen: GameScreen, width: int = 200, height: int = 700):
        super().__init__(name)

        self.game_screen = game_screen

        self.width = width
        self.height = height

        self.action_buttons: RectangularContainer = \
            RectangularContainer("action_buttons_container", width, height)

        self.create_buttons()

    def add_action_button(self, action_button: ActionButton):
        self.action_buttons.add_child(action_button)

    def create_buttons(self):
        action_processors = [
            GraphicalGoActionButtonProcessor(self.game_screen),
            GraphicalTakeActionButtonProcessor(self.game_screen),
            GraphicalEscapeActionButtonProcessor(self.game_screen),
            GraphicalMoveActionButtonProcessor(self.game_screen)
        ]

        for action_processor in action_processors:
            action_name = action_processor.get_name()
            action_button = ActionButton(f"{action_name}_button", action_processor)
            self.add_action_button(action_button)

    def get_children(self) -> list[GameObject]:
        return [self.action_buttons]


