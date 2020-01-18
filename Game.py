from enum import Enum
from Piece import *

class Game:
    
    def __init__(self, board, players):
        self.board = board
        self.players = players

    def initialize(self, game_type):
        self.board.clear()

        if game_type == GameType.CLASSIC:
            for player in self.players:
                for i in range(self.board.size):
                    Pawn(self.board, self.board.convert((1, i), player), player)

                Queen(self.board, self.board.convert((0, 3), player), player)


    def play(self, on_move, on_end):
        on_move(self.players[0], ((0, 0), (1, 1)))


class GameType(Enum):
    EMPTY = 0
    CLASSIC = 1