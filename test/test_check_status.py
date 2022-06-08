import sys
import pathlib

test_path = pathlib.Path(__file__).resolve().parent
source_path = test_path.parent.joinpath("src")
sys.path.insert(0, str(source_path))

import check_status as cs

def test_if_site_is_up_return_200():
    url = 'https://www.random.org/integers/'
    status = cs.Status(url)
    is_up = status.is_up()
    assert is_up == True

