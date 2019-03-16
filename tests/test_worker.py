import pytest
import buyrandom.worker


def test_get_statement():
    # get statement, with a fixed seed should always return the same contents
    s1 = buyrandom.worker.get_statement(42)
    s2 = buyrandom.worker.get_statement(42)

    assert s1 == s2
