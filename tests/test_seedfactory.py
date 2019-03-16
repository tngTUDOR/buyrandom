import pytest
from buyrandom.seedfactory import SeedFactory

def test_a_seed():

    sf = SeedFactory(42)
    sn1 = sf.a_seed()
    sa1 = sf.a_seed()
    sp1 = sf.a_seed()

    sf2 = SeedFactory(42)
    sn2 = sf2.a_seed()
    sa2 = sf2.a_seed()
    sp2 = sf2.a_seed()

    assert sn1 == sn2 and sa1 == sa2 and sp1 == sp2
