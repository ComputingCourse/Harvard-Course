from um import count

def test_inword():
    assert count("jummy") == 0

def test_punct():
    assert count("hello ,um bye") == 1
    assert count("hello .um. bye") == 1

def test_end():
    assert count("Hello UM bye") == 1
    assert count("hello ,um") == 1