from blocky_game.graphics.animations import AnimationsBox
from blocky_game.graphics.game_renderer import GameRenderer
from blocky_game.model.actions import Action
from blocky_game.model.actions_generator import TextActionGenerator
from blocky_game.model.board_state import BoardState


class ActionsList:
    def __init__(self, actions_list_path: str | None,
                 animations_box: AnimationsBox, renderer: GameRenderer,
                 board_state: BoardState):
        self.actions_strings = []
        self.action_index = 0

        self.actions_generator = TextActionGenerator(animations_box, renderer, board_state)

        if actions_list_path is None:
            return

        with open(actions_list_path, "r") as file:
            self.actions_strings = file.readlines()

    def done(self) -> bool:
        return self.action_index >= len(self.actions_strings)

    def update_index(self):
        self.action_index = min(self.action_index + 1, len(self.actions_strings))

    def get_action(self) -> Action | None:
        if self.done():
            return None

        action_description = self.actions_strings[self.action_index]
        self.actions_generator.process_action_description(action_description)

        return self.actions_generator.get_last_action()
