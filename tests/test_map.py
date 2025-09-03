import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from polythorogue.map import Map

def test_generate_map_villages():
    m = Map.generate(5, 5, villages=2, seed=42)
    count = sum(1 for row in m.tiles for tile in row if tile.village)
    assert count == 2
    assert m.width == 5 and m.height == 5
