from calculator import add, calculate_total

def test_add():
    assert add(2, 3) == 5

def test_total():
    assert calculate_total([2, 3, 4]) == 24
