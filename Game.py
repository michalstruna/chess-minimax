import numpy as np
from enum import Enum

from Piece import *
from Player import PlayerType

class Board:

    def __init__(self, size):
        self.size = size
        self.fields = np.zeros((size, size), dtype = Piece)

    def __getitem__(self, key):
        return self.fields[key]

    def __setitem__(self, key, value):
        self.fields[key] = value

    def add_piece(self, piece):
        self.fields[piece.coord] = piece

    def is_valid_coord(self, coord):
        return coord[0] >= 0  and coord[0] < self.size and coord[1] >= 0 and coord[1] < self.size

    def clear(self):
        for row in self.fields:
            for field in row:
                if field:
                    field.remove()

    def convert(self, coord, player):
        return coord if player.direction > 0 else (self.size - coord[0] - 1, coord[1])

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