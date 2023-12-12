import random

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)
    
# roll function with argument will generate a random number between 1 and the argument