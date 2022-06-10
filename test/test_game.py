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
    assert game.latest_feedback()['output']['perfect'] == 1
    assert game.latest_feedback()['output']['correct'] == 1
    assert game.latest_feedback()['output']['incorrect'] == 2

def test_init_game_with_random_code():
    game = gm.Game()
    assert len(game.code) == 4
    assert isinstance(game.code[0], int)

def test_game_decrements_attempts_after_input():
    starting_attempts = 10
    game = gm.Game(attempts=starting_attempts)
    input = [1,2,3,4]
    game.evaluate(input)
    final_attempts = game.attempts_left
    assert (starting_attempts - final_attempts) == 1

def test_when_attempts_is_0_the_player_loses():
    starting_attempts = 1
    game = gm.Game(code=[0,0,0,0], attempts=starting_attempts)
    input = [1,2,3,4]
    game.evaluate(input)
    assert game.player_lose == True

def test_if_input_matches_code_the_player_wins():
    starting_attempts = 1
    game = gm.Game(code=[0,0,0,0], attempts=starting_attempts)
    input = [0,0,0,0]
    game.evaluate(input)
    assert game.player_lose == False
    assert game.player_win == True