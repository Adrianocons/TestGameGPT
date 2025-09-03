from dataclasses import dataclass
import random
from typing import List, Optional

@dataclass
class Tile:
    terrain: str  # 'land' or 'water'
    village: bool = False
    unit: Optional['Unit'] = None

class Map:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles: List[List[Tile]] = [
            [Tile('land') for _ in range(width)]
            for _ in range(height)
        ]

    @classmethod
    def generate(cls, width: int, height: int, land_ratio: float = 0.8, villages: int = 5, seed: Optional[int] = None) -> 'Map':
        if seed is not None:
            random.seed(seed)
        grid = cls(width, height)
        for y in range(height):
            for x in range(width):
                terrain = 'land' if random.random() < land_ratio else 'water'
                grid.tiles[y][x].terrain = terrain
        placed = 0
        while placed < villages:
            x = random.randrange(width)
            y = random.randrange(height)
            tile = grid.tiles[y][x]
            if tile.terrain == 'land' and not tile.village:
                tile.village = True
                placed += 1
        return grid

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def get_tile(self, x: int, y: int) -> Tile:
        return self.tiles[y][x]

    def render(self) -> str:
        lines = []
        for y in range(self.height):
            line = ''
            for x in range(self.width):
                tile = self.tiles[y][x]
                if tile.unit:
                    char = str(tile.unit.player)
                elif tile.village:
                    char = 'V'
                elif tile.terrain == 'water':
                    char = '~'
                else:
                    char = '.'
                line += char
            lines.append(line)
        return '\n'.join(lines)
