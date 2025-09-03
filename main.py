from board import Board
from utils import Color, sq_to_xy
from move import Move

def parse_move_uci(s: str) -> Move:
    s = s.strip()
    fx, fy = sq_to_xy(s[:2])
    tx, ty = sq_to_xy(s[2:4])
    promo = s[4].lower() if len(s) >= 5 else None
    return Move(fx,fy,tx,ty,promo)

def main():
    b = Board()
    print("OOP Chess — type 'help' for commands.")
    while True:
        b.pretty()
        res = b.result()
        if res: print("Game over:", res); break
        side = "White" if b.turn==Color.WHITE else "Black"
        inp = input(f"{side} to move > ").strip()
        if inp in ("q","quit","exit"): break
        try:
            m = parse_move_uci(inp)
            b.push(m)
        except Exception as e:
            print("Invalid move:", e)

if __name__ == "__main__":
    main()
