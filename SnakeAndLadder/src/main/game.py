from SnakeAndLadder.src.main.player import Player
from SnakeAndLadder.src.main.board import Board
from SnakeAndLadder.src.main.utils import roll
from typing import List, Optional


class Game:
    """
    class to drive Snake Ladder Game
    """
    __slots__ = ["_board", "_players", "_winner", "_currentTurn"]

    _board: Board
    _players: List[Player]
    _winner: Optional[Player]
    _currentTurn: int

    def __init__(self, board: Board, players: List[Player]) -> None:
        self._board = board
        self._players = players
        self._currentTurn = 0
        self._winner = None

    def move(self, player: Player) -> None:
        if self._players[self._currentTurn] == player:
            steps = roll()
            next_pos = self._board.move(steps, player.current_position)
            player.current_position = next_pos
            if player.current_position == self._board.end_pos:
                self._winner = player
                print(f"Player {player} wins !!!")
            self._currentTurn = (self._currentTurn + 1) % len(self._players)
            return
        print(f"It's not player: {player} turn")

    def get_winner(self) -> Optional[Player]:
        if self._winner is None:
            print(f"No winner yet")
            return
        print(f"Winner is {self._winner}")
        return self._winner


