import pytest 
import math

#pytest test_example_5.py -v --maxfail 1
def test_sqrt_fails():
    num = 25
    assert math.sqrt(num) == 6

def test_square_fails():
    num = 7
    assert num * num == 40

def test_equal_fails():
    assert 10 == 11

