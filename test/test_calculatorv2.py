import pytest
import calculatorv2 as calc
from pydantic import ValidationError

def test_add_valid():
    assert calc.add(2, 3) == 5
    assert calc.add(2.0, 3.0) == 5

def test_add_invalid_input():
    with pytest.raises(ValidationError):
        calc.add(a=2, b="3.0")

def test_subtract_valid():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(5.5, 2.5) == 3.0

def test_subtract_invalid_input():
    with pytest.raises(ValidationError):
        calc.subtract(a="3", b=3)

def test_divide_valid():
    assert calc.divide(10, 2) == 5.0

def test_divide_invalid_input():
    with pytest.raises(ValidationError):
        calc.divide(a=10, b="3")

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)
