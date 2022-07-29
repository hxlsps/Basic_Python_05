from code_example import Calc, Util

def test_calc():
    cals = Calc()
    input = [1, 2, 3, 4]
    assert cals.sum(input) == 10

def test_util():
    util = Util()
    input = 'hello world'
    assert util.upper_case(input) == 'HELLO WORLD'

