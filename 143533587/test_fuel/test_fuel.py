import pytest
from fuel import convert
from fuel import gauge

def test_convertvalueError():
    with pytest.raises(ValueError):
        convert("1.3/3")
    with pytest.raises(ValueError):
        convert("1/1.3")
    with pytest.raises(ValueError):
        convert("2/1")

def test_convertzero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert():
    assert convert("2/3") == 67
    assert convert("3/4") == 75

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"