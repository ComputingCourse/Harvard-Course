from bank import value

def test_hello():
    assert value("hello") == 0

def test_hey():
    assert value("hey") == 20

def test_random():
    assert value("random") == 100

def test_upper():
    assert value("HELLO") == 0
    assert value("HEY") == 20
    assert value("RANDOM") == 100