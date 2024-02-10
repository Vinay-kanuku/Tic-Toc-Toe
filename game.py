import math
import random
from LocalRepo.player import HumanPlayer, ComputerPlayer


class TicTokToe:
    def __init__(self) -> None:
        self.board = self.make_board()
        self.current_winner = None

    def winner(self):
        pass

    def available_moves(self):
        return [i for i, spot in self.board if spot == " "]

    def no_of_empty_squares(self):
        return len(" " in self.board)

    @staticmethod
    def make_board():
        board = [" " for _ in range(9)]
        return board

    @staticmethod
    def print_board():
        initial_board = [[str(j) for j in range(j * 3, (j + 1) * 3)] for j in range(3)]
        print()
        for row in initial_board:
            print(" | " + " | ".join(row) + " | ")

        print("kk")

    def empty_squres(self) -> bool:
        return " " in self.board


def play(game, x_player, y_player, play_game=True):
    print(game.print_board())
    letter = "x"
    while game.empty_squres():
        if letter == "x":
            spot = x_player.get_move(game)
        else:
            spot = y_player.get_move(game)


if __name__ == "__main__":
    x_player = HumanPlayer("X")
    y_player = ComputerPlayer("Y")
    t = TicTokToe()
    play(t, x_player, y_player, True)
