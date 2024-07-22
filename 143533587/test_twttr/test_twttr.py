from twttr import shorten

def test_shortword():
    assert shorten("Twitter") == "Twttr"

def test_sentence():
    assert shorten("Hello world") == "Hll wrld"

def test_upper():
    assert shorten("TWITTER") == "TWTTR"

def test_num():
    assert shorten("Hello 123") == "Hll 123"

def test_punc():
    assert shorten("Hello, world") == "Hll, wrld"