import sys
import pathlib

test_path = pathlib.Path(__file__).resolve().parent
source_path = test_path.parent.joinpath("src")
sys.path.insert(0, str(source_path))

import game as gm

def test_evalutate_input():
    game = gm.Game([1,2,3,4])
    input = [1,0,2,5]
    game.evaluate(input)
    assert game.latest_feedback()['perfect'] == 1
    assert game.latest_feedback()['correct'] == 1
    assert game.latest_feedback()['incorrect'] == 2

def test_init_game_with_random_code():
    game = gm.Game()
    assert len(game.code) == 4
    assert isinstance(game.code[0], int)