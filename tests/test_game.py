import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from polythorogue.game import Game

def test_game_step_changes_turn():
    g = Game(width=3, height=3, players=2, seed=1)
    first_turn = g.turn
    g.step()
    assert g.turn != first_turn
