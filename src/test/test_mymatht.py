from src.main.MyMath import add_tow_numbers
from src.main.MyMathT import mul_tow_numbers

def test_add_tow_numbers():
    assert 3 == add_tow_numbers(2, 2)

def test_mul_tow_numbers():
    assert 3 == mul_tow_numbers(1, 3)
