from dataclasses import dataclass
from utils import xy_to_sq

@dataclass
class Move:
    fx: int; fy: int; tx: int; ty: int
    promotion: str | None = None
    is_en_passant: bool = False
    is_castle: bool = False

    def uci(self) -> str:
        s = xy_to_sq(self.fx, self.fy) + xy_to_sq(self.tx, self.ty)
        if self.promotion:
            s += self.promotion
        return s
