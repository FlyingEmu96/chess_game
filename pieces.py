from utils import Color
from move import Move

class Piece:
    def __init__(self, color: int):
        self.color = color
        self.has_moved = False

    def symbol(self): raise NotImplementedError
    def legal_vectors(self): raise NotImplementedError
    def generate_pseudo(self, board, x, y): raise NotImplementedError

class King(Piece):
    def symbol(self): return "K" if self.color==Color.WHITE else "k"
    def legal_vectors(self): return [(dx,dy,False) for dx in (-1,0,1) for dy in (-1,0,1) if dx or dy]

class Queen(Piece):
    def symbol(self): return "Q" if self.color==Color.WHITE else "q"
    def legal_vectors(self):
        return [(dx,dy,True) for dx,dy in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))]

class Rook(Piece):
    def symbol(self): return "R" if self.color==Color.WHITE else "r"
    def legal_vectors(self): return [(1,0,True),(-1,0,True),(0,1,True),(0,-1,True)]

class Bishop(Piece):
    def symbol(self): return "B" if self.color==Color.WHITE else "b"
    def legal_vectors(self): return [(1,1,True),(1,-1,True),(-1,1,True),(-1,-1,True)]

class Knight(Piece):
    def symbol(self): return "N" if self.color==Color.WHITE else "n"
    def legal_vectors(self): return [(dx,dy,False) for dx,dy in
        [(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]]

class Pawn(Piece):
    def symbol(self): return "P" if self.color==Color.WHITE else "p"
    def generate_pseudo(self, board, x, y):
        # (full pawn move logic goes here, same as before)
        ...
