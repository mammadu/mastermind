import evaluate
import random_interface as ri

class Game:
    def __init__(self, code=None, attempts=10):
        if code == None:
            self.code = self.generate_code()
        else:
            self.code = code
        self.feedback_list = []
        self.attempts_left = attempts
        self.player_win = False
        self.player_lose = False

    def evaluate(self, input):
        evaluator = evaluate.Evaluator()
        output = evaluator.evaluate(self.code, input)
        feedback = {
            'input': input
            , 'output': output
        }
        self.feedback_list.append(feedback)
        self.decrement_attempts()
        self.evaluate_game_state()

    def latest_feedback(self):
        return self.feedback_list[len(self.feedback_list) - 1]

    def generate_code(self, min=0, max=7, length=4):
        rand = ri.RandomInterface()
        code = rand.generate_random_list(min, max, length)
        return code

    def decrement_attempts(self):
        self.attempts_left = self.attempts_left - 1

    def evaluate_game_state(self):
        if self.latest_feedback()['output']['perfect'] == len(self.code):
            self.player_win = True
        elif self.attempts_left == 0:
            self.player_lose = True