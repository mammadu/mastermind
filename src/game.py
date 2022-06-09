import evaluate
import random_interface as ri

class Game:
    def __init__(self, code=None):
        if code == None:
            self.code = self.generate_code()
        else:
            self.code = code
        self.feedback_list = []

    def evaluate(self, input):
        evaluator = evaluate.Evaluator()
        output = evaluator.evaluate(self.code, input)
        feedback = {
            'input': input
            , 'output': output
        }
        self.feedback_list.append(feedback)

    def latest_feedback(self):
        return self.feedback_list[len(self.feedback_list) - 1]

    def generate_code(self, min=0, max=7, length=4):
        rand = ri.RandomInterface()
        code = rand.generate_random_list(min, max, length)
        return code
