from Player import Player, Color
from Board import Board
from Piece import Pawn, Queen
import unittest
import sys

sys.path.append('..')


def get_init():
    board = Board(8)
    player = Player(Color.GREEN, 1)
    player2 = Player(Color.RED, -1)
    return board, player, player2


class PawnTest(unittest.TestCase):

    def test_init_pos(self):
        pos = (1, 1)
        board, player, player2 = get_init()
        pawn = Pawn(board, pos, player)
        board.add_piece(pawn)

        self.assertEqual(pawn.coord, pos)

    def test_init_move(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (1, 1), player)
        board.add_piece(pawn)
        moves = pawn.get_moves()

        self.assertIn((2, 1), moves)
        self.assertIn((3, 1), moves)
        self.assertEqual(len(moves), 2)

    def test_init_move_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (6, 1), player2)

        board.add_piece(pawn)
        moves = pawn.get_moves()

        self.assertIn((5, 1), moves)
        self.assertIn((4, 1), moves)
        self.assertEqual(len(moves), 2)

    def test_move(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (5, 7), player)
        board.add_piece(pawn)
        moves = pawn.get_moves()

        self.assertIn((6, 7), moves)
        self.assertEqual(len(moves), 1)

    def test_move_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (5, 2), player2)
        board.add_piece(pawn)
        moves = pawn.get_moves()

        self.assertIn((4, 2), moves)
        self.assertEqual(len(moves), 1)

    def test_move_2(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (6, 7), player)
        board.add_piece(pawn)
        moves = pawn.get_moves()

        self.assertIn((7, 7), moves)
        self.assertEqual(len(moves), 1)

    def test_move_2_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (1, 0), player2)
        board.add_piece(pawn)
        moves = pawn.get_moves()

        self.assertIn((0, 0), moves)
        self.assertEqual(len(moves), 1)

    def test_move_before_end(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (7, 2), player)
        board.add_piece(pawn)
        moves = pawn.get_moves()

        self.assertEqual(len(moves), 0)

    def test_move_before_end_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (0, 2), player2)
        board.add_piece(pawn)
        moves = pawn.get_moves()

        self.assertEqual(len(moves), 0)

    def test_move_before_own_piece(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (4, 4), player)
        pawn2 = Pawn(board, (5, 4), player)
        board.add_piece(pawn)
        board.add_piece(pawn2)
        moves = pawn.get_moves()

        self.assertEqual(len(moves), 0)

    def test_move_before_own_piece_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (5, 5), player2)
        pawn2 = Pawn(board, (4, 5), player2)
        board.add_piece(pawn)
        board.add_piece(pawn2)
        moves = pawn.get_moves()

        self.assertEqual(len(moves), 0)

    def test_move_before_enemy_piece(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (4, 4), player)
        pawn2 = Pawn(board, (5, 4), player2)
        board.add_piece(pawn)
        board.add_piece(pawn2)
        moves = pawn.get_moves()

        self.assertEqual(len(moves), 0)

    def test_move_before_enemy_piece_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (5, 5), player2)
        pawn2 = Pawn(board, (4, 5), player)
        board.add_piece(pawn)
        board.add_piece(pawn2)
        moves = pawn.get_moves()

        self.assertEqual(len(moves), 0)

    def test_attack_move(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (4, 4), player)
        pawn2 = Pawn(board, (5, 5), player2)
        board.add_piece(pawn)
        board.add_piece(pawn2)
        moves = pawn.get_moves()

        self.assertIn((5, 5), moves)
        self.assertIn((5, 4), moves)
        self.assertEqual(len(moves), 2)

    def test_attack_move_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (4, 4), player2)
        pawn2 = Pawn(board, (3, 3), player)
        board.add_piece(pawn)
        board.add_piece(pawn2)
        moves = pawn.get_moves()

        self.assertIn((3, 3), moves)
        self.assertIn((3, 4), moves)
        self.assertEqual(len(moves), 2)

    def test_double_attack_move(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (4, 4), player)
        pawn2 = Pawn(board, (5, 5), player2)
        pawn3 = Pawn(board, (5, 3), player2)
        board.add_piece(pawn)
        board.add_piece(pawn2)
        board.add_piece(pawn3)
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
        board.add_piece(pawn)
        board.add_piece(pawn2)
        board.add_piece(pawn3)
        moves = pawn.get_moves()

        self.assertIn((3, 3), moves)
        self.assertIn((3, 4), moves)
        self.assertIn((3, 5), moves)
        self.assertEqual(len(moves), 3)

    def test_attack(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (4, 4), player)
        pawn2 = Pawn(board, (5, 5), player2)
        board.add_piece(pawn)
        board.add_piece(pawn2)
        pawn.move(pawn2.coord)
        
        self.assertEqual(pawn.coord, pawn2.coord)
        self.assertNotIn(pawn2, player2.pieces)

    def test_attack_reverse(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (6, 6), player2)
        pawn2 = Pawn(board, (5, 7), player)
        board.add_piece(pawn)
        board.add_piece(pawn2)
        pawn.move(pawn2.coord)
        
        self.assertEqual(pawn.coord, pawn2.coord)
        self.assertNotIn(pawn2, player.pieces)

    def test_invalid_move(self):
        board, player, player2 = get_init()
        pawn = Pawn(board, (1, 2), player)
        board.add_piece(pawn)

        with self.assertRaises(ValueError):
            pawn.move((2, 1))