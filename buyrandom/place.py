import random
places = [
        "Paris, Texas",
        "Barcelona",
        "the coffee shop",
        "Paris, France"
        ]
def get_place(seed=42):
    random.seed(seed)
    return random.choice(places)
