import numpy as np

from Piece import Piece

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
        return coord if player.direction < 0 else (-coord[0] - 1, coord[1])