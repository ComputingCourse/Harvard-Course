from plates import is_valid

def test_length():
    assert is_valid("AAAAAAA") == False
    assert is_valid("A") == False
    assert is_valid("AAAA") == True

def test_start():
    assert is_valid("A22") == False
    assert is_valid("AA2") == True

def test_num():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True

def test_punc():
    assert is_valid("AAA,.2") == False
    assert is_valid("AAA  2") == False

def test_zero():
    assert is_valid("AAA02") == False