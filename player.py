import random
import math

class Player:
    def __init__(self, letter) -> None:
        self.letter = letter
 

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        return random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        avalable_moves_now  = game.available_moves()
        try:
            spot = int(input("Enter your human move :"))
            if spot not in avalable_moves_now :
                raise ValueError
        except ValueError:
            print("Invalid move")

        return spot

    