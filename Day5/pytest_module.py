import pytest

def add(a, b):
    return a+b

def test_add():
    assert add(4,5) == 9

def test_adds():
    assert add(44, 4) == 98