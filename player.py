import random
import math

class Player:
    def __init__(self, letter) -> None:
        self.letter = letter
 

class ComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game):
        pass 