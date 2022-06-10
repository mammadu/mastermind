from pydoc import plain
from game import Game
from os import system, name

class Interface:
    def __init__(self):
        self.game = Game()

    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def display_feedback(self):
        try:
            for feedback in self.game.feedback_list:
            # feedback = self.game.latest_feedback()
                print(f"input: {feedback['input']} \t feedback: {feedback['output']}")
        except IndexError as e:
            pass
        print()
        print(f"attempts left: {self.game.attempts_left}")

    def get_user_input(self):
        user_input = input(f"Enter guess, separate numbers with spaces: ")
        if user_input.lower() == 'quit':
            user_input = user_input.lower()
        else:
            print(user_input)
            try:
                user_input = user_input.split()
                user_input = list(map(int, user_input))
            except ValueError as e:
                user_input = None
        return user_input

    def main(self):
        welcome_message = f"""
Welcome to Mastermind, the codebreaking game!
You will have {self.game.attempts_left} attempts to break the code.
The code is {self.game.length} numbers long.
Each number can be between {self.game.min} and {self.game.max} inclusive.
Enter 'quit' to exit out of the game.
Good Luck!
"""
        while self.game.player_win == False and self.game.player_lose == False:
            print(welcome_message)
            self.display_feedback()
            user_input = None
            while user_input == None:
                user_input = self.get_user_input()
                if user_input == 'quit':
                    print('Goodbye')
                    quit()
                elif user_input == None:
                    print('Only enter numbers separated by spaces')
                elif len(user_input) != self.game.length:
                    print(f'You must enter {self.game.length} numbers, separated by spaces')
                    user_input = None
            self.game.evaluate(user_input)
            self.clear()
        if self.game.player_win == True:
            print(f"""
You win! 
The code was {self.game.code}.
Congratulations!
            """
            )
        elif self.game.player_lose == True:
            print(
                f"""
You lose...
The code was {self.game.code}
Better luck next time!"
"""
            )