from __future__ import annotations
from typing import List, Tuple
from .unit import Unit

class Player:
    def __init__(self, identifier: int):
        self.id = identifier
        self.units: List[Tuple[Unit, int, int]] = []  # (unit, x, y)
        self.score = 0
