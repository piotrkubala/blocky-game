from abc import ABC
import re

from blocky_game.graphics.animations import AnimationsBox
from blocky_game.graphics.game_renderer import GameRenderer
from blocky_game.model.actions import Action, GoAction, TakeAction, EscapeAction, MoveAction
from blocky_game.model.board_state import BoardState
from blocky_game.model.game_objects import Direction


class ActionGenerator(ABC):
    def __init__(self, animations_box: AnimationsBox, renderer: GameRenderer, board_state: BoardState):
        self.actions = []

        self.animations_box = animations_box
        self.renderer = renderer
        self.board_state = board_state

        self.objects_container = self.board_state.game_objects_container

    def get_last_action(self) -> Action | None:
        if self.actions:
            return self.actions[-1]
        return None


class TextActionGenerator(ActionGenerator):
    def __parse_go_action(self, parameters: list[str]):
        if len(parameters) != 11:
            raise ValueError("Invalid number of parameters for 'go' action")

        person, room1, room2, place1, place2, entrance1, \
            entrance2, direction, _, colour, key = parameters

        person_object = self.objects_container.get_people()[person]
        room1_object = self.objects_container.get_rooms()[room1]
        room2_object = self.objects_container.get_rooms()[room2]
        place1_object = self.objects_container.get_places()[place1]
        place2_object = self.objects_container.get_places()[place2]
        entrance1_object = self.objects_container.get_entrances()[entrance1]
        entrance2_object = self.objects_container.get_entrances()[entrance2]
        direction_object = Direction.from_name(direction)
        colour_object = self.objects_container.get_colours()[colour]
        key_object = self.objects_container.get_keys()[key]

        return GoAction(self.animations_box, self.renderer, self.board_state,
                        person_object, room1_object, room2_object,
                        place1_object, place2_object, entrance1_object,
                        entrance2_object, direction_object, colour_object, key_object)

    def __parse_take_action(self, parameters: list[str]):
        if len(parameters) != 3:
            raise ValueError("Invalid number of parameters for 'take' action")

        person, takeable_thing, room = parameters

        person_object = self.objects_container.get_people()[person]
        takeable_thing_object = self.objects_container.get_takeables()[takeable_thing]
        room_object = self.objects_container.get_rooms()[room]

        return TakeAction(self.animations_box, self.renderer, self.board_state,
                          person_object, takeable_thing_object, room_object)

    def __parse_escape_action(self, parameters: list[str]):
        if len(parameters) != 3:
            raise ValueError("Invalid number of parameters for 'escape' action")

        person, map_exit, room = parameters

        person_object = self.objects_container.get_people()[person]
        room_object = self.objects_container.get_rooms()[room]
        map_exit_object = self.objects_container.get_map_exits()[map_exit]

        return EscapeAction(self.animations_box, self.renderer, self.board_state,
                            person_object, map_exit_object, room_object)

    def __parse_move_action(self, parameters: list[str]):
        if len(parameters) != 7:
            raise ValueError("Invalid number of parameters for 'move' action")

        moved_room, place1, place2, direction, person, dwelled_room, terminal = parameters

        moved_room_object = self.objects_container.get_rooms()[moved_room]
        place1_object = self.objects_container.get_places()[place1]
        place2_object = self.objects_container.get_places()[place2]
        direction_object = Direction.from_name(direction)
        person_object = self.objects_container.get_people()[person]
        dwelled_room_object = self.objects_container.get_rooms()[dwelled_room]
        terminal_object = self.objects_container.get_terminals()[terminal]

        return MoveAction(self.animations_box, self.renderer, self.board_state,
                          moved_room_object, place1_object, place2_object, direction_object,
                          person_object, dwelled_room_object, terminal_object)

    def __parse_action_description(self, action_description: str) -> Action:
        # should be of the form "action_name(param1, param2, ..., paramN)"

        without_white_chars = re.sub(r"\s+", "", action_description)
        expression_match = re.findall(r"^([a-z]+)\(([a-zA-Z0-9_,]+)\)$", without_white_chars)

        if not expression_match or len(expression_match[0]) != 2:
            raise ValueError(f"Invalid action description: {action_description}")

        match_groups = expression_match[0]
        action_name = match_groups[0]
        parameters = match_groups[1].split(",")

        match action_name:
            case "go":
                return self.__parse_go_action(parameters)
            case "take":
                return self.__parse_take_action(parameters)
            case "escape":
                return self.__parse_escape_action(parameters)
            case "move":
                return self.__parse_move_action(parameters)
            case _:
                raise ValueError(f"Invalid action name: {action_name}")

    def __init__(self, animations_box: AnimationsBox, renderer: GameRenderer, board_state: BoardState):
        super().__init__(animations_box, renderer, board_state)

    def process_action_description(self, action_description: str):
        try:
            action = self.__parse_action_description(action_description)
            self.actions.append(action)
        except ValueError as e:
            print(e)


class GraphicalActionGenerator(ActionGenerator):
    def __init__(self, animations_box: AnimationsBox, renderer: GameRenderer, board_state: BoardState):
        super().__init__(animations_box, renderer, board_state)
