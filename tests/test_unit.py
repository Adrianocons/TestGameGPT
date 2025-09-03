import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from polythorogue.map import Map
from polythorogue.unit import Unit

def test_unit_move():
    m = Map.generate(3, 3, land_ratio=1.0, villages=0, seed=1)
    unit = Unit(player=0)
    m.get_tile(1, 1).unit = unit
    assert unit.move(m, 1, 1, 2, 1) is True
    assert m.get_tile(2, 1).unit == unit
    assert m.get_tile(1, 1).unit is None

def test_unit_attack():
    a = Unit(player=0)
    b = Unit(player=1, hp=3)
    assert a.attack_unit(b) is True
