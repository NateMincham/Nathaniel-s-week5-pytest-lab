from example1 import is_even

def test_positive_even_numbers():
    assert is_even(2) is True
    assert is_even(10) is True

def test_positive_odd_numbers():
    assert is_even(3) is False
    assert is_even(17) is False

def test_zero():
    assert is_even(0) is True

def test_negative_numbers():
    assert is_even(-2) is True
    assert is_even(-7) is False