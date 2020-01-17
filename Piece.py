from enum import Enum
from abc import ABC, abstractmethod

class Piece(ABC):

    def __init__(self, board, coord, owner):
        self.board = board
        self.coord = coord
        self.owner = owner
        self.owner.pieces.append(self)
    
    @abstractmethod
    def get_moves(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def move(self, coord):
        if coord not in self.get_moves():
            raise ValueError("Invalid move.")

        current = self.board.fields[coord]

        if current:
            current.owner.pieces.remove(current) # TODO: Castling is move to field with own field.

        self.board.fields[self.coord] = None
        self.board.fields[coord] = self
        self.coord = coord

class Pawn(Piece):

    def __init__(self, board, coord, owner):
        super().__init__(board, coord, owner)

    def __str__(self):
        return "P"

    def get_moves(self):
        moves = []

        move = (self.coord[0] + self.owner.direction, self.coord[1])

        if self.board.is_valid_coord(move) and not self.board[move]:
            moves.append(move)

        move = (self.coord[0] + self.owner.direction * 2, self.coord[1])

        if self.board.is_valid_coord(move) and not self._is_used():
            moves.append(move)

        move = (self.coord[0] + self.owner.direction, self.coord[1] - 1)

        if self.board.is_valid_coord(move) and self.board[move]:
            moves.append(move)

        move = (self.coord[0] + self.owner.direction, self.coord[1] + 1)

        if self.board.is_valid_coord(move) and self.board[move]:
            moves.append(move)

        # TODO: En passant.
        # TODO: Transformation.

        return moves

    def _is_used(self):
        if self.owner.direction > 0:
            return self.coord[0] != 1
        else:
            return self.coord[0] != self.board.size - 2

class Queen(Piece):

    def __init__(self, board, coord, owner):
        super().__init__(board, coord, owner)

    def __str__(self):
        return "Q"

    def get_moves(self):
        moves = []

        for change in ((1, self.board.size), (-1, -1)):
            for i in range(self.coord[0] + change[0], change[1], change[0]):
                move = (i, self.coord[1])

                if self.board.is_valid_coord(move):
                    moves.append(move)

                    if self.board[i, self.coord[1]]:
                        break

        for change in ((1, self.board.size), (-1, -1)):
            for i in range(self.coord[1] + change[0], change[1], change[0]):
                move = (self.coord[0], i)

                if self.board.is_valid_coord(move):
                    moves.append(move)

                    if self.board[self.coord[0], i]:
                        break

        return moves