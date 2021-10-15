from typing import List, Dict
from SnakeAndLadder.src.main.snake_and_ladder import Snake, Ladder


class InvalidSnakeLadderConfig(Exception):
    pass


class Board:

    __slots__ = ["_START", "_END", "_snakes", "_ladder"]
    _START: int
    _END: int
    _snakes: Dict[int, Snake]
    _ladder: Dict[int, Ladder]

    def __init__(self, snakes: List[Snake], ladders: List[Ladder]) -> None:
        self._START = 1
        self._END = 100

        self._snakes = {}
        for snake in snakes:
            self._snakes[snake.start] = snake

        self._ladder = {}
        for ladder in ladders:
            self._ladder[ladder.start] = ladder

        if self._validate_snakes_ladder(self._snakes, self._ladder) is False:
            raise InvalidSnakeLadderConfig("Snake and ladder cannot have same start point")

    @staticmethod
    def _validate_snakes_ladder(snakes: Dict[int, Snake], ladders: Dict[int, Ladder]) -> bool:
        for start in snakes:
            if start in ladders:
                return False
        return True

    @property
    def end_pos(self) -> int:
        return self._END

    def move(self, steps: int, current_pos: int) -> int:
        if steps < 0 or steps + current_pos > self._END:
            print(f"Invalid move {steps}")
            return current_pos
        next_pos = steps + current_pos
        if next_pos in self._ladder:
            print(f"Move up the ladder from {next_pos} -> {self._ladder[next_pos].end}")
            next_pos = self._ladder[next_pos].end
        elif next_pos in self._snakes:
            print(f"Snake bite !!! move down {next_pos} -> {self._snakes[next_pos].end}")
            next_pos = self._snakes[next_pos].end
        return next_pos
