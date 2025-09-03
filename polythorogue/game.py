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
        self.game_over = False
        self.message = ""
        self._place_initial_units()

    def _place_initial_units(self) -> None:
        if len(self.players) >= 2:
            positions = [(0, 0), (self.map.width - 1, self.map.height - 1)]
        else:
            positions = [(0, 0)]
        for i, player in enumerate(self.players):
            if i < len(positions):
                x, y = positions[i]
            else:
                x, y = i, i
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

    def move_player(self, dx: int, dy: int) -> None:
        if self.game_over:
            return
        player = self.players[0]
        if not player.units:
            return
        unit, x, y = player.units[0]
        nx, ny = x + dx, y + dy
        if not self.map.in_bounds(nx, ny):
            return
        dest = self.map.get_tile(nx, ny)
        if dest.terrain != 'land':
            return
        current_tile = self.map.get_tile(x, y)
        if dest.unit is not None:
            if dest.unit.player != 0:
                enemy_player = self.players[dest.unit.player]
                enemy_player.units = [u for u in enemy_player.units if u[0] is not dest.unit]
                self.message = "You win!"
                self.game_over = True
            else:
                return
        current_tile.unit = None
        dest.unit = unit
        player.units[0] = (unit, nx, ny)
        if dest.village and not self.game_over:
            self.message = "You reached the village!"
            self.game_over = True
        if not self.game_over:
            self.step_ai()

    def step_ai(self) -> None:
        if self.game_over:
            return
        for i in range(1, len(self.players)):
            player = self.players[i]
            new_positions = []
            for unit, x, y in player.units:
                dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                self.random.shuffle(dirs)
                moved = False
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if self.map.in_bounds(nx, ny):
                        dest = self.map.get_tile(nx, ny)
                        if dest.terrain != 'land':
                            continue
                        if dest.unit is None:
                            self.map.get_tile(x, y).unit = None
                            dest.unit = unit
                            new_positions.append((unit, nx, ny))
                            moved = True
                            break
                        if dest.unit.player == 0:
                            self.players[0].units = []
                            self.map.get_tile(x, y).unit = None
                            dest.unit = unit
                            new_positions.append((unit, nx, ny))
                            self.message = "You were caught!"
                            self.game_over = True
                            return
                if not moved:
                    new_positions.append((unit, x, y))
            player.units = new_positions
