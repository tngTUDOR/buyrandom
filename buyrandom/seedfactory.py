import random
import sys

class SeedFactory:
    
    state = None

    def __init__(self, initial_seed):
        self.seed = initial_seed
        random.seed(initial_seed)
        self.state = random.getstate()

    def a_seed(self):
        v = random.randint(0, sys.maxsize)
        self.state = random.getstate()
        return v

