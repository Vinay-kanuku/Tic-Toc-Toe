import math
import random
from player import HumanPlayer1, ComputerPlayer, HumanPlayer2
from time import sleep


class TicTokToe:
    def __init__(self) -> None:
        self.board = self.make_board()
        self.current_winner = None

    def winner(self, letter, spot):
        flag = True
        row_index = spot // 3  # calculating the row index from the spot player  choose
        row = [
            i for i in self.board[row_index * 3 : (row_index + 1) * 3]
        ]  # taking the entire row
        if all(value == letter for value in row):
            return True
        col_index = spot % 3  # calculating column index from the spot the player choose
        col = [i for i in self.board[col_index:9:3]]
        if all(value == letter for value in col):
            return True
        if spot % 2 == 0:
            if all(
                value == letter for value in self.board[0:9:4]
            ):  # extracting a diagonal
                return True
            if all(value == letter for value in self.board[2:7:2]):
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
    letter = "X"
    flag = False
    while game.empty_squres():
        if letter == "X":
            spot = x_player.get_move(game)
            game.make_move(spot, letter)
        else:
            spot = y_player.get_move(game)
            game.make_move(spot=spot, letter=letter)
            print(f"{y_player.letter} making a move")
        print(game.print_current_board_state())
        if game.winner(letter=letter, spot=spot):
            print(f"{letter} player wins")
            flag = True
            break
        letter = "O" if letter == "X" else "X"
    if not flag:
        print("It is a tie")


if __name__ == "__main__":
    while True:
        try:
            oponent = int(input("Choose your oponent \nComputer:(0) or Human:(1): "))
            break
        except Exception:
            print("Enter integers only")
    x_player = HumanPlayer1("X")
    if oponent:
        y_player = HumanPlayer2("O")
    else:
        y_player = ComputerPlayer("O")
    t = TicTokToe()
    play(t, x_player, y_player, True)
