from enum import Enum


class Color(Enum):
    GREEN = "green"
    RED = "red"


class PlayerType(Enum):
    AI = 0
    HUMAN = 1


class Player:

    def __init__(self, color, direction, player_type):
        self.color = color
        self.direction = direction
        self.pieces = []
        self.type = player_type
