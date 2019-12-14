from enum import Enum


class Color(Enum):
    GREEN = "green"
    RED = "red"


class Player:

    def __init__(self, color, direction):
        self.color = color
        self.direction = direction
        self.pieces = []