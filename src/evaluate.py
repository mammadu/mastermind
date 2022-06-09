from random import random


class Evaluator:
    def evaluate(self, random_list, user_input):
        random_dict = self.create_dict_from_list(random_list)
        user_dict = self.create_dict_from_list(user_input)
        evaluation = {
            'perfect': 0
            , 'correct': 0
            , 'incorrect': 0
        }
        for key in random_dict:
            if key in user_dict:
                diff = random_dict[key] - user_dict[key]
            else:
                diff = random_dict[key]
            evaluation['correct'] = evaluation['correct'] + random_dict[key] - max(0, diff)
            
        for index in range(0,len(random_list)):
            if random_list[index] == user_input[index]:
                evaluation['correct'] = evaluation['correct'] - 1
                evaluation['perfect'] = evaluation['perfect'] + 1
        evaluation['incorrect'] = len(random_list) - (evaluation['correct'] + evaluation['perfect'])
        return evaluation

    def create_dict_from_list(self, list):
        dict = {}
        for item in list:
            if item in dict:
                dict[item] = dict[item] + 1
            else:
                dict[item] = 1
        return dict
