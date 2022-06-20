import sys
import pathlib

test_path = pathlib.Path(__file__).resolve().parent
source_path = test_path.parent.joinpath("src")
sys.path.insert(0, str(source_path))

import console_interface as ci

def test_convert_user_input_to_list_of_ints():
    interface = ci.Interface()
    ci.input = lambda a: "0 1 2 3"
    input = interface.get_user_input()
    assert input == [0,1,2,3]

def test_bad_input_returns_None():
    interface = ci.Interface()
    ci.input = lambda a: "abc"
    input = interface.get_user_input()
    assert input == None

def test_select_easy_difficulty():
    interface = ci.Interface()
    ci.input = lambda a: "EASY"
    assert interface.select_difficulty() == "easy"

def test_select_hard_difficulty():
    interface = ci.Interface()
    ci.input = lambda a: "hArD"
    assert interface.select_difficulty() == "hard"

def test_only_allows_easy_or_hard_difficulty():
    interface = ci.Interface()
    ci.input = lambda a: "extreee333mmee "
    assert interface.select_difficulty() == "please select easy or hard"