FILES = "abcdefgh"
RANKS = "12345678"

def sq_to_xy(sq: str):
    f, r = sq[0], sq[1]
    return FILES.index(f), RANKS.index(r)

def xy_to_sq(x: int, y: int) -> str:
    return f"{FILES[x]}{RANKS[y]}"

class Color:
    WHITE = 0
    BLACK = 1

    @staticmethod
    def other(c: int) -> int:
        return Color.BLACK if c == Color.WHITE else Color.WHITE
