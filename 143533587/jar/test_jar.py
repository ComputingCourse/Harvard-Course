from jar import Jar
import pytest

def test_init():
    jar = Jar("13")
    assert jar.capacity == 13

def test_str():
    jar = Jar("12")
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
    assert jar.size == 4

def test_error():
    jar = Jar("12")
    with pytest.raises(ValueError):
        jar.deposit(13)
    with pytest.raises(ValueError):
        jar.deposit(1)
        jar.withdraw(3)
def test_cap():
    with pytest.raises(ValueError):
        jar1 = Jar("cat")