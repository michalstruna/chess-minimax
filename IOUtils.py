from colored import fg, bg, attr
from argparse import ArgumentParser

from Piece import Piece

class Reader:

    def read_args(self):
        parser = ArgumentParser()
        return parser.parse_args()

class Writer:

    def write_board(self, board):
        egde_color = "grey_50"
        print(bg(egde_color) + " " * (board.size * 3 + 4) + attr("reset"))

        for i, row in enumerate(board.fields):
            print(bg(egde_color)  + "  " + attr("reset"), end = "")

            for j, cell in enumerate(row):
                background = "black" if j % 2 == (0 if i % 2 == 0 else 1) else "white"
                foreground = cell.owner.color if cell else "black"
                piece = str(cell) if cell else " "

                print(bg(background), fg(foreground) + attr("bold") + piece + " " + attr("reset"), end = "")

            print(bg(egde_color) + "  " + attr("reset"))

        print(bg(egde_color) + " " * (board.size * 3 + 4) + attr("reset"))