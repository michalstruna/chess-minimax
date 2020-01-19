import unittest
import sys

sys.path.append('..')

from Player import Player, Color, PlayerType
from Game import Board
from Piece import Pawn, Queen


def get_init():
    board = Board(8)
    player = Player(Color.GREEN, 1, PlayerType.HUMAN)
    player2 = Player(Color.RED, -1, PlayerType.HUMAN)
    return board, player, player2


class PawnTest(unittest.TestCase):

    def test_init_pos(self):
        pos = (1, 1)
        board, player, player2 = get_init()
        pawn = Pawn(board, pos, player)

        self.assertEqual(pawn.coord, pos)

    def test_init_move(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (1, 1), player)
        moves = pawn.get_moves()

        self.assertIn((2, 1), moves)
        self.assertIn((3, 1), moves)
        self.assertEqual(len(moves), 2)

    def test_init_move_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (6, 1), player2)

        moves = pawn.get_moves()

        self.assertIn((5, 1), moves)
        self.assertIn((4, 1), moves)
        self.assertEqual(len(moves), 2)

    def test_move(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (5, 7), player)
        moves = pawn.get_moves()

        self.assertIn((6, 7), moves)
        self.assertEqual(len(moves), 1)

    def test_move_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (5, 2), player2)
        moves = pawn.get_moves()

        self.assertIn((4, 2), moves)
        self.assertEqual(len(moves), 1)

    def test_move_2(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (6, 7), player)
        moves = pawn.get_moves()

        self.assertIn((7, 7), moves)
        self.assertEqual(len(moves), 1)

    def test_move_2_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (1, 0), player2)
        moves = pawn.get_moves()

        self.assertIn((0, 0), moves)
        self.assertEqual(len(moves), 1)

    def test_move_before_end(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (7, 2), player)
        moves = pawn.get_moves()

        self.assertEqual(len(moves), 0)

    def test_move_before_end_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (0, 2), player2)
        moves = pawn.get_moves()

        self.assertEqual(len(moves), 0)

    def test_move_before_own_piece(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (4, 4), player)
        pawn2 = Pawn(board, (5, 4), player)
        moves = pawn.get_moves()

        self.assertEqual(len(moves), 0)

    def test_move_before_own_piece_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (5, 5), player2)
        pawn2 = Pawn(board, (4, 5), player2)
        moves = pawn.get_moves()

        self.assertEqual(len(moves), 0)

    def test_move_before_enemy_piece(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (4, 4), player)
        pawn2 = Pawn(board, (5, 4), player2)
        moves = pawn.get_moves()

        self.assertEqual(len(moves), 0)

    def test_move_before_enemy_piece_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (5, 5), player2)
        pawn2 = Pawn(board, (4, 5), player)
        moves = pawn.get_moves()

        self.assertEqual(len(moves), 0)

    def test_attack_move(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (4, 4), player)
        pawn2 = Pawn(board, (5, 5), player2)
        moves = pawn.get_moves()

        self.assertIn((5, 5), moves)
        self.assertIn((5, 4), moves)
        self.assertEqual(len(moves), 2)

    def test_attack_move_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (4, 4), player2)
        pawn2 = Pawn(board, (3, 3), player)
        moves = pawn.get_moves()

        self.assertIn((3, 3), moves)
        self.assertIn((3, 4), moves)
        self.assertEqual(len(moves), 2)

    def test_double_attack_move(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (4, 4), player)
        pawn2 = Pawn(board, (5, 5), player2)
        pawn3 = Pawn(board, (5, 3), player2)
        moves = pawn.get_moves()

        self.assertIn((5, 5), moves)
        self.assertIn((5, 3), moves)
        self.assertIn((5, 4), moves)
        self.assertEqual(len(moves), 3)

    def test_double_attack_move_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (4, 4), player2)
        pawn2 = Pawn(board, (3, 3), player)
        pawn3 = Pawn(board, (3, 5), player)
        moves = pawn.get_moves()

        self.assertIn((3, 3), moves)
        self.assertIn((3, 4), moves)
        self.assertIn((3, 5), moves)
        self.assertEqual(len(moves), 3)

    def test_attack(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (4, 4), player)
        pawn2 = Pawn(board, (5, 5), player2)
        pawn.move(pawn2.coord)

        self.assertEqual(pawn.coord, pawn2.coord)
        self.assertNotIn(pawn2, player2.pieces)

    def test_attack_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (6, 6), player2)
        pawn2 = Pawn(board, (5, 7), player)
        pawn.move(pawn2.coord)

        self.assertEqual(pawn.coord, pawn2.coord)
        self.assertNotIn(pawn2, player.pieces)

    def test_invalid_move(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (1, 2), player)

        with self.assertRaises(ValueError):
            pawn.move((2, 1))


class QueenTest(unittest.TestCase):

    def test_init_pos(self):
        pos = (1, 1)
        board, player, player2 = get_init()
        queen = Queen(board, pos, player)

        self.assertEqual(queen.coord, pos)

    def test_corner_move(self):
        board, player, player2 = get_init()
        queen = Queen(board, (0, 0), player)
        moves = queen.get_moves()

        self.assertEqual(len(moves), 21)
        self.assertIn((1, 0), moves)
        self.assertIn((0, 1), moves)
        self.assertIn((1, 1), moves)
        self.assertIn((7, 0), moves)
        self.assertIn((0, 7), moves)
        self.assertIn((7, 7), moves)

    def test_center_move(self):
        board, player, player2 = get_init()
        queen = Queen(board, (3, 3), player)
        moves = queen.get_moves()

        self.assertEqual(len(moves), 27)
        self.assertIn((0, 0), moves)
        self.assertIn((7, 7), moves)
        self.assertIn((3, 0), moves)
        self.assertIn((3, 7), moves)
        self.assertIn((7, 3), moves)
        self.assertIn((0, 3), moves)
        self.assertIn((0, 6), moves)
        self.assertIn((6, 0), moves)

    def test_corner_barricade_move(self):
        board, player, player2 = get_init()
        queen = Queen(board, (0, 0), player)
        pawn = Pawn(board, (2, 2), player)
        pawn2 = Pawn(board, (2, 0), player2)
        moves = queen.get_moves()

        self.assertEqual(len(moves), 10)

    def test_center_no_move(self):
        board, player, player2 = get_init()
        queen = Queen(board, (3, 3), player)
        queen2 = Queen(board, (2, 2), player)
        queen3 = Queen(board, (4, 4), player)
        queen4 = Queen(board, (3, 4), player)
        queen5 = Queen(board, (4, 3), player)
        queen6 = Queen(board, (2, 4), player)
        queen7 = Queen(board, (4, 2), player)
        queen8 = Queen(board, (2, 3), player)
        queen9 = Queen(board, (3, 2), player)
        moves = queen.get_moves()

        self.assertEqual(len(moves), 0)

    def test_attack(self):
        board, player, player2 = get_init()
        queen = Queen(board, (3, 3), player2)
        queen2 = Queen(board, (2, 2), player)
        queen.move(queen2.coord)

        self.assertEqual(queen.coord, queen2.coord)
        self.assertNotIn(queen2, player.pieces)
        self.assertIn(queen, player2.pieces)

    def test_invalid_move(self):
        board, player, player2 = get_init()
        queen = Queen(board, (1, 2), player)

        with self.assertRaises(ValueError):
            queen.move((3, 3))