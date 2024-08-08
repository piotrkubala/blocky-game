from .game_objects import (
    Person, Key, Colour, Entrance, Place, Room, GameBoard, MapExit, Terminal, GameObject, TakeableThing
)


class GameObjectsContainer:
    def __init__(self):
        self.people: dict[str, Person] = {}
        self.keys: dict[str, Key] = {}
        self.colours: dict[str, Colour] = {}
        self.entrances: dict[str, Entrance] = {}
        self.places: dict[str, Place] = {}
        self.rooms: dict[str, Room] = {}
        self.game_boards: dict[str, GameBoard] = {}
        self.map_exits: dict[str, MapExit] = {}
        self.terminals: dict[str, Terminal] = {}

    def add_object(self, game_object: GameObject):
        match game_object:
            case Person() as person:
                self.add_person(person)
            case Key() as key:
                self.add_key(key)
            case Colour() as colour:
                self.add_colour(colour)
            case Entrance() as entrance:
                self.add_entrance(entrance)
            case Place() as place:
                self.add_place(place)
            case Room() as room:
                self.add_room(room)
            case GameBoard() as game_board:
                self.add_game_board(game_board)
            case MapExit() as map_exit:
                self.map_exits[map_exit.name] = map_exit
            case Terminal() as terminal:
                self.terminals[terminal.name] = terminal
            case _:
                raise ValueError(f"Unknown object type: {type(game_object)}")

    def add_person(self, person: Person):
        self.people[person.name] = person

    def add_key(self, key: Key):
        self.keys[key.name] = key

    def add_colour(self, colour: Colour):
        self.colours[colour.name] = colour

    def add_entrance(self, entrance: Entrance):
        self.entrances[entrance.name] = entrance

    def add_place(self, place: Place):
        self.places[place.name] = place

    def add_room(self, room: Room):
        self.rooms[room.name] = room

    def add_game_board(self, game_board: GameBoard):
        self.game_boards[game_board.name] = game_board

    def get_people(self) -> dict[str, Person]:
        return self.people

    def get_keys(self) -> dict[str, Key]:
        return self.keys

    def get_colours(self) -> dict[str, Colour]:
        return self.colours

    def get_entrances(self) -> dict[str, Entrance]:
        return self.entrances

    def get_places(self) -> dict[str, Place]:
        return self.places

    def get_rooms(self) -> dict[str, Room]:
        return self.rooms

    def get_game_boards(self) -> dict[str, GameBoard]:
        return self.game_boards

    def get_map_exits(self) -> dict[str, MapExit]:
        return self.map_exits

    def get_terminals(self) -> dict[str, Terminal]:
        return self.terminals

    def get_takeables(self) -> dict[str, TakeableThing]:
        takeables = {}
        takeables.update(self.keys)
        takeables.update(self.colours)
        return takeables

    def get_all_objects(self) -> dict[str, GameObject]:
        all_objects = {}
        all_objects.update(self.people)
        all_objects.update(self.keys)
        all_objects.update(self.colours)
        all_objects.update(self.entrances)
        all_objects.update(self.places)
        all_objects.update(self.rooms)
        all_objects.update(self.game_boards)
        all_objects.update(self.map_exits)
        all_objects.update(self.terminals)
        return all_objects

    def is_game_ended(self) -> bool:
        return any(map(lambda person: person.escaped, self.people.values()))
