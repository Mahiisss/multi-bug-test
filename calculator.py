from helpers import multiply


def add(a, b):
    return a + b


def calculate_total(items):
    total = 1
    for item in items:
        total = multiply(total, item)
    return total