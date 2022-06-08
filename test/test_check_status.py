import sys
import pathlib

test_path = pathlib.Path(__file__).resolve().parent
source_path = test_path.parent.joinpath("src")
sys.path.insert(0, str(source_path))

import check_status as cs

def test_if_status_is_200_to_299_return_true():
    url = 'https://www.random.org/integers/'
    status = cs.Status(url)
    is_up = status.is_up()
    assert is_up == True

def test_if_site_is_not_200_to_299_return_false():
    url = 'https://www.random.org/spelling_mistake/'
    status = cs.Status(url)
    is_up = status.is_up()
    assert is_up == False

def test_if_site_is_fake_return_false():
    url = 'https://www.fake_website.fake/'
    status = cs.Status(url)
    is_up = status.is_up()
    assert is_up == False

def test_log_status_of_site_to_csv():
    url = 'https://www.random.org/integers/'
    status = cs.Status(url)
    status.log_status(status, logger)