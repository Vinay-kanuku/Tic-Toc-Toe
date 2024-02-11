import math
import random
from player import HumanPlayer, ComputerPlayer
from time import sleep

class TicTokToe:
    def __init__(self) -> None:
        self.board = self.make_board()
        self.current_winner = None

    def winner(self, letter, spot):
        row_index = spot // 3
        row = [i for i in self.board[row_index * 3 : (row_index + 1) * 3]]
        if all(value == letter for value in row):
            return True
        col_index = spot % 3
        col = [i for i in self.board[col_index:8:3]]
        if all(value == letter for value in col):
            return True

    def print_current_board_state(self):
        current_board = [[j for j in self.board[j * 3 : (j + 1) * 3]] for j in range(3)]
        for row in current_board:
            print(" | " + " | ".join(row) + " | ")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def no_of_empty_squares(self):
        return len(" " in self.board)

    @staticmethod
    def make_board():
        board = [" " for _ in range(9)]
        # board = [[str(j) for j in range(j * 3, (j + 1) * 3)] for j in range(3)]
        return board

    @staticmethod
    def print_board():
        initial_board = [[str(j) for j in range(j * 3, (j + 1) * 3)] for j in range(3)]
        print()
        for row in initial_board:
            print(" | " + " | ".join(row) + " | ")

    def empty_squres(self) -> bool:
        return " " in self.board

    def make_move(self, spot, letter):
        while True:
            if self.board[spot] == " ":
                self.board[spot] = letter
                break
            else:
                try:
                    spot = int(input("You made an invalid move try again>>> "))
                except Exception:
                    print("Enter an integer")


def play(game, x_player, y_player, play_game=True):
    print(game.print_board())
    letter = "x"
    while game.empty_squres():
        print(game.empty_squres())
        if letter == "x":
            spot = x_player.get_move(game)
            game.make_move(spot, letter)
            game.winner(letter=letter, spot=spot)
        else:
            spot = y_player.get_move(game)
            game.make_move(spot=spot, letter=letter)
            print("Computer making a move")
            sleep(2)
            game.winner(letter=letter, spot=spot)
        print(game.print_current_board_state())
        if game.winner(letter=letter, spot=spot):
            print(f"{letter} player wins")
            break
        letter = "y" if letter == "x" else "x"


if __name__ == "__main__":
    x_player = HumanPlayer("X")
    y_player = ComputerPlayer("Y")
    t = TicTokToe()
    play(t, x_player, y_player, True)
