from utils import Color, sq_to_xy, xy_to_sq
from move import Move
from pieces import King, Queen, Rook, Bishop, Knight, Pawn

class Board:
    def __init__(self):
        self.grid = [[None]*8 for _ in range(8)]
        self.turn = Color.WHITE
        self.history = []
        self.en_passant = None
        self.wk = self.wq = self.bk = self.bq = True
        self._place_start()

    def _place(self, x,y,p): self.grid[y][x] = p
    def at(self, x,y): return self.grid[y][x]
    def remove(self,x,y): self.grid[y][x] = None

    def _place_start(self):
        # same setup code as before: pawns, rooks, knights, bishops, queen, king
        ...

    def legal_moves(self):
        # same filtering of pseudo moves as before
        ...

    def push(self, move: Move):
        # apply a move and update game state
        ...

    def _pop(self): ...
    def in_check(self, color): ...
    def result(self): ...
    def fen(self): ...
    def pretty(self): ...
