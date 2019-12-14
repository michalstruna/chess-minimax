#!/usr/bin/python3

from Piece import Pawn, Queen
from Board import Board
from Player import Player, Color
from IOUtils import Writer

writer = Writer()

me = Player(Color.GREEN.value, 1)
enemy = Player(Color.RED.value, -1)

board = Board(8)
board.add_piece(Queen(board, (0, 3), me))

board.add_piece(Pawn(board, (6, 0), enemy))
board.add_piece(Pawn(board, (6, 1), enemy))
board.add_piece(Pawn(board, (6, 2), enemy))
board.add_piece(Pawn(board, (6, 3), enemy))
board.add_piece(Pawn(board, (6, 4), enemy))
board.add_piece(Pawn(board, (6, 5), enemy))
board.add_piece(Pawn(board, (6, 6), enemy))
board.add_piece(Pawn(board, (6, 7), enemy))

writer.write_board(board)

while True:
    moves = me.pieces[0].get_moves()

    if not moves:
        break

    move = moves[0]

    me.pieces[0].move(move)
    writer.write_board(board)