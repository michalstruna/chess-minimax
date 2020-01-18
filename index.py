#!/usr/bin/python3

import time

from Piece import Pawn, Queen
from Board import Board
from Player import Player, Color
from IOUtils import Reader, Writer

reader = Reader()
writer = Writer()


args = reader.read_args()

me = Player(Color.GREEN.value, 1)
enemy = Player(Color.RED.value, -1)

board = Board(8)
Pawn(board, (1, 3), enemy)
Pawn(board, (6, 0), enemy)
Pawn(board, (6, 1), enemy)
Pawn(board, (6, 2), enemy)
Pawn(board, (6, 3), enemy)
Pawn(board, (6, 4), enemy)
Pawn(board, (6, 5), enemy)
Pawn(board, (6, 6), enemy)
Pawn(board, (6, 7), enemy)

while True:
    writer.write_board(board)
    (command, *args) = input("Zadej příkaz: ").split(sep = " ")

    if command == "move":
        (y0, x0, y1, x1) = tuple(map(int, args))
        start = (y0, x0)
        end = (y1, x1)

        print(start)
        print(end)

        if board.is_valid_coord(start) and board.is_valid_coord(end) and board[start]:
            board[start].move(end)

    print("...AI je na tahu...")
    time.sleep(2)