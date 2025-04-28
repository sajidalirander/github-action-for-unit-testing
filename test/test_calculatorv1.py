import pytest
from calculatorv1 import add, subtract, divide

def test_add_valid():
    assert add(2, 3) == 5
    assert add(2.0, 3.0) == 5

def test_add_invalid():
    with pytest.raises(TypeError):
        add(2, "3")

def test_subtract_valid():
    assert subtract(5, 3) == 2
    assert subtract(5.5, 2.5) == 3.0

def test_subtract_invalid():
    with pytest.raises(TypeError):
        subtract("5", 3)

def test_divide_valid():
    assert divide(10, 2) == 5.0

def test_divide_invalid_type():
    with pytest.raises(TypeError):
        divide(10, "2")

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
