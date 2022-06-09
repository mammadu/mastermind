import sys
import pathlib
import random_api_wrapper
import python_random_wrapper

test_path = pathlib.Path(__file__).resolve().parent

path_list = {
    'source_path': test_path.parent.joinpath("src")
}

for value in path_list.values():
    sys.path.insert(0, str(value))

import random_interface as ri
import check_status as cs

def test_if_random_site_is_up_use_random_api_wrapper():
    interface = ri.RandomInterface()
    assert isinstance(interface.wrapper, type(random_api_wrapper.Wrapper()))

def test_if_random_site_is_down_use_python_random_wrapper():
    interface = ri.RandomInterface('https://www.random.org/fake_path/')
    assert isinstance(interface.wrapper, type(python_random_wrapper.Wrapper()))
