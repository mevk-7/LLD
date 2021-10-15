
class Player:
    __slots__ = ["_name", "_id", "_current_position"]
    _name: str
    _id: int
    _current_position: int

    def __init__(self, name: str, id_: int) -> None:
        self._name = name
        self._id = id_
        self._current_position = 1

    @property
    def current_position(self) -> int:
        return self._current_position

    @current_position.setter
    def current_position(self, new_position: int) -> None:
        if new_position != self._current_position:
            print(f"Player {self._name}: moved to {new_position}")
            self._current_position = new_position

    def __str__(self):
        return self._name

