from check_status import Status
import random_api_wrapper
import python_random_wrapper

class RandomInterface:
    def __init__(self, url='https://www.random.org/integers/'):
        status = Status(url)
        if status.is_up() == True:
            self.wrapper = random_api_wrapper.Wrapper()
        else:
            self.wrapper = python_random_wrapper.Wrapper()
    
    def generate_random_list(self, min=0, max=7, length=4):
        return self.wrapper.generate_random_numbers(min, max, length)