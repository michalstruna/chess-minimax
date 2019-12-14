import numpy as np

from Piece import Piece

class Board:

    def __init__(self, size):
        self.size = size
        self.fields = np.zeros((size, size), dtype = Piece)

    def __getitem__(self, key):
        return self.fields[key]

    def add_piece(self, piece):
        self.fields[piece.coord] = piece

    def is_valid_coord(self, coord):
        return coord[0] >= 0  and coord[0] < self.size and coord[1] >= 0 and coord[1] < self.size