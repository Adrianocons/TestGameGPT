import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from polythorogue.game import Game


def test_move_player_moves_unit():
    g = Game(width=4, height=4, players=2, seed=1)
    unit, x, y = g.players[0].units[0]
    # ensure destination is land
    g.map.get_tile(x + 1, y).terrain = "land"
    g.move_player(1, 0)
    assert g.players[0].units[0][1:] == (x + 1, y)
