class Brain:

    def __init__(self, me, enemy, board):
        self.me = me
        self.enemy = enemy
        self.board = board

    def get_best_move(self):
        moves = self.get_moves()
        return moves[0] if moves else None

    def get_moves(self):
        moves = []

        for piece in self.me.pieces:
            moves = moves + list(map(lambda move: (piece.coord, move), piece.get_moves()))

        return moves