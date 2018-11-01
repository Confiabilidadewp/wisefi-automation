import random

class create:

    def __init__(self, initial=1, final=2):
        self.initial = initial
        self.final = final

    def run(self):

        result = random.randint(self.initial, self.final)
        return result
