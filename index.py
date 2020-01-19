#!/usr/bin/python3

import time
import sys

from Piece import Pawn, Queen
from Player import Player, Color, PlayerType
from IOUtils import Reader, Writer
from Game import Game, GameType, Board
from AI import Brain

reader = Reader()
writer = Writer()

args = reader.read_args()

board = Board(8)

me = Player(Color.GREEN.value, 1, PlayerType.HUMAN)
enemy = Player(Color.RED.value, -1, PlayerType.AI)

enemy.brain = Brain(enemy, me, board)

game = Game(board, [enemy, me])
game.initialize(GameType.CLASSIC)

def get_human_move(player):
    command, args = reader.read_command()

    try:
        if command == "move":
            (y0, x0, y1, x1) = map(int, args)
            start = (y0, x0)
            end = (y1, x1)

            if board[start] and board[start].owner == player and end in board[start].get_moves(): # TODO: Move check to Game class.
                return (start, end)
            else:
                raise ValueError("Invalid move.")
        elif command == "show":
            writer.write_board(board)
            return get_human_move(player)
        else:
            raise ValueError("Invalid command.")
    except:
        print("Chyba, zadejde příkaz znovu: " + str(sys.exc_info()[1]))
        return get_human_move(player)

def on_move(player, move):
    writer.write_board(board)

def on_end(winner, move):
    print(winner, move)

game.play(get_human_move, on_move, on_end)