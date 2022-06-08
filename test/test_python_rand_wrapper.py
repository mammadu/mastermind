import sys
import pathlib

test_path = pathlib.Path(__file__).resolve().parent
source_path = test_path.parent.joinpath("src")
sys.path.insert(0, str(source_path))

import python_random_wrapper as pyrand

# the generate numbers function should return a list of random numbers
def test_generate_number():
    rand = pyrand.Wrapper()
    # min = 0
    # max = 1
    # length = 1
    # list = rand.generate_random_numbers(min, max, length)
    # assert type(list[0]) == int

# def test_generate_multiple_numbers():
#     rand = api.Wrapper()
#     min = 0
#     max = 7
#     length = 4
#     list = rand.generate_random_numbers(min, max, length)
#     assert len(list) == length