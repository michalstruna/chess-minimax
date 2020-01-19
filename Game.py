from enum import Enum
from Piece import *
from Player import PlayerType

class Game:
    
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.move = 0

    def initialize(self, game_type):
        self.board.clear()
        self.move = 0

        if game_type == GameType.CLASSIC:
            for player in self.players:
                for i in range(self.board.size):
                    Pawn(self.board, self.board.convert((1, i), player), player)

                Queen(self.board, self.board.convert((0, 3), player), player)


    def play(self, get_human_move, on_move, on_end):
        while True:
            player = self.players[self.move % 2]
            start, end = get_human_move(player) if player.type == PlayerType.HUMAN else player.brain.get_best_move()

            if self.board[start] and self.board[start].owner == player:
                self.board[start].move(end)

            self.move += 1
            on_move(player, (start, end))


class GameType(Enum):
    EMPTY = 0
    CLASSIC = 1