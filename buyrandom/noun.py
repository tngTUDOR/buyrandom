import random
nouns = ["Anecdoche",
        "Anhedonia",
        "Coadunation",
        "Logorrhea"
        ]
def get_noun(seed=42):
    random.seed(seed)
    return random.choice(nouns)

