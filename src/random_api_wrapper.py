from pydoc import plain
from pyparsing import col
import requests

class Wrapper:
    def generate_random_numbers(self, min, max, length):
        base_url = 'https://www.random.org/integers/'
        query_string = {
            'num': length
            , 'min': min
            , 'max': max
            , 'col': 1
            , 'base': 10
            , 'format': 'plain'
            , 'rnd': 'new'
        }
        response = requests.get(base_url, params=query_string)
        string_list = response.text.split('\n')[:-1] #the -1 removes the empty space at the end of the list
        random_number_list = list(map(int, string_list))
        return random_number_list
