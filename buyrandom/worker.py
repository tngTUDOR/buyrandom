from buyrandom.noun import get_noun
from buyrandom.adjective import get_adjective
from buyrandom.place import get_place
from buyrandom.seedfactory import *

def get_statement(seed):
    factory = SeedFactory(seed)
    
    s1 = factory.a_seed()
    s2 = factory.a_seed()
    s3 = factory.a_seed()

    a_noun = get_noun(s1)
    an_adjective = get_adjective(s2)
    a_place = get_place(s3)
    return "For sale: {} {} from {}".format(an_adjective, a_noun, a_place)
