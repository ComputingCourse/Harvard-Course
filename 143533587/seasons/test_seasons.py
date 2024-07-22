from seasons import valid
from seasons import calculate

def test_valid():
    assert valid("2023-09-07") == True
    assert valid("2023-15-07") == False
    assert valid("hello") == False

def test_calc():
    assert calculate("2022-09-07") == 525600
    assert calculate("2023-09-06") == 1440