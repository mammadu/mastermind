import evaluate
import random_interface as ri

class Game:
    def __init__(self, code=None):
        if code == None:
            self.code = self.generate_code()
        else:
            self.code = code
        self.feedback = []
    
    def evaluate(self, input):
        evaluator = evaluate.Evaluator()
        feedback = evaluator.evaluate(self.code, input)
        self.feedback.append(feedback)
    
    def latest_feedback(self):
        return self.feedback[len(self.feedback) - 1]

    def generate_code(self):
        rand = ri.RandomInterface()
        code = rand.generate_random_list()
        return code
