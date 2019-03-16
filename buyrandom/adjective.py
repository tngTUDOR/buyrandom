import random

adjectives = [ "blue", "parisian", "trenchant", "Fubsy", "red", "fast", "fair", "low", "old", "new" ]

def get_adjective(seed=42):
    random.seed(seed)
    return random.choice(adjectives)

