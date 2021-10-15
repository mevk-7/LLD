from SnakeAndLadder.src.main.snake_and_ladder import Snake, Ladder
from SnakeAndLadder.src.main.player import Player
from SnakeAndLadder.src.main.game import Game
from SnakeAndLadder.src.main.board import Board


if __name__ == '__main__':
    s1 = Snake(20, 10)
    s2 = Snake(61, 20)
    s3 = Snake(70, 40)
    l1 = Ladder(23, 55)
    l2 = Ladder(43, 84)
    l3 = Ladder(55, 87)

    board = Board([s1, s2, s3], [l1, l2, l3])

    p1 = Player("Batman", 1)
    p2 = Player("SuperMan", 2)

    game = Game(board, [p1, p2])

    while game.get_winner() is None:
        game.move(p1)
        game.move(p2)
    print(f"Winner is {game.get_winner()}")


