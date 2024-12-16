import pytest

from app.calc1 import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

def test_add():
    assert calc.add(2, 3) == 5

def test_subtract():
    assert calc.subtract(10, 4) == 6

def test_multiply():
    assert calc.multiply(3, 5) == 15

def test_divide():
    assert calc.divide(10, 2) == 5
