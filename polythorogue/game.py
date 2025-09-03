import random
from typing import List
from .map import Map
from .player import Player
from .unit import Unit

class Game:
    def __init__(self, width: int = 8, height: int = 8, players: int = 2, seed: int | None = None):
        self.map = Map.generate(width, height, seed=seed)
        self.players: List[Player] = [Player(i) for i in range(players)]
        self.turn = 0
        self.random = random.Random(seed)
        self._place_initial_units()

    def _place_initial_units(self) -> None:
        for i, player in enumerate(self.players):
            x, y = i, i  # place diagonally
            unit = Unit(player=i)
            tile = self.map.get_tile(x, y)
            tile.unit = unit
            player.units.append((unit, x, y))

    def step(self) -> None:
        player = self.players[self.turn]
        new_positions = []
        for unit, x, y in player.units:
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            self.random.shuffle(dirs)
            moved = False
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if self.map.in_bounds(nx, ny):
                    dest = self.map.get_tile(nx, ny)
                    if dest.terrain == 'land' and dest.unit is None:
                        self.map.get_tile(x, y).unit = None
                        dest.unit = unit
                        new_positions.append((unit, nx, ny))
                        moved = True
                        break
            if not moved:
                new_positions.append((unit, x, y))
        player.units = new_positions
        self.turn = (self.turn + 1) % len(self.players)

    def render(self) -> str:
        return self.map.render()
