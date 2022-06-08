import random

class Wrapper:
    def generate_random_numbers(self, min, max, length):
        list = []
        for i in range (0, length):
            random_int = random.randint(min,max)
            list.append(random_int)
        return list
