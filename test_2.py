from example2 import reverse_string

def test_normal_word():
    assert reverse_string("hello") == "olleh"

def test_single_character():
    assert reverse_string("a") == "a"

def test_empty_string():
    assert reverse_string("") == ""

def test_sentence():
    assert reverse_string("python test") == "tset nohtyp"

def test_numbers_as_string():
    assert reverse_string("12345") == "54321"