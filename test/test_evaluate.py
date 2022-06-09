import sys
import pathlib

test_path = pathlib.Path(__file__).resolve().parent
source_path = test_path.parent.joinpath("src")
sys.path.insert(0, str(source_path))

import evaluate as ev

def test_matching_values_in_wrong_location_should_be_correct():
    random_list = [0,1,2,3]
    user_input = [1,2,3,0]
    evaluator = ev.Evaluator()
    result = evaluator.evaluate(random_list, user_input)
    assert result['correct'] == len(random_list)

def test_matching_values_in_right_location_should_be_perfect():
    random_list = [1,2,0,3]
    user_input = [1,2,3,0]
    evaluator = ev.Evaluator()
    result = evaluator.evaluate(random_list, user_input)
    assert result['perfect'] == 2

def test_count_incorrect_values():
    random_list = [0,1,2,3]
    user_input = [4,5,6,7]
    evaluator = ev.Evaluator()
    result = evaluator.evaluate(random_list, user_input)
    assert result['incorrect'] == 4