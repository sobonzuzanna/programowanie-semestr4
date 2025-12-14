import pytest
from my_awesome_lib.math_tools import sumuj, odejmij, srednia

# suma
def test_sumuj():
    assert sumuj(2, 3) == 5

def test_sumuj_ujemne():
    assert sumuj(-2, -3) == -5

# różnica
def test_odejmij():
    assert odejmij(5, 3) == 2

def test_odejmij_ujemne():
    assert odejmij(-5, -3) == -2

# średnia
def test_srednia():
    assert srednia(4, 6) == 5

def test_srednia_zero():
    assert srednia(0, 0) == 0