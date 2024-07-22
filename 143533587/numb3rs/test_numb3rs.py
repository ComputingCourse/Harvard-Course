from numb3rs import validate

def test_edge():
    assert validate("255.0.123.21") == True
    assert validate("256.0.123.21") == False
    assert validate("255.-1.123.21") == False

def test_error():
    assert validate("255.0.123.21.32") == False
    assert validate("255,0.123,21") == False
    assert validate("cat") == False
    assert validate("255.21.21.43.267") == False
    assert validate("255.21.21.277") == False