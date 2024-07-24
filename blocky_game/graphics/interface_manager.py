from blocky_game.model.game_objects import GameScreen
from blocky_game.model.interface_objects import ActionButtonContainer


class InterfaceManager:
    def __initialize_interface(self):
        action_button_container = ActionButtonContainer("action_button_container", self.game_screen)
        action_button_container.set_position(self.screen_width, self.screen_height)

        self.game_screen.interface.add_child(action_button_container)

    def __init__(self, game_screen: GameScreen, screen_width: int, screen_height: int):
        self.game_screen = game_screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.__initialize_interface()
