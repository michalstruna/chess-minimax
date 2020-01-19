from enum import Enum
from abc import ABC, abstractmethod
import sys


class Piece(ABC):

    def __init__(self, board, coord, owner):
        self.board = board
        self.coord = coord
        self.owner = owner
        self.owner.pieces.append(self)
        self.board.add_piece(self)

    @abstractmethod
    def get_moves(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def generate_moves(self, change, max_count = sys.maxsize, can_attack = True, can_no_attack = True):
        pos = (self.coord[0], self.coord[1])  # TODO: Copy.
        moves = []

        for i in range(max_count):
            pos = (pos[0] + change[0], pos[1] + change[1])

            if not self.board.is_valid_coord(pos):
                break

            if self.board[pos]:
                if can_attack and self.board[pos].owner != self.owner:
                    moves.append(pos)

                break
            else:
                if can_no_attack:
                    moves.append(pos)
                else:
                    break

        return moves

    def move(self, coord):
        if coord not in self.get_moves():
            raise ValueError("Invalid move.")

        current = self.board[coord]

        if current:
            # TODO: Castling is move to field with own field.
            current.remove()

        self.board[self.coord] = None
        self.board[coord] = self
        self.coord = coord

    def remove(self):
        self.board[self.coord] = None
        self.owner.pieces.remove(self)


class Pawn(Piece):

    def __str__(self):
        return "P"

    def get_moves(self):
        moves = self.generate_moves((self.owner.direction, 0), 1 if self._is_used() else 2, can_attack = False)
        moves += self.generate_moves((self.owner.direction, 1), 1, can_no_attack = False)
        moves += self.generate_moves((self.owner.direction, -1), 1, can_no_attack = False) 

        # TODO: En passant.
        # TODO: Transformation.

        return moves

    def _is_used(self):
        if self.owner.direction > 0:
            return self.coord[0] != 1
        else:
            return self.coord[0] != self.board.size - 2


class Queen(Piece):

    def __str__(self):
        return "Q"

    def get_moves(self):
        moves = []

        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i != 0 or j != 0:
                    moves = moves + self.generate_moves((i, j))

        return moves

class King(Piece):

    def __str__(self):
        return "K"

    def get_moves(self):
        moves = []

        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i != 0 or j != 0:
                    moves = moves + self.generate_moves((i, j), 1)

        return moves