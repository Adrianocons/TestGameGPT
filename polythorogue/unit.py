from dataclasses import dataclass
from typing import Optional

@dataclass
class Unit:
    player: int
    hp: int = 10
    attack: int = 3
    moves: int = 1

    def move(self, game_map, from_x: int, from_y: int, to_x: int, to_y: int) -> bool:
        if not game_map.in_bounds(to_x, to_y):
            return False
        dest = game_map.get_tile(to_x, to_y)
        if dest.terrain != 'land' or dest.unit is not None:
            return False
        game_map.get_tile(from_x, from_y).unit = None
        dest.unit = self
        return True

    def attack_unit(self, other: 'Unit') -> bool:
        other.hp -= self.attack
        return other.hp <= 0
