import pytest

def add_one(value):
	return value + 1

def test_add_one():
    output = add_one(5)
    assert output == 6
    assert type(output) == int
