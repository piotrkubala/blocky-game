from abc import abstractmethod, ABC


class GraphicalActionButtonProcessor(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


class GraphicalGoActionButtonProcessor(GraphicalActionButtonProcessor):
    def get_name(self) -> str:
        return "go"


class GraphicalTakeActionButtonProcessor(GraphicalActionButtonProcessor):
    def get_name(self) -> str:
        return "take"


class GraphicalEscapeActionButtonProcessor(GraphicalActionButtonProcessor):
    def get_name(self) -> str:
        return "escape"


class GraphicalMoveActionButtonProcessor(GraphicalActionButtonProcessor):
    def get_name(self) -> str:
        return "move"
