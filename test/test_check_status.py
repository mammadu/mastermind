import sys
import pathlib

test_path = pathlib.Path(__file__).resolve().parent

path_list = {
    'source_path': test_path.parent.joinpath("src")
    , 'log_path': test_path.parent.joinpath("logs")
}

for value in path_list.values():
    sys.path.insert(0, str(value))

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
    log_file_location = test_path.joinpath("random_api_status.csv")
    status.log_status(True, logger=cs.CSVLogger(str(log_file_location)))
    assert log_file_location.is_file() == True
    log_file_location.unlink()
